#!/usr/bin/env python3
"""Check standalone skill names, local links, and MIT license files offline.

Requires only Python 3.9+. This is a package integrity check, not a behavioral
evaluator or a replacement for YAML validation.
"""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def verify():
    names, links = [], 0
    for skill in sorted((ROOT / 'skills').iterdir()):
        if not skill.is_dir():
            continue
        names.append(skill.name)
        entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
        if not re.search(r'^name: ' + re.escape(skill.name) + r'$', entry, re.M):
            raise ValueError('Skill name mismatch: ' + skill.name)
        for path in skill.rglob('*'):
            if path.is_symlink():
                raise ValueError('Package contains a symlink: ' + str(path))
            if path.suffix != '.md':
                continue
            text = path.read_text(encoding='utf-8')
            for raw in re.findall(r'\]\(([^)]+)\)', text):
                link = raw.strip('<>')
                parsed = urlsplit(link)
                if parsed.scheme:
                    if parsed.scheme not in ('https', 'http', 'mailto'):
                        raise ValueError('Nonportable link: ' + raw)
                    continue
                if not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(skill.resolve()) or not target.is_file():
                    raise ValueError('Missing or escaping local reference in ' + str(path) + ': ' + raw)
                links += 1
        license_text = (skill / 'LICENSE').read_text(encoding='utf-8')
        if not license_text.startswith('MIT License\n') or 'Permission is hereby granted, free of charge' not in license_text:
            raise ValueError('MIT license is missing: ' + skill.name)
        if not re.search(r'^license: MIT$', entry, re.M):
            raise ValueError('License metadata missing: ' + skill.name)
        if (skill / 'references/sources.json').exists():
            raise ValueError('Unexpected source registry in distribution: ' + skill.name)
    return {'skills': names, 'local_links_checked': links, 'licenses_checked': len(names)}



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        print(json.dumps(verify(), indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()

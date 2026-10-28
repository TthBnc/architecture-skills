#!/usr/bin/env python3
"""Install the bundled standalone skills without overwriting existing skills.

Requires only Python 3.9+. Already identical installs are left alone.
"""
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(folder):
    result = {}
    for path in folder.rglob('*'):
        if path.name == '.DS_Store':
            continue
        if path.is_symlink():
            raise ValueError('Symlinks are not supported in skill packages: ' + str(path))
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def install(target):
    packages = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())
    if not packages:
        raise ValueError('No bundled skills found.')
    pending = []
    # Complete all conflict checks before creating any installed skill.
    for package in packages:
        destination = target / package.name
        if destination.is_symlink():
            raise ValueError('Existing symlink left unchanged: ' + str(destination))
        if destination.exists():
            if not destination.is_dir() or fingerprint(package) != fingerprint(destination):
                raise ValueError('Different existing skill left unchanged: ' + str(destination) + '. Choose another --target or deliberately move that skill before installing.')
            print('Already identical: ' + str(destination))
        else:
            fingerprint(package)
            pending.append(package)
    if not pending:
        return
    target.mkdir(parents=True, exist_ok=True)
    created = []
    with tempfile.TemporaryDirectory(prefix='.architecture-skills-stage-', dir=target) as temp:
        stage = Path(temp)
        for package in pending:
            shutil.copytree(package, stage / package.name, ignore=shutil.ignore_patterns('.DS_Store'))
        try:
            for package in pending:
                destination = target / package.name
                # mkdir is an exclusive claim: never replace a concurrent install.
                destination.mkdir()
                created.append(destination)
                for child in (stage / package.name).iterdir():
                    shutil.move(str(child), str(destination / child.name))
                print('Installed: ' + str(destination))
        except BaseException:
            for destination in reversed(created):
                shutil.rmtree(destination)
            raise


def main():
    default_root = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, default=default_root / 'skills', help='Destination skill root (default: CODEX_HOME/skills or ~/.codex/skills)')
    args = parser.parse_args()
    try:
        install(args.target.expanduser().resolve())
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()

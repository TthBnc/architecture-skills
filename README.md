# Architecture Skills

**Based on [Hello Interview's public, free learning material](https://www.hellointerview.com/learn).** Independently adapted into practical agent skills; this project is not affiliated with or endorsed by Hello Interview.

Five practical agent skills for designing software systems, reviewing architectures, and practising system design interviews.

**Free to use, modify, and redistribute for personal or commercial purposes under the [MIT License](LICENSE).** Keep the copyright and permission notice when redistributing copies or substantial portions.

## Skills

| Skill | What it does |
| --- | --- |
| [system-design](skills/system-design/SKILL.md) | Develop architectures and architectural decisions from requirements and constraints. |
| [system-design-review](skills/system-design-review/SKILL.md) | Review proposed architectures for correctness, reliability, scaling, and operational risks. |
| [low-level-design](skills/low-level-design/SKILL.md) | Design component responsibilities, interfaces, state ownership, and lifecycles. |
| [ml-system-design](skills/ml-system-design/SKILL.md) | Design ML data pipelines, evaluation, training, retrieval, and serving. |
| [system-design-practice](skills/system-design-practice/SKILL.md) | Run interactive mock interviews with gradual hints and grounded feedback. |

Each skill is independently usable and includes focused Markdown references. It does not require a companion skill, a reference server, or a specific model.

## Install

Clone the repository and run the standard-library installer with Python 3.9 or newer:

```sh
git clone https://github.com/TthBnc/architecture-skills.git
cd architecture-skills
python3 tools/install_skills.py
```

On Windows, use `py -3 tools/install_skills.py`.

The default destination is `$CODEX_HOME/skills` when configured, otherwise `~/.codex/skills`. Use `--target PATH` to choose another directory. The installer skips identical copies and preserves different existing skills. You can also copy an individual folder from `skills/` into a compatible agent's skill directory.

## Use

```text
$system-design Design a document-processing service for our existing application.

$system-design-review Review this booking design for concurrency and retry failures.

$low-level-design Design a cancellable CSV importer with clear interfaces.

$ml-system-design Design recommendations for a small catalog with sparse feedback.

$system-design-practice Run a senior-level rate-limiter mock, one question at a time.
```

The workflows adapt to the user's scope, stack, workload, and team. Design requests produce reviewable decisions; implementation and deployment require their own task authorization. Current vendor limits, costs, and guarantees should be verified when they affect a real decision.

Bundled references are local files. Model inference uses the selected agent's normal runtime or connection.

## Check the packages

```sh
python3 tools/verify_skills.py
```

This checks package names, local reference links, and license files. It does not certify future designs or measure model quality.

## License

[MIT](LICENSE). Every skill folder includes its own license copy so it can be redistributed independently. The material is provided as is, without warranty.

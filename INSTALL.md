# Installation

Keep the whole repository together so `SKILL.md`, `scripts/`, `config/`, and `references/` preserve their relative paths.

## Codex

Copy or clone the repository to one of:

- `~/.agents/skills/job-application-form-filler/`
- `~/.codex/skills/job-application-form-filler/`

## OpenCode and other agents

Place the repository in the product's configured user-level or project-level skills directory. If automatic skill discovery is unavailable, explicitly tell the agent to read `SKILL.md`.

## Create private data

Run:

```bash
python scripts/init_private_data.py
```

The default private location is `~/.job-application-form-filler`. Override it with either:

```bash
python scripts/init_private_data.py --data-dir /private/path
```

or the `JOB_APPLICATION_DATA_DIR` environment variable.

Do not place real applicant data inside a public repository.

# Job Application Form Filler

A token-efficient, privacy-safe Agent Skill for filling Chinese or English job-application forms from a verified private fact bank.

## Why this version is lightweight

The agent does not read an entire resume database. A small deterministic script selects only the profile sections and experiences needed for the current role. Platform instructions are also loaded on demand.

## Public/private separation

This repository contains only workflow rules, schemas, scripts, and fictional examples. Real applicant data belongs outside the repository, by default in:

```text
~/.job-application-form-filler/
```

Never commit completed private files, resumes, screenshots, certificates, identity documents, referral URLs, cookies, or application-state files.

## Quick start

```bash
python scripts/init_private_data.py
```

Edit the generated private JSON files locally, then build a minimal context packet:

```bash
python scripts/build_context.py --role operations --sections identity,education,skills,awards --max-experiences 3
```

Use `--list` to inspect experience IDs without loading full descriptions. For a dedicated project section, request projects separately:

```bash
python scripts/build_context.py --role operations --sections awards --kinds project --max-experiences 2
```

## Supported role profiles

- operations / ecommerce / marketing / brand
- product
- data
- finance
- consulting / strategy / research
- state-owned / comprehensive management
- general

## Safety defaults

- Never invent missing facts.
- Keep internships out of employment history when a separate internship section exists.
- Saving a draft does not authorize submission.
- Uploading attachments requires explicit authorization.

See [INSTALL.md](INSTALL.md) for Codex, OpenCode, and other agents.

## License

MIT

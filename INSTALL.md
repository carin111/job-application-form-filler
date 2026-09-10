# Installation

This repository follows the common Agent Skills layout: `SKILL.md` is at the repository root and supporting guidance is under `references/`.

## Codex

Copy the entire folder to either:

- `~/.agents/skills/job-application-form-filler/`
- `~/.codex/skills/job-application-form-filler/`

## OpenCode and other agents

Copy the entire folder into the product's configured user-level or project-level skills directory. Keep `SKILL.md` at the skill root and preserve the relative paths under `references/`.

If automatic discovery is unavailable, instruct the agent explicitly:

> Read and follow `job-application-form-filler/SKILL.md`. Use my private verified fact bank, fill the form, save the draft, and do not submit or upload attachments.

## Private customization

Do not edit the public templates with real data inside a public clone. Instead, copy these files to a private, ignored location:

- `references/profile-template.md`
- `references/experience-bank-template.md`

Then provide those private files to the agent at runtime.

# Job Application Form Filler

A privacy-safe, reusable Agent Skill for filling Chinese or English job-application forms from a verified user fact bank.

## What it does

- maps a job description to the most relevant experiences;
- preserves detailed source descriptions instead of reducing them to generic bullets;
- keeps internships in the correct section;
- checks dates, awards, education, languages, and role-specific summaries;
- saves drafts when authorized while treating final submission and attachment upload as separate actions;
- leaves unknown fields blank rather than guessing.

## Privacy design

This public repository contains **no real applicant data**. The profile and experience files are templates only. Create a private copy and fill it locally. Do not commit completed personal fact banks, resumes, identity documents, contact details, or application screenshots.

## Structure

```text
job-application-form-filler/
├── SKILL.md
├── INSTALL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── profile-template.md
    ├── experience-bank-template.md
    ├── targeting-rules.md
    ├── form-playbook.md
    └── privacy-checklist.md
```

## Quick start

1. Install the folder in your agent's skills directory.
2. Copy the two template files to a private location.
3. Fill them only with facts you can verify.
4. Ask the agent to use this skill for a target role and to save without submitting.

Example:

> Use the job-application-form-filler skill. Tailor my verified experience bank to this ecommerce operations role, fill the open application form, save the draft, but do not submit or upload attachments.

## License

MIT

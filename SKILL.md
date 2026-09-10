---
name: job-application-form-filler
description: Fill or update Chinese and English job-application forms from a user-provided verified fact bank, tailor experience selection to the target role, and preserve detailed source descriptions without inventing information. Use for campus recruitment, experienced-hire applications, resume centers, and profile-completion workflows. Save drafts only when authorized; never submit applications or upload attachments without explicit permission.
---

# Job Application Form Filler

Use this skill when a user asks an AI agent to fill, update, or tailor an online job-application or resume form.

## Read only what is needed

- Read `references/profile-template.md` to build or check the verified personal fact bank.
- Read `references/experience-bank-template.md` to structure canonical experience descriptions.
- Read `references/targeting-rules.md` when selecting content for a target role.
- Read `references/form-playbook.md` before operating a browser form.
- Read `references/privacy-checklist.md` before saving, exporting, or publishing data.

## Core workflow

1. Inspect the target page and identify the company, role, language, required sections, field limits, and existing content.
2. Determine the target direction from the user's request or JD. Ask only when a missing fact blocks progress.
3. Use only facts verified in the current conversation or the user's private fact bank. Never invent dates, metrics, titles, awards, certificates, contacts, tools, or responsibilities.
4. Select and reorder experiences by relevance. Rephrase for readability and keyword alignment without changing factual scope.
5. Preserve detailed canonical descriptions. Shorten only for a real field limit or an explicit user request.
6. Put internships in **Internship Experience / 实习经历**, not **Employment / 工作经历**, unless the form provides no internship section.
7. Fill and verify every applicable date field. Select values from rendered dropdown options rather than relying on injected text.
8. Review all entered information before saving.
9. Save a draft only when authorized. Final submission, consent to unrelated terms, messaging recruiters, and attachment uploads require separate explicit authorization.

## Unknown and sensitive fields

- Leave unknown information blank. Do not infer identity numbers, addresses, salary, GPA, contact details, demographic attributes, or employer contacts.
- If a required field cannot be skipped, ask one concise question.
- Do not overwrite user-entered information unless the user asks or a verified correction is available.
- Do not store personal data in this public skill. Keep private fact banks outside public repositories.

## Completion report

After operating a form, state:

- what was filled or updated;
- what was left blank and why;
- whether the draft was saved;
- that no application was submitted and no attachment was uploaded, unless the user explicitly authorized those actions.

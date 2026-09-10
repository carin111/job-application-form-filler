---
name: job-application-form-filler
description: Fill Chinese or English job-application forms from a private verified fact bank. Select only role-relevant experiences, preserve factual detail, and save drafts without submitting or uploading attachments unless explicitly authorized.
---

# Job Application Form Filler

1. Identify the target role, language, platform, required sections, and field limits.
2. Do **not** load the full private database. Run `scripts/build_context.py` with the closest role and only the sections needed by the visible form. Request `--kinds project` separately only when a project section exists.
3. Read `references/core-rules.md`. Read one matching file under `references/platforms/` only when needed.
4. Fill from the generated context only. Never invent or upgrade facts. Keep internships in the internship section. Preserve detailed descriptions unless a field limit requires shortening.
5. Verify dates and saved values. Unknown required facts need one concise user question; optional unknowns stay blank.
6. Editing, saving, uploading, consenting, messaging, and submitting are separate permissions. Default to save-only when authorized; never upload or submit without explicit authorization.
7. Record progress with `scripts/update_application_state.py` when work may continue across turns.

Private data lives outside this repository. Resolve it from `--data-dir`, `JOB_APPLICATION_DATA_DIR`, or `~/.job-application-form-filler`.

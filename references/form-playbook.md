# Form playbook

## Before editing

- Use an already-open authenticated browser session only when the user has authorized browser operation.
- Confirm the current site, company, role, and whether the page is a resume center or a live application.
- Inspect existing values before changing them.
- Identify required fields, repeatable sections, character limits, date controls, save controls, submit controls, and attachment controls.

## Data entry

- Populate internships under **实习经历 / Internship Experience**, not **工作经历 / Employment**, unless no internship section exists.
- Add all verified dates. Choose values from rendered dropdowns and verify the visible result.
- Complete one repeated entry at a time because dynamic forms often re-index controls.
- Preserve detailed canonical descriptions as far as field limits permit.
- Add education, awards, languages, projects, and certificates whenever the corresponding sections exist and the facts are relevant.
- Do not replace a user's richer existing text with a shorter generic summary.
- Do not enter `UNKNOWN`, placeholders, or internal notes into the live form.

## Dynamic-form reliability

- Refresh the accessibility or DOM view after adding or deleting an item.
- Complete date fields immediately after each entry to avoid assigning dates to the wrong record.
- After every save, inspect visible titles, organizations, dates, and the beginning/end of long descriptions.
- If a value was injected programmatically, confirm it persists after blur, rerender, or save.
- Stop after repeated failures rather than creating duplicate entries.

## Authorization boundaries

Treat these as separate actions:

1. editing fields;
2. saving a draft/profile;
3. uploading an attachment;
4. accepting optional consent or marketing terms;
5. submitting an application;
6. sending a recruiter message.

Authorization for one action does not authorize the others. Unless the user explicitly says otherwise, stop after saving the draft and do not upload files or submit.

## Final checklist

- Correct company, role, and language
- Personal data comes only from the verified private bank
- Education entries and dates are complete
- Experiences are in the correct section and ordered by relevance
- Each experience has organization, title, dates, and detailed description
- Projects, awards, languages, certificates, and summary are filled where applicable
- No placeholders or unknown values were entered
- Existing user content was not unintentionally overwritten
- No attachment was uploaded
- Draft saved if authorized
- Application not submitted without explicit authorization

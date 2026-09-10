# Privacy checklist

Before publishing or committing, remove:

- names, usernames, phones, emails, birth dates, addresses, contacts, IDs, and salary;
- identifiable combinations of schools, employers, titles, dates, awards, and metrics;
- resumes, screenshots, portraits, transcripts, certificates, and identity documents;
- application IDs, referral codes, signed URLs, cookies, tokens, credentials, and browser data;
- machine-specific paths containing usernames.

Safe public material includes blank schemas, placeholders, generic workflows, and clearly fictional examples.

Before pushing, inspect the Git diff and run `scripts/scan_public_repo.py`. Keep real data in the external private directory.

# Privacy checklist

Run this checklist before publishing, sharing, or committing a skill repository.

## Remove personal identifiers

- real names and usernames
- phone numbers and email addresses
- exact birth dates
- identity, passport, student, or employee numbers
- home, school, dormitory, or workplace addresses
- emergency and family contacts
- personal website URLs tied to an individual

## Remove identifying history

- exact combinations of schools, employers, dates, titles, awards, and metrics that identify one applicant
- referee and employer-contact information
- application IDs, referral codes, resume IDs, signed URLs, and browser-session data
- screenshots, resumes, certificates, transcripts, identity documents, and headshots

## Remove secrets and machine-specific data

- API keys, cookies, tokens, passwords, and authentication files
- absolute local paths containing usernames
- browser profiles and exported session data
- private repository URLs

## Safe public content

- blank templates
- generic workflows
- fictional examples clearly labeled as fictional
- placeholder values such as `<FULL_NAME>`
- privacy and authorization boundaries

## Verification commands

Before publishing, inspect the complete Git diff and search for likely identifiers, phone/email patterns, tokens, and absolute paths. A clean automated scan does not replace manual review.

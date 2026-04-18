# Day 26 — Attachments & Storage
![Day](https://img.shields.io/badge/Day-26-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement file attachment handling via Supabase Storage with signed URLs.
### Timebox

~3 hours
### Study

- [Supabase Storage documentation](https://supabase.com/docs/guides/storage)
- [Handling uploads securely](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#media_types)
### Build

1. Configure a Supabase Storage bucket for attachments (public/private).
1. Implement backend logic for generating signed upload and download URLs.
1. Add file metadata fields to the `attachments` table (e.g., file name, size, content type).
1. Validate file types and sizes on upload to prevent misuse.
### Assignments

- Commit storage implementation and update API routes for attachments.
- Add UI for uploading and viewing attachments.
### DoD Checklist

- [ ] Signed URLs expire appropriately and protect file access.
- [ ] Unsupported file types are rejected gracefully.
- [ ] Attachments display correctly in the UI.
### Commit Message

`feat(attachments): integrate Supabase Storage with signed URL upload/download`
### Outcome Artifacts

- Storage bucket configuration and policies.
- Attachment upload API route and UI integration.
### Self‑Review Questions

- Are file type and size validations comprehensive?
- Do signed URLs provide adequate protection against unauthorized access?

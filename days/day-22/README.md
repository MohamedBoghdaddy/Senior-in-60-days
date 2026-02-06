# Day 22 — Schema Design
![Day](https://img.shields.io/badge/Day-22-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Define a relational schema using PostgreSQL/Supabase and write migrations.
### Timebox

~4 hours
### Study

- [PostgreSQL schema design](https://www.postgresql.org/docs/current/ddl-gestalt.html)
- [Supabase CLI documentation](https://supabase.com/docs/guides/cli)
### Build

1. Design tables: `orgs`, `memberships`, `projects`, `sprints`, `tasks`, `comments`, `attachments`, `audit_logs`.
1. Define primary keys, foreign keys, and unique constraints; include audit fields (`created_at`, `updated_at`, `deleted_at`).
1. Write migration scripts using Supabase CLI or a migration tool like Knex or Prisma.
1. Create indexes based on expected query patterns (e.g., `(org_id, created_at)` for tasks).
### Assignments

- Commit the migration scripts and ER diagram (use Mermaid or a simple diagramming tool).
- Document schema design decisions and assumptions.
### DoD Checklist

- [ ] Migrations run idempotently and set up all tables.
- [ ] Indexes exist for key queries.
- [ ] Documentation includes the ER diagram and rationale.
### Commit Message

`feat(db): design relational schema and add migrations for core tables`
### Outcome Artifacts

- Migration scripts committed in `migrations/`.
- `docs/schema.md` with ER diagram and design notes.
### Self‑Review Questions

- Are there any missing relationships or constraints?
- Does the schema support future features like soft deletes?

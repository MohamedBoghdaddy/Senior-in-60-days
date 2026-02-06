# Day 23 — Enable RLS
![Day](https://img.shields.io/badge/Day-23-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Enable and configure row-level security (RLS) for multi-tenant isolation in Supabase.
### Timebox

~3 hours
### Study

- [Supabase RLS guide](https://supabase.com/docs/guides/auth#policies)
- [PostgreSQL RLS policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
### Build

1. Enable RLS on all tables that need isolation (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY`).
1. Write initial RLS policies to restrict data access by organization (`org_id`) and membership.
1. Test cross-organization access to ensure unauthorized queries are blocked.
1. Document common RLS pitfalls and how to avoid them.
### Assignments

- Commit RLS configurations and policies.
- Add tests simulating users from different orgs trying to access data.
### DoD Checklist

- [ ] RLS is enabled on all relevant tables.
- [ ] Cross-org access queries return no rows.
- [ ] Documentation explains RLS setup and pitfalls.
### Commit Message

`feat(db): enable RLS and define initial multi-tenant policies`
### Outcome Artifacts

- Policy SQL scripts in migrations.
- Tests demonstrating RLS in action.
### Self‑Review Questions

- Are there any tables missing RLS enforcement?
- Do policies allow only the intended operations?

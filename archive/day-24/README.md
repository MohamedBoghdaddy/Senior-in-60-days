# Day 24 — Role-Based Policies
![Day](https://img.shields.io/badge/Day-24-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Define row-level security policies that respect user roles.
### Timebox

~3 hours
### Study

- [Supabase policies documentation](https://supabase.com/docs/)
- [Role-based access control in Postgres](https://www.postgresql.org/docs/current/sql-createpolicy.html)
### Build

1. Create RLS policies that factor in user roles (owner, admin, member) for select, insert, update, and delete operations.
1. Use role membership tables (e.g., `memberships`) to determine permissible actions.
1. Test scenarios where users attempt to exceed their role permissions.
1. Document policy logic and alternatives considered.
### Assignments

- Commit updated RLS policies and tests.
- Update `SECURITY.md` describing role-based policies.
### DoD Checklist

- [ ] Policies enforce role-based restrictions for all relevant operations.
- [ ] Tests confirm that owners and admins can perform additional actions compared to members.
- [ ] Documentation reflects policy logic.
### Commit Message

`feat(db): implement role-based RLS policies and update security docs`
### Outcome Artifacts

- RLS policy definitions updated in migration scripts.
- Tests verifying role-specific access.
- Updated `SECURITY.md` explaining RLS roles.
### Self‑Review Questions

- Are any roles overly permissive or restrictive?
- How are new roles or privileges integrated into the policies?

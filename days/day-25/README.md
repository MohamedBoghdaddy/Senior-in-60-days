# Day 25 — Pagination Strategy
![Day](https://img.shields.io/badge/Day-25-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement keyset pagination for scalable queries.
### Timebox

~2 hours
### Study

- [Keyset pagination article](https://hakibenita.com/keyset-pagination)
- [Postgres ordering and indexes](https://www.postgresql.org/docs/current/indexes-ordering.html)
### Build

1. Refactor task list queries to use keyset (cursor) pagination rather than offset/limit.
1. Add cursor parameters to API routes and update query logic in controllers.
1. Ensure indexes support sorting by created_at and id to allow stable ordering.
1. Update front‑end to consume cursor-based pagination.
### Assignments

- Commit query changes and update API docs.
- Write an ADR detailing the pagination strategy and why it was chosen.
### DoD Checklist

- [ ] Keyset pagination works and returns expected results.
- [ ] Backward pagination (previous page) is supported or noted if intentionally omitted.
- [ ] ADR explains trade-offs between offset and cursor approaches.
### Commit Message

`feat(db): implement keyset pagination and update API/ADR`
### Outcome Artifacts

- Updated queries using cursor-based pagination.
- ADR in `/docs/adrs` explaining pagination choices.
### Self‑Review Questions

- Does keyset pagination improve performance for large tables?
- How does the API handle invalid or expired cursors?

# Day 10 — Pagination
![Day](https://img.shields.io/badge/Day-10-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement pagination to handle long task lists efficiently.
### Timebox

~3 hours
### Study

- [Pagination patterns in web UIs](https://uxdesign.cc/pagination-best-practices-9748bf02ba79)
- [Next.js router API](https://nextjs.org/docs/app/api-reference/functions/use-router)
### Build

1. Add client-side pagination controls (previous/next, page numbers).
1. Synchronize pagination state with query parameters for shareable URLs.
1. Plan API shape for server-side pagination (offset or cursor).
1. Refactor list component to consume paginated data.
### Assignments

- Commit pagination implementation and update tests.
- Document the pagination strategy and API shape.
### DoD Checklist

- [ ] Pagination controls render and function correctly.
- [ ] URL reflects current page.
- [ ] Documentation updated to describe pagination approach.
### Commit Message

`feat(list): implement client-side pagination and plan server API`
### Outcome Artifacts

- Pagination controls in the tasks UI.
- Documentation of pagination strategy.
### Self‑Review Questions

- Does the pagination UI degrade gracefully on small screens?
- Are query parameters sanitized for invalid page numbers?

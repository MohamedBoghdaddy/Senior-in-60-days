# Day 09 — List Filters & Sorting
![Day](https://img.shields.io/badge/Day-09-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Add filtering, sorting, and query parameter handling to the tasks list.
### Timebox

~3 hours
### Study

- [React list rendering guidance](https://react.dev/learn/rendering-lists)
- [Next.js search params handling](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
### Build

1. Implement filter and sort controls for the tasks list (e.g., by status, priority, date).
1. Sync filter and sort state with URL query parameters.
1. Ensure stable sorting fields and sanitize input values.
1. Provide empty, loading, and error states for the list.
### Assignments

- Commit the filtering and sorting implementation.
- Update documentation to describe query parameter contract.
### DoD Checklist

- [ ] Filtering and sorting update URL correctly.
- [ ] Stable keys used for list items.
- [ ] Tests verify filter/sort behaviours.
### Commit Message

`feat(list): add filtering and sorting with query parameter sync`
### Outcome Artifacts

- Updated tasks list component with filters and sorting.
- Documentation of query params contract.
### Self‑Review Questions

- Are the filter options comprehensive?
- Do the query parameters reflect UI state accurately?

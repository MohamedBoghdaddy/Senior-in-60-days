# Day 13 — Next.js App Router & Caching
![Day](https://img.shields.io/badge/Day-13-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Deepen understanding of the App Router and implement caching strategies.
### Timebox

~3 hours
### Study

- [Next.js App Router advanced docs](https://nextjs.org/docs/app/building-your-application/routing)
- [Next.js caching strategies](https://nextjs.org/docs/app/building-your-application/caching)
### Build

1. Split data fetching between server and client components as appropriate.
1. Implement route handlers (e.g., `/api/tasks`) using Next.js API routes or server actions.
1. Apply caching headers or revalidation options to ensure fresh data without redundant fetches.
1. Document decisions in an ADR regarding rendering boundaries and caching choices.
### Assignments

- Commit rendering boundary and caching implementations.
- Write an ADR summarizing server/client component decisions.
### DoD Checklist

- [ ] Data fetching occurs in the correct layer (server or client).
- [ ] Caching controls prevent unnecessary network requests.
- [ ] ADR committed to `/docs/adrs`.
### Commit Message

`feat(app): implement server/client boundaries and caching strategy`
### Outcome Artifacts

- Server route handlers or actions implemented.
- ADR capturing rendering and caching trade-offs.
### Self‑Review Questions

- Do server components improve performance or complexity?
- Are caching settings appropriate for data freshness?

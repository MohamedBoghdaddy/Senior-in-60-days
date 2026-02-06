# Day 30 — Caching
![Day](https://img.shields.io/badge/Day-30-blue) ![Area](https://img.shields.io/badge/Area-performance-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement server-side caching for expensive read queries.
### Timebox

~3 hours
### Study

- [Redis caching best practices](https://redis.io/docs/manual/keyspace-events/)
- [Cache invalidation strategies](https://martinfowler.com/articles/cache-invalidation.html)
### Build

1. Add a caching layer for heavy list queries (e.g., tasks per org) using Redis.
1. Define cache keys and TTL; implement read-through caching where the first request populates the cache.
1. Implement invalidation rules on writes (create, update, delete) to ensure stale data isn’t served.
1. Document caching boundaries and where caching should not be used (e.g., user-specific data).
### Assignments

- Commit caching implementation and invalidation logic.
- Write an ADR describing caching trade-offs and invalidation strategy.
### DoD Checklist

- [ ] Cache hits improve response times significantly.
- [ ] Invalidation logic ensures data consistency.
- [ ] ADR committed in `/docs/adrs`.
### Commit Message

`feat(cache): implement Redis caching with invalidation and document strategy`
### Outcome Artifacts

- Caching layer integrated with API.
- ADR detailing caching decisions.
### Self‑Review Questions

- How do we avoid cache stampedes when keys expire?
- Is TTL configured to balance performance and freshness?

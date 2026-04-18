# Incident: Database Slowdown

## Timeline

- 02:10 UTC: Monitoring alerted on PostgreSQL query latency rising above 1.5s.
- 02:18 UTC: Teams observed backend paged through slow queries during listing search.
- 02:30 UTC: A slow query plan was identified for an unindexed filter.
- 02:45 UTC: Index added and service latency began returning to normal.

## Root cause

- A new filter was introduced without a supporting index on `listings(status, created_at)`.

## Impact

- Search requests were delayed by 3x.
- Some users experienced timeouts, and cache miss penalties increased.

## Mitigation and resolution

- Added the missing composite index.
- Warmed the Redis cache for hot queries.
- Restarted the backend to clear residual query plan cache.

## Prevention

- Implement query plan reviews for new filters.
- Add database monitoring alerts for slow query count and missing indexes.
- Use schema evolution checks in CI.

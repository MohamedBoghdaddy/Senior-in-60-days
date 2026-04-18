# Distributed Cache

## Requirements
- Reduce database load for repeated reads.
- Support shared state across service instances.
- Handle eviction, consistency, and invalidation.

## Scale estimation
- 100K cache reads per second.
- 10M cached keys.
- 50K cache writes per second.

## APIs
- Internal cache operations exposed through client libraries.
- Management API: `GET /cache/stats`, `POST /cache/invalidate`.

## Data model
- Key-value pairs with TTL and optional metadata.

## High-level architecture
- Redis or similar cluster for distributed caching.
- Cache-aside pattern for read-through behavior.
- Invalidation events for write-heavy updates.

## Critical components
- **Cache key design**: deterministic and collision-resistant.
- **Eviction policy**: TTL with LRU or LFU for hot data.
- **Consistency model**: eventual consistency is acceptable for many reads.

## Scaling strategy
- Partition keys across shards.
- Keep hot keys on dedicated nodes.
- Use local cache layers for ultra-low latency hot entries.

## Bottlenecks
- Cache churn from high write rates.
- Stale reads after underlying data changes.
- Network latency between app and cache cluster.

## Tradeoffs
- Strong consistency vs faster cached reads.
- Large TTLs for speed vs potential stale data.
- Cache-aside complexity vs direct database access.

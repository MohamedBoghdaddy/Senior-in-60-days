# Scaling Guide

## Growth stages

### Small usage

- Single backend instance.
- One primary PostgreSQL database.
- One MongoDB instance for unstructured content.
- Redis cache for session and hot data.
- Focus on correctness and observability.

### Medium usage

- Add backend replicas behind load balancing.
- Separate read replicas for PostgreSQL and MongoDB.
- Use Redis cluster for sharded caching and rate limit state.
- Push heavy work to BullMQ workers.

### Large usage

- Partition Postgres tables using logical shards.
- Scale MongoDB collections based on document type.
- Use CDN or edge cache for static data and frontend.
- Deploy AI service separately with autoscaling.

## Bottlenecks

- **Database query problems**: slow joins, missing indexes, row scans.
- **Cache churn**: too many writes and short TTLs reduce effectiveness.
- **Background queue growth**: backlog indicates processing bottleneck.
- **Rate limiting**: unbounded bursts consume capacity.

## Indexing

- Index filter columns used in WHERE clauses.
- Add composite indexes for multi-column sort operations.
- Avoid redundant indexes that increase write overhead.

## Caching

- Cache frequent reads with Redis.
- Use cache-aside for backend queries.
- Invalidate keys on writes or use short TTLs for dynamic data.

## Async processing

- Offload ingestion and AI enrichment to BullMQ.
- Use retry/backoff policies and dead-letter queues.
- Perform expensive transforms outside the request path.

## Read replicas

- Route read-only queries to replicas.
- Keep write traffic on primaries.
- Monitor replication lag and failover readiness.

## Rate limiting and fallbacks

- Enforce per-client limits with Redis.
- Degrade gracefully when backend load is high.
- Serve cached or stale-but-safe data if real-time processing is unavailable.

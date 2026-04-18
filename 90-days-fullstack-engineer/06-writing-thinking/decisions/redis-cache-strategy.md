# ADR: Redis Caching Strategy

## Status

Accepted

## Context

The backend must serve repeated search and listing read requests with low latency.

## Decision

Use Redis for cache-aside caching of listing details and rate limiting state.

## Consequences

- improves response time for frequently requested items.
- adds cache invalidation complexity.
- requires Redis health monitoring to avoid stale reads.

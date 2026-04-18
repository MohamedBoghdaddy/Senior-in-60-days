# Rate Limiter

## Requirements
- Prevent abuse by limiting requests per client.
- Support different limits for authenticated users, API keys, and anonymous traffic.
- Enforce global and endpoint-specific thresholds.

## Scale estimation
- 1M users.
- 50K requests per second across services.
- 20K token-based authenticated requests per second.

## APIs
- Rate limit is enforced transparently on existing APIs.
- Optional management API: `GET /rate-limit-status`.

## Data model
- `rate_limit_bucket(client_id, window_key, count, expires_at)` stored in Redis.

## High-level architecture
- API gateway or middleware intercepts requests.
- Token bucket or leaky bucket implementation in Redis.
- Fallback to a slower in-memory check if Redis is unavailable.

## Critical components
- **Policy store**: configuration for default and custom limits.
- **Enforcement interceptor**: atomically increments counters in Redis.
- **Penalty state**: temporary block when limits are exceeded.

## Scaling strategy
- Use Redis cluster with sharded keys.
- Keep counters small and TTL-based.
- Apply client grouping by API key, user role, or IP.

## Bottlenecks
- Single Redis instance limits throughput.
- Race conditions on concurrent increments.
- False positives from shared IPs.

## Tradeoffs
- Strict per-client limits vs usability for bursty workloads.
- In-memory fallback avoids outages but may weaken protection.
- Rate limits at gateway vs service-level enforcement.

# Interview Stories

## 1. Scaling a critical endpoint

**Situation:** The listing search endpoint became a bottleneck as user traffic grew.
**Task:** Improve performance without changing the front-end behavior.
**Action:** I identified missing composite indexes, introduced Redis caching for listing details, and added query validation to prevent unbounded scans.
**Result:** Search latency dropped by 60%, the cache hit rate improved, and the system handled peak traffic with fewer backend replicas.

## 2. Handling a 2AM outage

**Situation:** An external AI provider outage caused the AI insights page to fail during off-hours.
**Task:** Restore user-facing stability and prevent the same failure mode.
**Action:** I implemented retry/backoff logic in the AI service and a structured fallback response so the rest of the platform remained available.
**Result:** The outage impact was reduced from full page failure to degraded yet usable insights, and the incident was documented for faster future response.

## 3. Convincing the team to add caching

**Situation:** The team initially preferred raw database reads for simplicity.
**Task:** Demonstrate why caching would improve user experience and reliability.
**Action:** I shared a data-driven analysis of repeated query patterns, explained stale-data tradeoffs, and proposed a cache-aside strategy with short TTLs.
**Result:** We adopted Redis caching for high-volume listing reads, which improved throughput and reduced database load while preserving data freshness.

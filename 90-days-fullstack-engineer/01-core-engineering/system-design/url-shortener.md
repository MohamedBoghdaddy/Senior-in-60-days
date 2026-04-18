# URL Shortener

## Requirements
- Accept long URLs and return a short alias.
- Redirect requests from alias to long URL.
- Track click counts and basic analytics.
- Support millions of redirects and high read traffic.

## Scale estimation
- 100M stored URLs.
- 100K reads per second at peak.
- 10K writes per second during campaigns.

## APIs
- `POST /shorten` - create a short URL.
- `GET /{alias}` - redirect to original URL.
- `GET /metrics/{alias}` - analytics for owner.

## Data model
- `url_mapping(alias, original_url, owner_id, created_at, expires_at)`
- `click_event(alias, timestamp, referrer)`

## High-level architecture
- API gateway for request routing
- URL service for alias generation and validation
- cache layer for hot alias lookups
- write-through analytics queue

## Critical components
- **Alias generation**: deterministic base62 hashing or random collision-safe generation.
- **Redirect path**: look up alias in cache, fallback to database.
- **Analytics ingestion**: queue click events to avoid blocking redirects.

## Scaling strategy
- Cache hot URLs in Redis with strong TTLs.
- Use consistent hashing or sharded keys for database writes.
- Separate read path from write path for redirects and metrics.

## Bottlenecks
- Cold alias lookups on first access.
- Collisions in alias generation.
- Analytics write amplification under high read volumes.

## Tradeoffs
- Short alias length vs collision probability.
- Cache staleness vs real-time traffic stats.
- Using a relational DB for metadata vs NoSQL for high ingest.

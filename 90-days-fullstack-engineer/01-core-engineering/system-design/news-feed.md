# News Feed

## Requirements
- Personalized feed for users.
- Support content ranking, filtering, and refresh.
- Enable timeline updates and pagination.

## Scale estimation
- 20M active users.
- 200K feed requests per second.
- 1B content items.

## APIs
- `GET /feed` - fetch user feed.
- `POST /interactions` - record likes, comments, shares.

## Data model
- `content(id, publisher_id, type, created_at, metadata)`
- `feed_item(user_id, content_id, score, inserted_at)`
- `interaction(user_id, content_id, type, created_at)`

## High-level architecture
- Event ingestion pipeline for content and engagement.
- Feed generation service for pre-computed and real-time recommendations.
- Cache layer for hot feed windows.

## Critical components
- **Ranking engine**: combine recency, personalization, and business signals.
- **Cache invalidation**: keep feeds fresh while limiting recomputation.
- **Interaction capture**: use async writes to event store.

## Scaling strategy
- Precompute feeds for high-value users.
- Shard feed entries by user id.
- Apply paging and cursor-based navigation.

## Bottlenecks
- Feed generation cost for active users.
- Write amplification from interactions.
- Recomputation when content volume spikes.

## Tradeoffs
- Precomputed feeds reduce latency but cost more storage.
- Real-time generation avoids stale personalization but adds CPU load.
- Simplified ranking logic improves reliability at the expense of nuance.

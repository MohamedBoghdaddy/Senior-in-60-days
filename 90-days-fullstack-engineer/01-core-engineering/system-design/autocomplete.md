# Autocomplete

## Requirements
- Provide instant suggestions as users type.
- Support prefix matching and relevance ranking.
- Scale to tens of millions of indexed terms.

## Scale estimation
- 50M suggestion terms.
- 100K query requests per second.
- Frequent updates from user activity.

## APIs
- `GET /autocomplete?q=term` - return suggestions.
- `POST /autocomplete/index` - update indexed terms.

## Data model
- `term(id, text, score, category, updated_at)`

## High-level architecture
- Indexing service maintains term data.
- Query service uses a search engine or trie cache.
- Cache hot suggestions in Redis or in-memory.

## Critical components
- **Query ranking**: combine prefix score, popularity, and recency.
- **Autocomplete index**: optimized for prefix scans.
- **Refresh strategy**: incremental updates for new terms.

## Scaling strategy
- Partition index by term range.
- Use a dedicated search index like Elasticsearch or Redis.
- Cache top results for popular prefixes.

## Bottlenecks
- Long prefixes with a large candidate set.
- Index refresh latency.
- Memory pressure for in-memory structures.

## Tradeoffs
- Using a search engine vs custom data structure.
- Real-time update latency vs index performance.
- Broad suggestions vs narrow, precise results.

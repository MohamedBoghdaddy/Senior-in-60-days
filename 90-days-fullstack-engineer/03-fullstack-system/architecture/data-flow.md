# Data Flow

## Request flow
1. Frontend sends authenticated request to backend API.
2. Backend validates JWT, enforces RBAC, and checks rate limits.
3. Backend reads from Redis cache or Postgres/Mongo if cache miss.
4. Backend returns results to the client and updates cache asynchronously.

## Background flow
1. User actions or external ingestion triggers jobs into BullMQ.
2. Workers process jobs and write results to Postgres and Mongo.
3. Some jobs invoke the AI service for enrichment.
4. AI results are stored in MongoDB and surfaced by backend endpoints.

## AI interaction flow
1. Backend collects structured data and sends a POST to AI service.
2. AI service validates request schema and calls the model.
3. The AI service retries transient failures and falls back to a cached default.
4. AI response is validated, normalized, and returned to backend.

## Failure path examples
- **Cache failure**: backend reads directly from the database.
- **AI timeout**: fallback output is returned with a warning.
- **DB write error**: job is retried or moved to a dead-letter queue.

# Architecture Tradeoffs

## Polyglot persistence
- **Choice**: PostgreSQL for relational integrity, MongoDB for unstructured AI data.
- **Tradeoff**: additional operational burden vs flexibility for mixed workloads.
- **Rationale**: business entities and joins are best modeled in Postgres while AI artifacts, documents, and metadata benefit from Mongo's schema flexibility.

## Service split
- **Choice**: backend API + AI microservice.
- **Tradeoff**: cross-service latency vs isolated failure domains.
- **Rationale**: separating the AI service enables safe retries, fallback behavior, and distinct scaling profiles.

## Queue-based processing
- **Choice**: BullMQ for background jobs.
- **Tradeoff**: more complexity vs better reliability for ingestion and AI enrichment.
- **Rationale**: asynchronous processing offloads heavy tasks from the request path and improves resilience.

## Authentication and RBAC
- **Choice**: JWT access + refresh tokens.
- **Tradeoff**: token handling complexity vs stateless scalability.
- **Rationale**: stateless auth supports horizontal scaling and keeps session state minimal.

# System Walkthrough

## Architecture tour

The platform is organized around service boundaries:

- **Frontend**: a React shell presenting dashboards, listings, details, and AI insight pages.
- **Backend**: a Node.js API responsible for auth, data access, caching, and workflow orchestration.
- **AI service**: a FastAPI microservice providing structured document analysis.
- **Data layer**: PostgreSQL for relational business data, MongoDB for unstructured AI artifacts, Redis for caching and rate limiting.

## Data flow

1. Users request a listing page through the frontend.
2. The backend authenticates the request, checks cache, and fetches from Postgres/Mongo.
3. The AI service is invoked asynchronously for document scoring.
4. Results are returned to the UI and stored back into MongoDB for future retrieval.

## Failure handling points

- **Auth layer** returns clear 401/403 responses.
- **Cache fallback** reads directly from the database when Redis fails.
- **Background jobs** are retried through BullMQ and tracked for failures.
- **AI service** retries external calls and returns fallback data when needed.

## Scaling explanation

- Stateless backend instances are scaled horizontally.
- Redis handles shared rate limit state and hot cache traffic.
- Postgres and MongoDB use read replicas and partitioned collections when necessary.
- Kubernetes manifests allow each service to scale independently.

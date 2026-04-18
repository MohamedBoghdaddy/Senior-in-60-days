# Architecture: Production-Grade Multi-Service Platform

## System boundaries
- **API backend**: Node.js service that handles authentication, RBAC, listing search, cache coordination, and orchestration.
- **AI service**: FastAPI microservice responsible for scoring documents, extracting structured insights, and generating recommendations.
- **Frontend shell**: React application for authenticated dashboards, search, detail views, and AI insights.
- **Data services**: PostgreSQL for relational business data, MongoDB for unstructured content and AI-derived artifacts, Redis for cache and rate limiting.
- **Background workers**: BullMQ-based job processing for ingestion, analytics, and AI fallback retries.

## Service responsibilities
- **Backend**: manage user sessions, enforce access rules, coordinate data flows between DBs and AI service, and provide stable REST endpoints.
- **AI service**: accept structured prompts, validate responses, retry safely, and return normalized insights.
- **Frontend**: present operational dashboards, search/listing workflow, and AI-driven decisions transparently.
- **Infra**: containerized deployment, environment-controlled configuration, and Kubernetes manifests for staging.

## Key design principles
- **Clear separation** between API and AI inference services.
- **Environment-only secrets** through `.env` and deployment configs.
- **Responsibility-based service boundaries** to limit blast radius.
- **Structured logging** at each service boundary for traceability.

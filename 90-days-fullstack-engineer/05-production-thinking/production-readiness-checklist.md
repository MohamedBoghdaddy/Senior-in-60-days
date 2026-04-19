# Production Readiness Checklist

Run this checklist against any service before deploying to production.
Check each item and fill in the status and notes.

---

## Service: [Name] — Reviewed: [Date] — Reviewer: [Name]

---

## 1. Health and lifecycle

| Item | Status | Notes |
|------|--------|-------|
| Health check endpoint exists (`GET /health`) | | |
| Health check verifies DB connection | | |
| Health check verifies cache connection | | |
| Liveness probe configured in K8s | | |
| Readiness probe configured in K8s | | |
| Graceful shutdown handles SIGTERM | | |
| In-flight requests complete before shutdown | | |
| Startup validates required dependencies before binding port | | |
| Process exits with non-zero code on fatal startup failure | | |

---

## 2. Logging and observability

| Item | Status | Notes |
|------|--------|-------|
| Structured JSON logging (not string logs) | | |
| Every request log includes: method, path, status, duration_ms | | |
| Every request log includes: requestId, userId (if authenticated) | | |
| Error logs include: requestId, error code, message, stack (non-prod only) | | |
| Log levels are appropriate (info/warn/error — no debug in prod) | | |
| Prometheus metrics endpoint exposed (`GET /metrics`) | | |
| `http_requests_total` counter with method/route/status labels | | |
| `http_request_duration_seconds` histogram | | |
| Distributed trace context propagated (traceparent header) | | |

---

## 3. Error handling

| Item | Status | Notes |
|------|--------|-------|
| Error responses follow consistent schema (ProblemDetails or equivalent) | | |
| Stack traces are NOT returned to clients in production | | |
| Operational errors (expected) vs programmer errors (unexpected) are classified | | |
| 500 errors are logged with full context | | |
| External service failures have fallback behavior (not hard crash) | | |
| Database errors do not expose table/column names to clients | | |

---

## 4. Authentication and authorization

| Item | Status | Notes |
|------|--------|-------|
| JWT secret is strong (32+ chars, random) | | |
| JWT access tokens have short expiry (15min–1h) | | |
| Refresh tokens are stored securely (not in JWT payload) | | |
| Endpoints requiring auth have auth middleware applied | | |
| Auth middleware is not optional — no accidental public endpoints | | |
| RBAC enforced at service layer, not just route level | | |

---

## 5. Input validation and security

| Item | Status | Notes |
|------|--------|-------|
| All user input is validated at the API boundary | | |
| Validation errors return 422 with field-level details | | |
| SQL queries use parameterized statements (no string interpolation) | | |
| File upload endpoints validate MIME type and size | | |
| Rate limiting on all public endpoints | | |
| Rate limiting on auth endpoints (stricter) | | |
| CORS is configured explicitly (not wildcard `*` in production) | | |
| Helmet or equivalent security headers middleware applied | | |
| No secrets in code, environment variables, or Git history | | |

---

## 6. Database and data integrity

| Item | Status | Notes |
|------|--------|-------|
| Database connection pooling configured | | |
| Pool size is appropriate (not too large, not 1) | | |
| Slow query threshold is monitored | | |
| Migrations are reversible (or at least safe) | | |
| Zero-downtime migration pattern followed for schema changes | | |
| Indexes exist for all foreign keys | | |
| Indexes exist for all common filter/sort columns | | |

---

## 7. Reliability patterns

| Item | Status | Notes |
|------|--------|-------|
| External API calls have timeout set | | |
| Retry logic with exponential backoff for transient failures | | |
| Circuit breaker for external dependencies (or timeout fallback) | | |
| Background jobs have retry configuration | | |
| Background jobs have a dead letter queue or failed job handling | | |
| Cache failure does not crash the API (graceful cache miss) | | |

---

## 8. Container and infrastructure

| Item | Status | Notes |
|------|--------|-------|
| Container runs as non-root user | | |
| Docker image is multi-stage (build artifact only in final image) | | |
| Image uses specific tag (not `latest`) | | |
| `.dockerignore` excludes node_modules, .env, .git | | |
| Container image scanned for CVEs | | |
| Resource limits (CPU, memory) set in K8s manifest | | |
| Secrets in K8s Secrets (not ConfigMaps or hardcoded in manifests) | | |
| Rolling update strategy configured (not Recreate) | | |

---

## 9. CI/CD

| Item | Status | Notes |
|------|--------|-------|
| CI pipeline runs on every push to main | | |
| CI runs linting | | |
| CI runs tests | | |
| CI fails if tests fail | | |
| Container image built in CI | | |
| Security scan runs in CI | | |
| Deployment requires CI pass | | |

---

## 10. Documentation

| Item | Status | Notes |
|------|--------|-------|
| README describes how to run the service locally | | |
| README describes environment variables required | | |
| API endpoints documented (OpenAPI or equivalent) | | |
| Architecture decision records exist for key choices | | |
| Runbook exists for common operational issues | | |

---

## Summary

Total items checked: ___ / 60

**Blockers (must fix before deploy):**
1.
2.
3.

**Should fix (can deploy but prioritize):**
1.
2.

**Nice to have (next sprint):**
1.

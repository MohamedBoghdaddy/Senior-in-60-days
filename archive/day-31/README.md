# Day 31 — Structured Logging & Monitoring
![Day](https://img.shields.io/badge/Day-31-blue) ![Area](https://img.shields.io/badge/Area-performance-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Add structured logs, error tracking, and health endpoints for observability.
### Timebox

~3 hours
### Study

- [pino logging library](https://getpino.io/)
- [Sentry for Node](https://docs.sentry.io/platforms/node/)
### Build

1. Integrate a structured logging library such as Pino; include traceId, userId, orgId in each log entry.
1. Set up Sentry (or similar) for error tracking and performance monitoring; instrument API and front‑end.
1. Add health and readiness endpoints to the API; include checks for database, cache, and queue connections.
1. Create dashboards and alert rules for error rates and latency thresholds.
### Assignments

- Commit logging and error tracking setup.
- Document how to interpret logs and use dashboards in `observability.md`.
### DoD Checklist

- [ ] Structured logs written for each request with proper context.
- [ ] Errors captured by Sentry with stack traces.
- [ ] Health endpoints return appropriate status codes and details.
### Commit Message

`feat(obs): implement structured logging, error tracking, and health endpoints`
### Outcome Artifacts

- Logger configuration and middleware.
- Sentry integration and DSN configuration.
- Observability documentation.
### Self‑Review Questions

- Can we trace a request across multiple services using the logs?
- Are alert thresholds set to detect problems early without false positives?

# Day 15 — API Skeleton
![Day](https://img.shields.io/badge/Day-15-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Set up the Express server with a clean structure and centralized error handling.
### Timebox

~3 hours
### Study

- [Express routing docs](https://expressjs.com/en/guide/routing.html)
- [Node.js event loop guide](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)
### Build

1. Scaffold an Express app with `routes`, `controllers`, `services`, and `repositories` directories.
1. Implement a health endpoint (`GET /health`) returning status and timestamp.
1. Create a centralized error handling middleware that returns a standard error format (code, message, details, traceId).
1. Add request ID middleware to attach a unique ID to each incoming request for tracing.
### Assignments

- Commit API skeleton with health endpoint and error handler.
- Document API structure in the README or docs.
### DoD Checklist

- [ ] Express server starts without errors.
- [ ] Health endpoint responds with JSON and status 200.
- [ ] Error handler catches both synchronous and asynchronous errors.
### Commit Message

`feat(api): scaffold Express server with health endpoint and error handling`
### Outcome Artifacts

- API source files in `apps/api`.
- Error handler and request ID middleware.
### Self‑Review Questions

- Does the current structure separate concerns effectively?
- Is the error format clear and extensible?

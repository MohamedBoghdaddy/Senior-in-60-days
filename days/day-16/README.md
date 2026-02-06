# Day 16 — Input Validation & Error Contract
![Day](https://img.shields.io/badge/Day-16-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Validate API inputs and define a consistent error contract.
### Timebox

~3 hours
### Study

- [Zod documentation](https://zod.dev/)
- [Express error handling docs](https://expressjs.com/en/guide/error-handling.html)
### Build

1. Add validation middleware using Zod (or Joi) for route params, query parameters, and request bodies.
1. Extend the error handler to include validation errors with appropriate HTTP status codes (e.g., 400 for bad request).
1. Define and document a standard error response shape: `{ code, message, details, traceId }`.
1. Write tests covering valid and invalid input scenarios.
### Assignments

- Commit validation middleware and update error handling.
- Document the error contract in API docs or README.
### DoD Checklist

- [ ] Invalid requests return 400 with descriptive error messages.
- [ ] Standard error shape used consistently.
- [ ] Tests cover both success and failure paths.
### Commit Message

`feat(api): add input validation and standardize error responses`
### Outcome Artifacts

- Validation schemas and middleware functions.
- Updated error handler supporting validation errors.
### Self‑Review Questions

- Are all external inputs validated adequately?
- Does the error contract contain enough information without leaking internals?

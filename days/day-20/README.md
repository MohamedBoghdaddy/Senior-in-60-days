# Day 20 — OpenAPI & Integration Tests
![Day](https://img.shields.io/badge/Day-20-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Generate and document API specifications and write integration tests.
### Timebox

~3 hours
### Study

- [OpenAPI specification](https://www.openapis.org)
- [Supertest documentation](https://www.npmjs.com/package/supertest)
### Build

1. Generate OpenAPI (Swagger) documentation for all existing endpoints with examples.
1. Expose the spec at an endpoint such as `/api-docs`.
1. Set up integration test environment using Supertest (or similar) to call real API routes against a test database.
1. Write integration tests covering critical API flows (e.g., create and list tasks, unauthorized access).
### Assignments

- Commit generated OpenAPI spec and docs endpoint.
- Ensure integration tests run in CI.
### DoD Checklist

- [ ] OpenAPI UI accessible and shows accurate schemas.
- [ ] Integration tests pass against a test DB.
- [ ] Docs updated to explain how to run API tests.
### Commit Message

`docs(api): generate OpenAPI spec and implement integration tests`
### Outcome Artifacts

- `/api-docs` route serving Swagger UI.
- Integration test files in the test suite.
### Self‑Review Questions

- Do tests cover success and failure scenarios?
- Is the API spec kept in sync with code via CI?

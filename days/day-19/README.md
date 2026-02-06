# Day 19 — API Endpoints v1
![Day](https://img.shields.io/badge/Day-19-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement initial CRUD endpoints for core resources (orgs, projects, tasks).
### Timebox

~4 hours
### Study

- [RESTful API design principles](https://restfulapi.net/)
- [Express routing guide](https://expressjs.com/en/guide/routing.html)
### Build

1. Create controllers and routes for organizations, projects, and tasks (create, read, update, delete).
1. Apply validation, authentication, and RBAC middleware to each route.
1. Return proper HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 422).
1. Implement idempotency keys for POST and PUT requests to prevent duplicates.
### Assignments

- Commit initial API endpoints and unit tests.
- Update OpenAPI spec with routes and request/response schemas.
### DoD Checklist

- [ ] Endpoints return correct status codes and shape.
- [ ] Middleware executed in correct order (auth → RBAC → validation → handler).
- [ ] Idempotency keys correctly deduplicate requests.
### Commit Message

`feat(api): implement CRUD endpoints for orgs, projects, and tasks with middleware`
### Outcome Artifacts

- Controllers and route files for each resource.
- OpenAPI updated with new endpoints.
### Self‑Review Questions

- Are the routes RESTful and intuitive?
- Do error responses follow the standard contract?

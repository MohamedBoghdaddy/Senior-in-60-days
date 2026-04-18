# Day 18 — RBAC Middleware
![Day](https://img.shields.io/badge/Day-18-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement role-based access control to protect resources within organizations.
### Timebox

~3 hours
### Study

- [Role-based access control (RBAC) patterns](https://auth0.com/docs/get-started/authorization/rbac)
- [Express middleware patterns](https://expressjs.com/en/guide/writing-middleware.html)
### Build

1. Define roles (owner, admin, member) and store them in the database (e.g., membership table).
1. Implement RBAC middleware that checks the user’s role in the organization before executing route handlers.
1. Add tests for successful and forbidden access scenarios (401 vs 403).
1. Document RBAC rules and how to assign roles.
### Assignments

- Commit RBAC middleware and tests.
- Update API documentation to include authorization details.
### DoD Checklist

- [ ] Unauthorized users receive 401; authorized but insufficient role receives 403.
- [ ] RBAC logic encapsulated in reusable middleware.
- [ ] Tests cover all roles and paths.
### Commit Message

`feat(auth): add role-based access control middleware and tests`
### Outcome Artifacts

- Middleware functions for RBAC.
- Test suite covering role checks.
### Self‑Review Questions

- Are all sensitive routes protected by RBAC?
- Does the middleware support flexible role assignment (multiple roles, hierarchies)?

# Day 17 — Auth Setup
![Day](https://img.shields.io/badge/Day-17-blue) ![Area](https://img.shields.io/badge/Area-backend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement JWT-based authentication with access and refresh tokens.
### Timebox

~4 hours
### Study

- [JWT introduction](https://jwt.io/introduction)
- [OWASP authentication cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
### Build

1. Implement login endpoint issuing access and refresh tokens.
1. Securely store hashed refresh tokens in the database and implement rotation.
1. Add middleware to verify access tokens and attach `userId` and `orgId` to the request context.
1. Provide logout and token revocation endpoint.
### Assignments

- Commit auth implementation (login/logout, token issuance, middleware).
- Document auth flow and security considerations.
### DoD Checklist

- [ ] Users can log in and receive both tokens.
- [ ] Protected endpoints validate tokens properly and return 401 if invalid.
- [ ] Refresh token rotation works and old tokens are revoked.
### Commit Message

`feat(auth): implement JWT authentication with token rotation`
### Outcome Artifacts

- Auth routes (`/auth/login`, `/auth/logout`) implemented.
- Middleware for token verification.
- Docs describing token flows and expiration.
### Self‑Review Questions

- Are tokens signed with strong keys and reasonable lifetimes?
- Is refresh token storage and rotation handled securely?

# Day 32 — Rate Limiting & Security Hardening
![Day](https://img.shields.io/badge/Day-32-blue) ![Area](https://img.shields.io/badge/Area-security-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Protect the application from abuse and improve overall security posture.
### Timebox

~3 hours
### Study

- [express-rate-limit documentation](https://www.npmjs.com/package/express-rate-limit)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CORS and Helmet](https://expressjs.com/en/resources/middleware/cors.html)
### Build

1. Add rate-limiting middleware to protect against brute force and scraping attacks; scope limits by IP and user ID.
1. Enable Helmet middleware to set security-related HTTP headers.
1. Review and restrict CORS policies to allowed origins only.
1. Review secrets management and environmental variables (ensure no secrets committed).
### Assignments

- Commit security middleware and configuration.
- Perform a security audit and document findings in `SECURITY_AUDIT.md`.
### DoD Checklist

- [ ] Rate limits trigger 429 responses when thresholds exceeded.
- [ ] Security headers added by Helmet appear in responses.
- [ ] CORS only allows trusted origins.
### Commit Message

`feat(security): add rate limiting and security headers; audit secrets`
### Outcome Artifacts

- Rate limiting and security middleware in API code.
- Security audit document with identified risks and mitigations.
### Self‑Review Questions

- Are the rate limits appropriate for both anonymous and authenticated users?
- Have all secrets been removed from the codebase and secured via environment variables?

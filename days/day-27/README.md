# Day 27 — Audit Logging
![Day](https://img.shields.io/badge/Day-27-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Record audit logs for sensitive actions and expose them via an API.
### Timebox

~3 hours
### Study

- [Audit logging best practices](https://www.owasp.org/index.php/Logging_Cheat_Sheet)
- [Event sourcing patterns](https://martinfowler.com/eaaDev/EventSourcing.html)
### Build

1. Create triggers or service logic to insert audit entries on sensitive events (e.g., role changes, deletions).
1. Define an `audit_logs` table capturing action type, actor, timestamp, target, and metadata.
1. Implement an API endpoint to query audit logs with filters (e.g., by org, user, date).
1. Ensure audit logs are immutable (no updates or deletes).
### Assignments

- Commit audit logging logic and API endpoints.
- Add tests verifying logs are written and retrieved correctly.
### DoD Checklist

- [ ] Audit entries created on sensitive actions.
- [ ] Logs can be queried and filtered via API.
- [ ] No way to modify or delete audit logs.
### Commit Message

`feat(audit): implement audit logging for sensitive actions`
### Outcome Artifacts

- `audit_logs` table and triggers/service logic.
- Audit API route.
### Self‑Review Questions

- Which actions are considered sensitive and logged?
- How is audit data secured and protected from tampering?

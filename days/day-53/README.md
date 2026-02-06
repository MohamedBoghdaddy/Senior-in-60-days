# Day 53 — System Design & ADR Writing
![Day](https://img.shields.io/badge/Day-53-blue) ![Area](https://img.shields.io/badge/Area-system-design-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Consolidate architectural decisions and document them comprehensively.
### Timebox

~3 hours
### Study

- [ADR template (MADR)](https://adr.github.io/madr/)
- [Writing effective system design docs](https://www.pagerduty.com/blog/engineering-design-docs/)
### Build

1. Write a full system design document (5–8 pages) covering all components: web, API, database, queue, MongoDB, Firebase, and mobile.
1. Summarize major decisions made across the project in ADRs (auth strategy, RLS design, caching, offline sync, MongoDB/Firebase usage).
1. Include diagrams (e.g., sequence, component, deployment) using Mermaid or similar syntax.
### Assignments

- Commit `docs/system-design.md` and ADRs into `/docs/adrs`.
- Review ADRs for completeness and clarity.
### DoD Checklist

- [ ] System design document explains architecture and trade-offs clearly.
- [ ] ADRs cover all major decisions with context and alternatives.
- [ ] Diagrams are readable and reflect the implementation accurately.
### Commit Message

`docs: finalize system design and ADRs`
### Outcome Artifacts

- Comprehensive system design doc.
- ADRs for all key decisions.
### Self‑Review Questions

- Are there any undocumented decisions that should be captured?
- Does the system design doc provide a clear onboarding path for new engineers?

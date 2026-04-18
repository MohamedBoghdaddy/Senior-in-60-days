# Day 44 — Conflict Resolution & Sync
![Day](https://img.shields.io/badge/Day-44-blue) ![Area](https://img.shields.io/badge/Area-mobile-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Decide and implement a strategy to resolve conflicts between offline and server data.
### Timebox

~2 hours
### Study

- [Conflict resolution strategies](https://www.mongodb.com/docs/manual/faq/change-streams-conflict-resolution/)
- [Offline sync patterns](https://docs.microsoft.com/en-us/xamarin/essentials/preferences)
### Build

1. Choose a conflict resolution strategy (server-wins, client-wins, merge).
1. Implement conflict detection when syncing queued operations.
1. Handle conflicts in the UI (e.g., show a banner or merge dialog).
1. Document trade-offs and future improvements in an ADR.
### Assignments

- Commit conflict resolution implementation.
- Write an ADR in `/docs/adrs` explaining the chosen strategy.
### DoD Checklist

- [ ] Conflicts are detected and resolved according to the chosen strategy.
- [ ] User feedback is clear when a conflict occurs.
- [ ] ADR explains reasoning and alternatives considered.
### Commit Message

`feat(sync): implement conflict resolution strategy for offline writes`
### Outcome Artifacts

- Conflict resolution logic integrated.
- ADR capturing conflict strategy.
### Self‑Review Questions

- Does the strategy balance correctness with user control?
- What future improvements could enhance the UX for conflict resolution?

# Day 37 — Firebase Decision & Setup
![Day](https://img.shields.io/badge/Day-37-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Decide on using Firebase for push notifications or Firestore security demo and set it up.
### Timebox

~2 hours
### Study

- [Firebase Cloud Messaging (FCM) docs](https://firebase.google.com/docs/cloud-messaging)
- [Firestore security rules](https://firebase.google.com/docs/firestore/security/rules)
### Build

1. Evaluate whether to implement push notifications (FCM) or Firestore security rules demonstration.
1. Create a Firebase project and configure necessary services (FCM or Firestore).
1. Store credentials securely in environment variables.
1. Write an ADR capturing the decision and reasoning.
### Assignments

- Commit Firebase configuration and credentials (secured).
- Add ADR explaining the decision.
### DoD Checklist

- [ ] Firebase project set up correctly.
- [ ] Credentials stored securely and not checked into source control.
- [ ] ADR committed with clear decision and alternatives.
### Commit Message

`feat(firebase): evaluate and set up FCM/Firestore with ADR`
### Outcome Artifacts

- Firebase config files.
- ADR documenting the decision.
### Self‑Review Questions

- What value does Firebase add compared to existing stack?
- How are costs and complexity weighed?

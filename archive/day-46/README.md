# Day 46 — Push Notifications & Deep Linking
![Day](https://img.shields.io/badge/Day-46-blue) ![Area](https://img.shields.io/badge/Area-mobile-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Integrate push notifications and support deep linking into specific screens.
### Timebox

~3 hours
### Study

- [React Native Firebase messaging](https://rnfirebase.io/messaging/usage)
- [React Navigation deep linking](https://reactnavigation.org/docs/deep-linking)
### Build

1. If using FCM: register device tokens, request permissions, and configure listeners for incoming notifications.
1. Implement server-side logic to send notifications on relevant events (e.g., task assignment).
1. Set up deep linking so notifications open the correct screen (e.g., a specific task).
1. Handle notification lifecycle when the app is foregrounded, backgrounded, or closed.
### Assignments

- Commit notification and deep linking implementation.
- Test notifications across iOS and Android (emulators or devices).
### DoD Checklist

- [ ] Notifications are delivered and handled correctly.
- [ ] Deep links navigate to the intended screen without errors.
- [ ] Permissions are requested and stored appropriately.
### Commit Message

`feat(mobile): integrate push notifications and deep linking`
### Outcome Artifacts

- Server code sending notifications.
- Mobile listeners handling notifications and linking.
### Self‑Review Questions

- Are notifications handled in all app states?
- Is deep linking robust across platform variations (iOS vs Android)?

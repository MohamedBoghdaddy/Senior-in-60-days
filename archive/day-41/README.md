# Day 41 — Expo Setup & Navigation
![Day](https://img.shields.io/badge/Day-41-blue) ![Area](https://img.shields.io/badge/Area-mobile-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Initialize the React Native client and basic navigation for the mobile app.
### Timebox

~3 hours
### Study

- [Expo documentation](https://docs.expo.dev/)
- [React Navigation](https://reactnavigation.org/docs/getting-started)
### Build

1. Initialize an Expo project with TypeScript support.
1. Set up React Navigation (stack and tab navigators).
1. Implement login and home screens with basic navigation flows.
1. Persist authentication tokens securely using `expo-secure-store` or `react-native-keychain`.
### Assignments

- Commit the Expo project setup and navigation implementation.
- Update the mobile README with build and run instructions.
### DoD Checklist

- [ ] Mobile app runs on both iOS and Android emulators.
- [ ] Navigation flows correctly from login to home screen.
- [ ] Tokens are stored securely.
### Commit Message

`feat(mobile): initialize Expo app and set up navigation with secure storage`
### Outcome Artifacts

- Expo project under `apps/mobile` or similar directory.
- Navigation configuration and screens.
### Self‑Review Questions

- Does navigation state persist across app reloads?
- Are security considerations around token storage addressed?

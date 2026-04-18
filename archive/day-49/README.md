# Day 49 — Unit & Integration Tests
![Day](https://img.shields.io/badge/Day-49-blue) ![Area](https://img.shields.io/badge/Area-testing-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Ensure comprehensive test coverage for new features (mobile, MongoDB, Firebase).
### Timebox

~3 hours
### Study

- [Vitest advanced usage](https://vitest.dev/guide/working-with-vitest.html)
- [Integration testing patterns](https://blog.logrocket.com/guide-integration-testing-node-apps/)
### Build

1. Add unit tests for MongoDB and Firebase modules (services, helpers).
1. Expand integration tests to cover new endpoints and cross-service flows.
1. Ensure tests handle offline and error scenarios appropriately.
1. Use test containers or mocks for external services when necessary.
### Assignments

- Commit new unit and integration tests.
- Update test scripts and CI configuration to include new suites.
### DoD Checklist

- [ ] Test coverage for critical paths > 80%.
- [ ] Tests run reliably in CI without flakiness.
- [ ] Mocks or test containers handle external dependencies cleanly.
### Commit Message

`test: add unit and integration tests for new modules`
### Outcome Artifacts

- Expanded test coverage.
- CI configuration updated.
### Self‑Review Questions

- Are external dependencies adequately mocked or containerized?
- Do integration tests reflect realistic usage scenarios?

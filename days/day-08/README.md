# Day 08 — Forms & Validation
![Day](https://img.shields.io/badge/Day-08-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Build robust forms with validation and consistent patterns.
### Timebox

~3 hours
### Study

- [react-hook-form documentation](https://react-hook-form.com/get-started)
- [Zod documentation](https://zod.dev/)
- [Accessible forms guidance](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML#forms)
### Build

1. Integrate `react-hook-form` with `zod` for schema validation.
1. Build Create Task and Edit Task forms with inline validation errors.
1. Write component tests covering form submission and validation flows.
1. Document a standard pattern for building forms in this project.
### Assignments

- Commit forms implementation and tests.
- Add the form pattern guide to the documentation.
### DoD Checklist

- [ ] Invalid data shows user-friendly errors.
- [ ] Valid submissions trigger API calls (mock or real).
- [ ] Tests cover both success and failure cases.
### Commit Message

`feat(forms): implement robust forms with validation and tests`
### Outcome Artifacts

- Form components with validation logic.
- Tests demonstrating correct form behaviour.
- Documentation for form patterns.
### Self‑Review Questions

- Do the forms handle all necessary input states?
- Are validation messages clear and accessible?

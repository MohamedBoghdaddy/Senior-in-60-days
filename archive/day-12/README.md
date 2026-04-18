# Day 12 — Accessibility Audit
![Day](https://img.shields.io/badge/Day-12-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Ensure the application meets accessibility standards and provides a great UX for all users.
### Timebox

~3 hours
### Study

- [Accessibility (a11y) guide](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
- [Testing accessibility with axe](https://www.deque.com/axe/)
### Build

1. Audit existing components with an accessibility testing tool (e.g., axe) to identify issues.
1. Add keyboard navigation and focus management; ensure modals trap focus.
1. Provide ARIA attributes and semantic HTML where needed.
1. Write tests verifying accessible interactions and roles.
### Assignments

- Fix accessibility issues discovered during the audit.
- Update `A11Y.md` with a checklist and guidelines.
### DoD Checklist

- [ ] Accessibility issues are fixed and tests pass.
- [ ] Keyboard navigation works across the UI.
- [ ] A11Y checklist committed and referenced in docs.
### Commit Message

`chore(a11y): audit and improve accessibility; add guidelines`
### Outcome Artifacts

- A11Y report and checklist in the docs.
- Improved UI components with proper semantics.
### Self‑Review Questions

- Are all interactive elements reachable via keyboard?
- Do ARIA attributes accurately reflect component roles?

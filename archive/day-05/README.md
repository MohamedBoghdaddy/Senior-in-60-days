# Day 05 — Design System Components
![Day](https://img.shields.io/badge/Day-05-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Build a foundational design system with reusable UI components.
### Timebox

~4 hours
### Study

- [Storybook for React](https://storybook.js.org/docs/react/get-started/introduction)
- [Tailwind component patterns](https://tailwindcss.com/docs)
### Build

1. Create a component library in `packages/ui` with Button, Input, Modal, and Toast components.
1. Use Tailwind CSS classes to style components consistently.
1. Optionally set up Storybook to document and preview components.
1. Ensure components support variants and proper accessibility attributes.
### Assignments

- Commit UI components and update documentation.
- If using Storybook, include sample stories for each component.
### DoD Checklist

- [ ] Components render correctly in isolation.
- [ ] Props and variants are documented.
- [ ] Accessibility attributes present (aria-* as needed).
### Commit Message

`feat(ui): add foundational components (Button, Input, Modal, Toast)`
### Outcome Artifacts

- Files under `packages/ui` for each component.
- Optional Storybook stories for components.
### Self‑Review Questions

- Do components handle different states (disabled, loading)?
- Are the components themeable and composable?

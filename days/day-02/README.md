# Day 02 — Tooling & Linting
![Day](https://img.shields.io/badge/Day-02-blue) ![Area](https://img.shields.io/badge/Area-devops-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Enforce uniform code style and static analysis across the repo.
### Timebox

~3 hours
### Study

- [ESLint documentation](https://eslint.org/docs/latest/use/getting-started)
- [Prettier documentation](https://prettier.io/docs/en/index.html)
- [TypeScript strict mode](https://www.typescriptlang.org/tsconfig)
### Build

1. Configure ESLint with React and TypeScript plugins.
1. Configure Prettier and integrate with ESLint.
1. Set up Husky pre-commit hooks to run lint and format.
1. Enable TypeScript strict mode in tsconfig.
### Assignments

- Verify linting surfaces errors and Prettier auto-formats code.
- Document code style guidelines in the repository.
### DoD Checklist

- [ ] Running `npm run lint` shows no errors.
- [ ] Prettier formats code on commit via hook.
- [ ] TypeScript strict mode enabled and passing.
### Commit Message

`chore(lint): configure ESLint, Prettier, and husky hooks`
### Outcome Artifacts

- ESLint config file created (`.eslintrc` or `eslint.config.js`).
- Prettier config file created (`.prettierrc`).
### Self‑Review Questions

- Do lint rules cover all common errors?
- Is Prettier integrated seamlessly with ESLint?

# Day 01 — Monorepo Bootstrap
![Day](https://img.shields.io/badge/Day-01-blue) ![Area](https://img.shields.io/badge/Area-devops-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Initialize the project repository with a clean monorepo structure for web, API, and shared packages.
### Timebox

~3 hours
### Study

- [pnpm workspaces documentation](https://pnpm.io/workspaces)
- [GitHub ignoring files guide](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
### Build

1. Initialize Git repository and create directory structure: `apps/web`, `apps/api`, `packages/shared`.
1. Configure package manager workspaces (e.g., pnpm or Yarn).
1. Add `.gitignore`, `.nvmrc`, and an initial `README.md` placeholder.
### Assignments

- Commit the scaffold and initial configuration.
- Update the root README explaining the repo structure.
### DoD Checklist

- [ ] Repository is initialized and builds successfully.
- [ ] `npm install` works for all packages.
- [ ] Folder structure matches specification.
### Commit Message

`feat(setup): initialize monorepo structure and tooling`
### Outcome Artifacts

- Created directories: `apps/`, `packages/`. 
- Added `.gitignore` and `.nvmrc` files.
### Self‑Review Questions

- Does the workspace configuration support future package additions?
- Are there any untracked files that should be ignored?

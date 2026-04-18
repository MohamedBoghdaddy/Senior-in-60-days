# Day 03 — CI Setup
![Day](https://img.shields.io/badge/Day-03-blue) ![Area](https://img.shields.io/badge/Area-devops-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Establish continuous integration to ensure code quality and buildability.
### Timebox

~3 hours
### Study

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
### Build

1. Create GitHub Actions workflow to run lint, test, and build on push and pull requests.
1. Configure branch protection rules (if applicable).
1. Write `CONTRIBUTING.md` and a PR template instructing commit message format.
### Assignments

- Push workflow file to `.github/workflows` directory.
- Ensure pipeline fails if lint/tests fail.
### DoD Checklist

- [ ] CI pipeline triggers on push and PR.
- [ ] Commits follow Conventional Commits guidelines.
- [ ] PR template auto-populates with checklists.
### Commit Message

`ci: add GitHub Actions pipeline and contribution guidelines`
### Outcome Artifacts

- Added `.github/workflows/main.yml`.
- Created `CONTRIBUTING.md` and PR template.
### Self‑Review Questions

- Does the CI pipeline cover all relevant checks?
- Are commit guidelines clear to contributors?

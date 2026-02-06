# Day 51 — CI/CD Enhancements
![Day](https://img.shields.io/badge/Day-51-blue) ![Area](https://img.shields.io/badge/Area-devops-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Improve the CI pipeline, containerize the application, and set up preview deployments.
### Timebox

~3 hours
### Study

- [Docker documentation](https://docs.docker.com/get-started/)
- [GitHub Actions advanced](https://docs.github.com/en/actions/using-workflows)
### Build

1. Create a multi-stage Dockerfile for the API and optionally the web client.
1. Add docker-compose configuration for local development (DB, cache, queue).
1. Update GitHub Actions to build Docker images and run tests inside containers.
1. Configure preview deployments (e.g., Vercel for web, Railway/Fly.io for API).
### Assignments

- Commit Dockerfile(s) and docker-compose file.
- Update CI workflow to build and push images (if using a registry).
### DoD Checklist

- [ ] Containers build successfully and run locally.
- [ ] CI pipeline completes within a reasonable time.
- [ ] Preview deployments work and provide accessible URLs.
### Commit Message

`ci/devops: containerize services and enhance CI with preview deployments`
### Outcome Artifacts

- Docker and compose files in the repository.
- CI updated for container builds and deployments.
### Self‑Review Questions

- Does containerization simplify local setup?
- Are preview deployments stable and reflective of production?

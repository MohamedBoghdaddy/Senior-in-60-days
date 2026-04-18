# CI/CD Workflow

This document describes the GitHub Actions pipeline for the portfolio.

## Pipeline stages

1. **Checkout**: retrieve repository code.
2. **Install dependencies**: install Node and Python packages for each service.
3. **Static validation**: check backend and frontend linting and schema files.
4. **Test**: run unit test examples and integration smoke tests.
5. **Build**: build Docker images for backend, AI service, and frontend.
6. **Deploy to staging**: push artifacts and update staging environment.

## Production guidance

- Use environment variables and secrets stored in GitHub Actions.
- Do not run deploy steps on pull requests.
- Keep deployment steps idempotent.

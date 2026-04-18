# CI/CD Workflow

This folder documents the continuous integration and deployment plan.

## Recommended pipeline

1. Run lint and unit tests.
2. Build backend, frontend, and AI service artifacts.
3. Validate Docker images and compose manifests.
4. Deploy to staging using a secure pipeline.

## Pipeline goals

- catch issues early.
- verify build artifacts before deployment.
- keep production secrets out of repository.
- maintain repeatable, documented release steps.

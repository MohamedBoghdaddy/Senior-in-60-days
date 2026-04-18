# Docker Strategy

This section explains how the platform uses containerization.

## Principles

- Build service-specific images for backend, AI service, and frontend.
- Keep runtime configuration in environment variables.
- Avoid hardcoded secrets in Dockerfiles.
- Use multi-stage builds in production as appropriate.

## Local composition

The `03-fullstack-system/infra/docker-compose.yml` file assembles:

- PostgreSQL
- MongoDB
- Redis
- backend service
- AI service
- frontend service

## Production notes

- Image tags should be immutable.
- Secrets should come from a secure vault or Kubernetes Secret.
- Base images should be updated regularly.

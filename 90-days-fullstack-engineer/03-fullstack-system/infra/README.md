# Infrastructure

This folder contains Docker and Kubernetes artifacts for the multi-service platform.

## Files

- `Dockerfile.backend` — backend service container.
- `Dockerfile.ai` — AI FastAPI service container.
- `Dockerfile.frontend` — React frontend container.
- `docker-compose.yml` — local development stack.
- `k8s/` — Kubernetes deployment, service, and ingress manifests.

## Notes

- Environment variables are injected via deployment manifests and compose files.
- No secrets are hardcoded.
- The folder is intended as deployment scaffolding, not a full production cluster config.

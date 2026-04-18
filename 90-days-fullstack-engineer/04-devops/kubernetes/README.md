# Kubernetes Guide

This section describes the platform's Kubernetes deployment.

## Manifests

- `backend-deployment.yaml`: backend pool with scaled replicas.
- `backend-service.yaml`: internal service for backend traffic.
- `frontend-deployment.yaml`: frontend deployment with cluster routing.
- `frontend-service.yaml`: service for UI traffic.
- `ai-deployment.yaml`: AI microservice deployment.
- `ai-service.yaml`: internal AI service endpoint.
- `ingress.yaml`: ingress rules for routing external traffic.

## Design goals

- Separate service boundaries.
- Use ClusterIP services internally.
- Keep ingress as the single entry point for staging.
- Use secrets and config maps in production instead of inline env values.

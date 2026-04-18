# Production-Grade Multi-Service Backend

This backend demonstrates a realistic Node.js service for a multi-service platform.

## Features

- JWT authentication with refresh tokens
- RBAC enforcement sample
- PostgreSQL and MongoDB integration
- Redis caching layer
- BullMQ background job framework
- Structured logging and error handling
- Validation and request flow separation

## Run locally

1. Install dependencies: `npm install`
2. Copy `.env.example` to `.env`
3. Start with `npm run dev`

## Architecture

- `src/controllers` exposes REST endpoints.
- `src/services` orchestrates business rules.
- `src/repositories` abstracts Postgres, MongoDB, and cache access.
- `src/jobs` contains background processing logic.
- `src/middleware` handles authentication and errors.

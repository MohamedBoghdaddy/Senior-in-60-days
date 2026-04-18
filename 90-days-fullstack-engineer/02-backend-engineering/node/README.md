# Node.js Clean Architecture Boilerplate

This folder demonstrates a production-minded Node.js API structure.

## Key concepts
- **Controllers** handle HTTP requests and responses.
- **Services** contain business logic.
- **Repositories** encapsulate persistence details.
- **DTOs** define input/output contracts.
- **Middleware** enables auth, validation, and error handling.
- **Centralized logging** captures structured context.

## What is included
- Auth flow with JWT and refresh tokens.
- RBAC enforcement example.
- Validation middleware for request payloads.
- Error handling pipeline with typed responses.
- Environment-driven configuration.

## Running locally
1. Install dependencies: `npm install`
2. Copy `.env.example` to `.env`.
3. Start server: `npm run dev`

## Notes
This scaffold is intended as a reference for a senior backend engineer to show how the API layers are separated and how services remain testable and maintainable.

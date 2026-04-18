# Design Doc: System Boundaries

## Problem

The platform needs to remain understandable as it grows from a single service to a multi-service architecture.

## Constraints

- must support AI service integration.
- must support mixed relational and document data.
- must be easy to reason about in staging.

## Decision

Define three primary service boundaries:

- Backend API service for auth, business workflows, and data orchestration.
- AI microservice for downstream enrichment and scoring.
- Frontend shell for user interaction and visualization.

## Tradeoffs

- Having a separate AI service adds orchestration overhead but isolates failure domains.
- A single backend could be simpler but would couple AI logic with business workflows.

## Risks

- extra network latency between backend and AI service.
- additional operational complexity from separate deployment pipelines.

## Scaling considerations

- each service can scale independently.
- internal service communication is lightweight and uses HTTP.

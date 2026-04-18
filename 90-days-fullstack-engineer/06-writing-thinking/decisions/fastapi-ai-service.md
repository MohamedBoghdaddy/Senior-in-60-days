# ADR: FastAPI for AI Services

## Status

Accepted

## Context

The AI service must be lightweight, schema-driven, and easy to iterate.

## Decision

Use FastAPI to expose the AI inference endpoint with Pydantic validation.

## Consequences

- rapid development of request/response contracts.
- strong validation reduces invalid payloads.
- separate service enables independent scaling and fault isolation.

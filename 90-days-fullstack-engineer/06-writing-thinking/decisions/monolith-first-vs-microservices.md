# ADR: Monolith First vs Microservices Later

## Status

Accepted

## Context

The portfolio must show senior systems thinking without overengineering early.

## Decision

Start with a monolith-style backend that is structured in layers, then extract the AI service as a separate microservice.

## Consequences

- allows faster delivery and simpler local development.
- keeps the architecture ready for future service extraction.
- preserves the ability to isolate the AI service when needed.

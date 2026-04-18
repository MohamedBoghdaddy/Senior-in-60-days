# ADR: PostgreSQL + MongoDB Choice

## Status

Accepted

## Context

The platform needs relational business data alongside unstructured AI documents.

## Decision

Use PostgreSQL for core business entities and relational integrity.
Use MongoDB for AI artifacts, document content, and flexible schema storage.

## Consequences

- PostgreSQL supports complex joins and transactional consistency.
- MongoDB enables agile storage of AI outputs and unstructured metadata.
- The team accepts the operational cost of two database systems.

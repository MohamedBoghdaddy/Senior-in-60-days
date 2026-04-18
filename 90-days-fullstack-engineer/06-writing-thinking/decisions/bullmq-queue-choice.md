# ADR: BullMQ for Queues

## Status

Accepted

## Context

The platform requires reliable asynchronous ingestion and AI enrichment workflows.

## Decision

Choose BullMQ for node-based job queue processing with Redis as the broker.

## Consequences

- provides retries, delayed jobs, and visibility into queue health.
- depends on Redis availability.
- simplifies background processing in a Node.js architecture.

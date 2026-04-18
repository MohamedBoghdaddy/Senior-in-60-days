# Factory Pattern

## What it is
A factory encapsulates object creation logic behind a common interface.

## When to use it
- when object creation requires configuration or dependency injection.
- when you may need different implementations based on runtime conditions.
- when construction logic is complex and should be isolated.

## When not to use it
- when object instantiation is simple and stable.
- when the factory becomes a catch-all for unrelated logic.

## Realistic example
Use a factory to create a database connector:
- `createDatabaseClient(config)` returns a Postgres or Mongo client.
- `createLogger(level)` returns different logger implementations.

This helps keep service code decoupled from construction details.

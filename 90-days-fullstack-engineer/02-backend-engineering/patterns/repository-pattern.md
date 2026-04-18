# Repository Pattern

## What it is
A repository abstracts the persistence layer, exposing domain operations without leaking database details.

## When to use it
- when you need a consistent interface for data access across services.
- when you want to swap storage engines or mock persistence in tests.
- when you want to centralize query logic and reduce coupling.

## When not to use it
- for very simple CRUD applications where the storage API is already expressive.
- when repository abstraction hides necessary database semantics.

## Realistic example
In a Node.js service, `UserRepository` might expose methods like:
- `findById(id)`
- `findByEmail(email)`
- `save(user)`
- `saveRefreshToken(userId, token)`

This keeps controllers and services focused on business rules instead of SQL or ORM syntax.

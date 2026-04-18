# Strategy Pattern

## What it is
A strategy encapsulates interchangeable algorithms behind a common interface.

## When to use it
- when you want to swap behavior without branching logic.
- when different business rules are chosen at runtime.
- when you want to keep core code open for extension.

## When not to use it
- when only one algorithm exists and the abstraction adds unnecessary complexity.
- when behavior can be handled with a simple configuration flag.

## Realistic example
Implement authorization strategies based on role:
- `AdminAuthorizationStrategy`
- `MemberAuthorizationStrategy`
- `GuestAuthorizationStrategy`

The service chooses the strategy based on user role, keeping rules isolated and testable.

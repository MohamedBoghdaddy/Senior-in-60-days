# Tradeoff: API Design Style

## Problem

The platform must provide a stable API surface while supporting future feature changes.

## Constraints

- support secure auth and RBAC.
- expose search, listing, and AI workflows.
- remain maintainable as the system grows.

## Options considered

1. strict REST API with fixed resource shapes.
2. flexible RPC-style endpoints for complex flows.
3. hybrid pattern with REST for resources and RPC for actions.

## Decision

Adopt a hybrid approach:

- use REST for resource operations such as listings and auth.
- use targeted action endpoints for AI analysis and background job triggers.

## Tradeoffs

- REST improves discoverability and caching.
- RPC-style actions simplify complex workflows.
- a hybrid model accepts some inconsistency for practical service boundaries.

## Risks

- developers may need extra documentation for action endpoints.
- maintaining both styles can increase surface area.

## Scaling considerations

- keep REST resources stable while evolving action API contracts separately.

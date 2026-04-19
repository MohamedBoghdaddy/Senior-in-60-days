# Senior Engineer Behavior Checklist

This is not a list of technologies.
It is a list of behaviors and thinking patterns that distinguish senior engineers from mid-level engineers.

Use this at the end of each month to evaluate yourself honestly.
Rate each item: 0 (not doing it), 1 (starting to do it), 2 (doing it inconsistently), 3 (doing it reliably).

---

## Engineering depth

| Behavior | Day 30 | Day 60 | Day 90 |
|----------|--------|--------|--------|
| Can explain Node.js event loop with microtask/macrotask order without hesitation | | | |
| Can write and explain a SQL query plan (EXPLAIN ANALYZE output) | | | |
| Knows when to use an index and when not to | | | |
| Can explain JWT internals (header, payload, signature, expiry, rotation) | | | |
| Can explain the difference between authentication and authorization with examples | | | |
| Can name 3 ways to prevent SQL injection | | | |
| Can explain CQRS and when it adds complexity vs value | | | |
| Can explain the repository pattern's purpose and limitations | | | |
| Can name all 4 Docker image layer best practices | | | |
| Can explain the difference between liveness and readiness probes | | | |
| Can explain K8s rolling update with maxSurge and maxUnavailable | | | |
| Can write a proper multi-stage Dockerfile from memory | | | |

---

## Production thinking

| Behavior | Day 30 | Day 60 | Day 90 |
|----------|--------|--------|--------|
| Thinks about failure modes before building, not after | | | |
| Writes health check endpoints without being asked | | | |
| Adds structured logging with correlation IDs by default | | | |
| Handles SIGTERM gracefully in all long-running services | | | |
| Validates startup dependencies before binding to port | | | |
| Adds retry with exponential backoff to all external service calls | | | |
| Thinks about the impact of "what if Redis goes down?" before using Redis | | | |
| Adds resource limits (CPU, memory) to any container | | | |
| Can run a basic postmortem for any incident using 5 Whys | | | |
| Writes runbooks before an incident happens, not during | | | |

---

## Architecture and design

| Behavior | Day 30 | Day 60 | Day 90 |
|----------|--------|--------|--------|
| Writes a design doc before writing code for anything non-trivial | | | |
| Proposes architectural changes with explicit tradeoffs, not just benefits | | | |
| Knows when to use a queue vs a synchronous call | | | |
| Can estimate scale (DAU, QPS, storage) back-of-envelope in under 5 minutes | | | |
| Recognizes N+1 query patterns on sight | | | |
| Chooses database migration strategy that has zero-downtime deployment | | | |
| Writes ADRs for decisions that affect the team, not just personal notes | | | |
| Can design a rate limiter from scratch (algorithm, data structures, edge cases) | | | |
| Can articulate the CAP theorem with a concrete example | | | |
| Knows the difference between horizontal and vertical scaling and when each applies | | | |

---

## Code quality

| Behavior | Day 30 | Day 60 | Day 90 |
|----------|--------|--------|--------|
| Writes tests before considering code done | | | |
| Tests failure paths, not just happy paths | | | |
| Error messages contain enough context to debug without reading the code | | | |
| Validation is at the boundary (controller/input), not scattered everywhere | | | |
| No hardcoded secrets or config values in code | | | |
| Error classes have types that callers can distinguish | | | |
| Code review comments are specific (filename, line, what to change, why) | | | |
| Reviews PRs for security, not just style | | | |
| Names things clearly enough that comments are rarely needed | | | |

---

## Communication and collaboration

| Behavior | Day 30 | Day 60 | Day 90 |
|----------|--------|--------|--------|
| Can explain a complex system to a non-engineer in 5 minutes | | | |
| Can explain a complex system to a senior engineer with tradeoffs in 10 minutes | | | |
| Writes proposals that justify effort with concrete outcomes | | | |
| Sends status updates proactively (not just when asked) | | | |
| When blocked, documents the blocker clearly before asking for help | | | |
| Can give constructive code review feedback that is specific and non-personal | | | |
| Interview answers use specific examples, not vague generalities | | | |
| STAR format responses are natural (not rehearsed sounding) | | | |

---

## Self-awareness (score these only at Day 90)

| Question | Answer |
|----------|--------|
| What is the one area where you have grown the most? | |
| What is the one area where you are still weakest? | |
| What behavior from this list do you do most consistently? | |
| What behavior from this list do you still forget to do? | |
| What would a truly senior engineer critique about your work right now? | |

---

## Scoring guide

| Total score (sum of all items × 3) | What it means |
|------------------------------------|---------------|
| 0–40 | Junior level behaviors — consistent gap in execution habits |
| 41–80 | Mid-level — doing the right things inconsistently |
| 81–110 | Strong mid / approaching senior — most behaviors present, not all reliable |
| 111–130 | Senior-level execution — behaviors are instinct, not checklist |

Score at Day 30: ___ / 135
Score at Day 60: ___ / 135
Score at Day 90: ___ / 135

# 90-Day Engineering Roadmap

## What this is

A phase-by-phase overview of 90 days of structured engineering growth.
Each phase has a concrete goal, a measurable outcome, and a set of skills it builds.

For the day-by-day execution detail, see:
- [Phase 1 (Days 1–30)](phase-1-days-01-30.md)
- [Phase 2 (Days 31–60)](phase-2-days-31-60.md)
- [Phase 3 (Days 61–90)](phase-3-days-61-90.md)

---

## Phase 1: Engineering Foundation Upgrade (Days 1–30)

**The problem this phase solves:** You can build things but you do not deeply understand what happens inside Node.js, why SQL queries are slow, or how to think about backend architecture at a production level.

**What this phase builds:**
- Node.js internals: event loop, async patterns, streams, clustering, worker threads, debugging
- SQL and database depth: schema design, indexing, query optimization, transactions, window functions
- LeetCode pattern fluency: arrays, two pointers, sliding window, hash maps, trees, graphs in Python
- Backend architecture basics: REST design, validation, error handling, auth, repository pattern, logging
- Daily discipline: the habit of committing evidence every single day

**End-of-phase outcomes (you must produce these):**
- 30 LeetCode problems solved in Python with pattern notes committed
- A schema design doc for a real system you designed from scratch
- A written critique/code review of the existing Node.js backend
- 2 timed system design write-ups (rate limiter + one more)
- All notes from Day 1 to Day 30 filled in, not empty

**Resources mapped to this phase:**
- Hussein Nasser YouTube: event loop, async, Node.js architecture videos (2–3 hours total)
- NodeJS Complete Guide (Udemy): sections on event loop + async only (3–4 hours)
- Intro to Databases (Coursera): Weeks 1–3 selectively (8–10 hours)
- NeetCode YouTube: pattern intro videos before each LeetCode block (10–15 min each)

---

## Phase 2: Backend & Architecture Depth (Days 31–60)

**The problem this phase solves:** You have surface knowledge of .NET and you have never practiced system design under time pressure or written a real code review document.

**What this phase builds:**
- .NET Clean Architecture: layers, DI, CQRS, repository pattern, FluentValidation, xUnit testing
- System design under pressure: 6 timed 45-minute drills with written output
- Code review thinking: reading code critically, writing structured review comments
- LeetCode in C++: dynamic programming patterns, heap/priority queue patterns
- Production Node.js: health checks, graceful shutdown, metrics, integration tests

**End-of-phase outcomes (you must produce these):**
- A working .NET API built with clean architecture principles (committed)
- 6 system design write-ups in the repo (timed, completed under pressure)
- A formal written code review of the existing Node.js backend
- 10+ LeetCode solutions in C++ with notes
- A production readiness doc for the Node.js backend
- All notes from Day 31 to Day 60 filled in

**Resources mapped to this phase:**
- ASP.NET Core SOLID and Clean Architecture (Udemy): weeks 5–6 (15–20 hours, go deep)
- NeetCode YouTube: DP and heap pattern videos (before C++ LeetCode sessions)
- Hussein Nasser: system design framework video + selected architecture talks
- Software Design & Architecture Specialization (Coursera): Clean Architecture course selectively (5–8 hours)

---

## Phase 3: Production & Scalability Mode (Days 61–90)

**The problem this phase solves:** You have not containerized and orchestrated a real multi-service system, you have not set up proper observability, and you cannot articulate system design answers at a senior level.

**What this phase builds:**
- Docker: multi-stage builds, networking, compose production patterns, container security
- Kubernetes: pods, services, deployments, HPA, ConfigMaps, Secrets, Ingress, debugging
- Observability: structured logging, metrics with Prometheus, distributed tracing concepts, CI/CD pipelines
- Incident response: runbooks, postmortems, failure simulation
- Scaling patterns: caching layers, read replicas, async jobs, database scaling
- Senior communication: design proposals, architecture reviews, interview articulation

**End-of-phase outcomes (you must produce these):**
- Improved Dockerfiles and docker-compose with health checks, secrets, resource limits (committed)
- All K8s manifests updated with ConfigMaps/Secrets, HPA, liveness/readiness probes (committed)
- A GitHub Actions CI/CD pipeline that actually runs lint + test + build (committed)
- A structured logging + metrics setup in the backend (committed)
- 3 incident runbooks + 1 detailed postmortem (committed)
- A final system design write-up (45 min, timed)
- A "what I built and why it matters" portfolio narrative
- All notes from Day 61 to Day 90 filled in

**Resources mapped to this phase:**
- Docker & Kubernetes Practical Guide (Udemy): weeks 9–10 (25–30 hours, primary resource)
- TechWorld with Nana YouTube: K8s concepts, Prometheus/Grafana setup
- Hussein Nasser YouTube: observability and scaling deep dives
- freeCodeCamp YouTube: SQL/PostgreSQL refresher only if needed (not primary)

---

## Progress tracker

| Phase | Days | Status | Phase outcome artifact |
|-------|------|--------|----------------------|
| Phase 1: Foundation | 1–30 | [ ] | LeetCode tracker, schema doc, Node.js code review |
| Phase 2: Architecture | 31–60 | [ ] | .NET project, 6 system designs, C++ LeetCode |
| Phase 3: Production | 61–90 | [ ] | Docker/K8s improvements, CI/CD, observability, postmortem |

---

## Weekly checkpoints

Every 7 days, complete a [weekly review](../../tracking/weekly-review-template.md).

Every 30 days, update the [progress tracker](../../tracking/progress-tracker.md) with phase-level outcomes.

---

## Time realism

Assumes 2–4 focused hours on most weekdays, more on weekends.

| Resource | Mode | Phase | Hours |
|----------|------|-------|-------|
| Hussein Nasser YouTube | Selective (specific videos) | All | ~2h/week |
| NodeJS Complete Guide | Partial (event loop, async, REST sections) | 1 | ~20–25h total |
| Intro to Databases (Coursera) | Partial (skip what you know) | 1 | ~10h total |
| ASP.NET Core Clean Architecture | Full | 2 | ~20h total |
| Docker & Kubernetes Practical Guide | Full | 3 | ~30h total |
| NeetCode | Video per pattern before practice | All | ~15min/session |
| Software Design & Architecture | 1 course only (Clean Arch) | 2 | ~8h total |

Total estimated course time: ~90–100 hours over 90 days = ~1h/day average.
The remaining ~1–3 hours/day goes to building, coding, writing.

Do not spend more than 50% of any day watching videos.

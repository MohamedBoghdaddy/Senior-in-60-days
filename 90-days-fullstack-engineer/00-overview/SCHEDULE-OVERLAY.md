# Schedule Overlay

This file maps all 90 days across 4 dimensions:
- Day type: Regular (R) / Break The System (B) / Redesign (D) / Review Week (V)
- Code Review slot: which day this week's code review happens
- System Thinking Output: what type this week requires
- System component touched: which part of the platform this day works on

Use this alongside the [phase plan files](phase-1-days-01-30.md) — this overlay tells you WHAT ROLE each day plays.
The phase files tell you WHAT TO DO on that day.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| R | Regular day — primary learning + build task |
| B | BREAK THE SYSTEM day — full day, produces incident report |
| D | REDESIGN day — add 2h redesign block to regular day |
| CR | CODE REVIEW block embedded in this day |
| STO | SYSTEM THINKING OUTPUT block embedded in this day |

---

## Phase 1: Days 1–30

### Week 1 (Days 1–7) — Node.js internals

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 1 | R | — | Node.js backend (study) | — |
| 2 | R | — | Node.js backend (async) | — |
| 3 | R | — | Node.js backend (streams) | — |
| 4 | R | CR | Node.js backend (cluster/worker) | — |
| 5 | R | STO → Failure mode analysis: "What happens if each Node.js component fails?" | Node.js backend (debugging) | Failure mode analysis |
| 6 | B | **BREAK: Kill Node.js mid-request. What does the error handler do? Does it restart?** | Node.js backend (error handling) | — |
| 7 | R | — | Node.js backend (Week 1 review) | — |

**Week 1 Code Review focus:** Review `02-backend-engineering/node/src/utils/errors.js` and `errorHandler.js`
**Week 1 System Thinking Output:** Failure mode analysis — "What breaks if each Node.js component fails?"
**Week 1 Break:** Kill the Node.js process while requests are in flight. Observe behavior. Fix what you find.

---

### Week 2 (Days 8–14) — SQL depth

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 8 | R | — | PostgreSQL schema | — |
| 9 | R | — | PostgreSQL queries | — |
| 10 | R | — | PostgreSQL indexes | — |
| 11 | R | CR | PostgreSQL transactions | — |
| 12 | R | STO → Performance analysis: "Which queries in the current schema would be slow at 100K rows?" | PostgreSQL window functions | Performance analysis |
| 13 | B | **BREAK: Stop the Postgres container while the backend is running. How many endpoints fail? How do they fail?** | PostgreSQL (dependency failure) | — |
| 14 | D + R | **REDESIGN: Redesign the e-commerce schema from Day 8 after seeing what transactions and indexes require** | PostgreSQL schema (iteration) | — |

**Week 2 Code Review focus:** Review `03-fullstack-system/backend/src/repositories/postgresRepository.js`
**Week 2 System Thinking Output:** Performance analysis of current PostgreSQL usage
**Week 2 Break:** Postgres goes down. What does the backend return? 500? 503? Does it log anything useful?
**Week 2 Redesign:** Revisit Day 8 schema. What indexes did you learn it needs? Add them. Fix any normalization gaps.

---

### Week 3 (Days 15–21) — Backend architecture

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 15 | R | — | Node.js REST API | — |
| 16 | R | — | Node.js validation layer | — |
| 17 | R | — | Node.js auth service | — |
| 18 | R | CR | Node.js rate limiter | — |
| 19 | R | STO → Architecture diagram: "Draw the Node.js backend layers and data flow" | Node.js service layer | Architecture diagram |
| 20 | B | **BREAK: Set JWT_SECRET to a single character. What accepts it? What rejects it? How do you detect weak secrets?** | Node.js auth (security break) | — |
| 21 | R | — | Node.js backend (Week 3 review + architecture doc) | — |

**Week 3 Code Review focus:** Review `02-backend-engineering/node/src/services/authService.js`
**Week 3 System Thinking Output:** Architecture diagram of the Node.js backend layers
**Week 3 Break:** Weak JWT secret. What breaks? What does an attacker gain? What do you add to prevent this?

---

### Week 4 (Days 22–28) — Databases in depth

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 22 | R | — | MongoDB patterns | — |
| 23 | R | — | Redis patterns | — |
| 24 | R | — | Database migrations | — |
| 25 | R | CR | BullMQ / job queues | — |
| 26 | R | STO → Scaling plan: "What breaks first in this system at 10× traffic?" | Node.js metrics + health | Scaling plan |
| 27 | B | **BREAK: Set Redis to a wrong URL. Does the API start? Does caching fail silently or hard? Does rate limiting break?** | Redis (cache/rate limit failure) | — |
| 28 | D + R | **REDESIGN: Revisit the Node.js error handling from Day 6. After 4 weeks of building, what gaps do you now see?** | Node.js error hierarchy | — |

**Week 4 Code Review focus:** Review `03-fullstack-system/backend/src/services/listingService.js` (caching patterns)
**Week 4 System Thinking Output:** Scaling plan — first bottleneck at 10× load
**Week 4 Break:** Redis goes down. Does caching fail gracefully? Does rate limiting fail open or closed?
**Week 4 Redesign:** Error handling from Week 1. What would you add/change after 4 weeks of building?

---

### Days 29–30 — Phase 1 completion

| Day | Type | Disciplines | Notes |
|-----|------|------------|-------|
| 29 | R | — | System design drill + LeetCode |
| 30 | V | Phase 1 full review | Update all trackers. Verify docker-compose up runs cleanly. **DEPLOYMENT MILESTONE: Local full system** |

---

## Phase 2: Days 31–60

### Week 5 (Days 31–37) — .NET Clean Architecture foundation

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 31 | R | — | .NET CleanShop (setup) | — |
| 32 | R | — | .NET CleanShop (layers) | — |
| 33 | R | — | .NET CleanShop (domain) | — |
| 34 | R | CR | .NET CleanShop (application/CQRS) | — |
| 35 | R | STO → Tradeoff doc: "Repository pattern in .NET vs Node.js — what is the same, what is different?" | .NET CleanShop (infrastructure) | Tradeoff document |
| 36 | B | **BREAK: Delete the Infrastructure project reference. What compile errors appear? What does this reveal about the dependency rule?** | .NET CleanShop (architecture stress) | — |
| 37 | R | — | .NET CleanShop (testing) | — |

**Week 5 Code Review focus:** Review the CleanShop domain layer you wrote on Day 33
**Week 5 System Thinking Output:** Tradeoff doc — repository pattern in .NET vs Node.js
**Week 5 Break:** Delete Infrastructure project reference. Does the code still compile? What breaks first? What does this prove about the Clean Architecture dependency rule?

---

### Week 6 (Days 38–44) — .NET depth + C++ start

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 38 | R | — | .NET CleanShop (auth) | — |
| 39 | R | — | .NET CleanShop (CRUD surface) | — |
| 40 | R | — | .NET CleanShop (logging) | — |
| 41 | R | CR | .NET vs Node.js ADR | — |
| 42 | D + R | **REDESIGN: Review the CleanShop domain model from Day 33. After building auth and CRUD, what value objects or domain methods did you miss?** | .NET CleanShop domain (iteration) | — |
| 43 | R | STO → Architecture diagram: "How does CleanShop fit into the overall multi-service platform? Draw the service map." | Multi-service architecture | Architecture diagram |
| 44 | B | **BREAK: Send 500 concurrent POST /products requests to the CleanShop API. Does EF Core connection pool exhaust? What error appears?** | .NET CleanShop (load stress) | — |

**Week 6 Code Review focus:** Review the CleanShop Application layer (command handlers, validators)
**Week 6 System Thinking Output:** Architecture diagram — where does CleanShop sit in the full platform?
**Week 6 Break:** Overload CleanShop API. What happens at the EF Core level? What happens at the HTTP level?
**Week 6 Redesign:** CleanShop domain model — after building auth and full CRUD, what is missing?

---

### Week 7 (Days 45–51) — System design drills

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 45 | R | — | Chat system design (timed drill) | — |
| 46 | R | — | News feed design (timed drill) | — |
| 47 | R | — | Video streaming design (timed drill) | — |
| 48 | R | CR | System design framework | — |
| 49 | R | STO → Tradeoff doc: "After 6 system design drills, what patterns do I consistently get right vs consistently miss?" | System design meta-analysis | Tradeoff document |
| 50 | B | **BREAK: Kill the backend container while a BullMQ job is mid-execution. What happens to the job? Is it lost? Does it retry?** | BullMQ / job queue (reliability) | — |
| 51 | R | — | Debugging practice | — |

**Week 7 Code Review focus:** Review the BullMQ job setup in `03-fullstack-system/backend/src/jobs/`
**Week 7 System Thinking Output:** Meta-analysis of system design drills — patterns and gaps
**Week 7 Break:** Kill the backend during a BullMQ job. Does the job survive? Does BullMQ's at-least-once guarantee hold?

---

### Week 8 (Days 52–58) — Production Node.js

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 52 | R | — | Node.js graceful shutdown | — |
| 53 | R | — | Prometheus metrics | — |
| 54 | R | — | API design document | — |
| 55 | D + R | **REDESIGN: Revisit the Node.js backend auth from Day 17 + Day 27. After building auth in .NET and auditing security, what gaps remain in the Node.js auth?** | Node.js auth (iteration) | — |
| 56 | R | CR | Scaling writeup | — |
| 57 | R | STO → Scaling plan: "How does the full multi-service platform scale from 100 to 1M users? Which service is the bottleneck at each stage?" | Multi-service scaling | Scaling plan |
| 58 | B | **BREAK: Run the Node.js backend with `--max-old-space-size=50`. Load it with 1000 requests. When does it OOM? What does K8s do when a container OOMKills?** | Node.js (memory pressure) | — |

**Week 8 Code Review focus:** Review the Prometheus metrics middleware you added on Day 53
**Week 8 System Thinking Output:** Multi-service scaling plan — bottleneck at each stage
**Week 8 Break:** Memory pressure on Node.js. What is the OOM behavior? What does the health endpoint show before crash?
**Week 8 Redesign:** Node.js auth — what gaps remain after .NET auth and security audit?

---

### Days 59–60 — Phase 2 completion

| Day | Type | Disciplines | Notes |
|-----|------|------------|-------|
| 59 | R | — | Mock interview prep |
| 60 | V | Phase 2 full review | Update all trackers. Deploy to free-tier cloud. **DEPLOYMENT MILESTONE: Basic cloud deployment** |

---

## Phase 3: Days 61–90

### Week 9 (Days 61–67) — Docker

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 61 | R | — | Dockerfile.backend (multi-stage) | — |
| 62 | R | — | docker-compose (health checks) | — |
| 63 | R | — | .NET Dockerfile | — |
| 64 | R | CR | Docker networking | — |
| 65 | R | STO → Security threat model: "What are the 5 ways the current Docker setup can be attacked?" | Container security | Security threat model |
| 66 | B | **BREAK: Change the backend Dockerfile to run as root. Then try to escalate privileges inside the running container. Document what you can do.** | Container security (break) | — |
| 67 | D + R | **REDESIGN: Revisit docker-compose.yml from Day 62. After learning networking and security, what is still wrong?** | docker-compose (iteration) | — |

**Week 9 Code Review focus:** Review all Dockerfiles — multi-stage, non-root, layer efficiency
**Week 9 System Thinking Output:** Security threat model for the container setup
**Week 9 Break:** Run container as root. What can you do? What can't you do? Why does this matter?
**Week 9 Redesign:** docker-compose after networking and security knowledge. What was wrong with the first version?

---

### Week 10 (Days 68–74) — Kubernetes

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 68 | R | — | K8s Pod (deploy backend) | — |
| 69 | R | — | K8s Deployment + Services + probes | — |
| 70 | R | — | K8s ConfigMaps + Secrets | — |
| 71 | R | CR | K8s rolling update + rollback | — |
| 72 | R | STO → Architecture diagram: "Draw the full K8s cluster: nodes, pods, services, ingress, volumes" | K8s cluster architecture | Architecture diagram |
| 73 | B | **BREAK: Delete the backend pod manually (`kubectl delete pod`). What happens? How fast does K8s reschedule it? What do requests during that window see?** | K8s pod resilience | — |
| 74 | D + R | **REDESIGN: Revisit the K8s backend-deployment.yaml from Day 69. After adding HPA, ConfigMaps, and Secrets, what is still missing from production quality?** | K8s manifests (iteration) | — |

**Week 10 Code Review focus:** Review all K8s manifests — probes, resource limits, update strategy
**Week 10 System Thinking Output:** K8s cluster architecture diagram
**Week 10 Break:** Delete a pod. How fast does it recover? What do clients experience during the gap? Does readiness probe prevent traffic during restart?
**Week 10 Redesign:** All K8s manifests from Day 69 onward. After HPA, Secrets, and Ingress, what still needs improvement?

---

### Week 11 (Days 75–81) — Observability + CI/CD

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 75 | R | — | Structured logging | — |
| 76 | R | — | Prometheus + Grafana | — |
| 77 | R | — | Distributed tracing | — |
| 78 | R | CR | CI/CD pipeline | — |
| 79 | B | **BREAK: Simulate all 3 failure scenarios (DB down, memory leak, external API down) in sequence within 1 hour. Write a single postmortem covering all three.** | Full system (multi-failure) | — |
| 80 | R | STO → Failure mode analysis: "For each service in the platform, what is the failure mode and what is the fallback?" | Full system failure analysis | Failure mode analysis |
| 81 | D + R | **REDESIGN: Revisit the structured logging from Day 75. After adding tracing (Day 77) and CI (Day 78), are logs consistent across all services? Are correlation IDs propagated everywhere?** | Observability stack (iteration) | — |

**Week 11 Code Review focus:** Review the GitHub Actions CI/CD pipeline you wrote on Day 78
**Week 11 System Thinking Output:** Failure mode analysis — every service, every failure mode, every fallback
**Week 11 Break:** Multi-failure simulation. Can you run 3 incidents in 1 hour? What breaks your ability to debug? What observability gap did you find?
**Week 11 Redesign:** Logging + tracing consistency across all services.

---

### Week 12 (Days 82–90) — Scaling, senior behavior, final

| Day | Type | Disciplines embedded | System component | System Thinking Output |
|-----|------|---------------------|-----------------|----------------------|
| 82 | R | — | Caching strategy doc | — |
| 83 | R | — | Async architecture design doc | — |
| 84 | R | — | Database scaling doc | — |
| 85 | D + R | **REDESIGN: Go back to Day 26's health/metrics endpoints. After adding Prometheus (Day 76) and tracing (Day 77), what should the health endpoint return? What should it NOT return?** | Observability (final iteration) | — |
| 86 | R | STO → Scaling plan: "Ride-hailing system. Design the scaling plan not just the architecture." | System design (senior final) | Scaling plan |
| 87 | B | **BREAK: Final system stress test. Disable Redis, stop one backend pod, corrupt one MongoDB document, and run 500 concurrent requests. What holds? What breaks? Document everything.** | Full system (final stress) | — |
| 88 | R | CR | Portfolio narrative | — |
| 89 | R | — | Mock interview log | — |
| 90 | V | Phase 3 full review | Tag v1.0. **DEPLOYMENT MILESTONE: Production-style demo** |

**Week 12 Code Review focus:** Final review of the system end-to-end — README, architecture docs, test coverage
**Week 12 System Thinking Output:** Final scaling plan — not just architecture, but how each component scales
**Week 12 Break:** Multi-failure final stress test. This is the capstone break day.
**Week 12 Redesign:** Health/metrics endpoint — has it kept up with all the observability you added?

---

## Summary: All Break Days

| Day | Week | What breaks | Primary lesson |
|-----|------|-------------|----------------|
| 6 | 1 | Node.js killed mid-request | Error handling and recovery |
| 13 | 2 | Postgres container stopped | Dependency failure graceful degradation |
| 20 | 3 | Weak JWT secret | Auth security and secret validation |
| 27 | 4 | Redis wrong URL | Cache failure modes (fail open vs closed) |
| 36 | 5 | .NET infrastructure reference deleted | Clean Architecture dependency rule |
| 44 | 6 | 500 concurrent requests to CleanShop | Connection pool exhaustion |
| 50 | 7 | Backend killed during BullMQ job | Job durability and at-least-once delivery |
| 58 | 8 | Node.js memory-constrained | OOM behavior and memory management |
| 66 | 9 | Container run as root | Container privilege escalation |
| 73 | 10 | Pod deleted manually | K8s pod recovery and request continuity |
| 79 | 11 | 3 failures in 1 hour | Multi-incident response |
| 87 | 12 | Redis + pod + MongoDB + load | Full system stress — final capstone |

---

## Summary: All Redesign Days

| Day | Week | What gets redesigned | Why at this point |
|-----|------|---------------------|-------------------|
| 14 | 2 | E-commerce schema (Day 8) | After learning transactions and indexes |
| 28 | 4 | Node.js error handling (Day 6) | After 4 weeks of seeing where errors surface |
| 42 | 6 | CleanShop domain model (Day 33) | After building auth and full CRUD |
| 55 | 8 | Node.js auth (Day 17) | After .NET auth and security audit |
| 67 | 9 | docker-compose (Day 62) | After networking and security |
| 74 | 10 | K8s manifests (Day 69) | After HPA, Secrets, and Ingress |
| 81 | 11 | Logging stack (Day 75) | After tracing and CI/CD |
| 85 | 12 | Health/metrics endpoint (Day 26) | After Prometheus and tracing |

---

## Summary: All System Thinking Outputs

| Week | Type | Topic |
|------|------|-------|
| 1 | Failure mode analysis | Node.js component failures |
| 2 | Performance analysis | PostgreSQL at 100K rows |
| 3 | Architecture diagram | Node.js backend layers |
| 4 | Scaling plan | First bottleneck at 10× load |
| 5 | Tradeoff document | Repository pattern: .NET vs Node.js |
| 6 | Architecture diagram | CleanShop in the multi-service platform |
| 7 | Tradeoff document | System design drills meta-analysis |
| 8 | Scaling plan | Multi-service scaling from 100 to 1M users |
| 9 | Security threat model | Docker setup attack surface |
| 10 | Architecture diagram | Full K8s cluster |
| 11 | Failure mode analysis | Every service, every failure mode |
| 12 | Scaling plan | Ride-hailing final scaling plan |

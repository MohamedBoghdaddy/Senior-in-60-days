# Phase 3: Production & Scalability Mode — Days 61–90

**Goal:** Containers, orchestration, observability, CI/CD, scaling patterns, and senior communication. By Day 90 you must have real Docker/K8s artifacts, a working CI pipeline, structured logging + metrics, 3 incident runbooks, a postmortem, and all 30 daily notes filled in.

---

## Week 9 — Docker Deep Dive (Days 61–67)

### Day 61
- **Objective:** Understand Docker internals — not just "run a container."
- **Study (1h):** Docker & Kubernetes Practical Guide (Udemy) — Sections 1–3: what Docker is, images vs containers, layers. Read Docker docs on multi-stage builds. Look at the existing `Dockerfile.backend` in `03-fullstack-system/infra/`.
- **Build task (1.5h):** Rewrite `Dockerfile.backend` as a proper multi-stage build: Stage 1 (`builder`): install all deps, compile/build. Stage 2 (`runner`): copy only the production artifact, install only production deps, use `node:20-alpine`, run as non-root user (`USER node`). Verify the final image size is significantly smaller than a single-stage build. Write a comment at the top of the Dockerfile explaining each stage's purpose.
- **LeetCode C++ (45min):** Binary Search (C++) — write iterative + recursive + search in rotated array.
- **Reflection output:** `notes/day-61.md` — "What is a Docker layer? Why does instruction order in a Dockerfile matter for build caching? What is the most common Dockerfile mistake you see?"
- **Estimated time:** 3.5h
- **Why this day matters:** Multi-stage builds are a production requirement. Running as root in a container is a security risk. These are two signals senior engineers check on sight.

---

### Day 62
- **Objective:** Fix the docker-compose for production-like local development.
- **Study (30min):** Docker docs on health checks, depends_on with condition, resource limits. Look at the existing `docker-compose.yml` in `03-fullstack-system/infra/`.
- **Build task (2h):** Rewrite the `docker-compose.yml` with production patterns: (1) Add `healthcheck` to postgres (using `pg_isready`), redis (using `redis-cli ping`), and backend (using `GET /health`). (2) Change `depends_on` for backend to use `condition: service_healthy` for postgres and redis (so the backend waits until they are actually ready, not just started). (3) Add `restart: unless-stopped` to all services. (4) Add `mem_limit: 512m` and `cpus: '0.5'` to backend. (5) Move sensitive values (JWT_SECRET, passwords) to a `.env` file referenced with `env_file`. Commit.
- **LeetCode C++ (45min):** Find Minimum in Rotated Sorted Array (C++) + Search a 2D Matrix (C++).
- **Reflection output:** `notes/day-62.md` — "What is the problem with `depends_on` without health checks? What happens to a Node.js server if it starts before the database is ready?"
- **Estimated time:** 3h

---

### Day 63
- **Objective:** Add Docker images for .NET and understand multi-service build patterns.
- **Build task (2.5h):** (1) Write a `Dockerfile` for the `CleanShop` .NET API using multi-stage build: Stage 1: `mcr.microsoft.com/dotnet/sdk:8.0` for restore and publish. Stage 2: `mcr.microsoft.com/dotnet/aspnet:8.0-alpine` for runtime, non-root user. (2) Add `CleanShop` as a service in the docker-compose: it should use the .NET Dockerfile, connect to the existing postgres container, and expose port 5001. (3) Add a health check for the .NET service. (4) Verify `docker-compose up` starts all services including the .NET API. Commit.
- **LeetCode C++ (45min):** Median of Two Sorted Arrays (C++) + First Bad Version (C++).
- **Reflection output:** `notes/day-63.md` — "What is the difference between `sdk` and `aspnet` Docker images for .NET? Why do you need both?"
- **Estimated time:** 3.5h

---

### Day 64
- **Objective:** Understand Docker networking deeply.
- **Study (1h):** Docker docs on networking: bridge, host, overlay, none. How containers in the same compose file communicate. How to expose ports vs internal-only services. Docker DNS resolution (service names as hostnames).
- **Build task (1.5h):** (1) Add a second docker-compose file `docker-compose.monitoring.yml` with Prometheus and Grafana services. Prometheus should scrape the backend's `/metrics` endpoint. Grafana should connect to Prometheus. (2) Use Docker's `--network` to join both compose files to the same network. (3) Verify Prometheus can scrape the backend metrics. Commit. Write `04-devops/docker/networking-guide.md` explaining how service-to-service communication works in your compose setup.
- **LeetCode C++ (45min):** Single Element in Sorted Array (C++) + Capacity to Ship Packages (C++) — binary search on answer.
- **Reflection output:** `notes/day-64.md` — "Explain how container A reaches container B by name in Docker Compose. What would break if you put them on different networks?"
- **Estimated time:** 3.5h

---

### Day 65
- **Objective:** Container security — run hardened containers.
- **Study (45min):** Read OWASP Docker Security Cheat Sheet (search for it). Read about Docker image scanning with `docker scout` or `trivy`. Read about secrets management (Docker secrets vs env vars).
- **Build task (2h):** Security-harden all Dockerfiles: (1) Ensure all services run as non-root users. (2) Use specific image tags (not `latest`). (3) Add `.dockerignore` files to exclude `node_modules`, `.git`, `.env`, `obj/`, `bin/`. (4) Run `docker scout cves` (or `trivy image`) against the backend image and document any critical vulnerabilities found. (5) Write `04-devops/docker/security-checklist.md` — 10-point checklist for secure Docker images. Commit.
- **LeetCode C++ (45min):** Koko Eating Bananas (C++) + Minimize Max Distance to Gas Station (C++).
- **Reflection output:** `notes/day-65.md` — "Why is running as root in a container dangerous? What can an attacker do if they escape the container process?"
- **Estimated time:** 3.5h

---

### Day 66
- **Objective:** Learn Docker debugging and operational skills.
- **Study (30min):** `docker stats`, `docker logs`, `docker exec`, `docker inspect`. Read about what to do when a container exits immediately.
- **Build task (2h):** Write `04-devops/docker/debugging-runbook.md` — an operational runbook for common Docker problems: (1) Container exits immediately (how to diagnose). (2) Container is running but service is unreachable (how to diagnose). (3) High CPU or memory in a container (how to diagnose). (4) Containers cannot communicate with each other (how to diagnose). For each: the exact commands to run, what output to look for, common causes, and fixes. Then: deliberately break one service (wrong env var) and follow your own runbook to fix it.
- **LeetCode (1h):** Revisit 2 LeetCode problems you found hardest in C++ this week and re-solve from scratch.
- **Reflection output:** `notes/day-66.md`
- **Estimated time:** 3.5h

---

### Day 67 — Week 9 Review + Docker ADR
- **Objective:** Produce a Docker architecture ADR.
- **Build task (2h):** Write `06-writing-thinking/decisions/containerization-strategy.md` — ADR for the containerization strategy: (1) Why Docker over bare metal or VMs for local development and staging. (2) Why multi-stage builds. (3) Why non-root containers. (4) Image registry strategy (where images are stored). (5) Known limitations of the current docker-compose setup in production. Also update `04-devops/docker/README.md` to be a real guide (not a placeholder) covering: how to build, how to run, how to debug, what each service does.
- **LeetCode (45min):** Recover from any LeetCode gaps this week.
- **Reflection output:** `notes/day-67.md` + `notes/week-09-review.md`
- **Estimated time:** 3h

---

## Week 10 — Kubernetes (Days 68–74)

### Day 68
- **Objective:** Understand K8s architecture from first principles.
- **Study (1.5h):** Docker & Kubernetes Practical Guide (Udemy) — Kubernetes sections: architecture (control plane, worker nodes, etcd, scheduler, kube-proxy). What is a Pod. What is a Node. What is a Deployment. TechWorld with Nana YouTube — "Kubernetes Tutorial for Beginners" first 30 minutes.
- **Build task (1.5h):** Install minikube (or use k3s/kind). Start a local cluster. Deploy the Node.js backend as a single Pod: (1) Write a `Pod` manifest for the backend (NOT a deployment yet — raw Pod). (2) Apply it with `kubectl apply`. (3) Use `kubectl describe pod` and `kubectl logs` to verify it started. (4) Use `kubectl port-forward` to access it. Write `04-devops/kubernetes/00-concepts.md` — your notes on K8s core concepts with a diagram.
- **LeetCode C++ (45min):** Max Points on a Line (C++) + Minimum Number of Arrows to Burst Balloons (C++).
- **Reflection output:** `notes/day-68.md` — "What is the difference between a Pod and a container? What is the control plane and why is it separate from worker nodes?"
- **Estimated time:** 3.5h

---

### Day 69
- **Objective:** Use Deployments, Services, and understand K8s networking.
- **Study (1h):** Docker & Kubernetes — Deployments and Services section. Difference between ClusterIP, NodePort, LoadBalancer.
- **Build task (2h):** Upgrade the existing K8s manifests in `03-fullstack-system/infra/k8s/`: (1) Add `readinessProbe` and `livenessProbe` to backend-deployment.yaml (using the `/health` endpoint). (2) Verify the Deployment has `replicas: 2`. (3) Add `resources.requests` and `resources.limits` for CPU and memory. (4) Apply and verify with `kubectl get pods`, `kubectl describe deployment`. Write `04-devops/kubernetes/deployment-guide.md` explaining what each section of the deployment manifest does.
- **LeetCode C++ (45min):** Task Scheduler (C++) revisit + Meeting Rooms II (C++) — interval scheduling.
- **Reflection output:** `notes/day-69.md` — "What is the difference between a liveness probe and a readiness probe? What happens if liveness fails? What if readiness fails?"
- **Estimated time:** 3.5h

---

### Day 70
- **Objective:** ConfigMaps and Secrets — never hardcode config in K8s manifests.
- **Study (30min):** K8s docs on ConfigMaps and Secrets. Why base64 encoding in Secrets is not encryption. How to use them as env vars vs mounted volumes.
- **Build task (2h):** Replace all hardcoded env vars in the existing K8s manifests: (1) Create a `ConfigMap` for non-sensitive config (LOG_LEVEL, PORT, BULLMQ_QUEUE_NAME). (2) Create a `Secret` for sensitive values (JWT_SECRET, DB passwords). (3) Update the backend deployment manifest to reference these. (4) Update the AI service and frontend manifests similarly. Apply and verify all pods still start. Commit the updated manifests.
- **LeetCode C++ (45min):** Non-overlapping Intervals (C++) + Car Pooling (C++).
- **Reflection output:** `notes/day-70.md` — "K8s Secrets are only base64 encoded, not encrypted. What is the correct way to manage secrets in a production Kubernetes cluster?"
- **Estimated time:** 3h

---

### Day 71
- **Objective:** Rolling updates, rollbacks, and deployment strategies.
- **Study (45min):** K8s docs on deployment strategies: RollingUpdate vs Recreate. `maxSurge` and `maxUnavailable`. `kubectl rollout` commands.
- **Build task (2h):** (1) Add `strategy: { type: RollingUpdate, rollingUpdate: { maxSurge: 1, maxUnavailable: 0 } }` to the backend deployment. (2) Simulate a bad deployment: change the image tag to something that doesn't exist. Apply it. Watch `kubectl get pods` show the failure. (3) Roll back using `kubectl rollout undo`. (4) Write `04-devops/kubernetes/rollback-runbook.md` — step-by-step procedure: how to detect a bad deployment, how to roll back, how to verify rollback was successful.
- **LeetCode C++ (45min):** Insert Interval (C++) + Minimum Interval to Include Each Query (C++).
- **Reflection output:** `notes/day-71.md` — "What is `maxUnavailable: 0` in a rolling update? When would you use `Recreate` strategy instead of `RollingUpdate`?"
- **Estimated time:** 3h

---

### Day 72
- **Objective:** Horizontal Pod Autoscaling.
- **Study (30min):** K8s HPA docs. What metrics HPA uses. How `metrics-server` works. When HPA is not sufficient (and you need KEDA for queue-based scaling).
- **Build task (2h):** (1) Install `metrics-server` in minikube. (2) Write an HPA manifest for the backend: scale between 2 and 10 replicas when CPU exceeds 70%. (3) Apply it with `kubectl apply`. (4) Generate load using a simple loop: `while true; do curl http://backend/health; done`. (5) Watch `kubectl get hpa` to see scaling events. (6) Write `04-devops/kubernetes/hpa-guide.md` explaining when HPA helps and when it doesn't (e.g., it can't scale down a database).
- **LeetCode (45min):** Review any remaining weak areas.
- **Reflection output:** `notes/day-72.md` — "HPA scales pods, but what about stateful services like databases? What do you do when the database is the bottleneck, not the API pods?"
- **Estimated time:** 3h

---

### Day 73
- **Objective:** Ingress and production traffic routing.
- **Study (30min):** K8s Ingress docs. nginx Ingress controller. TLS termination. Path-based routing.
- **Build task (2h):** Improve the existing `ingress.yaml` in `03-fullstack-system/infra/k8s/`: (1) Add path-based routing: `/api/*` → backend service, `/ai/*` → AI service, `/*` → frontend. (2) Add TLS termination using a self-signed cert (for local testing) via a K8s Secret. (3) Add rate limiting annotation for nginx ingress (e.g., `nginx.ingress.kubernetes.io/limit-rps: "10"`). (4) Write a comment in the manifest explaining what each annotation does. Apply and verify traffic routing works.
- **LeetCode (45min):** Solve 2 hard-level problems of your choice in any language.
- **Reflection output:** `notes/day-73.md` — "What is the role of an Ingress controller in K8s? Why do you terminate TLS at the Ingress level rather than at each service pod?"
- **Estimated time:** 3h

---

### Day 74 — Week 10 Review + K8s Operations Runbook
- **Objective:** Produce a K8s operations reference.
- **Build task (2h):** Write `04-devops/kubernetes/operations-runbook.md` — a real operational runbook for the deployed system: (1) How to check cluster health (`kubectl get nodes`, `kubectl get pods -A`). (2) How to debug a crashing pod (`kubectl describe pod X`, `kubectl logs X`, `kubectl logs X --previous`). (3) How to scale a deployment manually. (4) How to update an image (rolling update procedure). (5) How to roll back. (6) How to check resource usage. (7) How to port-forward to a service for local debugging. For each: exact commands with expected output.
- **Reflection output:** `notes/day-74.md` + `notes/week-10-review.md`
- **Estimated time:** 3h

---

## Week 11 — Observability, CI/CD, Incident Response (Days 75–81)

### Day 75
- **Objective:** Production-quality structured logging.
- **Study (30min):** Read about the ELK stack (Elasticsearch, Logstash, Kibana) and the Grafana Loki alternative. Understand log aggregation: why you can't just SSH into containers to read logs.
- **Build task (2h):** Upgrade logging in the Node.js backend (`02-backend-engineering/node` and `03-fullstack-system/backend`): (1) Every request log must include: `requestId` (UUID generated per request), `method`, `path`, `statusCode`, `duration_ms`, `userId` (if authenticated). (2) Every error log must include: `requestId`, `errorCode`, `errorMessage`, `stack` (only in non-production). (3) Add a `correlationId` header that passes through from the client (or generate one if absent). (4) Verify the JSON log output is queryable (you could grep or parse it). Commit.
- **LeetCode (45min):** Review + catch up on any remaining problems.
- **Reflection output:** `notes/day-75.md` — "Why is `console.log('Request received')` not useful in production? What 5 fields must be in every request log?"
- **Estimated time:** 3h

---

### Day 76
- **Objective:** Prometheus metrics from scratch — real instrumentation.
- **Study (30min):** Docker & Kubernetes course — Prometheus section. TechWorld with Nana — Prometheus + Grafana setup video.
- **Build task (2h):** (1) Verify the `prom-client` metrics from Day 53 are working. (2) Add to the Prometheus docker-compose: a `scrape_configs` entry that scrapes the backend. (3) Import a Grafana dashboard for Node.js metrics. (4) Create a custom Grafana dashboard panel showing: request rate (req/s), p95 latency, error rate (5xx%). (5) Write `05-production-thinking/observability.md` — your observability strategy: what you measure, what dashboards you have, what you would alert on, what SLOs you would set.
- **LeetCode (45min):** Any 2 problems you have been avoiding.
- **Reflection output:** `notes/day-76.md` — "What is the difference between RED (Rate, Errors, Duration) and USE (Utilization, Saturation, Errors) monitoring frameworks? When do you use each?"
- **Estimated time:** 3.5h

---

### Day 77
- **Objective:** Distributed tracing concepts and implementation.
- **Study (45min):** OpenTelemetry documentation — what tracing is, spans, traces, context propagation. Read about Jaeger as a backend. Read why tracing matters in multi-service systems (especially when you have Node.js + AI service + .NET).
- **Build task (1.5h):** Add basic OpenTelemetry instrumentation to the Node.js backend: (1) Install `@opentelemetry/sdk-node` and `@opentelemetry/auto-instrumentations-node`. (2) Set up the SDK to export traces to console (or Jaeger if you set it up). (3) Propagate the `traceparent` header to the AI service call so traces span both services. (4) Write `05-production-thinking/tracing.md` — explain: what a trace is, what a span is, how context propagation works across HTTP calls, and why this matters when debugging a slow request.
- **LeetCode (45min):** Final C++ session — solve 2 problems from any category that test your weakest area.
- **Reflection output:** `notes/day-77.md` — "A user reports their AI insights are slow. You have Prometheus, structured logs, and distributed traces. What do you check first, second, third?"
- **Estimated time:** 3h

---

### Day 78
- **Objective:** Build a real CI/CD pipeline.
- **Study (30min):** GitHub Actions docs — workflows, jobs, steps, artifacts. Read about the difference between CI (build + test) and CD (deploy).
- **Build task (2.5h):** Replace or improve the existing `.github/workflows/ci-cd.yml` with a real pipeline: Stage 1 (`lint-and-test`): checkout → install deps → run eslint → run Jest tests → fail the job if any step fails. Stage 2 (`build-image`): only runs if Stage 1 passes → build Docker image → tag with Git SHA. Stage 3 (`security-scan`): run `trivy` against the built image, fail on CRITICAL vulnerabilities. The pipeline must actually be valid YAML that would run on GitHub Actions. Test it by committing and watching the Actions tab.
- **Reflection output:** `notes/day-78.md` — "What is the difference between CI and CD? Why should a security scan be in the pipeline rather than a manual step?"
- **Estimated time:** 3.5h
- **Why this day matters:** A CI pipeline that runs on every push is a production-readiness signal. It protects the main branch and catches regressions automatically.

---

### Day 79
- **Objective:** Incident response simulation — know what to do at 3am.
- **Study (30min):** Google SRE book — Incident Management chapter (available free online). Read the principles: incident commander, communication, timeline, severity levels.
- **Build task (2h):** Simulate 3 failure scenarios and write runbooks for each in `05-production-thinking/incidents/`: (1) `runbook-db-connection-lost.md`: Database is down. What do you check? What is the recovery sequence? How do you communicate status? (2) `runbook-memory-leak.md`: Node.js service OOMKilled repeatedly. How do you diagnose? What is the immediate mitigation vs the fix? (3) `runbook-external-api-down.md`: AI service (external dependency) returns 503. What is the fallback behavior? How do users experience it? For each runbook: Detection → Triage → Mitigation → Resolution → Prevention. Include exact commands.
- **Reflection output:** `notes/day-79.md` — "What is the first thing you do when you get paged at 3am for a production incident? Walk me through the first 5 minutes."
- **Estimated time:** 3.5h

---

### Day 80
- **Objective:** Write a professional postmortem.
- **Study (15min):** Re-read `05-production-thinking/postmortems/template.md`. Look at `05-production-thinking/postmortems/example.md` — is it detailed enough? Probably not.
- **Build task (2.5h):** Write a detailed postmortem in `05-production-thinking/postmortems/db-connection-incident.md` for the database failure scenario from Day 79. Use the format: (1) Executive summary (3 sentences: what happened, how long, impact). (2) Timeline (minute-by-minute from alert to resolution). (3) Root cause analysis (5 Whys). (4) Impact (users affected, revenue impact, SLA violation). (5) Immediate remediation (what stopped the bleeding). (6) Long-term prevention (3–5 action items, each with an owner and due date). (7) Lessons learned. This should be 600–900 words. Treat it as something you would share with leadership.
- **Reflection output:** `notes/day-80.md` — "What makes a postmortem blameless? Why is the 5 Whys technique important?"
- **Estimated time:** 3.5h
- **Why this day matters:** The ability to write a postmortem is a senior signal that most engineers never practice until they are already senior.

---

### Day 81 — Week 11 Review + Production Readiness Checklist
- **Objective:** Produce a production readiness checklist.
- **Build task (2h):** Write `05-production-thinking/production-readiness-checklist.md` — a real checklist you would run against any service before deploying to production: (1) Health check endpoint (passes/fails). (2) Graceful shutdown (handles SIGTERM). (3) Structured JSON logging (requestId, userId, duration). (4) Error classification (operational vs programmer). (5) Authentication + authorization. (6) Input validation. (7) Rate limiting. (8) Database connection pooling. (9) Retry logic with backoff for external calls. (10) Circuit breaker for external dependencies. (11) Prometheus metrics endpoint. (12) Liveness + readiness probes. (13) Resource limits (CPU, memory). (14) Non-root container user. (15) Secrets in K8s Secrets (not ConfigMaps or env in manifests). For each: what it means, why it matters, how to verify it.
- **Reflection output:** `notes/day-81.md` + `notes/week-11-review.md`
- **Estimated time:** 3h

---

## Week 12 — Scaling, Senior Behavior, Final Preparation (Days 82–90)

### Day 82
- **Objective:** Caching architecture — design a complete caching strategy.
- **Study (45min):** Hussein Nasser — any caching deep dive video. Review the existing Redis caching in `03-fullstack-system/backend/src/services/listingService.js`.
- **Build task (2h):** Write `05-production-thinking/scaling/caching-strategy.md` — a complete caching architecture document for the platform: (1) What is currently cached (listing details) and why. (2) What should also be cached (search results, user sessions, rate limit counters) — for each: TTL, invalidation strategy, cache key format. (3) What should NOT be cached and why (user-specific sensitive data, real-time inventory). (4) Cache warming: how do you prevent cache stampede on startup or after a flush? (5) Multi-layer caching: when does a CDN make sense over Redis? (6) Failure mode: what happens when Redis goes down — does the API degrade gracefully or fail hard? Verify current behavior. Fix if needed.
- **Reflection output:** `notes/day-82.md`
- **Estimated time:** 3.5h

---

### Day 83
- **Objective:** Async architecture — event-driven design.
- **Study (45min):** Hussein Nasser — event-driven architecture video. Read about the outbox pattern for reliable event publishing.
- **Build task (2h):** Write `06-writing-thinking/design-docs/async-notification-system.md` — a design document for an async notification system built on top of the existing platform: (1) Problem: when a listing is created, send email + push notification to subscribers. (2) Why do this asynchronously (not in the request path). (3) Architecture: BullMQ job queue → email job + push notification job. (4) Failure handling: what happens if email service is down. (5) Exactly-once delivery: how do you prevent duplicate notifications. (6) Ordering: do notifications need to arrive in order? (7) The outbox pattern: how do you guarantee a BullMQ job is created if the DB transaction commits.
- **Reflection output:** `notes/day-83.md` — "What is the outbox pattern? What problem does it solve? Why can't you just publish to a queue inside a database transaction?"
- **Estimated time:** 3.5h

---

### Day 84
- **Objective:** Database scaling patterns — know the options and when each applies.
- **Build task (2h):** Write `05-production-thinking/scaling/database-scaling.md` — a reference document on database scaling patterns: (1) Vertical scaling: when does it work, when does it stop working. (2) Read replicas: what queries benefit, how to configure in Node.js (connection strings), what the replication lag risk is. (3) Connection pooling (PgBouncer): why raw database connections are expensive, what a pool size should be, what happens when pool is exhausted. (4) Partitioning: range vs list vs hash, when to use. (5) Sharding: when you truly need it, why it is painful, what you give up. (6) CQRS with separate read/write stores: when this pattern is worth its complexity. For each: a concrete scenario where you would apply it.
- **LeetCode (45min):** Two final system design warm-ups — answer from memory: "How does consistent hashing work?" and "What is a Bloom filter and when would you use one?" Write notes in `notes/day-84-algorithms-in-systems.md`.
- **Reflection output:** `notes/day-84.md`
- **Estimated time:** 3.5h

---

### Day 85
- **Objective:** Senior behavior — write like a senior engineer communicates.
- **Study (30min):** Read "How to write a design doc" (Google or Increment magazine). Read "Designing with Humans" or any article on engineering communication. What makes a technical proposal persuasive to non-engineers?
- **Build task (2h):** Write `notes/day-85-technical-proposal.md` — a mock technical proposal as if presenting to your engineering team: "Proposal: Add distributed tracing to the platform." Cover: (1) Problem statement (what is currently hard to debug). (2) Proposed solution (OpenTelemetry + Jaeger). (3) Estimated engineering effort (be honest: 2 days to instrument, 1 day to set up Jaeger). (4) Alternatives considered (and why rejected). (5) Risks and unknowns. (6) Success criteria (how will we know this worked). Write this as something you would actually send in Slack or present in a meeting.
- **Reflection output:** `notes/day-85.md` — "What makes a technical proposal fail to get approved? What is the most important section?"
- **Estimated time:** 3h

---

### Day 86
- **Objective:** Full system design interview — timed, final drill.
- **Build task (3h):** Set a 45-minute timer. Design a ride-hailing system (like Uber). Write your full answer in `notes/day-86-ride-hailing-design.md`: (1) Requirements. (2) Scale estimation. (3) Core APIs. (4) Data model. (5) Location tracking architecture (how does the driver's GPS update get to the rider in real time?). (6) Matching algorithm (how does Uber pair a rider with the nearest driver?). (7) Trip lifecycle state machine. (8) Bottlenecks and tradeoffs. Compare to `01-core-engineering/system-design/ride-hailing.md` and write a self-critique. Then: write a 200-word reflection on what you would have missed on Day 1 of this 90-day journey that you did not miss today.
- **Reflection output:** `notes/day-86.md`
- **Estimated time:** 4h
- **Why this day matters:** This system design is the same as Day 29's URL Shortener, but for a much harder problem. The quality of your answer reflects 86 days of growth.

---

### Day 87
- **Objective:** Final LeetCode session — master the patterns you know.
- **Build task (2.5h):** Review all LeetCode solutions in `01-core-engineering/leetcode/solutions/`. Update the problem tracker with your status (solved/not solved) and difficulty rating. Write `01-core-engineering/leetcode/pattern-cheatsheet.md` — your personal cheatsheet: for each pattern (Two Pointers, Sliding Window, Hash Map, Trees BFS/DFS, Graphs BFS/DFS/Topo, DP, Backtracking, Heaps, Binary Search, Intervals), write: the signal that tells you to use this pattern, the template code in Python, the template code in C++, and 2 example problems.
- **LeetCode (1h):** Solve 3 problems you have not solved yet, using the cheatsheet as reference.
- **Reflection output:** `notes/day-87.md` — "Which patterns are you strongest in? Which are you still weakest in? What is your LeetCode plan after Day 90?"
- **Estimated time:** 3.5h

---

### Day 88
- **Objective:** Portfolio narrative — tell the story of what you built.
- **Build task (2.5h):** Write `07-showcase/portfolio-narrative.md` — a 700-word portfolio statement you could share with a hiring manager or a technical recruiter: (1) What this repo is and what it proves. (2) The 3 most technically interesting things you built in 90 days (be specific: which file, what it does, why it was hard). (3) What you understand now about production engineering that you did not understand 90 days ago. (4) The one artifact you are most proud of and why. Update `07-showcase/system-walkthrough.md` to be a genuine 10-minute walkthrough guide of the full system for a technical interviewer.
- **Reflection output:** `notes/day-88.md`
- **Estimated time:** 3h

---

### Day 89
- **Objective:** Mock interview preparation — full rehearsal.
- **Build task (2h):** Write `notes/day-89-mock-interview-log.md` — a mock interview simulation: (1) System design (45 min): design a distributed job queue. Write your answer. (2) Technical deep dive (30 min): write answers to these 3 questions as if speaking out loud: "Walk me through the Node.js event loop", "What happens in a K8s rolling update at the infrastructure level?", "How would you debug a memory leak in production with no reproduction steps?" (3) Behavioral (15 min): answer "Why are you interested in senior/staff engineer roles?" and "What's the most complex system you've worked on and what was your contribution?" Evaluate yourself: what felt weak? What needs more practice?
- **Reflection output:** `notes/day-89.md`
- **Estimated time:** 3h

---

### Day 90 — Final Review and Closure
- **Objective:** Close the 90 days with evidence and a clear "what's next."
- **Build task (2.5h):** (1) Update `tracking/progress-tracker.md` — mark Phase 3 complete. List every major artifact produced in all 90 days. (2) Verify the entire project builds: `docker-compose up` works, `dotnet test` passes, Node.js backend starts without errors. (3) Write `notes/phase-03-review.md` (600 words): what is your Docker/K8s understanding now? What does your observability setup look like? What incident can you handle that you could not on Day 1? (4) Write `notes/day-90-what-next.md` — "What are the 5 most important things I will work on in the next 90 days?" Be honest about what is still weak. (5) Tag the repository `v1.0` in git. Commit and push everything.
- **Reflection output:** `notes/day-90.md` + `notes/phase-03-review.md` + `notes/day-90-what-next.md`
- **Estimated time:** 3h
- **Why this day matters:** Finishing is a senior behavior. Shipping is a senior behavior. Tagging a release and writing what comes next is how senior engineers think about their own growth.

---

## Phase 3 non-negotiable outcomes

Before calling Day 90 done, verify every item:

- [ ] `Dockerfile.backend` — multi-stage, non-root user, committed
- [ ] `docker-compose.yml` — health checks, `condition: service_healthy`, env_file, committed
- [ ] `docker-compose.monitoring.yml` — Prometheus + Grafana, committed
- [ ] All K8s manifests updated: readiness/liveness probes, resource limits, ConfigMaps/Secrets, HPA
- [ ] `04-devops/docker/debugging-runbook.md` — operational runbook committed
- [ ] `04-devops/kubernetes/operations-runbook.md` — K8s runbook committed
- [ ] `04-devops/kubernetes/rollback-runbook.md` — rollback procedure committed
- [ ] `.github/workflows/ci-cd.yml` — real pipeline: lint + test + build + image scan
- [ ] `05-production-thinking/incidents/runbook-db-connection-lost.md` — committed
- [ ] `05-production-thinking/incidents/runbook-memory-leak.md` — committed
- [ ] `05-production-thinking/incidents/runbook-external-api-down.md` — committed
- [ ] `05-production-thinking/postmortems/db-connection-incident.md` — full postmortem
- [ ] `05-production-thinking/production-readiness-checklist.md` — committed
- [ ] `05-production-thinking/observability.md` — observability strategy
- [ ] `06-writing-thinking/design-docs/async-notification-system.md` — design doc
- [ ] `01-core-engineering/leetcode/pattern-cheatsheet.md` — committed
- [ ] `notes/day-86-ride-hailing-design.md` — final system design drill
- [ ] `07-showcase/portfolio-narrative.md` — 700-word portfolio statement
- [ ] All 30 `notes/day-XX.md` files (Day 61–90) are non-empty
- [ ] All weekly reviews written (weeks 9–12)
- [ ] Progress tracker shows all 3 phases complete
- [ ] Repository tagged `v1.0`

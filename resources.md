# Resource Map — 90-Day Engineering Transformation

This file maps every resource to the exact phase, week, and purpose.
Do not open a course until its phase begins.
Do not binge watch. Spend no more than 50% of any day on video content.
The other 50% must be building, coding, or writing.

---

## What was wrong with the previous resource list

The previous `resources/README.md` mapped 60 days to: React, Next.js, Supabase, React Native, TypeScript frontend, Storybook, Expo, Firebase, Firestore.

That is not this plan.
That plan was for a different goal. This plan is for Node.js depth, .NET, SQL, Docker, K8s, system design, and LeetCode.

---

## The core resource stack

### 1. Node.js — The Complete Guide (Udemy)
**URL:** https://www.udemy.com/course/nodejs-the-complete-guide-incl-mvc-rest-apis-graphql-deno/
**Phase:** Phase 1 (Days 1–7 and Days 15–20)
**Mode:** PARTIAL — do not complete the whole course
**What to watch:**
- Section on event loop and async (Days 1–2)
- Section on Streams (Day 3)
- Section on REST APIs and Express middleware (Days 15–16)
- Section on authentication (Day 17)
**What to skip:**
- GraphQL section (not relevant to this plan)
- Deno section (not relevant)
- React/Rendering section (not relevant)
- Deploy section (use the Docker/K8s material instead)
**Estimated time for this plan:** 20–25 hours

---

### 2. ASP.NET Core — SOLID and Clean Architecture (Udemy)
**URL:** https://www.udemy.com/course/aspnet-core-solid-and-clean-architecture-net-5-and-up/
**Phase:** Phase 2 (Days 31–42)
**Mode:** MOST OF IT — this is the primary .NET resource
**What to watch:**
- All sections on Clean Architecture layers (Days 31–33)
- DI and service lifetimes (Day 31)
- Domain modeling (Day 33)
- Application layer and CQRS (Day 34)
- Infrastructure and EF Core (Day 35)
- Validation (Day 36–37)
- Authentication (Day 38)
**What to skip:**
- Advanced deployment sections (covered in Phase 3 instead)
- UI sections
**Estimated time for this plan:** 15–20 hours

---

### 3. Clean Architecture in .NET Core MVC [2025] — Complete Guide (Udemy)
**URL:** https://www.udemy.com/course/clean-architecture-in-net-core-mvc-complete-guide/
**Phase:** Phase 2, supplementary (Days 32–40)
**Mode:** SUPPLEMENTARY — use alongside the above course when you want a second perspective
**Estimated time:** 5–8 hours selectively

---

### 4. Introduction to Databases for Back-End Development (Coursera)
**URL:** https://www.coursera.org/learn/intro-to-databases-back-end-development
**Phase:** Phase 1 (Days 8–14)
**Mode:** PARTIAL — skip what you already know
**What to use:**
- Week 1: ER modeling and normalization (Day 8)
- Week 2: SQL fundamentals — use as reference for Days 9–13
- Week 3: Advanced SQL — window functions context (Day 12)
**What to skip:**
- Week 1 basics (SQL SELECT, INSERT, UPDATE, DELETE — you know this)
- Any NoSQL sections (covered separately)
**Estimated time for this plan:** 8–10 hours

---

### 5. Docker & Kubernetes: The Practical Guide (Udemy)
**URL:** https://www.udemy.com/course/docker-kubernetes-the-practical-guide/
**Phase:** Phase 3 (Days 61–74)
**Mode:** MOST OF IT — this is the primary infra resource
**What to watch:**
- Docker images, containers, layers (Day 61)
- Multi-stage builds (Day 61)
- Docker networking (Day 64)
- Docker Compose (Days 62–63)
- Kubernetes architecture (Day 68)
- Deployments and Services (Day 69)
- ConfigMaps and Secrets (Day 70)
- Deployments and rolling updates (Day 71)
- HPA (Day 72)
- Ingress (Day 73)
**What to skip:**
- AWS ECS section (not relevant)
- Managed Kubernetes (EKS/GKE) sections for this plan — focus on concepts
**Estimated time for this plan:** 25–30 hours

---

### 6. Mastering Data Structures & Algorithms using C and C++ (Udemy)
**URL:** https://www.udemy.com/course/datastructurescncpp/
**Phase:** Phase 2 (before C++ LeetCode starts, Day 37–38)
**Mode:** VERY PARTIAL — only use the STL section
**What to watch:**
- STL containers: vector, map, unordered_map, set, priority_queue (Day 37–38)
- STL algorithms: sort, binary_search, lower_bound, upper_bound
**What to skip:**
- All basic data structures (you already know these)
- All basic algorithms in C (use C++ STL instead)
**Estimated time for this plan:** 4–6 hours

---

### 7. Software Design and Architecture Specialization (Coursera)
**URL:** https://www.coursera.org/specializations/software-design-architecture
**Phase:** Phase 2 (Days 32–36)
**Mode:** ONE COURSE ONLY — "Design Patterns" course
**What to use:**
- Object Oriented Design course: UML basics, SOLID principles (skim — 2 hours)
- Design Patterns course: use the sections on Factory, Strategy, Repository, Observer (Days 32–36)
**What to skip:**
- Software Architecture course: too theoretical for this plan, use the Hussein Nasser channel instead
- Service-Oriented Architecture course: skip entirely
**Estimated time for this plan:** 6–10 hours

---

## YouTube channels (use throughout all phases)

### Hussein Nasser
**URL:** https://www.youtube.com/@hnasr
**Usage:** Weekly, throughout all phases. His videos are dense and specific.
**Best videos for this plan:**
- Node.js event loop (Phase 1, Day 1)
- Node.js clustering (Phase 1, Day 4)
- HTTP/2, HTTP/3 deep dives (Phase 2, Week 7)
- PostgreSQL indexing and performance (Phase 1, Days 10–13)
- System design: Uber, Twitter, WhatsApp (Phase 2, Week 7)
- Redis architecture (Phase 1, Days 23–25)
- Event-driven architecture (Phase 3, Day 83)
- Load balancers (Phase 3, Days 68–69)
**Time budget:** ~2 hours/week. Do not binge. Watch one video, take notes, then build.

---

### TechWorld with Nana
**URL:** https://www.youtube.com/@TechWorldwithNana
**Usage:** Phase 3 specifically (Docker and K8s weeks)
**Best videos:**
- Docker tutorial for beginners (Day 61 — first 30 min as warm-up)
- Kubernetes tutorial for beginners (Day 68 — first 30 min as warm-up)
- Prometheus + Grafana setup (Day 76)
- Kubernetes crash course (supplement for Days 68–74)
**Time budget:** 1–2 hours per relevant day, not more.

---

### NeetCode
**URL:** https://www.youtube.com/@NeetCode
**Usage:** Before each LeetCode pattern block (5–10 minutes max per video)
**Best videos:**
- Arrays & Hashing overview (Phase 1, before Day 1 LeetCode)
- Two Pointers overview (Phase 1, Day 1–7)
- Sliding Window overview (Phase 1, Day 8–14)
- Trees overview (Phase 1, Day 15–21)
- Graphs overview (Phase 1, Day 22–28)
- DP overview (Phase 2, before Day 32)
- Heaps overview (Phase 2, before Day 42)
- Backtracking overview (Phase 2, Day 48–49)
**Rule:** Watch the pattern overview video. Then solve the problem yourself. Do not watch solutions first.

---

### freeCodeCamp
**URL:** https://www.youtube.com/@freecodecamp
**Usage:** BACKUP ONLY — if you need a SQL or PostgreSQL refresher
**When to use:** If you are struggling with Phase 1 SQL material and need more scaffolding.
**What to use:** Their PostgreSQL full course. Skip sections on basic SELECT if you already know them.
**When NOT to use:** As a primary learning path. This plan has primary resources already.

---

## Algorithms Specialization (Stanford, Coursera)
**URL:** https://www.coursera.org/specializations/algorithms
**Usage:** NOT IN THIS PLAN's primary track
**Why it's not primary:** Too theoretical for 90 days focused on building. The algorithms you need for LeetCode are best learned from NeetCode + practice.
**When to add it:** After Day 90, if you want to deepen algorithm theory for FAANG-level interviews.

---

## Cloud Computing Specialization (Coursera)
**URL:** https://www.coursera.org/specializations/cloud-computing
**Usage:** NOT IN THIS PLAN
**Why:** Covers distributed systems theory (great content) but the scope extends beyond 90 days.
**When to add it:** After completing Phase 3 if you want to deepen distributed systems theory.

---

## Books (reference, not required reading)

These are not assigned reading. Use them as reference when a topic needs depth.

| Book | When to reference |
|------|-------------------|
| Designing Data-Intensive Applications (Kleppmann) | Phase 1 Days 22–27 (Redis, databases), Phase 3 Day 84 (scaling) |
| System Design Interview (Alex Xu) | Phase 2 Week 7 (system design drills) — compare your designs |
| The Art of PostgreSQL (Stephane Faroult) | Phase 1 Days 8–14 (SQL depth) |
| Site Reliability Engineering (Google, free online) | Phase 3 Days 79–81 (incident response, postmortems) |
| Clean Architecture (Uncle Bob) | Phase 2 Days 32–33 (reference for .NET architecture) |

---

## Resource anti-patterns — do not do these

- Do not start Docker & Kubernetes course in Phase 1. It belongs in Phase 3.
- Do not watch entire Node.js course from start to finish. Only the sections listed above.
- Do not binge YouTube. One focused video per topic, then build.
- Do not open Coursera Algorithm Specialization. It is not in this plan.
- Do not watch React/Next.js tutorials. They are not in this plan.
- Do not bookmark 50 articles about a topic. Read one, understand it, build something.

---

## Time breakdown per week

| Week | Primary resource | Hours on resource | Hours on building/coding |
|------|-----------------|------------------|--------------------------|
| 1 | Hussein Nasser (event loop) + NodeJS course (sections 1–3) | 3–4h | 8–12h |
| 2 | Coursera Databases + freeCodeCamp SQL backup | 3–4h | 8–12h |
| 3 | NodeJS course (REST sections) | 2–3h | 9–13h |
| 4 | Hussein Nasser (Redis, MongoDB) | 2–3h | 9–13h |
| 5–6 | ASP.NET Core Clean Architecture | 5–7h/week | 7–11h/week |
| 7 | Hussein Nasser (system design) | 2–3h | 10–14h |
| 8 | C/C++ DSA course (STL only) | 2–3h | 9–13h |
| 9 | Docker & K8s course (Docker sections) | 5–7h | 7–11h |
| 10 | Docker & K8s course (K8s sections) | 5–7h | 7–11h |
| 11 | TechWorld with Nana (Prometheus/Grafana) | 2–3h | 9–13h |
| 12 | Hussein Nasser (scaling/async) | 2–3h | 9–13h |

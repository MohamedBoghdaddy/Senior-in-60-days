# Phase 2: Backend & Architecture Depth — Days 31–60

**Goal:** Build real .NET clean architecture. Practice system design under pressure 6 times. Write real code reviews. Start LeetCode in C++. Produce production-quality backend artifacts.

By Day 60 you must have: a working .NET API committed, 6 system design write-ups, a formal code review document, C++ LeetCode solutions, and all 30 daily notes filled in.

---

## Week 5 — .NET Clean Architecture Foundation (Days 31–37)

### Day 31
- **Objective:** Understand the .NET ecosystem from first principles before writing code.
- **Study (1h):** ASP.NET Core Clean Architecture (Udemy) — Watch Section 1: course overview + .NET architecture fundamentals. Write notes on: solution structure, SDK vs runtime, `WebApplication.CreateBuilder`, the middleware pipeline, DI container lifecycle.
- **Build task (1.5h):** Create a new .NET 8 Web API project using `dotnet new webapi -n CleanShop`. Explore the generated code. Delete the WeatherForecast controller. Understand what `Program.cs` does. Add a `HealthController` with a `GET /health` endpoint that returns `{ status: "ok", timestamp: DateTime.UtcNow }`. Run it with `dotnet run`. Commit.
- **LeetCode (45min):** Climbing Stairs (Python) — DP. Coin Change (Python) — DP bottom-up and top-down.
- **Reflection output:** `notes/day-31.md` — "What is the difference between `AddTransient`, `AddScoped`, and `AddSingleton` in ASP.NET Core DI? Give a concrete example of when you would use each."
- **Estimated time:** 3.5h
- **Why this day matters:** .NET is not just "another framework." Its DI model, middleware pipeline, and hosting model are deeply different from Node.js. Understanding the runtime before writing business logic prevents structural mistakes.

---

### Day 32
- **Objective:** Understand Clean Architecture layers and why they exist.
- **Study (1h):** ASP.NET Core Clean Architecture (Udemy) — Section 2: Clean Architecture overview. Uncle Bob's Clean Architecture layers: Domain, Application, Infrastructure, Presentation. The dependency rule: outer layers depend on inner layers, never the reverse. Write notes on what belongs in each layer and why.
- **Build task (1.5h):** Restructure the `CleanShop` project into 4 separate projects: `CleanShop.Domain`, `CleanShop.Application`, `CleanShop.Infrastructure`, `CleanShop.API`. Set up project references following the dependency rule. Add a `Product` domain entity with `Id`, `Name`, `Price`, `StockCount`. Commit the solution structure.
- **LeetCode (45min):** Longest Increasing Subsequence (Python) — both O(n²) and O(n log n) approaches.
- **Reflection output:** `notes/day-32.md` — "Why does the Domain layer not reference the Infrastructure layer? What problem does this solve? Draw the dependency arrows."
- **Estimated time:** 3.5h

---

### Day 33
- **Objective:** Build the Domain layer — rich entities and value objects.
- **Study (45min):** ASP.NET Core Clean Architecture — Section 3: Domain modeling. Difference between anemic domain model and rich domain model. Value objects: why `Money` is better than `decimal Price`. Domain events.
- **Build task (2h):** In `CleanShop.Domain`: (1) Add a `Price` value object (immutable, validates non-negative). (2) Add a `ProductId` value object (wraps Guid, prevents raw Guid confusion). (3) Make `Product` use these value objects. (4) Add a domain method `Product.ApplyDiscount(Percentage p)` that validates the discount is between 0–100 and returns a new Product. (5) Write xUnit tests for the domain logic — does discount work, does negative price throw, does invalid discount throw.
- **LeetCode (45min):** Word Break (Python) + Edit Distance (Python) — DP classic.
- **Reflection output:** `notes/day-33.md` — "What is the difference between a Value Object and an Entity in Domain-Driven Design? Why can't a Value Object have an identity?"
- **Estimated time:** 3.5h

---

### Day 34
- **Objective:** Build the Application layer — use cases with CQRS.
- **Study (1h):** ASP.NET Core Clean Architecture — Section 4: Application layer. CQRS pattern: Commands change state, Queries return data. MediatR library. Pipeline behaviors (cross-cutting concerns as pipeline stages).
- **Build task (2h):** Add MediatR to `CleanShop.Application`. Create: (1) `GetProductByIdQuery` + `GetProductByIdQueryHandler` — returns a `ProductDto`. (2) `CreateProductCommand` + `CreateProductCommandHandler` — creates a product, returns its ID. (3) `IProductRepository` interface in Application (not Infrastructure). (4) A `ValidationBehavior<TRequest, TResponse>` pipeline behavior that validates commands using FluentValidation before the handler runs. (5) `CreateProductCommandValidator` that validates Name is not empty, Price > 0, StockCount >= 0.
- **LeetCode (45min):** Maximum Product Subarray (Python) + House Robber (Python).
- **Reflection output:** `notes/day-34.md` — "What problem does CQRS solve? What is a MediatR pipeline behavior and why is it better than cross-cutting concerns in each handler?"
- **Estimated time:** 3.5h

---

### Day 35
- **Objective:** Build the Infrastructure layer — EF Core + repository implementation.
- **Study (1h):** ASP.NET Core Clean Architecture — Section 5: Infrastructure. EF Core basics: DbContext, migrations, repository implementation. Why Infrastructure implements interfaces defined in Application.
- **Build task (2h):** In `CleanShop.Infrastructure`: (1) Add `ProductDbContext` with a `Products` DbSet. (2) Implement `ProductRepository : IProductRepository` using EF Core. (3) Add an EF Core migration. (4) Configure the project to use SQLite (simpler for local dev). (5) Wire everything together in `Program.cs` — register `DbContext`, register repositories, register MediatR. (6) Test the full flow: POST /products creates a product, GET /products/{id} returns it.
- **LeetCode (45min):** Unique Paths (Python) + Jump Game (Python).
- **Reflection output:** `notes/day-35.md` — "Why do we define `IProductRepository` in Application but implement it in Infrastructure? What would break if Infrastructure defined the interface?"
- **Estimated time:** 3.5h

---

### Day 36
- **Objective:** Add proper .NET error handling and HTTP response standards.
- **Study (30min):** ASP.NET Core — ProblemDetails standard (RFC 7807). Read how to return consistent `{ type, title, status, detail }` error responses. Look at the existing `ExceptionMiddleware.cs` in `02-backend-engineering/dotnet/Middleware/`.
- **Build task (2h):** (1) Replace the basic exception middleware with a proper ProblemDetails middleware that maps: `NotFoundException` → 404, `ValidationException` → 422 with field errors, generic exceptions → 500 (no stack trace to client). (2) Add a `NotFoundException` domain exception class. (3) In `GetProductByIdQueryHandler`, throw `NotFoundException` when the product does not exist. (4) Write integration tests using `WebApplicationFactory` to verify the 404 response format. Commit.
- **LeetCode (45min):** Partition Equal Subset Sum (Python) + Target Sum (Python) — DP with knapsack.
- **Reflection output:** `notes/day-36.md` — "What is the ProblemDetails standard? Why should an API return consistent error shapes instead of custom error formats?"
- **Estimated time:** 3.5h

---

### Day 37
- **Objective:** Add proper .NET integration tests and commit the full .NET project.
- **Study (30min):** xUnit documentation on `WebApplicationFactory`. Read about test categories: unit (domain logic), integration (API + real DB).
- **Build task (2h):** Write a complete test suite for the `CleanShop.API`: (1) `GetProductById_WhenExists_Returns200WithProduct` (2) `GetProductById_WhenNotFound_Returns404WithProblemDetails` (3) `CreateProduct_WithValidData_Returns201WithId` (4) `CreateProduct_WithInvalidPrice_Returns422WithFieldError` (5) `CreateProduct_WithEmptyName_Returns422WithFieldError`. Make all tests pass. Commit everything. The `.NET` solution is now a real portfolio artifact.
- **LeetCode (45min):** Coin Change II (Python) + Longest Common Subsequence (Python).
- **Reflection output:** `notes/day-37.md` + `notes/week-05-review.md` — What does the CleanShop project prove about your .NET knowledge? What is still missing?
- **Estimated time:** 3.5h

---

## Week 6 — .NET Depth + LeetCode C++ Introduction (Days 38–44)

### Day 38
- **Objective:** Add authentication and authorization to the .NET project.
- **Study (45min):** ASP.NET Core Clean Architecture — JWT section. Review the existing `02-backend-engineering/dotnet/` auth patterns.
- **Build task (2h):** Add JWT authentication to `CleanShop.API`: (1) `LoginCommand` + `LoginCommandHandler` that validates credentials and returns a JWT. (2) Configure `AddAuthentication().AddJwtBearer(...)` in `Program.cs`. (3) Protect `POST /products` with `[Authorize]`. (4) Add a `RegisterCommand` for user registration. (5) Write an integration test that: (a) registers a user, (b) logs in and gets a token, (c) uses the token to create a product, (d) verifies a request without a token returns 401.
- **LeetCode C++ start (45min):** Two Sum (C++) + Valid Parentheses (C++). For C++ LeetCode: always write the time/space complexity and note any STL containers used (`unordered_map`, `stack`, etc.).
- **Reflection output:** `notes/day-38.md` — "What is the difference between authentication and authorization? How does ASP.NET Core's `[Authorize]` attribute implement authorization?"
- **Estimated time:** 3.5h

---

### Day 39
- **Objective:** Build the complete CRUD API surface for the .NET project.
- **Build task (3h):** Add remaining product CRUD to `CleanShop.API`: (1) `UpdateProductCommand` — update name, price, stock. (2) `DeleteProductCommand` — soft delete (add `IsDeleted` flag). (3) `ListProductsQuery` — paginated list with keyset pagination. (4) `ApplyDiscountCommand` — uses the domain method from Day 33. (5) Wire all endpoints. (6) Write 3 tests per new endpoint. The API should now be a genuinely functional product API. Commit.
- **LeetCode C++ (45min):** 3Sum (C++) + Container With Most Water (C++).
- **Reflection output:** `notes/day-39.md` — "Looking at the full CleanShop API, what would you change before deploying it to production? Name 5 things."
- **Estimated time:** 3.5h

---

### Day 40
- **Objective:** Add observability to the .NET project.
- **Study (30min):** ASP.NET Core logging with `ILogger<T>`. Read about Serilog for structured logging in .NET.
- **Build task (2h):** (1) Add Serilog to `CleanShop.API` with JSON output. (2) Add structured logging to every command handler: log `ProductId`, `UserId`, `CommandType` for every operation. (3) Add a logging pipeline behavior (MediatR) that logs every command/query name and duration. (4) Add a `GET /health` endpoint that checks DB connectivity and returns the result. Commit.
- **LeetCode C++ (45min):** Merge Intervals (C++) + Group Anagrams (C++) — STL practice.
- **Reflection output:** `notes/day-40.md` — "What fields should be in every log line from a command handler? Why does logging duration matter?"
- **Estimated time:** 3h

---

### Day 41
- **Objective:** Write a proper ADR comparing Node.js vs .NET for API development.
- **Build task (2.5h):** Write `90-days-fullstack-engineer/06-writing-thinking/decisions/nodejs-vs-dotnet-api.md` — a formal ADR: (1) Context: you are choosing a backend technology for a new B2B SaaS API. (2) Options considered: Node.js + Express, .NET 8 + Clean Architecture. (3) For each: performance characteristics, ecosystem, testing story, hiring market, operational cost. (4) Decision: which would you choose and why (be specific, not generic). (5) Consequences: what are the accepted tradeoffs. This ADR must be 500+ words and show that you have actually built in both.
- **LeetCode C++ (45min):** Binary Search (C++) + Search in Rotated Sorted Array (C++).
- **Reflection output:** `notes/day-41.md` — "What surprised you about .NET compared to Node.js? What does .NET do better? What does Node.js do better?"
- **Estimated time:** 3h

---

### Day 42
- **Objective:** Produce a code review of your own .NET project as if you were a senior reviewer.
- **Build task (2h):** Write `notes/day-42-dotnet-code-review.md` — a structured code review of the `CleanShop` project you built. Format as if you were commenting on a PR: (1) Review the domain model: is the value object usage appropriate? Are entities truly encapsulated? (2) Review the application layer: are commands and queries well-named? Are handlers focused? (3) Review the infrastructure layer: is the repository abstraction appropriate? (4) Review tests: are they testing behavior or implementation? Do they test failure paths? (5) Write at least 10 specific review comments (filename + line reference + what to change + why). (6) List the top 3 things you would prioritize fixing.
- **LeetCode C++ (45min):** Top K Frequent Elements (C++) — use priority queue. Find Median from Data Stream (C++) — two-heap approach.
- **Reflection output:** `notes/day-42.md` + `notes/week-06-review.md`
- **Estimated time:** 3.5h

---

## Week 7 — System Design Drills (Days 43–49)

### Day 43
- **Objective:** System design drill #2 — Notification System.
- **Build task (2.5h):** Set a 45-minute timer. Design a notification system (email, SMS, push notifications for 10M users). Write your answer in `notes/day-43-notification-system-design.md`: (1) Requirements. (2) Scale. (3) API design. (4) Data model. (5) Architecture. (6) How do you handle delivery failures (retry, DLQ)? (7) How do you prevent duplicate notifications? (8) Bottlenecks + tradeoffs. After timer stops, compare to `01-core-engineering/system-design/notification-system.md`. Write self-critique.
- **LeetCode C++ (45min):** Kth Largest Element (C++) — quickselect + heap approaches. Merge K Sorted Lists (C++).
- **Reflection output:** `notes/day-43.md`
- **Estimated time:** 3.5h

---

### Day 44
- **Objective:** System design drill #3 — Distributed Cache.
- **Build task (2.5h):** 45-minute timed drill. Design a distributed cache (like Redis). Write in `notes/day-44-distributed-cache-design.md`. Focus on: eviction policies (LRU, LFU, TTL), consistency (single-node vs cluster), replication, partitioning strategies (consistent hashing), what to do when a node fails. Compare to `system-design/distributed-cache.md`. Self-critique.
- **LeetCode C++ (45min):** LRU Cache (C++) — `unordered_map` + doubly linked list. Sliding Window Maximum (C++).
- **Reflection output:** `notes/day-44.md`
- **Estimated time:** 3.5h

---

### Day 45
- **Objective:** System design drill #4 — Chat System.
- **Build task (2.5h):** 45-minute timed drill. Design a real-time chat system (like Slack). Write in `notes/day-45-chat-system-design.md`. Focus on: WebSocket vs polling vs long polling (justify your choice), message ordering guarantees, message storage, read receipts, presence (who is online), group chats, message search. Compare to `system-design/chat-system.md`. Self-critique.
- **LeetCode C++ (45min):** Task Scheduler (C++) — greedy. Reorganize String (C++).
- **Reflection output:** `notes/day-45.md`
- **Estimated time:** 3.5h

---

### Day 46
- **Objective:** System design drill #5 — News Feed / Timeline.
- **Build task (2.5h):** 45-minute timed drill. Design a social media news feed (like Twitter timeline). Write in `notes/day-46-news-feed-design.md`. Focus on: fanout on write vs fanout on read (and the celebrity problem), feed ranking, pagination, caching the feed, what happens when a user follows 10,000 accounts. Compare to `system-design/news-feed.md`. Self-critique.
- **LeetCode C++ (45min):** Minimum Cost to Connect Ropes (C++) + Furthest Building (C++) — heap problems.
- **Reflection output:** `notes/day-46.md`
- **Estimated time:** 3.5h

---

### Day 47
- **Objective:** System design drill #6 — Video Streaming Platform.
- **Build task (2.5h):** 45-minute timed drill. Design a video streaming platform (like YouTube). Write in `notes/day-47-video-streaming-design.md`. Focus on: video upload pipeline (transcoding, storage), CDN for delivery, thumbnail generation, view count accuracy, comments, search indexing. Compare to `system-design/video-streaming.md`. Self-critique.
- **LeetCode C++ (45min):** IPO (C++) — greedy with two heaps + Sort K Closest to Origin (C++).
- **Reflection output:** `notes/day-47.md`
- **Estimated time:** 3.5h

---

### Day 48
- **Objective:** Build a personal system design framework.
- **Study (1h):** Watch Hussein Nasser — any 2–3 system design framework videos (search for his "how to answer system design questions"). Write notes on frameworks: RESHADED, Capacity Estimation basics, back-of-envelope calculations.
- **Build task (1.5h):** Write `90-days-fullstack-engineer/01-core-engineering/system-design/SYSTEM-DESIGN-FRAMEWORK.md` — your personal checklist for any system design question: (1) Requirements gathering questions (list 10 you always ask). (2) Scale estimation formula sheet (users → DAU → QPS → storage). (3) Architecture component checklist (load balancer, cache, queue, DB, CDN — when does each apply?). (4) Tradeoff decision tree. (5) Failure modes to always consider. This is your personal reference.
- **LeetCode C++ (45min):** Find K Pairs with Smallest Sums (C++) + Swim in Rising Water (C++).
- **Reflection output:** `notes/day-48.md` + `notes/week-07-review.md` — "After 6 system design drills, what patterns keep appearing? What component do you consistently underdesign?"
- **Estimated time:** 3.5h

---

### Day 49
- **Objective:** Consolidate C++ LeetCode — heap and priority queue pattern mastery.
- **Build task (2.5h):** Review all C++ LeetCode solutions from Days 38–48. For each: verify complexity, ensure STL usage is correct. Write `90-days-fullstack-engineer/01-core-engineering/leetcode/cpp-patterns.md` — a reference doc covering: (1) When to use `priority_queue` vs `multiset`. (2) Max-heap vs min-heap in C++ (the trick for max-heap). (3) `unordered_map` vs `map` — when to use each. (4) Common C++ STL patterns for LeetCode (pair sorting, lambda comparators). (5) 5 heap problems and their patterns.
- **LeetCode C++ (1h):** Solve 2 problems from your weak areas in C++.
- **Reflection output:** `notes/day-49.md`
- **Estimated time:** 3.5h

---

## Week 8 — Code Review, Debugging, Production Node.js (Days 50–56)

### Day 50
- **Objective:** Build a code review practice — read code critically.
- **Study (45min):** Google Engineering Practices — Code Review guide (search "google eng practices code review"). Read all of it. It is not long. Write notes on: what to look for, how to phrase comments, what is NOT worth blocking on.
- **Build task (2h):** Write `notes/day-50-code-review-template.md` — a formal code review template: (1) Header: PR title, author, reviewer, date. (2) Must-fix section (correctness, security, data loss risk). (3) Should-fix section (performance, maintainability, clarity). (4) Nit section (style, naming). (5) Positive section (what was done well). Then: do a complete code review of the `03-fullstack-system/backend/src/` Node.js service. Write the full review using this template. Minimum 15 specific comments.
- **LeetCode C++ (45min):** Two Sum (C++ revisit with different approach) + Clone Graph (C++).
- **Reflection output:** `notes/day-50.md` — "What are the 3 most important things to check in a code review? What should you NOT comment on?"
- **Estimated time:** 3.5h
- **Why this day matters:** Writing code reviews is a differentiator. Most candidates cannot do it. This document is a portfolio piece.

---

### Day 51
- **Objective:** Debug systematically — not by luck.
- **Study (45min):** Read "How to debug anything" (search for Julia Evans debugging zine or similar). Write notes on: hypothesis-driven debugging, binary search debugging, rubber duck debugging, printf debugging vs step-through debugging.
- **Build task (1.5h):** (1) Write a script `notes/day-51-debug-exercise.js` with 3 intentional bugs (logic error, async error, off-by-one). (2) Using VS Code debugger (not console.log), find and fix all 3 bugs. (3) Write `notes/day-51-debugging-process.md` — for each bug: what hypothesis you formed, how you tested it, what you found, what the fix was. This is debugging as a professional discipline.
- **LeetCode C++ (45min):** Course Schedule (C++) — topological sort. Number of Islands (C++).
- **Reflection output:** `notes/day-51.md` — "Describe your debugging process for a production issue where you have no reproduction steps. What do you do first?"
- **Estimated time:** 3h

---

### Day 52
- **Objective:** Add production readiness features to the Node.js backend.
- **Build task (2.5h):** Add the following to `02-backend-engineering/node/src/index.js`: (1) Graceful shutdown: on `SIGTERM`, stop accepting connections, wait for in-flight requests to finish (with a 30-second timeout), then exit. (2) Startup validation: before binding to port, verify database connection is available; if not, exit with code 1. (3) Health endpoint upgrade: `GET /health` returns status, DB connection status, Redis connection status, uptime, memory usage. (4) Write an integration test for graceful shutdown behavior. Commit.
- **LeetCode C++ (45min):** Word Search (C++) — backtracking. Subsets (C++).
- **Reflection output:** `notes/day-52.md` — "Why does graceful shutdown matter in Kubernetes? What happens if a pod receives SIGTERM and immediately exits?"
- **Estimated time:** 3.5h

---

### Day 53
- **Objective:** Add Prometheus metrics to the Node.js backend.
- **Study (30min):** `prom-client` npm package documentation. Read about the 4 metric types: Counter, Gauge, Histogram, Summary. Understand what each is for.
- **Build task (2h):** Add `prom-client` to the Node.js backend: (1) `http_requests_total` — counter, labeled by method, route, status code. (2) `http_request_duration_seconds` — histogram, labeled by method, route. (3) `active_connections` — gauge. (4) Expose these on `GET /metrics` in Prometheus text format. (5) Add middleware that records every request into these metrics. (6) Write a note explaining what you would alert on from these metrics. Commit.
- **LeetCode C++ (45min):** Combination Sum (C++) + Permutations (C++).
- **Reflection output:** `notes/day-53.md` — "What is the difference between a Counter and a Gauge? What is a histogram bucket? What SLO would you set based on `http_request_duration_seconds`?"
- **Estimated time:** 3h

---

### Day 54
- **Objective:** Write a complete API design document.
- **Build task (2.5h):** Write `90-days-fullstack-engineer/06-writing-thinking/design-docs/listing-api-design.md` — a formal API design document for the listing service: (1) Purpose and consumers. (2) Base URL and versioning strategy. (3) Endpoints (full list with method, path, request/response schema). (4) Authentication model (who can access what). (5) Pagination strategy (keyset, explain why). (6) Error response schema (ProblemDetails or custom — justify). (7) Rate limits. (8) Breaking vs non-breaking changes policy. (9) What is not yet implemented and why. Treat this as something you would share with a frontend team.
- **LeetCode C++ (45min):** Letter Combinations of a Phone Number (C++) + Palindrome Partitioning (C++).
- **Reflection output:** `notes/day-54.md` — "What makes an API design document useful? What is the difference between a design doc for internal teams vs an external API?"
- **Estimated time:** 3.5h

---

### Day 55
- **Objective:** Write integration tests for the listing API.
- **Study (30min):** `supertest` documentation. Review existing test setup if any in the Node.js backend.
- **Build task (2h):** Write 5 integration tests for the listing service (`03-fullstack-system/backend`) using supertest + Jest: (1) `GET /listings` returns paginated list. (2) `GET /listings?search=term` returns filtered results. (3) `GET /listings/:id` returns listing with document field. (4) `GET /listings/:id` returns 404 for non-existent ID. (5) `GET /listings/:id` returns cached result on second call (verify Redis was hit). For the Redis test, use a real Redis instance or a mock — document your choice. Commit.
- **LeetCode C++ (45min):** Restore IP Addresses (C++) + N-Queens (C++).
- **Reflection output:** `notes/day-55.md` — "What is the difference between a unit test and an integration test? When does hitting a real Redis in a test make sense vs mocking it?"
- **Estimated time:** 3.5h

---

### Day 56 — Week 8 + Phase 2 checkpoint
- **Objective:** Produce a scaling architecture writeup.
- **Build task (2.5h):** Write `notes/day-56-scaling-the-listing-service.md` — a 600-word engineering document: "How I would scale the listing service from 100 users to 1 million users." Cover: (1) Current architecture and its limits. (2) First bottleneck you would hit and how to fix it (likely DB reads). (3) Second bottleneck (likely app server). (4) When you would introduce a CDN and why. (5) When you would introduce a read replica and why. (6) When you would shard the database. (7) What you would NOT do yet (premature optimization examples). Be specific. No vague "scale horizontally."
- **LeetCode C++ (45min):** Rat in a Maze (C++) + Word Search II with Trie (C++).
- **Reflection output:** `notes/day-56.md` + `notes/week-08-review.md`
- **Estimated time:** 3.5h

---

## Days 57–60: Phase 2 Completion

### Day 57
- **Objective:** Create a full architecture decision log.
- **Build task (2.5h):** Review all existing ADRs in `06-writing-thinking/decisions/`. Write 2 new ADRs that are missing: (1) `error-handling-strategy.md` — how errors are classified, propagated, and returned to clients in the Node.js backend. (2) `testing-strategy.md` — what types of tests exist, what each covers, what is not tested and why. Then write `notes/day-57-architecture-walkthrough.md` — a 400-word plain text walkthrough: "If a new engineer joins the team and asks 'how does this system work?', what do you say in 5 minutes?" This is a senior communication exercise.
- **LeetCode C++ (45min):** Implement Trie (C++) + Word Dictionary with Wildcard (C++).
- **Reflection output:** `notes/day-57.md`
- **Estimated time:** 3.5h

---

### Day 58
- **Objective:** Write mock interview answers — behavioral.
- **Build task (2h):** Write `notes/day-58-behavioral-interview-prep.md` — 5 STAR-format answers to behavioral questions: (1) "Tell me about a time you improved performance in a production system." (2) "Tell me about a time you had to make a technical decision with incomplete information." (3) "Tell me about a time you disagreed with your team's technical direction." (4) "Describe a complex system you designed from scratch." (5) "Tell me about the biggest technical mistake you made and what you learned." For each: Situation (2 sentences), Task (1 sentence), Action (4–6 sentences of what YOU specifically did), Result (measurable outcome). Use real examples from this repo's work.
- **LeetCode C++ (45min):** Course Schedule II (C++) + Alien Dictionary (C++) — advanced topological.
- **Reflection output:** `notes/day-58.md`
- **Estimated time:** 3h

---

### Day 59
- **Objective:** Write mock interview answers — technical.
- **Build task (2h):** Write `notes/day-59-technical-interview-prep.md` — written answers to 5 technical questions: (1) "What happens when you send an HTTP request from a browser to an API?" (Go as deep as you can: DNS, TCP, TLS, HTTP, backend routing.) (2) "How does a database index work internally?" (3) "What is the Node.js event loop and how does it handle async operations?" (4) "Explain CQRS. When would you use it and when would you not?" (5) "How would you design the auth system for a multi-tenant SaaS API?" Write each answer as if speaking to a senior interviewer. Use specifics, not vague terms.
- **LeetCode C++ (45min):** Pick any 2 problems you found hardest this phase and re-solve from memory.
- **Reflection output:** `notes/day-59.md`
- **Estimated time:** 3h

---

### Day 60 — Phase 2 Review
- **Objective:** Close Phase 2 with a complete evidence checkpoint.
- **Build task (2h):** (1) Update `tracking/progress-tracker.md` — mark Phase 2 done, list what you actually produced. (2) Count all system design write-ups (must be 6). Count C++ LeetCode solutions (must be 15+). (3) Verify the CleanShop .NET project builds and tests pass: `dotnet test`. (4) Write `notes/phase-02-review.md` (600 words): what is your .NET understanding now? What system design weaknesses do you see in yourself? What does your code review instinct look like now vs Day 30? (5) Identify the 3 things you need to go into Phase 3 with most urgently.
- **Reflection output:** `notes/day-60.md` + `notes/phase-02-review.md`
- **Estimated time:** 3h

---

## Phase 2 non-negotiable outcomes

Before you start Phase 3, check these off:

- [ ] `CleanShop` .NET project with clean architecture, tests, and auth — committed and building
- [ ] `notes/day-42-dotnet-code-review.md` — self-review of your .NET code
- [ ] `notes/day-41.md` — Node.js vs .NET ADR written
- [ ] 6 timed system design write-ups committed (Days 29, 43, 44, 45, 46, 47)
- [ ] `01-core-engineering/system-design/SYSTEM-DESIGN-FRAMEWORK.md` — your personal framework
- [ ] `notes/day-50-code-review-template.md` + full code review written
- [ ] `notes/day-56-scaling-the-listing-service.md` — scaling writeup
- [ ] 15+ C++ LeetCode solutions committed with complexity notes
- [ ] `notes/day-58-behavioral-interview-prep.md` — 5 STAR answers
- [ ] `notes/day-59-technical-interview-prep.md` — 5 technical answers
- [ ] All 30 `notes/day-XX.md` files (Day 31–60) are non-empty
- [ ] All weekly reviews written (weeks 5–8)
- [ ] Progress tracker updated

# Phase 1: Engineering Foundation Upgrade — Days 1–30

**Goal:** Close the gap between building things and deeply understanding them.
By Day 30 you must have 30 LeetCode solutions committed, a real schema design doc, a Node.js code review writeup, and all 30 daily notes filled in.

---

## Week 1 — Node.js Internals (Days 1–7)

### Day 1
- **Objective:** Understand Node.js from the inside out — not just "it's non-blocking."
- **Study (1h):** Hussein Nasser — "Node.js event loop explained" (YouTube). Take notes on: call stack, libuv thread pool, event queue, microtask queue, macrotask queue. Write the execution order for a script with `setTimeout`, `Promise.resolve`, and `process.nextTick`.
- **Build task (1h):** Write a Node.js script (`notes/day-01-eventloop.js`) that demonstrates the execution order difference between `process.nextTick`, `Promise.resolve().then`, `setImmediate`, and `setTimeout(fn, 0)`. Add comments explaining why each fires when it does.
- **LeetCode (45min):** Two Sum (Python) + Best Time to Buy and Sell Stock (Python). For each: write the approach comment, write the code, write the time/space complexity.
- **Reflection output:** `notes/day-01.md` — "What I now know about the event loop that I didn't before. What surprised me. What I need to re-read."
- **Estimated time:** 3h
- **Why this day matters:** You have used `async/await` for years without understanding why the event loop makes it safe to write that way. This foundation affects every production Node.js decision.
- **Artifact to commit:** `notes/day-01-eventloop.js`, two LeetCode solutions in `90-days-fullstack-engineer/01-core-engineering/leetcode/solutions/day01/`, `notes/day-01.md`

---

### Day 2
- **Objective:** Master async patterns and understand why unhandled rejections crash servers.
- **Study (1h):** NodeJS Complete Guide (Udemy) — sections on Promises, async/await, error handling with async. Read Node.js docs on `unhandledRejection` and `uncaughtException`. Write notes on the difference.
- **Build task (1h):** Write a script (`notes/day-02-async.js`) demonstrating: callback hell → promise chain → async/await refactor → proper error handling → catching unhandledRejection. Add comments at each step explaining what changed and why.
- **LeetCode (45min):** Product of Array Except Self (Python) + Maximum Subarray — Kadane's Algorithm (Python).
- **Reflection output:** `notes/day-02.md` — "When should I use `.catch()` vs `try/catch` vs `process.on('unhandledRejection')`? What is my rule?"
- **Estimated time:** 3h
- **Why this day matters:** Most Node.js production bugs come from improper async error handling. This day builds the instinct.
- **Artifact to commit:** Script + 2 LeetCode solutions + notes.

---

### Day 3
- **Objective:** Understand Node.js Streams — one of the most underused and most important features.
- **Study (1h):** Node.js docs on Streams (Readable, Writable, Transform, Duplex). Hussein Nasser — any streams video. Focus on: backpressure, pipe, why streaming is better than buffering for large files.
- **Build task (1.5h):** Build a file transformation pipeline: read a large text file → transform (uppercase) → write to new file, using streams (no `fs.readFileSync`). Then build a second example: HTTP response streaming. Compare memory usage between stream and non-stream approaches.
- **LeetCode (45min):** Merge Intervals (Python) + Contains Duplicate (Python).
- **Reflection output:** `notes/day-03.md` — "When would I use streams in a real API? Name 3 production scenarios."
- **Estimated time:** 3.5h
- **Why this day matters:** File uploads, CSV processing, S3 piping, database exports — all require streams. Not knowing them is a gap.
- **Artifact to commit:** Stream pipeline script + 2 LeetCode solutions + notes.

---

### Day 4
- **Objective:** Understand Cluster vs Worker Threads and when to use each.
- **Study (45min):** Node.js docs on Cluster module and Worker Threads. Read the article "Node.js single-threaded myth" (search for it). Write notes: I/O-bound vs CPU-bound, what Cluster solves, what Worker Threads solve.
- **Build task (1.5h):** Build two demos: (1) A cluster demo showing multiple workers handling HTTP requests with `cluster.fork()`. (2) A worker thread demo that offloads a CPU-intensive calculation (e.g., computing Fibonacci to a large number) without blocking the event loop. Commit both with comments.
- **LeetCode (45min):** 3Sum (Python) + Move Zeroes (Python).
- **Reflection output:** `notes/day-04.md` — "I have an API that runs image compression on upload. Should I use Cluster or Worker Threads? Justify your answer."
- **Estimated time:** 3h
- **Why this day matters:** Cluster is for scaling across CPU cores. Worker Threads is for isolating CPU work. Confusing them is a common mid-level gap.
- **Artifact to commit:** Two demo scripts + LeetCode solutions + notes.

---

### Day 5
- **Objective:** Learn to debug Node.js professionally — not just `console.log`.
- **Study (1h):** Node.js docs on `--inspect` flag. VS Code debugger for Node.js. Read "Finding a memory leak in Node.js" (search for Clinicjs or Node clinic blog post). Notes on: what a heap snapshot is, what retains memory, what causes leaks.
- **Build task (1.5h):** (1) Set up VS Code debugger for the existing Node.js backend (`02-backend-engineering/node`). Set a breakpoint in `authController.js` and step through it. (2) Write a script that intentionally has a memory leak (global array that grows on interval). Use `--inspect` and Chrome DevTools to take a heap snapshot and identify the leak. Write the steps you followed.
- **LeetCode (45min):** Valid Palindrome II (Python) + Container With Most Water (Python).
- **Reflection output:** `notes/day-05.md` — "3 signs that a Node.js process has a memory leak. What tools do I use to find it. What are the most common causes."
- **Estimated time:** 3.5h
- **Why this day matters:** Senior engineers can debug under pressure. Junior engineers add more `console.log`. This day starts that gap closing.
- **Artifact to commit:** Memory leak script + debugging notes + LeetCode solutions.

---

### Day 6
- **Objective:** Build a production-grade error handling architecture.
- **Study (30min):** Review the existing `02-backend-engineering/node/src/utils/errors.js` and `errorHandler.js`. Read Express error handling docs. Read "Operational vs Programmer errors" (Joyent Node.js error handling guide).
- **Build task (2h):** Rewrite the error handling in `02-backend-engineering/node/src/utils/errors.js` to have: a proper error hierarchy (`AppError` → `ValidationError`, `AuthError`, `NotFoundError`, `DatabaseError`), error codes, HTTP status mapping, and `isOperational` flag. Update `errorHandler.js` to use these. Write 3 unit tests for the error classes.
- **LeetCode (45min):** Sort Colors (Python) — Dutch National Flag algorithm. Squares of a Sorted Array (Python).
- **Reflection output:** `notes/day-06.md` — "What is the difference between an operational error and a programmer error in Node.js? How should each be handled differently in production?"
- **Estimated time:** 3.5h
- **Why this day matters:** Error handling is how a junior shows senior taste. The existing errors.js is shallow. Making it production-grade is the difference.
- **Artifact to commit:** Improved error utilities + tests + LeetCode + notes.

---

### Day 7 — Week 1 Review
- **Objective:** Consolidate Week 1 before moving to databases.
- **Study (none new):** Re-read your notes from Day 1–6.
- **Build task (2h):** Write a 400–600 word document called `notes/week-01-review.md` that covers: (1) The 3 most important things you learned about Node.js internals this week. (2) A diagram (text-based is fine) showing the event loop execution order. (3) One thing from the existing Node.js backend that you would change now and why. (4) Review all 12 LeetCode solutions from this week and write the pattern name and key insight for each.
- **LeetCode (1h):** Retry the hardest problem from this week without looking at your previous solution. Write the new solution from memory.
- **Reflection output:** `notes/day-07.md` + `notes/week-01-review.md`
- **Estimated time:** 3h
- **Why this day matters:** Learning without consolidation evaporates. This day locks in Week 1.
- **Artifact to commit:** Week review doc + retried LeetCode + notes.

---

## Week 2 — SQL Depth + LeetCode Sliding Window/Hash Maps (Days 8–14)

### Day 8
- **Objective:** Design a real database schema from scratch — not fill in a template.
- **Study (1h):** Coursera "Intro to Databases" — Week 1 on ER modeling (selective: skip what you already know, focus on cardinality, normalization). Write notes on: 1NF, 2NF, 3NF — with a real example of what violates each.
- **Build task (1.5h):** Design an e-commerce schema from scratch: users, products, orders, order_items, reviews, categories, addresses. Write the complete DDL (`notes/day-08-ecommerce-schema.sql`). Include: primary keys, foreign keys, proper types, NOT NULL constraints, indexes on FK columns. No copy-paste from tutorials.
- **LeetCode (45min):** Longest Substring Without Repeating Characters (Python) + Minimum Size Subarray Sum (Python).
- **Reflection output:** `notes/day-08.md` — "What normalization decisions did I make and why? Where did I consciously choose to denormalize and why?"
- **Estimated time:** 3.5h
- **Why this day matters:** Schema design is a senior signal. A bad schema cannot be fixed with application code.
- **Artifact to commit:** Schema SQL file + LeetCode + notes.

---

### Day 9
- **Objective:** Master SQL JOINs deeply enough to explain every type without thinking.
- **Study (30min):** Review your schema from Day 8. Write 10 JOIN query exercises against it (e.g., "get all orders with user name and item count", "get top 5 products by review count").
- **Build task (1.5h):** Write all 10 query solutions in `notes/day-09-sql-joins.sql`. For each: add a comment explaining which JOIN type you used and why. Include at least one self-join and one multi-table join (3+ tables).
- **LeetCode (45min):** Longest Repeating Character Replacement (Python) + Permutation in String (Python).
- **Reflection output:** `notes/day-09.md` — "What is the difference between a LEFT JOIN and a LEFT OUTER JOIN? When does a JOIN return more rows than either source table? Give a real example."
- **Estimated time:** 3h
- **Why this day matters:** JOINs are the backbone of relational data. Most N+1 bugs come from not knowing when to JOIN vs when to query separately.
- **Artifact to commit:** SQL exercises file + LeetCode + notes.

---

### Day 10
- **Objective:** Understand indexing well enough to explain query plans and index choices.
- **Study (1h):** PostgreSQL docs on indexes (B-tree, Hash, GIN). Read "Use the Index, Luke" (use-the-index-luke.com) — Chapter 1 and Chapter on composite indexes. Run `EXPLAIN ANALYZE` on 3 queries from Day 9.
- **Build task (1.5h):** Add indexes to your Day 8 schema: (1) Add a composite index for a common filter+sort pattern. (2) Run `EXPLAIN ANALYZE` before and after. (3) Write `notes/day-10-indexing.sql` showing the before/after query plans (paste the output as SQL comments). (4) Demonstrate a case where an index hurts performance (write counts) and explain why.
- **LeetCode (45min):** Subarrays with K Different Integers (Python) + Sliding Window Maximum (Python).
- **Reflection output:** `notes/day-10.md` — "When should I not add an index? What are the 3 most important things to check when a query is slow?"
- **Estimated time:** 3.5h
- **Why this day matters:** Everyone adds indexes. Few understand when they help, when they hurt, and how to read a query plan.
- **Artifact to commit:** Indexing SQL file + notes + LeetCode.

---

### Day 11
- **Objective:** Understand transaction isolation levels — a topic most engineers get wrong.
- **Study (1h):** PostgreSQL docs on transaction isolation. Write notes on: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE. For each: what anomaly it allows (dirty read, non-repeatable read, phantom read). Draw a timeline diagram for each anomaly.
- **Build task (1.5h):** Write `notes/day-11-transactions.sql` with: (1) A BEGIN/COMMIT block for a bank transfer (debit one account, credit another, check balance). (2) A transaction that demonstrates the difference between READ COMMITTED and REPEATABLE READ using two sessions (explain in comments). (3) A SAVEPOINT example.
- **LeetCode (45min):** Fruit Into Baskets (Python) + Minimum Window Substring (Python) — hard, look at pattern hints if stuck.
- **Reflection output:** `notes/day-11.md` — "You are building a payment system. Which isolation level would you choose? What are the tradeoffs? What would you do about phantom reads?"
- **Estimated time:** 3.5h
- **Why this day matters:** Transaction isolation is a classic senior interview topic. Most engineers have never been asked to explain phantom reads with an example.
- **Artifact to commit:** Transactions SQL + LeetCode + notes.

---

### Day 12
- **Objective:** Learn window functions — the most underused SQL feature.
- **Study (45min):** PostgreSQL docs on window functions. Focus on: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM OVER`, `PARTITION BY`, `ORDER BY` in window context.
- **Build task (1.5h):** Write `notes/day-12-window-functions.sql` with 7 real queries against your e-commerce schema: (1) Rank products by sales per category. (2) Find the running total of order amounts per user. (3) Show each order and the previous order date for the same user (`LAG`). (4) Find users whose order count is in the top 10%. (5) Calculate 7-day rolling average of daily revenue. (6) Dense rank categories by total revenue. (7) Find the first order date per user.
- **LeetCode (45min):** Two Sum II - Input Array is Sorted (Python) + 4Sum (Python).
- **Reflection output:** `notes/day-12.md` — "When would you use a window function instead of a subquery or GROUP BY? Give a concrete example from this week's queries."
- **Estimated time:** 3h
- **Why this day matters:** Window functions appear in every SQL interview. More importantly, they prevent ugly self-joins and subqueries in production analytics.
- **Artifact to commit:** Window functions SQL + LeetCode + notes.

---

### Day 13
- **Objective:** Learn the N+1 problem and keyset pagination — two production gotchas.
- **Study (45min):** "Use the Index, Luke" — keyset pagination chapter. Read about N+1 queries in Node.js/ORM context. Look at the existing `postgresRepository.js` in `03-fullstack-system/backend/src/repositories/` and identify if it has any N+1 patterns.
- **Build task (1.5h):** (1) Demonstrate an N+1 query in Node.js (write a script that fetches 20 orders then fetches each user separately in a loop). Write the fix using a JOIN. Measure the query count difference. (2) Rewrite the `searchListings` function in `postgresRepository.js` to use keyset pagination instead of OFFSET. Explain why in a code comment.
- **LeetCode (45min):** Group Anagrams (Python) + Top K Frequent Elements (Python) — hash map patterns.
- **Reflection output:** `notes/day-13.md` — "You have a table with 10 million rows and you need to paginate through all of them for a data export. Why does OFFSET fail? What do you use instead?"
- **Estimated time:** 3h
- **Why this day matters:** N+1 and OFFSET pagination are production performance killers that every senior engineer must be able to identify on sight.
- **Artifact to commit:** N+1 demo + fixed pagination code + LeetCode + notes.

---

### Day 14 — Week 2 Review + SQL Mini Project
- **Objective:** Consolidate SQL knowledge with a complete schema exercise.
- **Build task (2.5h):** Design and build a booking system schema in `notes/day-14-booking-schema.sql`: users, venues, time_slots, bookings, payments, reviews. Requirements: (1) A user cannot book a slot that is already booked (how do you enforce this? UNIQUE constraint? Application lock? Optimistic locking?). (2) Write 5 production-relevant queries (search available slots, user booking history with venue name, revenue by venue, review summary). (3) Add appropriate indexes. (4) Write a 200-word design note on your choices.
- **LeetCode (45min):** Word Pattern (Python) + LRU Cache (Python) — classic hash map.
- **Reflection output:** `notes/day-14.md` + `notes/week-02-review.md` (400+ words on what SQL depth you've built this week)
- **Estimated time:** 3.5h
- **Why this day matters:** Schema design under constraints is a classic senior interview question. The double-booking problem alone has ended many interviews.
- **Artifact to commit:** Booking schema + week review + LeetCode + notes.

---

## Week 3 — Backend Architecture Depth + LeetCode Trees (Days 15–21)

### Day 15
- **Objective:** Become opinionated about REST API design.
- **Study (1h):** Microsoft REST API design best practices (search "Microsoft Azure REST API guidelines"). Richardson Maturity Model. HTTP idempotency rules (which methods MUST be idempotent and why). Read the existing `02-backend-engineering/node/src/routes/authRoutes.js` and `listingController.js`.
- **Build task (1.5h):** Write `notes/day-15-api-review.md` — a code review of the existing Node.js backend REST API. Cover: (1) Are routes named correctly? (2) Are correct HTTP methods used? (3) Are status codes correct? (4) What is missing (versioning, pagination, consistent error format)? (5) What would you add? Write at least 8 specific review comments as if you are a senior reviewer.
- **LeetCode (45min):** Validate Binary Search Tree (Python) + Binary Tree Level Order Traversal — BFS (Python).
- **Reflection output:** `notes/day-15.md` — "What is the difference between a 400 and a 422? When would you use each? What is idempotency and which HTTP methods must be idempotent?"
- **Estimated time:** 3h
- **Why this day matters:** Writing code reviews is a senior signal. Day 15 produces a real written review of real code. This is evidence.

---

### Day 16
- **Objective:** Add production-quality request validation with proper error messages.
- **Study (30min):** Read Zod documentation (quick start). Look at the existing `validateRequest.js` middleware in the Node.js backend.
- **Build task (2h):** Replace the existing validation in the Node.js backend (`02-backend-engineering/node`) with Zod schemas: (1) Add a Zod schema for the login request body. (2) Add a Zod schema for registration (email format, password minimum length, required fields). (3) Make `validateRequest.js` generic — it takes any Zod schema and validates `req.body`, returning structured errors (field, message, code). (4) Write 3 unit tests for the validation middleware.
- **LeetCode (45min):** Lowest Common Ancestor of BST (Python) + Balanced Binary Tree (Python).
- **Reflection output:** `notes/day-16.md` — "What is the difference between validating at the route level vs validating in the service layer? What should be validated where?"
- **Estimated time:** 3.5h
- **Why this day matters:** Validation is the first line of defense. Inconsistent validation is a security risk. Structured validation errors are a UX responsibility.

---

### Day 17
- **Objective:** Understand JWT deeply — not just "add a token."
- **Study (1h):** JWT.io introduction. Read the JWT spec parts on header, payload, signature. OWASP Authentication Cheat Sheet — read the JWT section specifically. Look at `authService.js` in the existing Node.js backend.
- **Build task (1.5h):** Audit and improve the existing auth implementation: (1) Is the JWT secret validated to be strong enough? (2) Is `expiresIn` set on access tokens? What is it set to? Is it appropriate? (3) Is the refresh token stored securely (not in the JWT payload)? (4) Write a document `notes/day-17-auth-audit.md` listing every issue found + proposed fix for each. (5) Fix at least 2 of the issues in code.
- **LeetCode (45min):** Serialize and Deserialize Binary Tree (Python) + Path Sum II (Python).
- **Reflection output:** `notes/day-17.md` — "What is the difference between authentication and authorization? What are 3 ways a JWT can be compromised? How do you mitigate each?"
- **Estimated time:** 3.5h
- **Why this day matters:** Auth is always a senior question. The ability to audit an existing auth system critically is a signal.

---

### Day 18
- **Objective:** Understand middleware composition and rate limiting.
- **Study (30min):** Express middleware docs. Read about the sliding window vs token bucket rate limiting algorithms.
- **Build task (2h):** (1) Build a rate limiter middleware from scratch (no `express-rate-limit` library) using Redis as the counter store. Use the sliding window algorithm. Add it to the Node.js backend on the `/auth/login` route with a limit of 10 requests/15 minutes per IP. (2) Write the middleware as a higher-order function that accepts `limit` and `windowMs` as config. (3) Write a test that verifies the rate limiter rejects the 11th request.
- **LeetCode (45min):** Maximum Depth of Binary Tree (Python) + Binary Tree Right Side View (Python).
- **Reflection output:** `notes/day-18.md` — "What is the difference between token bucket and sliding window rate limiting? Which would you use for an API that has occasional large bursts from legitimate users?"
- **Estimated time:** 3.5h
- **Why this day matters:** Rate limiting is both a security and reliability concern. Building it from scratch shows you understand it; using a library without understanding it is a risk.

---

### Day 19
- **Objective:** Understand and evaluate the repository pattern in production.
- **Study (45min):** Read `repository-pattern.md` in `02-backend-engineering/patterns/`. Look at `userRepository.js` and `postgresRepository.js`. What is testable about this design? What is not? What would make it better?
- **Build task (1.5h):** (1) Write 3 unit tests for `authService.js` in the Node.js backend — mock the `userRepository`. Focus on: test login with wrong password returns AuthError, test login with non-existent user, test successful login returns tokens. (2) Write a note explaining where the service tests reveal seams in the architecture (where is coupling too tight?).
- **LeetCode (45min):** Construct Binary Tree from Preorder and Inorder Traversal (Python) + Kth Smallest Element in a BST (Python).
- **Reflection output:** `notes/day-19.md` — "What is the purpose of the repository pattern? What does it let you test in isolation? What does it NOT solve?"
- **Estimated time:** 3h
- **Why this day matters:** Testing discipline is a senior signal. Writing tests that expose architectural seams is an advanced skill.

---

### Day 20
- **Objective:** Add production-grade structured logging with correlation IDs.
- **Study (30min):** Pino documentation (quick start). Read about structured logging vs string logging. Read why correlation IDs matter in distributed systems.
- **Build task (2h):** Upgrade the logging in `02-backend-engineering/node/src/utils/logger.js`: (1) Use Pino with JSON output. (2) Add a request middleware that generates a `requestId` (UUID) for every request, stores it on `req` and `res` headers (`X-Request-ID`). (3) Pass `requestId` and `userId` (from auth context if available) to every log line. (4) Log at appropriate levels: `info` for requests, `warn` for auth failures, `error` for exceptions. (5) Demonstrate that log output is structured JSON.
- **LeetCode (45min):** Invert Binary Tree (Python) + Diameter of Binary Tree (Python).
- **Reflection output:** `notes/day-20.md` — "Why is `console.log('something happened')` not acceptable in production? What makes a log line useful to an on-call engineer at 3am?"
- **Estimated time:** 3.5h
- **Why this day matters:** Observability starts with good logs. Correlation IDs are how you trace a single request through distributed systems.

---

### Day 21 — Week 3 Review + Architecture Document
- **Objective:** Produce a real architecture artifact.
- **Build task (2.5h):** Write `90-days-fullstack-engineer/06-writing-thinking/design-docs/node-backend-architecture.md` — a proper architecture document for the existing Node.js backend: (1) Purpose and context. (2) Architecture diagram (text-based: show layers and their relationships). (3) Key architectural decisions made. (4) What is good about the current design. (5) What are the known weaknesses. (6) What you would change in v2 and why. This should be 600–800 words. Treat it as something you would actually share with a team.
- **LeetCode (45min):** Symmetric Tree (Python) + Count Good Nodes in BST (Python).
- **Reflection output:** `notes/day-21.md` + `notes/week-03-review.md`
- **Estimated time:** 3.5h
- **Why this day matters:** Writing architecture documents is a senior engineering skill. A doc that only you could write about a system you know deeply is evidence.

---

## Week 4 — Databases in Depth + LeetCode Graphs (Days 22–28)

### Day 22
- **Objective:** Understand MongoDB document modeling — not just "it's NoSQL."
- **Study (1h):** MongoDB docs on data modeling — embedding vs referencing decision tree. When does embedding cause document growth problems? When does referencing cause N+1? Read the existing `mongoRepository.js` and `03-fullstack-system` MongoDB usage.
- **Build task (1.5h):** Write `notes/day-22-mongodb-patterns.js` — 3 aggregation pipeline exercises against a hypothetical collection: (1) Count documents per category with a filter. (2) $lookup join between two collections (e.g., listings + users). (3) $group + $sort + $limit to get the top 5 most-reviewed items. For each: write the pipeline, explain what each stage does, write the time complexity.
- **LeetCode (45min):** Number of Islands (Python) — BFS approach + DFS approach, write both. Clone Graph (Python).
- **Reflection output:** `notes/day-22.md` — "When would you store a user's order history as embedded documents vs as a separate collection? What happens to embedded documents when the array grows to 10,000 items?"
- **Estimated time:** 3h

---

### Day 23
- **Objective:** Build a Redis rate limiter and understand all cache patterns.
- **Study (45min):** Redis docs on INCR/EXPIRE (atomic operations). Read about cache-aside vs write-through vs write-behind patterns. Understand when each is appropriate.
- **Build task (2h):** Write `notes/day-23-redis-patterns.js` with implementations of: (1) Cache-aside pattern (check cache, miss → fetch from DB, store in cache). (2) Rate limiter using Redis `INCR` + `EXPIRE` (sliding window). (3) Pub/sub demo (publisher pushes to a channel, subscriber logs it). (4) Distributed lock using `SET NX EX`. For each: add a comment explaining the pattern name and the failure mode to watch for.
- **LeetCode (45min):** Course Schedule (Python) — topological sort BFS. Pacific Atlantic Water Flow (Python).
- **Reflection output:** `notes/day-23.md` — "What is cache stampede? How do you prevent it? What is the difference between a cache and a message queue?"
- **Estimated time:** 3h

---

### Day 24
- **Objective:** Learn zero-downtime database migration strategy.
- **Study (45min):** Read about the Expand/Contract migration pattern. Read about blue-green deployments and how they interact with database migrations. Look at what happens if you rename a column in a running system.
- **Build task (1.5h):** Write `notes/day-24-migration-strategy.md` — a concrete migration plan for adding a `full_name` column to the `users` table in the existing schema, with zero downtime: Phase 1: add nullable column. Phase 2: backfill. Phase 3: make NOT NULL. Phase 4: remove old column. For each phase: write the SQL, explain what code change is needed, explain why this sequence prevents downtime.
- **LeetCode (45min):** Rotting Oranges (Python) + Word Ladder (Python).
- **Reflection output:** `notes/day-24.md` — "Your team needs to rename `user_name` to `display_name` in a live database with 5M rows. Walk me through the migration plan."
- **Estimated time:** 3h
- **Why this day matters:** This is a classic senior-level question. Most engineers who have not shipped a large migration do not know the answer.

---

### Day 25
- **Objective:** Understand message queues and background job patterns deeply.
- **Study (45min):** BullMQ docs — queue concepts, job types, retry strategies, dead letter queue. Review the existing `ingestJob.js` and `queue.js` in `03-fullstack-system/backend/src/jobs/`.
- **Build task (1.5h):** Improve the existing BullMQ implementation: (1) Add `attempts: 3` and `backoff: { type: 'exponential', delay: 1000 }` retry config to the queue. (2) Add a `failed` event handler that logs failed jobs with context. (3) Add a `completed` event handler. (4) Write a function that checks if the queue is healthy (connected, not backlogged) and can be called from a `/health` endpoint. (5) Add a comment explaining what a dead letter queue is and why it matters.
- **LeetCode (45min):** Network Delay Time — Dijkstra (Python) + Cheapest Flights Within K Stops (Python).
- **Reflection output:** `notes/day-25.md` — "What happens to a BullMQ job when Redis goes down? How do you ensure exactly-once processing? What is the difference between at-least-once and exactly-once delivery?"
- **Estimated time:** 3h

---

### Day 26
- **Objective:** Learn to profile and optimize a Node.js service.
- **Study (45min):** Read about V8 profiling, `--prof` flag, clinicjs tool. Read about Node.js memory management and common leak patterns (closures, event listener accumulation, global caches).
- **Build task (1.5h):** (1) Add `GET /health` and `GET /metrics` endpoints to the Node.js backend in `02-backend-engineering/node`. Health check should return `{ status: 'ok', uptime: X, memory: {...}, pid: X }`. Metrics should return `{ requestCount: X, errorCount: X, avgResponseTime: Xms }` (use in-memory counters for now). (2) Write an integration test for the health endpoint. (3) Run the Node.js backend and hit it with 100 requests using `curl` in a loop. Check memory stays flat.
- **LeetCode (45min):** Accounts Merge (Python) + Graph Valid Tree (Python).
- **Reflection output:** `notes/day-26.md` — "What metrics would you expose on a `/metrics` endpoint for a production API? Why does memory monitoring matter even in a managed environment?"
- **Estimated time:** 3h

---

### Day 27
- **Objective:** Security audit of the existing codebase.
- **Study (1h):** OWASP Top 10 for APIs (2023). OWASP Authentication Cheat Sheet. Read the existing Node.js backend for any visible security issues.
- **Build task (1.5h):** Write `notes/day-27-security-audit.md` — a security review of the existing Node.js backend: (1) Check for SQL injection (are queries parameterized?). (2) Check for improper error disclosure (does the error handler leak stack traces to clients?). (3) Check for missing rate limiting on sensitive endpoints. (4) Check for JWT secret hardcoding or weak secrets. (5) Check for missing input sanitization. (6) Check for CORS misconfiguration. For each finding: severity (critical/high/medium/low), what the risk is, what the fix is. Then fix the top 2 issues in code.
- **LeetCode (45min):** Number of Connected Components in Undirected Graph (Python) + Redundant Connection (Python).
- **Reflection output:** `notes/day-27.md` — "You are reviewing a PR. What are the 5 security questions you check first?"
- **Estimated time:** 3.5h
- **Why this day matters:** Security review is a senior responsibility. Writing one is a portfolio artifact.

---

### Day 28
- **Objective:** Produce a senior reflection document.
- **Study (none new):** Review your notes from Day 22–27.
- **Build task (2h):** Write `notes/day-28-backend-reflection.md` — a 600-word engineering reflection titled "What I would do differently if I started the Node.js backend today." Cover: (1) Architecture changes. (2) Testing strategy changes. (3) Security changes. (4) Observability changes. (5) What took the most time to understand and why. This is not a list of fixes. It is a narrative that shows engineering judgment.
- **LeetCode (45min):** Max Area of Island (Python) + Surrounded Regions (Python).
- **Reflection output:** `notes/day-28.md`
- **Estimated time:** 3h
- **Why this day matters:** The ability to reflect critically on your own work is a senior-level signal. Interviewers ask this question. The answer is in this document.

---

## Days 29–30: Phase 1 Completion

### Day 29
- **Objective:** System design under time pressure — first timed drill.
- **Build task (2.5h):** Set a 45-minute timer. Design a URL shortener from scratch. Write your answer in `notes/day-29-url-shortener-design.md` using this structure: (1) Requirements (functional + non-functional). (2) Scale estimation (DAU, QPS, storage). (3) API design. (4) Data model. (5) High-level architecture (components and their roles). (6) Core algorithm (how do you generate short codes?). (7) Bottlenecks. (8) Tradeoffs. After 45 minutes, stop. Then compare to `90-days-fullstack-engineer/01-core-engineering/system-design/url-shortener.md`. Write a 200-word self-critique: what did you miss, what did you get right.
- **LeetCode (45min):** Combination Sum (Python) + Subsets (Python) — backtracking patterns.
- **Reflection output:** `notes/day-29.md`
- **Estimated time:** 3.5h

---

### Day 30 — Phase 1 Review
- **Objective:** Close Phase 1 with a complete evidence checkpoint.
- **Build task (2h):** (1) Update `90-days-fullstack-engineer/tracking/progress-tracker.md` — mark Phase 1 done, list what you actually produced. (2) Count how many LeetCode solutions you have in the solutions folder. If fewer than 25, spend an hour solving the gap. (3) Write `notes/week-04-review.md` + `notes/phase-01-review.md` (500 words): what is your Node.js understanding now vs Day 1? What SQL query patterns do you know cold? What still feels uncertain? What do you want to strengthen in Phase 2?
- **Reflection output:** `notes/day-30.md` + `notes/phase-01-review.md`
- **Estimated time:** 3h
- **Why this day matters:** Phase reviews are mandatory. If you skip them, the 90 days become 90 isolated days with no arc.

---

## Phase 1 non-negotiable outcomes

Before you start Phase 2, check these off:

- [ ] 25+ LeetCode solutions in Python committed with complexity notes
- [ ] `notes/day-01-eventloop.js` — event loop demo committed
- [ ] `notes/day-08-ecommerce-schema.sql` — e-commerce schema committed
- [ ] `notes/day-14-booking-schema.sql` — booking system schema committed
- [ ] `notes/day-15-api-review.md` — Node.js API code review written
- [ ] `notes/day-17-auth-audit.md` — auth security audit written
- [ ] `notes/day-21.md` backend architecture document written
- [ ] `notes/day-27-security-audit.md` — security review committed
- [ ] `notes/day-28-backend-reflection.md` — reflection doc committed
- [ ] `notes/day-29-url-shortener-design.md` — timed system design committed
- [ ] All 30 `notes/day-XX.md` files are non-empty
- [ ] All 4 weekly reviews written
- [ ] Progress tracker updated

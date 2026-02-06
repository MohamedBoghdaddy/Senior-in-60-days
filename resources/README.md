# Resources Index — Production-Grade Full-Stack Engineering (60 Days)

![Track](https://img.shields.io/badge/Track-Senior--in--60--days-0B5394) ![Focus](https://img.shields.io/badge/Focus-React%2BNode%2BSecurity%2BPerformance-1D76DB) ![Format](https://img.shields.io/badge/Format-Official--first-0E8A16)

---

## Primary Books (Reference Shelf)

- **Designing Data-Intensive Applications** (Martin Kleppmann) — data modeling, consistency, replication, queues, caching.
- **OWASP Cheat Sheet Series** (official) — practical security patterns and checklists (use as default security reference).  
  https://cheatsheetseries.owasp.org/
- **System Design Interview** (Alex Xu) — tradeoffs and architecture checkpoints.
- **Refactoring** (Martin Fowler) — safe refactors and maintainable code.

> Tip: treat the OWASP Cheat Sheet Series as your "security unit tests" for decisions (auth, session, XSS, CSRF, secrets).

---

## Video & Talks (High-Signal)

- React Conf (official channel)  
  https://www.youtube.com/@ReactConfOfficial
- NodeConf (official)  
  https://www.youtube.com/@nodeconf
- Sentry (official) — observability talks  
  https://www.youtube.com/@Sentry
- Grafana Labs (official) — observability talks  
  https://www.youtube.com/@Grafana

---

## How to Use This File

- Follow resources **day by day in ascending order**
- Read first → build immediately → write notes
- Do **not binge**. Each link is chosen to support that day’s assignment
- If a resource does **not** help you **design, secure, scale, test, or explain** your system — skip it

---

## Day-by-Day Study Links

Each day links to the exact references listed in that day’s `README.md` (official-first).

| Day | Topic (from daily README) | Links |
|---:|---|---|
| 01 | Initialize the project repository with a clean monorepo structure for web, API, and shared packages. | [pnpm Workspaces](https://pnpm.io/workspaces)<br>[GitHub — Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) |
| 02 | Enforce uniform code style and static analysis across the repo (TypeScript strict, lint, formatting). | [ESLint — Getting Started](https://eslint.org/docs/latest/use/getting-started)<br>[Prettier Docs](https://prettier.io/docs/en/index.html)<br>[TypeScript `tsconfig` Reference](https://www.typescriptlang.org/tsconfig) |
| 03 | Establish CI to ensure code quality and buildability (lint, typecheck, tests). | [GitHub Actions Docs](https://docs.github.com/en/actions)<br>[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) |
| 04 | Scaffold the Next.js application with basic routing and layout. | [Next.js App Router — Routing](https://nextjs.org/docs/app/building-your-application/routing)<br>[Tailwind CSS Docs](https://tailwindcss.com/docs) |
| 05 | Build a foundational design system with reusable UI components. | [Storybook for React](https://storybook.js.org/docs/react/get-started/introduction)<br>[Tailwind Component Patterns](https://tailwindcss.com/docs) |
| 06 | Implement data fetching/caching with TanStack Query and define state ownership rules. | [TanStack Query (React) Overview](https://tanstack.com/query/v4/docs/react/overview)<br>[React State — Complete Guide](https://react.dev/learn/state-a-complete-guide)<br>[React Hooks Reference](https://react.dev/reference/react) |
| 07 | Review + refactor + testing pass on Week 1 work; stabilize. | [Vitest](https://vitest.dev/)<br>[React Testing Library](https://testing-library.com/docs/react-testing-library/intro) |
| 08 | Build robust forms with validation and consistent patterns. | [React Hook Form](https://react-hook-form.com/get-started)<br>[Zod](https://zod.dev/)<br>[MDN — Accessible Forms](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML#forms) |
| 09 | Add filtering, sorting, and URL query parameter handling to the tasks list. | [React — Rendering Lists](https://react.dev/learn/rendering-lists)<br>[Next.js — `useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) |
| 10 | Implement pagination to handle long task lists efficiently. | [Use the Index, Luke — Pagination](https://use-the-index-luke.com/no-offset)<br>[Next.js — `useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) |
| 11 | Diagnose and optimize rendering performance for the tasks list. | [React DevTools Profiler](https://react.dev/learn/profile-performance-with-the-devtools-profiler)<br>[React — Optimizing Performance](https://react.dev/learn/optimizing-performance) |
| 12 | Ensure accessibility standards and improve UX for keyboard/screen readers. | [WAI — Accessibility Fundamentals](https://www.w3.org/WAI/fundamentals/accessibility-intro/)<br>[axe Accessibility Testing](https://www.deque.com/axe/) |
| 13 | Deepen App Router understanding and implement caching strategies. | [Next.js App Router](https://nextjs.org/docs/app/building-your-application/routing)<br>[Next.js Caching](https://nextjs.org/docs/app/building-your-application/caching) |
| 14 | Architecture checkpoint: document decisions and align boundaries (ADR). | [MADR (ADR Template)](https://adr.github.io/madr/)<br>[Design Docs (PagerDuty)](https://www.pagerduty.com/blog/engineering-design-docs/) |
| 15 | Set up Express server with clean structure + centralized error handling. | [Express — Routing](https://expressjs.com/en/guide/routing.html)<br>[Node.js — Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick) |
| 16 | Validate API inputs and define consistent error contract. | [Zod](https://zod.dev/)<br>[Express — Error Handling](https://expressjs.com/en/guide/error-handling.html) |
| 17 | Implement JWT auth with access + refresh tokens. | [JWT Introduction](https://jwt.io/introduction)<br>[OWASP — Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) |
| 18 | Implement RBAC to protect org-scoped resources. | [Auth0 — RBAC Concepts](https://auth0.com/docs/get-started/authorization/rbac)<br>[Express — Writing Middleware](https://expressjs.com/en/guide/writing-middleware.html) |
| 19 | Implement CRUD endpoints for core resources (orgs, projects, tasks). | [REST API Design (Microsoft)](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)<br>[Express — Routing](https://expressjs.com/en/guide/routing.html) |
| 20 | Generate OpenAPI spec and write integration tests. | [OpenAPI Initiative](https://www.openapis.org/)<br>[Supertest](https://www.npmjs.com/package/supertest) |
| 21 | Stabilize API and improve test coverage. | [Jest](https://jestjs.io/docs/getting-started)<br>[Postman — API Testing](https://learning.postman.com/docs/writing-scripts/test-scripts/) |
| 22 | Define relational schema using PostgreSQL/Supabase and write migrations. | [PostgreSQL DDL (Schema Design)](https://www.postgresql.org/docs/current/ddl.html)<br>[Supabase CLI](https://supabase.com/docs/guides/cli) |
| 23 | Enable/configure RLS for multi-tenant isolation in Supabase. | [Supabase — RLS](https://supabase.com/docs/guides/auth/row-level-security)<br>[PostgreSQL — Row Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) |
| 24 | Define RLS policies that respect user roles. | [PostgreSQL — `CREATE POLICY`](https://www.postgresql.org/docs/current/sql-createpolicy.html)<br>[Supabase Policies Guide](https://supabase.com/docs/guides/auth/row-level-security) |
| 25 | Implement keyset pagination for scalable queries. | [Use the Index, Luke — Keyset Pagination](https://use-the-index-luke.com/no-offset)<br>[PostgreSQL — Indexes](https://www.postgresql.org/docs/current/indexes.html) |
| 26 | Implement file attachments via Supabase Storage with signed URLs. | [Supabase Storage](https://supabase.com/docs/guides/storage)<br>[OWASP — File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) |
| 27 | Record audit logs for sensitive actions; expose via API. | [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)<br>[Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) |
| 28 | Database review checkpoint: validate schema, indexes, RLS; write next steps. | [arc42 Architecture Docs](https://docs.arc42.org/)<br>[Design Review Checklist](https://github.com/joelparkerhenderson/design-review-checklist) |
| 29 | Add background jobs using BullMQ + Redis. | [BullMQ](https://docs.bullmq.io/)<br>[Redis Getting Started](https://redis.io/docs/getting-started/) |
| 30 | Implement server-side caching for expensive reads. | [MDN — HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)<br>[Cache Invalidation (Fowler)](https://martinfowler.com/articles/cache-invalidation.html) |
| 31 | Add structured logs, error tracking, and health endpoints. | [Pino](https://getpino.io/)<br>[Sentry for Node](https://docs.sentry.io/platforms/node/) |
| 32 | Protect from abuse and improve security posture (rate limit, helmet, CORS). | [express-rate-limit](https://www.npmjs.com/package/express-rate-limit)<br>[OWASP Top 10](https://owasp.org/www-project-top-ten/)<br>[CORS Middleware](https://expressjs.com/en/resources/middleware/cors.html) |
| 33 | Benchmark under load and identify bottlenecks. | [k6](https://k6.io/docs/)<br>[k6 Test Analysis](https://k6.io/docs/testing-guides/test-analysis/) |
| 34 | Reduce technical debt, expand coverage, stabilize codebase. | [Practical Test Pyramid (Fowler)](https://martinfowler.com/articles/practical-test-pyramid.html)<br>[Refactoring (Fowler)](https://refactoring.com/) |
| 35 | Choose and set up MongoDB module (activity feed or analytics). | [MongoDB Atlas](https://www.mongodb.com/docs/atlas/)<br>[MongoDB — Data Modeling Intro](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/) |
| 36 | Implement chosen MongoDB feature; expose via API. | [MongoDB Node Driver](https://www.mongodb.com/docs/drivers/node/current/)<br>[MongoDB Aggregation](https://www.mongodb.com/docs/manual/aggregation/) |
| 37 | Choose Firebase module (push notifications or Firestore rules demo). | [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)<br>[Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started) |
| 38 | Implement chosen Firebase feature (FCM or rules demo). | [FCM — First Message](https://firebase.google.com/docs/cloud-messaging/android/first-message)<br>[Firestore Rules — Get Started](https://firebase.google.com/docs/firestore/security/get-started) |
| 39 | Optimize costs/performance for MongoDB + Firebase modules. | [Firebase Pricing](https://firebase.google.com/pricing)<br>[MongoDB Indexes](https://www.mongodb.com/docs/manual/indexes/) |
| 40 | Update architecture docs to reflect MongoDB/Firebase additions. | [Mingrammer Diagrams](https://diagrams.mingrammer.com/)<br>[MongoDB — SQL vs NoSQL](https://www.mongodb.com/nosql-explained) |
| 41 | Initialize React Native client + navigation. | [Expo](https://docs.expo.dev/)<br>[React Navigation](https://reactnavigation.org/docs/getting-started) |
| 42 | Add data synchronization in mobile using TanStack Query. | [TanStack Query — React Native](https://tanstack.com/query/v4/docs/react/react-native)<br>[React Native — Networking](https://reactnative.dev/docs/network) |
| 43 | Enable offline writes via queue + idempotency; persist locally. | [react-native-mmkv](https://github.com/mrousavy/react-native-mmkv)<br>[Offline Guidance (Android)](https://developer.android.com/topic/performance/vitals/offline) |
| 44 | Implement conflict resolution strategy between offline and server state. | [Offline-First (Fowler)](https://martinfowler.com/articles/offline-first.html)<br>[Conflict Resolution Overview](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) |
| 45 | Optimize large list rendering using FlatList tuning. | [Optimizing FlatList](https://reactnative.dev/docs/optimizing-flatlist)<br>[RN Performance](https://reactnative.dev/docs/performance) |
| 46 | Integrate push notifications + deep linking. | [RNFirebase — Messaging](https://rnfirebase.io/messaging/usage)<br>[React Navigation — Deep Linking](https://reactnavigation.org/docs/deep-linking) |
| 47 | Add mobile tests and write a short mobile engineering writeup. | [RN Testing Library](https://testing-library.com/docs/react-native-testing-library/intro/)<br>[Detox](https://wix.github.io/Detox/docs/getting-started/introduction/) |
| 48 | Consolidate changes across stack; stabilize. | [Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)<br>[Android Testing Overview](https://developer.android.com/training/testing) |
| 49 | Ensure coverage for mobile + MongoDB + Firebase modules. | [Vitest — Advanced](https://vitest.dev/guide/)<br>[Node Integration Testing Patterns](https://www.joyent.com/node-js/production/design/errors) |
| 50 | Implement E2E tests for critical web flows. | [Playwright](https://playwright.dev/docs/intro)<br>[Cypress Best Practices](https://docs.cypress.io/guides/references/best-practices) |
| 51 | Improve CI, containerize services, add preview deploy notes. | [Docker — Getting Started](https://docs.docker.com/get-started/)<br>[GitHub Actions — Workflows](https://docs.github.com/en/actions/using-workflows) |
| 52 | Final testing pass; close outstanding tasks. | [Jest Coverage](https://jestjs.io/docs/cli#--coverage)<br>[Refactoring for Testability](https://martinfowler.com/articles/refactoring-microservice-testability.html) |
| 53 | Consolidate architecture decisions; finalize ADRs and system design docs. | [MADR](https://adr.github.io/madr/)<br>[Design Docs (PagerDuty)](https://www.pagerduty.com/blog/engineering-design-docs/) |
| 54 | Refactor for structure/readability; run thorough code review. | [Google Code Review Guide](https://google.github.io/eng-practices/review/)<br>[Human Code Reviews (mtlynch)](https://mtlynch.io/human-code-reviews-1/) |
| 55 | Practice incident response; write a postmortem for simulated outage. | [SRE — Incident Management](https://sre.google/sre-book/incident-management/)<br>[Atlassian Postmortems](https://www.atlassian.com/incident-management/postmortem) |
| 56 | Dependency audit and hardening (supply chain, secrets, configs). | [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)<br>[OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) |
| 57 | Finalize architecture documentation and presentation readiness. | [Design Review Checklist](https://github.com/joelparkerhenderson/design-review-checklist)<br>[arc42](https://docs.arc42.org/) |
| 58 | Package with polished documentation and a demo video. | [Make a README](https://www.makeareadme.com/)<br>[Loom — Demo Recording Tips](https://www.loom.com/blog/how-to-record-a-great-video-presentation) |
| 59 | Deploy and verify accessibility; validate end-to-end experience. | [Vercel Docs](https://vercel.com/docs)<br>[Railway Docs](https://docs.railway.app/) |
| 60 | Tag a release and finalize interview prep artifacts. | [interviewing.io — Prep](https://interviewing.io/blog/how-to-prepare-for-your-next-interview)<br>[GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) |

---

## Core Books (Read Gradually)

- Designing Data-Intensive Applications — Martin Kleppmann
- System Design Interview — Alex Xu
- Refactoring — Martin Fowler
- Site Reliability Engineering — Google
- Building Secure & Reliable Systems — Google

---

# Resources Index — Production-Grade Full-Stack Engineering (60 Days)

![Track](https://img.shields.io/badge/Track-Senior-in-60-days-0B5394) ![Focus](https://img.shields.io/badge/Focus-React%2BNode%2BSecurity%2BPerformance-1D76DB) ![Format](https://img.shields.io/badge/Format-Official-first-0E8A16)

---

## Primary Books (Reference Shelf)

- **Designing Data-Intensive Applications** (Martin Kleppmann) — data modeling, consistency, replication, queues, caching.
- **Web Application Security**: **OWASP Cheat Sheet Series** (official) — practical security patterns and checklists. (Use as the default security reference.)
- **System Design Interview** (Alex Xu) — practicing tradeoffs and architecture checkpoints.
- **Refactoring** (Martin Fowler) — safe refactors and maintainable code.

> Tip: treat the OWASP Cheat Sheet Series as your "security unit tests" for decisions (auth, session, XSS, CSRF, secrets).

---

## Video & Talks (High-Signal)

- **React Conf** talks (official recordings)
- **NodeConf** talks (official recordings)
- **Sentry / Grafana** engineering talks on observability (official channels)

---

## Day-by-Day Study Links

Each day links to the exact references listed in that day’s `README.md` (official-first).

| Day | Topic (from daily README) | Links |
|---:|---|---|
| 01 | Initialize the project repository with a clean monorepo structure for web, API,  | [pnpm workspaces documentation](https://pnpm.io/workspaces)<br>[GitHub ignoring files guide](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) |
| 02 | Enforce uniform code style and static analysis across the repo. | [ESLint documentation](https://eslint.org/docs/latest/use/getting-started)<br>[Prettier documentation](https://prettier.io/docs/en/index.html)<br>[TypeScript strict mode](https://www.typescriptlang.org/tsconfig) |
| 03 | Establish continuous integration to ensure code quality and buildability. | [GitHub Actions documentation](https://docs.github.com/en/actions)<br>[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) |
| 04 | Scaffold the Next.js application with basic routing and layout. | [Next.js App Router docs](https://nextjs.org/docs/app/building-your-application/routing)<br>[Tailwind CSS documentation](https://tailwindcss.com/docs) |
| 05 | Build a foundational design system with reusable UI components. | [Storybook for React](https://storybook.js.org/docs/react/get-started/introduction)<br>[Tailwind component patterns](https://tailwindcss.com/docs) |
| 06 | Implement data fetching and caching with TanStack Query and define state ownersh | [TanStack Query documentation](https://tanstack.com/query/v4/docs/react/overview)<br>[React state management guide](https://react.dev/learn/state-a-complete-guide)<br>[useMemo & useCallback hooks](https://react.dev/reference/react) |
| 07 | Refactor and test code created in Week 1 to ensure stability and maintainability | [Vitest documentation](https://vitest.dev/)<br>[React Testing Library docs](https://testing-library.com/docs/react-testing-library/intro) |
| 08 | Build robust forms with validation and consistent patterns. | [react-hook-form documentation](https://react-hook-form.com/get-started)<br>[Zod documentation](https://zod.dev/)<br>[Accessible forms guidance](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML#forms) |
| 09 | Add filtering, sorting, and query parameter handling to the tasks list. | [React list rendering guidance](https://react.dev/learn/rendering-lists)<br>[Next.js search params handling](https://nextjs.org/docs/app/api-reference/functions/use-search-params) |
| 10 | Implement pagination to handle long task lists efficiently. | [Pagination patterns in web UIs](https://uxdesign.cc/pagination-best-practices-9748bf02ba79)<br>[Next.js router API](https://nextjs.org/docs/app/api-reference/functions/use-router) |
| 11 | Diagnose and optimize rendering performance for the tasks list. | [React DevTools Profiler](https://react.dev/learn/profile-performance-with-the-devtools-profiler)<br>[Optimizing performance in React](https://react.dev/learn/optimizing-performance) |
| 12 | Ensure the application meets accessibility standards and provides a great UX for | [Accessibility (a11y) guide](https://www.w3.org/WAI/fundamentals/accessibility-intro/)<br>[Testing accessibility with axe](https://www.deque.com/axe/) |
| 13 | Deepen understanding of the App Router and implement caching strategies. | [Next.js App Router advanced docs](https://nextjs.org/docs/app/building-your-application/routing)<br>[Next.js caching strategies](https://nextjs.org/docs/app/building-your-application/caching) |
| 14 | Pause to evaluate the architecture built so far and document high-level design d | [Architecture Decision Records guide](https://adr.github.io/madr/)<br>[Writing effective design documents](https://www.freecodecamp.org/news/how-to-write-a-good-software-design-doc/) |
| 15 | Set up the Express server with a clean structure and centralized error handling. | [Express routing docs](https://expressjs.com/en/guide/routing.html)<br>[Node.js event loop guide](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick) |
| 16 | Validate API inputs and define a consistent error contract. | [Zod documentation](https://zod.dev/)<br>[Express error handling docs](https://expressjs.com/en/guide/error-handling.html) |
| 17 | Implement JWT-based authentication with access and refresh tokens. | [JWT introduction](https://jwt.io/introduction)<br>[OWASP authentication cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) |
| 18 | Implement role-based access control to protect resources within organizations. | [Role-based access control (RBAC) patterns](https://auth0.com/docs/get-started/authorization/rbac)<br>[Express middleware patterns](https://expressjs.com/en/guide/writing-middleware.html) |
| 19 | Implement initial CRUD endpoints for core resources (orgs, projects, tasks). | [RESTful API design principles](https://restfulapi.net/)<br>[Express routing guide](https://expressjs.com/en/guide/routing.html) |
| 20 | Generate and document API specifications and write integration tests. | [OpenAPI specification](https://www.openapis.org)<br>[Supertest documentation](https://www.npmjs.com/package/supertest) |
| 21 | Stabilize the API and update test coverage. | [Jest testing framework](https://jestjs.io/docs/getting-started)<br>[API testing strategies](https://www.getpostman.com/api-testing) |
| 22 | Define a relational schema using PostgreSQL/Supabase and write migrations. | [PostgreSQL schema design](https://www.postgresql.org/docs/current/ddl-gestalt.html)<br>[Supabase CLI documentation](https://supabase.com/docs/guides/cli) |
| 23 | Enable and configure row-level security (RLS) for multi-tenant isolation in Supa | [Supabase RLS guide](https://supabase.com/docs/guides/auth#policies)<br>[PostgreSQL RLS policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) |
| 24 | Define row-level security policies that respect user roles. | [Supabase policies documentation](https://supabase.com/docs/)<br>[Role-based access control in Postgres](https://www.postgresql.org/docs/current/sql-createpolicy.html) |
| 25 | Implement keyset pagination for scalable queries. | [Keyset pagination article](https://hakibenita.com/keyset-pagination)<br>[Postgres ordering and indexes](https://www.postgresql.org/docs/current/indexes-ordering.html) |
| 26 | Implement file attachment handling via Supabase Storage with signed URLs. | [Supabase Storage documentation](https://supabase.com/docs/guides/storage)<br>[Handling uploads securely](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#media_types) |
| 27 | Record audit logs for sensitive actions and expose them via an API. | [Audit logging best practices](https://www.owasp.org/index.php/Logging_Cheat_Sheet)<br>[Event sourcing patterns](https://martinfowler.com/eaaDev/EventSourcing.html) |
| 28 | Reflect on database design and RLS policies, and plan next steps. | [Design review template](https://docs.microsoft.com/en-us/learn/modules/design-review/)<br>[Software architecture documentation](https://docs.arc42.org/) |
| 29 | Introduce background job processing using BullMQ and Redis. | [BullMQ documentation](https://docs.bullmq.io/)<br>[Redis Quickstart](https://redis.io/docs/getting-started/) |
| 30 | Implement server-side caching for expensive read queries. | [Redis caching best practices](https://redis.io/docs/manual/keyspace-events/)<br>[Cache invalidation strategies](https://martinfowler.com/articles/cache-invalidation.html) |
| 31 | Add structured logs, error tracking, and health endpoints for observability. | [pino logging library](https://getpino.io/)<br>[Sentry for Node](https://docs.sentry.io/platforms/node/) |
| 32 | Protect the application from abuse and improve overall security posture. | [express-rate-limit documentation](https://www.npmjs.com/package/express-rate-limit)<br>[OWASP Top 10](https://owasp.org/www-project-top-ten/)<br>[CORS and Helmet](https://expressjs.com/en/resources/middleware/cors.html) |
| 33 | Benchmark and identify performance bottlenecks under load. | [k6 load testing tool](https://k6.io/docs/)<br>[Interpreting performance metrics](https://docs.k6.io/docs/test-analysis) |
| 34 | Address technical debt, expand coverage, and stabilize the codebase. | [Testing strategies overview](https://martinfowler.com/articles/practical-test-pyramid.html)<br>[Refactoring best practices](https://refactoring.com/) |
| 35 | Decide on and set up a MongoDB module for activity feeds or analytics. | [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/)<br>[Bucket pattern for time series](https://www.mongodb.com/presentations/data-modeling-time-series-event-bucket-pattern) |
| 36 | Implement the chosen MongoDB feature and expose it via the API. | [MongoDB Node.js driver](https://www.mongodb.com/docs/drivers/node/current/)<br>[Aggregation pipeline best practices](https://www.mongodb.com/docs/manual/aggregation/) |
| 37 | Decide on using Firebase for push notifications or Firestore security demo and s | [Firebase Cloud Messaging (FCM) docs](https://firebase.google.com/docs/cloud-messaging)<br>[Firestore security rules](https://firebase.google.com/docs/firestore/security/rules) |
| 38 | Implement the chosen Firebase feature (push notifications or Firestore rules dem | [Firebase Cloud Messaging integration](https://firebase.google.com/docs/cloud-messaging/ios/first-message)<br>[Firestore security rules examples](https://firebase.google.com/docs/firestore/security/get-started) |
| 39 | Optimize costs and performance for MongoDB and Firebase modules. | [Firebase cost management](https://firebase.google.com/pricing)<br>[MongoDB indexing strategies](https://www.mongodb.com/docs/manual/indexes/) |
| 40 | Update architectural documentation to reflect MongoDB and Firebase additions. | [System architecture templates](https://diagrams.mingrammer.com/)<br>[Comparing SQL and NoSQL](https://www.mongodb.com/nosql-explained) |
| 41 | Initialize the React Native client and basic navigation for the mobile app. | [Expo documentation](https://docs.expo.dev/)<br>[React Navigation](https://reactnavigation.org/docs/getting-started) |
| 42 | Set up data synchronization in the mobile client using TanStack Query. | [TanStack Query for React Native](https://tanstack.com/query/v4/docs/react/react-native)<br>[React Native networking overview](https://reactnative.dev/docs/network) |
| 43 | Enable offline write capability in the mobile app using a queue with idempotency | [MMKV storage documentation](https://github.com/mrousavy/react-native-mmkv)<br>[Offline-first apps guidance](https://developer.android.com/topic/performance/vitals/offline) |
| 44 | Decide and implement a strategy to resolve conflicts between offline and server  | [Conflict resolution strategies](https://www.mongodb.com/docs/manual/faq/change-streams-conflict-resolution/)<br>[Offline sync patterns](https://docs.microsoft.com/en-us/xamarin/essentials/preferences) |
| 45 | Optimize large lists rendering in the mobile app using FlatList tuning. | [FlatList performance guide](https://reactnative.dev/docs/optimizing-flatlist)<br>[React Native performance overview](https://reactnative.dev/docs/performance) |
| 46 | Integrate push notifications and support deep linking into specific screens. | [React Native Firebase messaging](https://rnfirebase.io/messaging/usage)<br>[React Navigation deep linking](https://reactnavigation.org/docs/deep-linking) |
| 47 | Add tests for mobile components and reflect on the mobile development process. | [Detox end-to-end testing](https://wix.github.io/Detox/docs/getting-started/configuration)<br>[React Native testing library](https://testing-library.com/docs/react-native-testing-library/intro/) |
| 48 | Consolidate mobile and backend changes; stabilize the codebase. | [Cross-platform testing strategies](https://developer.android.com/training/testing)<br>[Maintaining large codebases](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) |
| 49 | Ensure comprehensive test coverage for new features (mobile, MongoDB, Firebase). | [Vitest advanced usage](https://vitest.dev/guide/working-with-vitest.html)<br>[Integration testing patterns](https://blog.logrocket.com/guide-integration-testing-node-apps/) |
| 50 | Implement end-to-end tests for critical user flows across web and mobile. | [Playwright documentation](https://playwright.dev/docs/intro)<br>[Cypress best practices](https://docs.cypress.io/guides/references/best-practices) |
| 51 | Improve the CI pipeline, containerize the application, and set up preview deploy | [Docker documentation](https://docs.docker.com/get-started/)<br>[GitHub Actions advanced](https://docs.github.com/en/actions/using-workflows) |
| 52 | Perform final testing pass and finalize any outstanding tasks. | [Refactoring for testability](https://martinfowler.com/articles/refactoring-microservice-testability.html)<br>[Test coverage analysis](https://jestjs.io/docs/cli#--coverage) |
| 53 | Consolidate architectural decisions and document them comprehensively. | [ADR template (MADR)](https://adr.github.io/madr/)<br>[Writing effective system design docs](https://www.pagerduty.com/blog/engineering-design-docs/) |
| 54 | Improve structure and readability by refactoring and performing thorough code re | [Refactoring patterns](https://refactoring.guru/refactoring/techniques)<br>[Effective code reviews](https://mtlynch.io/human-code-reviews-1/) |
| 55 | Practice incident response and write a postmortem for a simulated outage. | [Incident response guide](https://sre.google/sre-book/handling-overload/)<br>[Postmortem templates](https://www.atlassian.com/incident-management/postmortem) |
| 56 | Audit dependencies and configurations for security vulnerabilities and harden th | [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)<br>[OWASP cheat sheets](https://cheatsheetseries.owasp.org/) |
| 57 | Finalize architecture documentation and prepare the project for presentation. | [Design review checklist](https://github.com/joelparkerhenderson/design-review-checklist)<br>[Architecture doc examples](https://engineering.atspotify.com/2020-04-07-the-spotify-squad-health-check/) |
| 58 | Package the project with polished documentation and a demo video. | [Writing a great README](https://www.makeareadme.com/)<br>[Recording technical demos](https://www.loom.com/blog/how-to-record-a-great-video-presentation) |
| 59 | Deploy the application and ensure all components are accessible for demonstratio | [Vercel deployment docs](https://vercel.com/docs)<br>[Railway deployment guide](https://docs.railway.app/deploy/) |
| 60 | Finalize the project, tag a release, and prepare for interviews. | [Preparing for technical interviews](https://interviewing.io/blog/how-to-prepare-for-your-next-interview)<br>[Writing a great portfolio](https://towardsdatascience.com/creating-an-impressive-portfolio-that-gets-you-hired-6a4184e5f09d) |
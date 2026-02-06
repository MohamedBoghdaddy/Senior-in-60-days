"""
Utility script to generate the 60‑day roadmap folder structure and
corresponding README files. Each day's README is scaffolded with
a consistent layout including badges, focus, timebox, study links,
build steps, assignments, definition of done (DoD) checklist, commit
message suggestion, outcome artifacts, and self‑review questions.

This script is meant to be run from the root of the repository. It
creates the `days`, `templates`, `resources`, `assignments`, and
`notes` directories if they do not already exist. Day folders are
named `day-XX` where `XX` is a zero‑padded number from 01–60.

To run this script:

    python generate_readmes.py

It will produce all README files with the appropriate content based
on the `days_data` structure defined below.
"""

import os
from pathlib import Path


def make_badge(label: str, message: str, color: str) -> str:
    """Return a shields.io badge markdown string."""
    label = label.replace(" ", "%20")
    message = message.replace(" ", "%20")
    return f"![{label}](https://img.shields.io/badge/{label}-{message}-{color})"


def make_section(title: str, content: str) -> str:
    """Return a markdown section with a heading and content."""
    return f"### {title}\n\n{content.strip()}\n"


def build_readme(day_number: int, data: dict) -> str:
    """Assemble the README markdown for a given day."""
    day_str = f"{day_number:02d}"
    title_line = f"# Day {day_str} — {data['title']}\n"
    # Badges
    badges = " ".join([
        make_badge("Day", day_str, "blue"),
        make_badge("Area", data.get("area", "misc"), "lightgrey"),
        make_badge("Priority", "P0", "red"),
    ])
    header = f"{badges}\n\n---\n"

    # Sections
    focus = make_section("Focus", data["focus"])
    timebox = make_section("Timebox", data.get("timebox", "~3 hours"))

    # Study links as a markdown list
    study_lines = []
    for item in data.get("study", []):
        study_lines.append(f"- [{item['name']}]({item['url']})")
    study_content = "\n".join(study_lines)
    study = make_section("Study", study_content)

    # Build steps
    build_lines = []
    for step in data.get("build", []):
        build_lines.append(f"1. {step}")
    build_content = "\n".join(build_lines)
    build_section = make_section("Build", build_content)

    # Assignments
    assign_lines = []
    for item in data.get("assignments", []):
        assign_lines.append(f"- {item}")
    assignments = make_section("Assignments", "\n".join(assign_lines))

    # DoD checklist
    dod_lines = []
    for item in data.get("dod", []):
        dod_lines.append(f"- [ ] {item}")
    dod_section = make_section("DoD Checklist", "\n".join(dod_lines))

    # Commit message
    commit_msg = make_section("Commit Message", f"`{data.get('commit_msg', '')}`")

    # Outcome artifacts
    outcome_lines = []
    for item in data.get("outcome", []):
        outcome_lines.append(f"- {item}")
    outcome_section = make_section("Outcome Artifacts", "\n".join(outcome_lines))

    # Self‑review questions
    review_lines = []
    for item in data.get("review_questions", []):
        review_lines.append(f"- {item}")
    review_section = make_section("Self‑Review Questions", "\n".join(review_lines))

    # Assemble
    return (
        title_line
        + header
        + focus
        + timebox
        + study
        + build_section
        + assignments
        + dod_section
        + commit_msg
        + outcome_section
        + review_section
    )


def main():
    # Base directory
    base_dir = Path(".")
    days_dir = base_dir / "days"
    templates_dir = base_dir / "templates"
    resources_dir = base_dir / "resources"
    assignments_dir = base_dir / "assignments"
    notes_dir = base_dir / "notes"

    # Ensure directories exist
    for d in [days_dir, templates_dir, resources_dir, assignments_dir, notes_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Data definitions for each day
    days_data = [
        {
            "title": "Monorepo Bootstrap",
            "area": "devops",
            "focus": "Initialize the project repository with a clean monorepo structure for web, API, and shared packages.",
            "timebox": "~3 hours",
            "study": [
                {"name": "pnpm workspaces documentation", "url": "https://pnpm.io/workspaces"},
                {"name": "GitHub ignoring files guide", "url": "https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files"},
            ],
            "build": [
                "Initialize Git repository and create directory structure: `apps/web`, `apps/api`, `packages/shared`.",
                "Configure package manager workspaces (e.g., pnpm or Yarn).",
                "Add `.gitignore`, `.nvmrc`, and an initial `README.md` placeholder.",
            ],
            "assignments": [
                "Commit the scaffold and initial configuration.",
                "Update the root README explaining the repo structure.",
            ],
            "dod": [
                "Repository is initialized and builds successfully.",
                "`npm install` works for all packages.",
                "Folder structure matches specification.",
            ],
            "commit_msg": "feat(setup): initialize monorepo structure and tooling",
            "outcome": [
                "Created directories: `apps/`, `packages/`. ",
                "Added `.gitignore` and `.nvmrc` files.",
            ],
            "review_questions": [
                "Does the workspace configuration support future package additions?",
                "Are there any untracked files that should be ignored?",
            ],
        },
        {
            "title": "Tooling & Linting",
            "area": "devops",
            "focus": "Enforce uniform code style and static analysis across the repo.",
            "timebox": "~3 hours",
            "study": [
                {"name": "ESLint documentation", "url": "https://eslint.org/docs/latest/use/getting-started"},
                {"name": "Prettier documentation", "url": "https://prettier.io/docs/en/index.html"},
                {"name": "TypeScript strict mode", "url": "https://www.typescriptlang.org/tsconfig"},
            ],
            "build": [
                "Configure ESLint with React and TypeScript plugins.",
                "Configure Prettier and integrate with ESLint.",
                "Set up Husky pre-commit hooks to run lint and format.",
                "Enable TypeScript strict mode in tsconfig.",
            ],
            "assignments": [
                "Verify linting surfaces errors and Prettier auto-formats code.",
                "Document code style guidelines in the repository.",
            ],
            "dod": [
                "Running `npm run lint` shows no errors.",
                "Prettier formats code on commit via hook.",
                "TypeScript strict mode enabled and passing.",
            ],
            "commit_msg": "chore(lint): configure ESLint, Prettier, and husky hooks",
            "outcome": [
                "ESLint config file created (`.eslintrc` or `eslint.config.js`).",
                "Prettier config file created (`.prettierrc`).",
            ],
            "review_questions": [
                "Do lint rules cover all common errors?",
                "Is Prettier integrated seamlessly with ESLint?",
            ],
        },
        {
            "title": "CI Setup",
            "area": "devops",
            "focus": "Establish continuous integration to ensure code quality and buildability.",
            "timebox": "~3 hours",
            "study": [
                {"name": "GitHub Actions documentation", "url": "https://docs.github.com/en/actions"},
                {"name": "Conventional Commits", "url": "https://www.conventionalcommits.org/en/v1.0.0/"},
            ],
            "build": [
                "Create GitHub Actions workflow to run lint, test, and build on push and pull requests.",
                "Configure branch protection rules (if applicable).",
                "Write `CONTRIBUTING.md` and a PR template instructing commit message format.",
            ],
            "assignments": [
                "Push workflow file to `.github/workflows` directory.",
                "Ensure pipeline fails if lint/tests fail.",
            ],
            "dod": [
                "CI pipeline triggers on push and PR.",
                "Commits follow Conventional Commits guidelines.",
                "PR template auto-populates with checklists.",
            ],
            "commit_msg": "ci: add GitHub Actions pipeline and contribution guidelines",
            "outcome": [
                "Added `.github/workflows/main.yml`.",
                "Created `CONTRIBUTING.md` and PR template.",
            ],
            "review_questions": [
                "Does the CI pipeline cover all relevant checks?",
                "Are commit guidelines clear to contributors?",
            ],
        },
        {
            "title": "Next.js Skeleton",
            "area": "frontend",
            "focus": "Scaffold the Next.js application with basic routing and layout.",
            "timebox": "~4 hours",
            "study": [
                {"name": "Next.js App Router docs", "url": "https://nextjs.org/docs/app/building-your-application/routing"},
                {"name": "Tailwind CSS documentation", "url": "https://tailwindcss.com/docs"},
            ],
            "build": [
                "Initialize a Next.js application using the App Router (`app/` directory).",
                "Create a basic layout with header and navigation placeholders.",
                "Set up initial pages for sign-in, sign-up, and dashboard.",
                "Integrate Tailwind CSS for styling with a configuration file.",
            ],
            "assignments": [
                "Commit the initial Next.js skeleton with styling.",
                "Document the folder structure in the README.",
            ],
            "dod": [
                "Application runs without errors (`npm run dev` works).",
                "Routing and navigation operate correctly.",
                "Tailwind classes compile successfully.",
            ],
            "commit_msg": "feat(web): scaffold Next.js app with basic layout and Tailwind",
            "outcome": [
                "`app/` directory with pages defined.",
                "`tailwind.config.js` created and configured.",
            ],
            "review_questions": [
                "Is the layout responsive and accessible at this stage?",
                "Does the App Router use file-based routing correctly?",
            ],
        },
        {
            "title": "Design System Components",
            "area": "frontend",
            "focus": "Build a foundational design system with reusable UI components.",
            "timebox": "~4 hours",
            "study": [
                {"name": "Storybook for React", "url": "https://storybook.js.org/docs/react/get-started/introduction"},
                {"name": "Tailwind component patterns", "url": "https://tailwindcss.com/docs"},
            ],
            "build": [
                "Create a component library in `packages/ui` with Button, Input, Modal, and Toast components.",
                "Use Tailwind CSS classes to style components consistently.",
                "Optionally set up Storybook to document and preview components.",
                "Ensure components support variants and proper accessibility attributes.",
            ],
            "assignments": [
                "Commit UI components and update documentation.",
                "If using Storybook, include sample stories for each component.",
            ],
            "dod": [
                "Components render correctly in isolation.",
                "Props and variants are documented.",
                "Accessibility attributes present (aria-* as needed).",
            ],
            "commit_msg": "feat(ui): add foundational components (Button, Input, Modal, Toast)",
            "outcome": [
                "Files under `packages/ui` for each component.",
                "Optional Storybook stories for components.",
            ],
            "review_questions": [
                "Do components handle different states (disabled, loading)?",
                "Are the components themeable and composable?",
            ],
        },
        {
            "title": "State Management & Query Setup",
            "area": "frontend",
            "focus": "Implement data fetching and caching with TanStack Query and define state ownership.",
            "timebox": "~3 hours",
            "study": [
                {"name": "TanStack Query documentation", "url": "https://tanstack.com/query/v4/docs/react/overview"},
                {"name": "React state management guide", "url": "https://react.dev/learn/state-a-complete-guide"},
                {"name": "useMemo & useCallback hooks", "url": "https://react.dev/reference/react"},
            ],
            "build": [
                "Install TanStack Query and wrap application with `QueryClientProvider`.",
                "Create an API client wrapper for fetch requests.",
                "Implement a simple `useQuery` hook for fetching a tasks list from the API (mock endpoint).",
                "Define an ADR discussing state ownership (local vs context vs server state).",
            ],
            "assignments": [
                "Commit query setup and state ownership ADR.",
                "Ensure tasks list re-renders only when data changes.",
            ],
            "dod": [
                "Queries cache properly with defined `staleTime` and `retry` policies.",
                "ADR explains reasoning for state placement.",
                "API client wrapper handles base URL and error parsing.",
            ],
            "commit_msg": "feat(state): configure TanStack Query and document state ownership decisions",
            "outcome": [
                "Added `QueryClient` provider in the app.",
                "Created `apiClient.ts` in shared package.",
                "ADR document in `/docs/adrs`.",
            ],
            "review_questions": [
                "Are you using React Query features effectively (cache, refetch)?",
                "Does the ADR capture trade-offs clearly?",
            ],
        },
        {
            "title": "Review & Testing Day #1",
            "area": "testing",
            "focus": "Refactor and test code created in Week 1 to ensure stability and maintainability.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Vitest documentation", "url": "https://vitest.dev/"},
                {"name": "React Testing Library docs", "url": "https://testing-library.com/docs/react-testing-library/intro"},
            ],
            "build": [
                "Refactor the codebase for clarity and modularity.",
                "Write unit tests for utility functions and UI components created in the first week.",
                "Resolve any technical debt or minor issues found during review.",
            ],
            "assignments": [
                "Commit tests and refactoring improvements.",
                "Write a short reflection in `notes/day-07.md` about lessons learned.",
            ],
            "dod": [
                "Unit tests run and pass in CI.",
                "No unused variables or lint errors remain.",
                "Reflection notes added to `notes/day-07.md`.",
            ],
            "commit_msg": "test(core): add unit tests and refactor modules (Week 1 review)",
            "outcome": [
                "Test files in `__tests__/` or similar directory.",
                "Updated code structure for maintainability.",
                "Reflection note in `/notes/day-07.md`.",
            ],
            "review_questions": [
                "Did the refactor improve readability?",
                "Do the tests cover edge cases?",
            ],
        },
        {
            "title": "Forms & Validation",
            "area": "frontend",
            "focus": "Build robust forms with validation and consistent patterns.",
            "timebox": "~3 hours",
            "study": [
                {"name": "react-hook-form documentation", "url": "https://react-hook-form.com/get-started"},
                {"name": "Zod documentation", "url": "https://zod.dev/"},
                {"name": "Accessible forms guidance", "url": "https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML#forms"},
            ],
            "build": [
                "Integrate `react-hook-form` with `zod` for schema validation.",
                "Build Create Task and Edit Task forms with inline validation errors.",
                "Write component tests covering form submission and validation flows.",
                "Document a standard pattern for building forms in this project.",
            ],
            "assignments": [
                "Commit forms implementation and tests.",
                "Add the form pattern guide to the documentation.",
            ],
            "dod": [
                "Invalid data shows user-friendly errors.",
                "Valid submissions trigger API calls (mock or real).",
                "Tests cover both success and failure cases.",
            ],
            "commit_msg": "feat(forms): implement robust forms with validation and tests",
            "outcome": [
                "Form components with validation logic.",
                "Tests demonstrating correct form behaviour.",
                "Documentation for form patterns.",
            ],
            "review_questions": [
                "Do the forms handle all necessary input states?",
                "Are validation messages clear and accessible?",
            ],
        },
        {
            "title": "List Filters & Sorting",
            "area": "frontend",
            "focus": "Add filtering, sorting, and query parameter handling to the tasks list.",
            "timebox": "~3 hours",
            "study": [
                {"name": "React list rendering guidance", "url": "https://react.dev/learn/rendering-lists"},
                {"name": "Next.js search params handling", "url": "https://nextjs.org/docs/app/api-reference/functions/use-search-params"},
            ],
            "build": [
                "Implement filter and sort controls for the tasks list (e.g., by status, priority, date).",
                "Sync filter and sort state with URL query parameters.",
                "Ensure stable sorting fields and sanitize input values.",
                "Provide empty, loading, and error states for the list.",
            ],
            "assignments": [
                "Commit the filtering and sorting implementation.",
                "Update documentation to describe query parameter contract.",
            ],
            "dod": [
                "Filtering and sorting update URL correctly.",
                "Stable keys used for list items.",
                "Tests verify filter/sort behaviours.",
            ],
            "commit_msg": "feat(list): add filtering and sorting with query parameter sync",
            "outcome": [
                "Updated tasks list component with filters and sorting.",
                "Documentation of query params contract.",
            ],
            "review_questions": [
                "Are the filter options comprehensive?",
                "Do the query parameters reflect UI state accurately?",
            ],
        },
        {
            "title": "Pagination",
            "area": "frontend",
            "focus": "Implement pagination to handle long task lists efficiently.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Pagination patterns in web UIs", "url": "https://uxdesign.cc/pagination-best-practices-9748bf02ba79"},
                {"name": "Next.js router API", "url": "https://nextjs.org/docs/app/api-reference/functions/use-router"},
            ],
            "build": [
                "Add client-side pagination controls (previous/next, page numbers).",
                "Synchronize pagination state with query parameters for shareable URLs.",
                "Plan API shape for server-side pagination (offset or cursor).",
                "Refactor list component to consume paginated data.",
            ],
            "assignments": [
                "Commit pagination implementation and update tests.",
                "Document the pagination strategy and API shape.",
            ],
            "dod": [
                "Pagination controls render and function correctly.",
                "URL reflects current page.",
                "Documentation updated to describe pagination approach.",
            ],
            "commit_msg": "feat(list): implement client-side pagination and plan server API",
            "outcome": [
                "Pagination controls in the tasks UI.",
                "Documentation of pagination strategy.",
            ],
            "review_questions": [
                "Does the pagination UI degrade gracefully on small screens?",
                "Are query parameters sanitized for invalid page numbers?",
            ],
        },
        {
            "title": "Performance Profiling",
            "area": "performance",
            "focus": "Diagnose and optimize rendering performance for the tasks list.",
            "timebox": "~3 hours",
            "study": [
                {"name": "React DevTools Profiler", "url": "https://react.dev/learn/profile-performance-with-the-devtools-profiler"},
                {"name": "Optimizing performance in React", "url": "https://react.dev/learn/optimizing-performance"},
            ],
            "build": [
                "Use React DevTools Profiler to record renders while interacting with the tasks list.",
                "Identify components with unnecessary re-renders and memoize them appropriately using `React.memo`, `useMemo`, and `useCallback`.",
                "Implement list virtualization using `react-window` for large lists.",
                "Write a performance note summarizing before/after results and decisions.",
            ],
            "assignments": [
                "Commit performance optimizations.",
                "Add `docs/performance.md` capturing findings and decisions.",
            ],
            "dod": [
                "Measured improvement in render times captured in the note.",
                "List virtualization reduces DOM nodes for large data sets.",
                "No broken functionality after optimization.",
            ],
            "commit_msg": "perf(list): profile and optimize rendering and add virtualization",
            "outcome": [
                "Performance report in `docs/performance.md`.",
                "Optimized list component using virtualization.",
            ],
            "review_questions": [
                "Which components caused the most re-renders and how were they optimized?",
                "Does virtualization produce any scroll flicker or UI bug?",
            ],
        },
        {
            "title": "Accessibility Audit",
            "area": "frontend",
            "focus": "Ensure the application meets accessibility standards and provides a great UX for all users.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Accessibility (a11y) guide", "url": "https://www.w3.org/WAI/fundamentals/accessibility-intro/"},
                {"name": "Testing accessibility with axe", "url": "https://www.deque.com/axe/"},
            ],
            "build": [
                "Audit existing components with an accessibility testing tool (e.g., axe) to identify issues.",
                "Add keyboard navigation and focus management; ensure modals trap focus.",
                "Provide ARIA attributes and semantic HTML where needed.",
                "Write tests verifying accessible interactions and roles.",
            ],
            "assignments": [
                "Fix accessibility issues discovered during the audit.",
                "Update `A11Y.md` with a checklist and guidelines.",
            ],
            "dod": [
                "Accessibility issues are fixed and tests pass.",
                "Keyboard navigation works across the UI.",
                "A11Y checklist committed and referenced in docs.",
            ],
            "commit_msg": "chore(a11y): audit and improve accessibility; add guidelines",
            "outcome": [
                "A11Y report and checklist in the docs.",
                "Improved UI components with proper semantics.",
            ],
            "review_questions": [
                "Are all interactive elements reachable via keyboard?",
                "Do ARIA attributes accurately reflect component roles?",
            ],
        },
        {
            "title": "Next.js App Router & Caching",
            "area": "frontend",
            "focus": "Deepen understanding of the App Router and implement caching strategies.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Next.js App Router advanced docs", "url": "https://nextjs.org/docs/app/building-your-application/routing"},
                {"name": "Next.js caching strategies", "url": "https://nextjs.org/docs/app/building-your-application/caching"},
            ],
            "build": [
                "Split data fetching between server and client components as appropriate.",
                "Implement route handlers (e.g., `/api/tasks`) using Next.js API routes or server actions.",
                "Apply caching headers or revalidation options to ensure fresh data without redundant fetches.",
                "Document decisions in an ADR regarding rendering boundaries and caching choices.",
            ],
            "assignments": [
                "Commit rendering boundary and caching implementations.",
                "Write an ADR summarizing server/client component decisions.",
            ],
            "dod": [
                "Data fetching occurs in the correct layer (server or client).",
                "Caching controls prevent unnecessary network requests.",
                "ADR committed to `/docs/adrs`.",
            ],
            "commit_msg": "feat(app): implement server/client boundaries and caching strategy",
            "outcome": [
                "Server route handlers or actions implemented.",
                "ADR capturing rendering and caching trade-offs.",
            ],
            "review_questions": [
                "Do server components improve performance or complexity?",
                "Are caching settings appropriate for data freshness?",
            ],
        },
        {
            "title": "System Design Checkpoint #1",
            "area": "system-design",
            "focus": "Pause to evaluate the architecture built so far and document high-level design decisions.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Architecture Decision Records guide", "url": "https://adr.github.io/madr/"},
                {"name": "Writing effective design documents", "url": "https://www.freecodecamp.org/news/how-to-write-a-good-software-design-doc/"},
            ],
            "build": [
                "Create a one-page design outline covering the web, API, and state management layers built so far.",
                "Identify current assumptions, risks, and potential improvements.",
                "Capture key trade-offs made (e.g., state placement, component structure).",
            ],
            "assignments": [
                "Commit `system-design-outline.md` in the docs folder.",
                "Write a reflection in `notes/day-14.md` about open questions and next steps.",
            ],
            "dod": [
                "Outline covers major components and interactions.",
                "Risks and mitigation strategies are explicitly listed.",
                "Reflection note committed.",
            ],
            "commit_msg": "docs(design): add initial system design outline and reflections",
            "outcome": [
                "`docs/system-design-outline.md` capturing current architecture.",
                "Reflection note in `/notes/day-14.md`.",
            ],
            "review_questions": [
                "Are there any unknowns that require deeper research?",
                "What dependencies or constraints might affect future design decisions?",
            ],
        },
        {
            "title": "API Skeleton",
            "area": "backend",
            "focus": "Set up the Express server with a clean structure and centralized error handling.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Express routing docs", "url": "https://expressjs.com/en/guide/routing.html"},
                {"name": "Node.js event loop guide", "url": "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick"},
            ],
            "build": [
                "Scaffold an Express app with `routes`, `controllers`, `services`, and `repositories` directories.",
                "Implement a health endpoint (`GET /health`) returning status and timestamp.",
                "Create a centralized error handling middleware that returns a standard error format (code, message, details, traceId).",
                "Add request ID middleware to attach a unique ID to each incoming request for tracing.",
            ],
            "assignments": [
                "Commit API skeleton with health endpoint and error handler.",
                "Document API structure in the README or docs.",
            ],
            "dod": [
                "Express server starts without errors.",
                "Health endpoint responds with JSON and status 200.",
                "Error handler catches both synchronous and asynchronous errors.",
            ],
            "commit_msg": "feat(api): scaffold Express server with health endpoint and error handling",
            "outcome": [
                "API source files in `apps/api`.",
                "Error handler and request ID middleware.",
            ],
            "review_questions": [
                "Does the current structure separate concerns effectively?",
                "Is the error format clear and extensible?",
            ],
        },
        {
            "title": "Input Validation & Error Contract",
            "area": "backend",
            "focus": "Validate API inputs and define a consistent error contract.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Zod documentation", "url": "https://zod.dev/"},
                {"name": "Express error handling docs", "url": "https://expressjs.com/en/guide/error-handling.html"},
            ],
            "build": [
                "Add validation middleware using Zod (or Joi) for route params, query parameters, and request bodies.",
                "Extend the error handler to include validation errors with appropriate HTTP status codes (e.g., 400 for bad request).",
                "Define and document a standard error response shape: `{ code, message, details, traceId }`.",
                "Write tests covering valid and invalid input scenarios.",
            ],
            "assignments": [
                "Commit validation middleware and update error handling.",
                "Document the error contract in API docs or README.",
            ],
            "dod": [
                "Invalid requests return 400 with descriptive error messages.",
                "Standard error shape used consistently.",
                "Tests cover both success and failure paths.",
            ],
            "commit_msg": "feat(api): add input validation and standardize error responses",
            "outcome": [
                "Validation schemas and middleware functions.",
                "Updated error handler supporting validation errors.",
            ],
            "review_questions": [
                "Are all external inputs validated adequately?",
                "Does the error contract contain enough information without leaking internals?",
            ],
        },
        {
            "title": "Auth Setup",
            "area": "backend",
            "focus": "Implement JWT-based authentication with access and refresh tokens.",
            "timebox": "~4 hours",
            "study": [
                {"name": "JWT introduction", "url": "https://jwt.io/introduction"},
                {"name": "OWASP authentication cheatsheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"},
            ],
            "build": [
                "Implement login endpoint issuing access and refresh tokens.",
                "Securely store hashed refresh tokens in the database and implement rotation.",
                "Add middleware to verify access tokens and attach `userId` and `orgId` to the request context.",
                "Provide logout and token revocation endpoint.",
            ],
            "assignments": [
                "Commit auth implementation (login/logout, token issuance, middleware).",
                "Document auth flow and security considerations.",
            ],
            "dod": [
                "Users can log in and receive both tokens.",
                "Protected endpoints validate tokens properly and return 401 if invalid.",
                "Refresh token rotation works and old tokens are revoked.",
            ],
            "commit_msg": "feat(auth): implement JWT authentication with token rotation",
            "outcome": [
                "Auth routes (`/auth/login`, `/auth/logout`) implemented.",
                "Middleware for token verification.",
                "Docs describing token flows and expiration.",
            ],
            "review_questions": [
                "Are tokens signed with strong keys and reasonable lifetimes?",
                "Is refresh token storage and rotation handled securely?",
            ],
        },
        {
            "title": "RBAC Middleware",
            "area": "backend",
            "focus": "Implement role-based access control to protect resources within organizations.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Role-based access control (RBAC) patterns", "url": "https://auth0.com/docs/get-started/authorization/rbac"},
                {"name": "Express middleware patterns", "url": "https://expressjs.com/en/guide/writing-middleware.html"},
            ],
            "build": [
                "Define roles (owner, admin, member) and store them in the database (e.g., membership table).",
                "Implement RBAC middleware that checks the user’s role in the organization before executing route handlers.",
                "Add tests for successful and forbidden access scenarios (401 vs 403).",
                "Document RBAC rules and how to assign roles.",
            ],
            "assignments": [
                "Commit RBAC middleware and tests.",
                "Update API documentation to include authorization details.",
            ],
            "dod": [
                "Unauthorized users receive 401; authorized but insufficient role receives 403.",
                "RBAC logic encapsulated in reusable middleware.",
                "Tests cover all roles and paths.",
            ],
            "commit_msg": "feat(auth): add role-based access control middleware and tests",
            "outcome": [
                "Middleware functions for RBAC.",
                "Test suite covering role checks.",
            ],
            "review_questions": [
                "Are all sensitive routes protected by RBAC?",
                "Does the middleware support flexible role assignment (multiple roles, hierarchies)?",
            ],
        },
        {
            "title": "API Endpoints v1",
            "area": "backend",
            "focus": "Implement initial CRUD endpoints for core resources (orgs, projects, tasks).",
            "timebox": "~4 hours",
            "study": [
                {"name": "RESTful API design principles", "url": "https://restfulapi.net/"},
                {"name": "Express routing guide", "url": "https://expressjs.com/en/guide/routing.html"},
            ],
            "build": [
                "Create controllers and routes for organizations, projects, and tasks (create, read, update, delete).",
                "Apply validation, authentication, and RBAC middleware to each route.",
                "Return proper HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 422).",
                "Implement idempotency keys for POST and PUT requests to prevent duplicates.",
            ],
            "assignments": [
                "Commit initial API endpoints and unit tests.",
                "Update OpenAPI spec with routes and request/response schemas.",
            ],
            "dod": [
                "Endpoints return correct status codes and shape.",
                "Middleware executed in correct order (auth → RBAC → validation → handler).",
                "Idempotency keys correctly deduplicate requests.",
            ],
            "commit_msg": "feat(api): implement CRUD endpoints for orgs, projects, and tasks with middleware",
            "outcome": [
                "Controllers and route files for each resource.",
                "OpenAPI updated with new endpoints.",
            ],
            "review_questions": [
                "Are the routes RESTful and intuitive?",
                "Do error responses follow the standard contract?",
            ],
        },
        {
            "title": "OpenAPI & Integration Tests",
            "area": "backend",
            "focus": "Generate and document API specifications and write integration tests.",
            "timebox": "~3 hours",
            "study": [
                {"name": "OpenAPI specification", "url": "https://www.openapis.org"},
                {"name": "Supertest documentation", "url": "https://www.npmjs.com/package/supertest"},
            ],
            "build": [
                "Generate OpenAPI (Swagger) documentation for all existing endpoints with examples.",
                "Expose the spec at an endpoint such as `/api-docs`.",
                "Set up integration test environment using Supertest (or similar) to call real API routes against a test database.",
                "Write integration tests covering critical API flows (e.g., create and list tasks, unauthorized access).",
            ],
            "assignments": [
                "Commit generated OpenAPI spec and docs endpoint.",
                "Ensure integration tests run in CI.",
            ],
            "dod": [
                "OpenAPI UI accessible and shows accurate schemas.",
                "Integration tests pass against a test DB.",
                "Docs updated to explain how to run API tests.",
            ],
            "commit_msg": "docs(api): generate OpenAPI spec and implement integration tests",
            "outcome": [
                "`/api-docs` route serving Swagger UI.",
                "Integration test files in the test suite.",
            ],
            "review_questions": [
                "Do tests cover success and failure scenarios?",
                "Is the API spec kept in sync with code via CI?",
            ],
        },
        {
            "title": "Review & Testing Day #2",
            "area": "testing",
            "focus": "Stabilize the API and update test coverage.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Jest testing framework", "url": "https://jestjs.io/docs/getting-started"},
                {"name": "API testing strategies", "url": "https://www.getpostman.com/api-testing"},
            ],
            "build": [
                "Refactor API code based on feedback from earlier days.",
                "Expand unit and integration tests to cover more cases (edge cases, error handling).",
                "Document lessons learned and remaining challenges in your notes.",
            ],
            "assignments": [
                "Commit improved tests and refactoring changes.",
                "Record a reflection in `notes/day-21.md` about testing challenges and successes.",
            ],
            "dod": [
                "Expanded tests pass consistently.",
                "CI remains green after refactors.",
                "Reflection note completed.",
            ],
            "commit_msg": "test(api): expand unit and integration coverage; refactor services",
            "outcome": [
                "Additional test cases added.",
                "Refactored API modules.",
                "Notes updated for day 21.",
            ],
            "review_questions": [
                "Are there still untested code paths?",
                "Did the refactor introduce any regression?",
            ],
        },
        {
            "title": "Schema Design",
            "area": "db",
            "focus": "Define a relational schema using PostgreSQL/Supabase and write migrations.",
            "timebox": "~4 hours",
            "study": [
                {"name": "PostgreSQL schema design", "url": "https://www.postgresql.org/docs/current/ddl-gestalt.html"},
                {"name": "Supabase CLI documentation", "url": "https://supabase.com/docs/guides/cli"},
            ],
            "build": [
                "Design tables: `orgs`, `memberships`, `projects`, `sprints`, `tasks`, `comments`, `attachments`, `audit_logs`.",
                "Define primary keys, foreign keys, and unique constraints; include audit fields (`created_at`, `updated_at`, `deleted_at`).",
                "Write migration scripts using Supabase CLI or a migration tool like Knex or Prisma.",
                "Create indexes based on expected query patterns (e.g., `(org_id, created_at)` for tasks).",
            ],
            "assignments": [
                "Commit the migration scripts and ER diagram (use Mermaid or a simple diagramming tool).",
                "Document schema design decisions and assumptions.",
            ],
            "dod": [
                "Migrations run idempotently and set up all tables.",
                "Indexes exist for key queries.",
                "Documentation includes the ER diagram and rationale.",
            ],
            "commit_msg": "feat(db): design relational schema and add migrations for core tables",
            "outcome": [
                "Migration scripts committed in `migrations/`.",
                "`docs/schema.md` with ER diagram and design notes.",
            ],
            "review_questions": [
                "Are there any missing relationships or constraints?",
                "Does the schema support future features like soft deletes?",
            ],
        },
        {
            "title": "Enable RLS",
            "area": "db",
            "focus": "Enable and configure row-level security (RLS) for multi-tenant isolation in Supabase.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Supabase RLS guide", "url": "https://supabase.com/docs/guides/auth#policies"},
                {"name": "PostgreSQL RLS policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html"},
            ],
            "build": [
                "Enable RLS on all tables that need isolation (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY`).",
                "Write initial RLS policies to restrict data access by organization (`org_id`) and membership.",
                "Test cross-organization access to ensure unauthorized queries are blocked.",
                "Document common RLS pitfalls and how to avoid them.",
            ],
            "assignments": [
                "Commit RLS configurations and policies.",
                "Add tests simulating users from different orgs trying to access data.",
            ],
            "dod": [
                "RLS is enabled on all relevant tables.",
                "Cross-org access queries return no rows.",
                "Documentation explains RLS setup and pitfalls.",
            ],
            "commit_msg": "feat(db): enable RLS and define initial multi-tenant policies",
            "outcome": [
                "Policy SQL scripts in migrations.",
                "Tests demonstrating RLS in action.",
            ],
            "review_questions": [
                "Are there any tables missing RLS enforcement?",
                "Do policies allow only the intended operations?",
            ],
        },
        {
            "title": "Role-Based Policies",
            "area": "db",
            "focus": "Define row-level security policies that respect user roles.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Supabase policies documentation", "url": "https://supabase.com/docs/"},
                {"name": "Role-based access control in Postgres", "url": "https://www.postgresql.org/docs/current/sql-createpolicy.html"},
            ],
            "build": [
                "Create RLS policies that factor in user roles (owner, admin, member) for select, insert, update, and delete operations.",
                "Use role membership tables (e.g., `memberships`) to determine permissible actions.",
                "Test scenarios where users attempt to exceed their role permissions.",
                "Document policy logic and alternatives considered.",
            ],
            "assignments": [
                "Commit updated RLS policies and tests.",
                "Update `SECURITY.md` describing role-based policies.",
            ],
            "dod": [
                "Policies enforce role-based restrictions for all relevant operations.",
                "Tests confirm that owners and admins can perform additional actions compared to members.",
                "Documentation reflects policy logic.",
            ],
            "commit_msg": "feat(db): implement role-based RLS policies and update security docs",
            "outcome": [
                "RLS policy definitions updated in migration scripts.",
                "Tests verifying role-specific access.",
                "Updated `SECURITY.md` explaining RLS roles.",
            ],
            "review_questions": [
                "Are any roles overly permissive or restrictive?",
                "How are new roles or privileges integrated into the policies?",
            ],
        },
        {
            "title": "Pagination Strategy",
            "area": "db",
            "focus": "Implement keyset pagination for scalable queries.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Keyset pagination article", "url": "https://hakibenita.com/keyset-pagination"},
                {"name": "Postgres ordering and indexes", "url": "https://www.postgresql.org/docs/current/indexes-ordering.html"},
            ],
            "build": [
                "Refactor task list queries to use keyset (cursor) pagination rather than offset/limit.",
                "Add cursor parameters to API routes and update query logic in controllers.",
                "Ensure indexes support sorting by created_at and id to allow stable ordering.",
                "Update front‑end to consume cursor-based pagination.",
            ],
            "assignments": [
                "Commit query changes and update API docs.",
                "Write an ADR detailing the pagination strategy and why it was chosen.",
            ],
            "dod": [
                "Keyset pagination works and returns expected results.",
                "Backward pagination (previous page) is supported or noted if intentionally omitted.",
                "ADR explains trade-offs between offset and cursor approaches.",
            ],
            "commit_msg": "feat(db): implement keyset pagination and update API/ADR",
            "outcome": [
                "Updated queries using cursor-based pagination.",
                "ADR in `/docs/adrs` explaining pagination choices.",
            ],
            "review_questions": [
                "Does keyset pagination improve performance for large tables?",
                "How does the API handle invalid or expired cursors?",
            ],
        },
        {
            "title": "Attachments & Storage",
            "area": "db",
            "focus": "Implement file attachment handling via Supabase Storage with signed URLs.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Supabase Storage documentation", "url": "https://supabase.com/docs/guides/storage"},
                {"name": "Handling uploads securely", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#media_types"},
            ],
            "build": [
                "Configure a Supabase Storage bucket for attachments (public/private).",
                "Implement backend logic for generating signed upload and download URLs.",
                "Add file metadata fields to the `attachments` table (e.g., file name, size, content type).",
                "Validate file types and sizes on upload to prevent misuse.",
            ],
            "assignments": [
                "Commit storage implementation and update API routes for attachments.",
                "Add UI for uploading and viewing attachments.",
            ],
            "dod": [
                "Signed URLs expire appropriately and protect file access.",
                "Unsupported file types are rejected gracefully.",
                "Attachments display correctly in the UI.",
            ],
            "commit_msg": "feat(attachments): integrate Supabase Storage with signed URL upload/download",
            "outcome": [
                "Storage bucket configuration and policies.",
                "Attachment upload API route and UI integration.",
            ],
            "review_questions": [
                "Are file type and size validations comprehensive?",
                "Do signed URLs provide adequate protection against unauthorized access?",
            ],
        },
        {
            "title": "Audit Logging",
            "area": "db",
            "focus": "Record audit logs for sensitive actions and expose them via an API.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Audit logging best practices", "url": "https://www.owasp.org/index.php/Logging_Cheat_Sheet"},
                {"name": "Event sourcing patterns", "url": "https://martinfowler.com/eaaDev/EventSourcing.html"},
            ],
            "build": [
                "Create triggers or service logic to insert audit entries on sensitive events (e.g., role changes, deletions).",
                "Define an `audit_logs` table capturing action type, actor, timestamp, target, and metadata.",
                "Implement an API endpoint to query audit logs with filters (e.g., by org, user, date).",
                "Ensure audit logs are immutable (no updates or deletes).",
            ],
            "assignments": [
                "Commit audit logging logic and API endpoints.",
                "Add tests verifying logs are written and retrieved correctly.",
            ],
            "dod": [
                "Audit entries created on sensitive actions.",
                "Logs can be queried and filtered via API.",
                "No way to modify or delete audit logs.",
            ],
            "commit_msg": "feat(audit): implement audit logging for sensitive actions",
            "outcome": [
                "`audit_logs` table and triggers/service logic.",
                "Audit API route.",
            ],
            "review_questions": [
                "Which actions are considered sensitive and logged?",
                "How is audit data secured and protected from tampering?",
            ],
        },
        {
            "title": "System Design Checkpoint #2",
            "area": "system-design",
            "focus": "Reflect on database design and RLS policies, and plan next steps.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Design review template", "url": "https://docs.microsoft.com/en-us/learn/modules/design-review/"},
                {"name": "Software architecture documentation", "url": "https://docs.arc42.org/"},
            ],
            "build": [
                "Summarize the schema design and RLS policy decisions made this week.",
                "Create an updated ER diagram reflecting changes (e.g., attachments, audit logs).",
                "Identify open questions around scalability, migrations, or future data features.",
            ],
            "assignments": [
                "Commit an updated `docs/schema.md` with new diagrams and notes.",
                "Write reflection in `notes/day-28.md` about lessons learned and upcoming challenges.",
            ],
            "dod": [
                "Updated design docs committed.",
                "Reflection note added.",
                "Open questions recorded for future sprints.",
            ],
            "commit_msg": "docs(design): update schema docs and reflect on RLS and audit logging",
            "outcome": [
                "Updated `docs/schema.md` with new diagrams.",
                "Reflection note in `notes/day-28.md`.",
            ],
            "review_questions": [
                "Are there any assumptions that need validation (e.g., data volume)?",
                "What trade-offs were made and are they still valid?",
            ],
        },
        {
            "title": "Queue Setup",
            "area": "performance",
            "focus": "Introduce background job processing using BullMQ and Redis.",
            "timebox": "~3 hours",
            "study": [
                {"name": "BullMQ documentation", "url": "https://docs.bullmq.io/"},
                {"name": "Redis Quickstart", "url": "https://redis.io/docs/getting-started/"},
            ],
            "build": [
                "Install and configure Redis locally (via Docker) and set up BullMQ queues.",
                "Create workers for notification emails, digest generation, and audit log enrichment.",
                "Implement retry and backoff strategies; configure a dead-letter queue for failed jobs.",
                "Add idempotency keys to jobs to avoid duplicate processing.",
            ],
            "assignments": [
                "Commit queue configuration and worker implementations.",
                "Document queue conventions and job lifecycle in `docs/queues.md`.",
            ],
            "dod": [
                "Jobs run successfully and produce expected side effects.",
                "Failed jobs are retried with exponential backoff and moved to dead-letter queue after max retries.",
                "Idempotency keys prevent duplicate processing.",
            ],
            "commit_msg": "feat(queue): configure BullMQ with workers, retries, and idempotency",
            "outcome": [
                "Redis and BullMQ configuration files.",
                "Worker scripts for notifications and audits.",
            ],
            "review_questions": [
                "Are job retries and backoff strategies appropriate for each job type?",
                "How are failed jobs monitored and recovered?",
            ],
        },
        {
            "title": "Caching",
            "area": "performance",
            "focus": "Implement server-side caching for expensive read queries.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Redis caching best practices", "url": "https://redis.io/docs/manual/keyspace-events/"},
                {"name": "Cache invalidation strategies", "url": "https://martinfowler.com/articles/cache-invalidation.html"},
            ],
            "build": [
                "Add a caching layer for heavy list queries (e.g., tasks per org) using Redis.",
                "Define cache keys and TTL; implement read-through caching where the first request populates the cache.",
                "Implement invalidation rules on writes (create, update, delete) to ensure stale data isn’t served.",
                "Document caching boundaries and where caching should not be used (e.g., user-specific data).",
            ],
            "assignments": [
                "Commit caching implementation and invalidation logic.",
                "Write an ADR describing caching trade-offs and invalidation strategy.",
            ],
            "dod": [
                "Cache hits improve response times significantly.",
                "Invalidation logic ensures data consistency.",
                "ADR committed in `/docs/adrs`.",
            ],
            "commit_msg": "feat(cache): implement Redis caching with invalidation and document strategy",
            "outcome": [
                "Caching layer integrated with API.",
                "ADR detailing caching decisions.",
            ],
            "review_questions": [
                "How do we avoid cache stampedes when keys expire?",
                "Is TTL configured to balance performance and freshness?",
            ],
        },
        {
            "title": "Structured Logging & Monitoring",
            "area": "performance",
            "focus": "Add structured logs, error tracking, and health endpoints for observability.",
            "timebox": "~3 hours",
            "study": [
                {"name": "pino logging library", "url": "https://getpino.io/"},
                {"name": "Sentry for Node", "url": "https://docs.sentry.io/platforms/node/"},
            ],
            "build": [
                "Integrate a structured logging library such as Pino; include traceId, userId, orgId in each log entry.",
                "Set up Sentry (or similar) for error tracking and performance monitoring; instrument API and front‑end.",
                "Add health and readiness endpoints to the API; include checks for database, cache, and queue connections.",
                "Create dashboards and alert rules for error rates and latency thresholds.",
            ],
            "assignments": [
                "Commit logging and error tracking setup.",
                "Document how to interpret logs and use dashboards in `observability.md`.",
            ],
            "dod": [
                "Structured logs written for each request with proper context.",
                "Errors captured by Sentry with stack traces.",
                "Health endpoints return appropriate status codes and details.",
            ],
            "commit_msg": "feat(obs): implement structured logging, error tracking, and health endpoints",
            "outcome": [
                "Logger configuration and middleware.",
                "Sentry integration and DSN configuration.",
                "Observability documentation.",
            ],
            "review_questions": [
                "Can we trace a request across multiple services using the logs?",
                "Are alert thresholds set to detect problems early without false positives?",
            ],
        },
        {
            "title": "Rate Limiting & Security Hardening",
            "area": "security",
            "focus": "Protect the application from abuse and improve overall security posture.",
            "timebox": "~3 hours",
            "study": [
                {"name": "express-rate-limit documentation", "url": "https://www.npmjs.com/package/express-rate-limit"},
                {"name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"},
                {"name": "CORS and Helmet", "url": "https://expressjs.com/en/resources/middleware/cors.html"},
            ],
            "build": [
                "Add rate-limiting middleware to protect against brute force and scraping attacks; scope limits by IP and user ID.",
                "Enable Helmet middleware to set security-related HTTP headers.",
                "Review and restrict CORS policies to allowed origins only.",
                "Review secrets management and environmental variables (ensure no secrets committed).",
            ],
            "assignments": [
                "Commit security middleware and configuration.",
                "Perform a security audit and document findings in `SECURITY_AUDIT.md`.",
            ],
            "dod": [
                "Rate limits trigger 429 responses when thresholds exceeded.",
                "Security headers added by Helmet appear in responses.",
                "CORS only allows trusted origins.",
            ],
            "commit_msg": "feat(security): add rate limiting and security headers; audit secrets",
            "outcome": [
                "Rate limiting and security middleware in API code.",
                "Security audit document with identified risks and mitigations.",
            ],
            "review_questions": [
                "Are the rate limits appropriate for both anonymous and authenticated users?",
                "Have all secrets been removed from the codebase and secured via environment variables?",
            ],
        },
        {
            "title": "Load Testing",
            "area": "performance",
            "focus": "Benchmark and identify performance bottlenecks under load.",
            "timebox": "~3 hours",
            "study": [
                {"name": "k6 load testing tool", "url": "https://k6.io/docs/"},
                {"name": "Interpreting performance metrics", "url": "https://docs.k6.io/docs/test-analysis"},
            ],
            "build": [
                "Write k6 scripts to simulate realistic traffic on key endpoints (e.g., list tasks, create task).",
                "Run load tests locally and record metrics such as p95 latency, throughput, and error rate.",
                "Identify performance bottlenecks and propose optimizations.",
                "Document results and recommended changes in `docs/load-testing.md`.",
            ],
            "assignments": [
                "Commit load testing scripts and results documentation.",
                "Implement at least one performance improvement based on findings.",
            ],
            "dod": [
                "Load testing script runs successfully.",
                "Report includes baseline metrics and analysis.",
                "Identified improvements documented and at least one implemented.",
            ],
            "commit_msg": "perf(test): add k6 load tests and address key bottlenecks",
            "outcome": [
                "`tests/load/` directory with k6 scripts.",
                "`docs/load-testing.md` summarizing results and improvements.",
            ],
            "review_questions": [
                "Which endpoints experience the highest latency under load?",
                "Are the improvements validated by a second test run?",
            ],
        },
        {
            "title": "Review & Testing Day #3",
            "area": "testing",
            "focus": "Address technical debt, expand coverage, and stabilize the codebase.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Testing strategies overview", "url": "https://martinfowler.com/articles/practical-test-pyramid.html"},
                {"name": "Refactoring best practices", "url": "https://refactoring.com/"},
            ],
            "build": [
                "Review and refactor modules based on load testing feedback (e.g., DB queries, caching).",
                "Extend unit tests and integration tests to cover recent features (audit logs, attachments).",
                "Record lessons learned and plan improvements.",
            ],
            "assignments": [
                "Commit refactor changes and new tests.",
                "Write reflection in `notes/day-34.md` about the impact of load testing.",
            ],
            "dod": [
                "Tests pass consistently after refactor.",
                "Reflections capture what went well and what needs attention.",
                "All major modules reviewed for potential improvements.",
            ],
            "commit_msg": "chore(refactor): address load testing feedback and expand test coverage",
            "outcome": [
                "Refactored modules with performance improvements.",
                "Expanded test suite.",
                "Reflection note in `/notes/day-34.md`.",
            ],
            "review_questions": [
                "Did the refactor simplify code and improve performance?",
                "What unresolved performance issues remain?",
            ],
        },
        {
            "title": "MongoDB Decision & Setup",
            "area": "db",
            "focus": "Decide on and set up a MongoDB module for activity feeds or analytics.",
            "timebox": "~3 hours",
            "study": [
                {"name": "MongoDB Atlas documentation", "url": "https://www.mongodb.com/docs/atlas/"},
                {"name": "Bucket pattern for time series", "url": "https://www.mongodb.com/presentations/data-modeling-time-series-event-bucket-pattern"},
            ],
            "build": [
                "Evaluate use cases for MongoDB (activity feed vs analytics) and decide which to implement.",
                "Set up a connection to MongoDB (e.g., using Mongoose or the native driver).",
                "Define schemas for the chosen use case (e.g., event buckets or aggregated metrics).",
                "Plan indexing strategy for efficient queries.",
            ],
            "assignments": [
                "Commit MongoDB configuration and schema definitions.",
                "Write an ADR explaining why MongoDB was chosen for this feature.",
            ],
            "dod": [
                "Connection to MongoDB established.",
                "Schemas defined for selected use case.",
                "ADR capturing decision and trade-offs created.",
            ],
            "commit_msg": "feat(mongo): decide on use case and set up MongoDB with schemas",
            "outcome": [
                "Mongo configuration files and models.",
                "ADR in `/docs/adrs` for MongoDB decision.",
            ],
            "review_questions": [
                "Why is MongoDB a better fit than Postgres for this feature?",
                "What potential challenges might arise with the chosen use case?",
            ],
        },
        {
            "title": "MongoDB Implementation",
            "area": "db",
            "focus": "Implement the chosen MongoDB feature and expose it via the API.",
            "timebox": "~3 hours",
            "study": [
                {"name": "MongoDB Node.js driver", "url": "https://www.mongodb.com/docs/drivers/node/current/"},
                {"name": "Aggregation pipeline best practices", "url": "https://www.mongodb.com/docs/manual/aggregation/"},
            ],
            "build": [
                "Implement backend logic for the chosen feature (activity feed or analytics) using MongoDB queries and aggregation.",
                "Create API routes to expose the feature (e.g., `/activity-feed` or `/analytics`).",
                "Add pagination and filtering to the API to handle large data sets.",
                "Test performance of the queries and ensure proper indexes are used.",
            ],
            "assignments": [
                "Commit the MongoDB feature implementation and API routes.",
                "Write tests covering data retrieval and performance.",
            ],
            "dod": [
                "API returns correct data from MongoDB.",
                "Indexes effectively support queries (checked via explain plans).",
                "Tests verify correct functionality and acceptable performance.",
            ],
            "commit_msg": "feat(mongo): implement selected feature and expose via API",
            "outcome": [
                "MongoDB models and service functions.",
                "New API endpoints for activity feed or analytics.",
            ],
            "review_questions": [
                "Are query patterns optimized with proper indexing?",
                "Does the API provide necessary filtering and pagination?",
            ],
        },
        {
            "title": "Firebase Decision & Setup",
            "area": "db",
            "focus": "Decide on using Firebase for push notifications or Firestore security demo and set it up.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Firebase Cloud Messaging (FCM) docs", "url": "https://firebase.google.com/docs/cloud-messaging"},
                {"name": "Firestore security rules", "url": "https://firebase.google.com/docs/firestore/security/rules"},
            ],
            "build": [
                "Evaluate whether to implement push notifications (FCM) or Firestore security rules demonstration.",
                "Create a Firebase project and configure necessary services (FCM or Firestore).",
                "Store credentials securely in environment variables.",
                "Write an ADR capturing the decision and reasoning.",
            ],
            "assignments": [
                "Commit Firebase configuration and credentials (secured).",
                "Add ADR explaining the decision.",
            ],
            "dod": [
                "Firebase project set up correctly.",
                "Credentials stored securely and not checked into source control.",
                "ADR committed with clear decision and alternatives.",
            ],
            "commit_msg": "feat(firebase): evaluate and set up FCM/Firestore with ADR",
            "outcome": [
                "Firebase config files.",
                "ADR documenting the decision.",
            ],
            "review_questions": [
                "What value does Firebase add compared to existing stack?",
                "How are costs and complexity weighed?",
            ],
        },
        {
            "title": "Firebase Implementation",
            "area": "db",
            "focus": "Implement the chosen Firebase feature (push notifications or Firestore rules demo).",
            "timebox": "~3 hours",
            "study": [
                {"name": "Firebase Cloud Messaging integration", "url": "https://firebase.google.com/docs/cloud-messaging/ios/first-message"},
                {"name": "Firestore security rules examples", "url": "https://firebase.google.com/docs/firestore/security/get-started"},
            ],
            "build": [
                "If using FCM: register device tokens, implement server code to send notifications on task events, and update mobile app to handle notifications and deep linking.",
                "If using Firestore rules: implement a simple Firestore integration and write rules enforcing organization and role-based access.",
                "Document cost-aware listener patterns and avoid unnecessary reads.",
            ],
            "assignments": [
                "Commit Firebase feature implementation (notifications or Firestore rules).",
                "Write tests or manual scripts verifying notifications or rules work as intended.",
            ],
            "dod": [
                "Push notifications delivered to the intended recipients or rules prevent unauthorized access.",
                "Security rules enforced according to roles and organization membership.",
                "Listeners minimized and cost considerations documented.",
            ],
            "commit_msg": "feat(firebase): implement selected feature (notifications or rules) and validate",
            "outcome": [
                "Server and mobile code for FCM or Firestore integration.",
                "Documentation covering implementation and cost considerations.",
            ],
            "review_questions": [
                "Do notifications or Firestore reads abide by cost-aware best practices?",
                "Are listeners properly cleaned up in the mobile app?",
            ],
        },
        {
            "title": "Cost & Listener Tuning",
            "area": "performance",
            "focus": "Optimize costs and performance for MongoDB and Firebase modules.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Firebase cost management", "url": "https://firebase.google.com/pricing"},
                {"name": "MongoDB indexing strategies", "url": "https://www.mongodb.com/docs/manual/indexes/"},
            ],
            "build": [
                "Audit MongoDB and Firebase usage for unnecessary queries or listeners.",
                "Optimize indexes and queries to reduce read/write costs.",
                "Implement listener cancellation and batching strategies in Firebase.",
                "Document cost-saving measures and limitations.",
            ],
            "assignments": [
                "Commit performance improvements to MongoDB and Firebase modules.",
                "Add cost awareness guidelines to the README or docs.",
            ],
            "dod": [
                "Reduced number of listeners and lower read/write costs.",
                "Queries leverage proper indexes for efficiency.",
                "Documentation explains how to avoid cost overruns.",
            ],
            "commit_msg": "chore(cost): audit and optimize MongoDB/Firebase usage for cost and performance",
            "outcome": [
                "Improved queries and listener handling.",
                "Cost and performance notes in documentation.",
            ],
            "review_questions": [
                "Are all unnecessary listeners removed or batched?",
                "How do indexing changes impact write throughput?",
            ],
        },
        {
            "title": "System Design Checkpoint #3",
            "area": "system-design",
            "focus": "Update architectural documentation to reflect MongoDB and Firebase additions.",
            "timebox": "~2 hours",
            "study": [
                {"name": "System architecture templates", "url": "https://diagrams.mingrammer.com/"},
                {"name": "Comparing SQL and NoSQL", "url": "https://www.mongodb.com/nosql-explained"},
            ],
            "build": [
                "Update the high-level architecture diagram to include MongoDB and Firebase modules and their interactions with the core system.",
                "Document reasons for choosing each technology (RLS vs NoSQL vs Firebase).",
                "Identify integration points and data flow between components.",
                "Note potential scalability or complexity risks introduced by the new modules.",
            ],
            "assignments": [
                "Commit updated architecture diagram and design notes in `/docs/architecture.md`.",
                "Write reflection in `notes/day-40.md` on integration challenges and benefits.",
            ],
            "dod": [
                "Diagram reflects current system topology accurately.",
                "Design notes clearly articulate trade-offs and rationale.",
                "Reflection captures integration lessons.",
            ],
            "commit_msg": "docs(architecture): update system design with MongoDB and Firebase modules",
            "outcome": [
                "Updated architecture diagram and doc.",
                "Reflection note in `/notes/day-40.md`.",
            ],
            "review_questions": [
                "Does the updated design highlight new dependencies clearly?",
                "Are there alternative approaches that could simplify the system?",
            ],
        },
        {
            "title": "Expo Setup & Navigation",
            "area": "mobile",
            "focus": "Initialize the React Native client and basic navigation for the mobile app.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Expo documentation", "url": "https://docs.expo.dev/"},
                {"name": "React Navigation", "url": "https://reactnavigation.org/docs/getting-started"},
            ],
            "build": [
                "Initialize an Expo project with TypeScript support.",
                "Set up React Navigation (stack and tab navigators).",
                "Implement login and home screens with basic navigation flows.",
                "Persist authentication tokens securely using `expo-secure-store` or `react-native-keychain`.",
            ],
            "assignments": [
                "Commit the Expo project setup and navigation implementation.",
                "Update the mobile README with build and run instructions.",
            ],
            "dod": [
                "Mobile app runs on both iOS and Android emulators.",
                "Navigation flows correctly from login to home screen.",
                "Tokens are stored securely.",
            ],
            "commit_msg": "feat(mobile): initialize Expo app and set up navigation with secure storage",
            "outcome": [
                "Expo project under `apps/mobile` or similar directory.",
                "Navigation configuration and screens.",
            ],
            "review_questions": [
                "Does navigation state persist across app reloads?",
                "Are security considerations around token storage addressed?",
            ],
        },
        {
            "title": "Data Sync Setup",
            "area": "mobile",
            "focus": "Set up data synchronization in the mobile client using TanStack Query.",
            "timebox": "~3 hours",
            "study": [
                {"name": "TanStack Query for React Native", "url": "https://tanstack.com/query/v4/docs/react/react-native"},
                {"name": "React Native networking overview", "url": "https://reactnative.dev/docs/network"},
            ],
            "build": [
                "Integrate TanStack Query into the Expo project; share API client code with the web app.",
                "Fetch projects and tasks from the API and display them in lists.",
                "Implement error and loading states appropriate for mobile.",
                "Ensure caching policies (stale time, refetch) are suitable for mobile connectivity.",
            ],
            "assignments": [
                "Commit data sync implementation and update mobile UI.",
                "Write documentation on how mobile data sync works and share it between platforms.",
            ],
            "dod": [
                "Data loads correctly with caching enabled.",
                "UI handles offline, loading, and error states gracefully.",
                "Shared types and API client code reused between web and mobile.",
            ],
            "commit_msg": "feat(mobile): integrate TanStack Query for data sync and display lists",
            "outcome": [
                "Shared API client module integrated in the mobile app.",
                "Mobile UI showing projects and tasks.",
            ],
            "review_questions": [
                "Is the data sync efficient and offline-aware?",
                "Are error states clear to mobile users?",
            ],
        },
        {
            "title": "Offline Queue",
            "area": "mobile",
            "focus": "Enable offline write capability in the mobile app using a queue with idempotency.",
            "timebox": "~3 hours",
            "study": [
                {"name": "MMKV storage documentation", "url": "https://github.com/mrousavy/react-native-mmkv"},
                {"name": "Offline-first apps guidance", "url": "https://developer.android.com/topic/performance/vitals/offline"},
            ],
            "build": [
                "Implement a local queue that stores create/update operations when offline.",
                "Persist queue entries using a fast key-value store (MMKV or AsyncStorage).",
                "Send queued operations when the device reconnects; use idempotency keys to avoid duplicates.",
                "Display sync status and conflict indicators to the user.",
            ],
            "assignments": [
                "Commit offline queue logic and UI feedback.",
                "Write tests or manual scripts simulating offline/online transitions.",
            ],
            "dod": [
                "Offline actions are queued and persisted across app restarts.",
                "Operations sync correctly when back online with no duplicates.",
                "UI indicates pending and synced items.",
            ],
            "commit_msg": "feat(mobile): implement offline queue with idempotent sync",
            "outcome": [
                "Offline queue module in mobile app.",
                "Indicator UI for offline/synced states.",
            ],
            "review_questions": [
                "How are conflicts between offline and server data resolved?",
                "Does the queue handle failure and retry gracefully?",
            ],
        },
        {
            "title": "Conflict Resolution & Sync",
            "area": "mobile",
            "focus": "Decide and implement a strategy to resolve conflicts between offline and server data.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Conflict resolution strategies", "url": "https://www.mongodb.com/docs/manual/faq/change-streams-conflict-resolution/"},
                {"name": "Offline sync patterns", "url": "https://docs.microsoft.com/en-us/xamarin/essentials/preferences"},
            ],
            "build": [
                "Choose a conflict resolution strategy (server-wins, client-wins, merge).",
                "Implement conflict detection when syncing queued operations.",
                "Handle conflicts in the UI (e.g., show a banner or merge dialog).",
                "Document trade-offs and future improvements in an ADR.",
            ],
            "assignments": [
                "Commit conflict resolution implementation.",
                "Write an ADR in `/docs/adrs` explaining the chosen strategy.",
            ],
            "dod": [
                "Conflicts are detected and resolved according to the chosen strategy.",
                "User feedback is clear when a conflict occurs.",
                "ADR explains reasoning and alternatives considered.",
            ],
            "commit_msg": "feat(sync): implement conflict resolution strategy for offline writes",
            "outcome": [
                "Conflict resolution logic integrated.",
                "ADR capturing conflict strategy.",
            ],
            "review_questions": [
                "Does the strategy balance correctness with user control?",
                "What future improvements could enhance the UX for conflict resolution?",
            ],
        },
        {
            "title": "FlatList Performance",
            "area": "mobile",
            "focus": "Optimize large lists rendering in the mobile app using FlatList tuning.",
            "timebox": "~2 hours",
            "study": [
                {"name": "FlatList performance guide", "url": "https://reactnative.dev/docs/optimizing-flatlist"},
                {"name": "React Native performance overview", "url": "https://reactnative.dev/docs/performance"},
            ],
            "build": [
                "Provide stable `keyExtractor` for list items.",
                "Implement `getItemLayout` where possible to optimize measurement.",
                "Memoize row components using `React.memo` and avoid re-renders.",
                "Tune `initialNumToRender`, `maxToRenderPerBatch`, and window sizes to balance performance and responsiveness.",
            ],
            "assignments": [
                "Commit FlatList optimizations.",
                "Write performance notes detailing measured improvements.",
            ],
            "dod": [
                "Scrolling remains smooth with large data sets.",
                "No noticeable flicker or layout jank.",
                "Performance notes with before/after metrics committed.",
            ],
            "commit_msg": "perf(mobile): optimize FlatList rendering for smooth scrolling",
            "outcome": [
                "Updated mobile list components with optimization props.",
                "Performance report in `/docs/performance-rn.md`.",
            ],
            "review_questions": [
                "How do the tuning parameters impact memory usage?",
                "Are there any trade-offs in delaying initial rendering?",
            ],
        },
        {
            "title": "Push Notifications & Deep Linking",
            "area": "mobile",
            "focus": "Integrate push notifications and support deep linking into specific screens.",
            "timebox": "~3 hours",
            "study": [
                {"name": "React Native Firebase messaging", "url": "https://rnfirebase.io/messaging/usage"},
                {"name": "React Navigation deep linking", "url": "https://reactnavigation.org/docs/deep-linking"},
            ],
            "build": [
                "If using FCM: register device tokens, request permissions, and configure listeners for incoming notifications.",
                "Implement server-side logic to send notifications on relevant events (e.g., task assignment).",
                "Set up deep linking so notifications open the correct screen (e.g., a specific task).",
                "Handle notification lifecycle when the app is foregrounded, backgrounded, or closed.",
            ],
            "assignments": [
                "Commit notification and deep linking implementation.",
                "Test notifications across iOS and Android (emulators or devices).",
            ],
            "dod": [
                "Notifications are delivered and handled correctly.",
                "Deep links navigate to the intended screen without errors.",
                "Permissions are requested and stored appropriately.",
            ],
            "commit_msg": "feat(mobile): integrate push notifications and deep linking",
            "outcome": [
                "Server code sending notifications.",
                "Mobile listeners handling notifications and linking.",
            ],
            "review_questions": [
                "Are notifications handled in all app states?",
                "Is deep linking robust across platform variations (iOS vs Android)?",
            ],
        },
        {
            "title": "Mobile Testing & Review",
            "area": "mobile",
            "focus": "Add tests for mobile components and reflect on the mobile development process.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Detox end-to-end testing", "url": "https://wix.github.io/Detox/docs/getting-started/configuration"},
                {"name": "React Native testing library", "url": "https://testing-library.com/docs/react-native-testing-library/intro/"},
            ],
            "build": [
                "Write unit tests for critical mobile components and hooks.",
                "If possible, set up Detox and write an end-to-end test covering login and basic navigation.",
                "Fix any discovered bugs or performance issues.",
                "Document lessons learned from building the mobile portion.",
            ],
            "assignments": [
                "Commit mobile tests and bug fixes.",
                "Write a reflection in `notes/day-47.md` capturing mobile development challenges and insights.",
            ],
            "dod": [
                "Mobile tests run and pass.",
                "Critical bugs identified and resolved.",
                "Reflection note completed.",
            ],
            "commit_msg": "test(mobile): add unit/e2e tests and reflect on mobile development",
            "outcome": [
                "Tests in `apps/mobile/__tests__/`.",
                "Bug fixes in mobile code.",
                "Reflection note in `/notes/day-47.md`.",
            ],
            "review_questions": [
                "Are the tests covering the most important user flows?",
                "What obstacles did you face during mobile development?",
            ],
        },
        {
            "title": "Review & Testing Day #4",
            "area": "testing",
            "focus": "Consolidate mobile and backend changes; stabilize the codebase.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Cross-platform testing strategies", "url": "https://developer.android.com/training/testing"},
                {"name": "Maintaining large codebases", "url": "https://martinfowler.com/bliki/TechnicalDebtQuadrant.html"},
            ],
            "build": [
                "Review cross-cutting concerns between mobile and backend (e.g., API contracts, error handling).",
                "Ensure test suites remain green after mobile integrations.",
                "Refactor duplicated logic across web and mobile into shared modules.",
            ],
            "assignments": [
                "Commit cross-cutting refactors and test updates.",
                "Update documentation where API contracts changed.",
            ],
            "dod": [
                "Tests remain stable across platforms.",
                "Duplicated code removed and shared modules created.",
                "API documentation reflects current reality.",
            ],
            "commit_msg": "chore(review): harmonize web/mobile code and stabilize tests",
            "outcome": [
                "Refactored shared modules.",
                "Updated API docs.",
            ],
            "review_questions": [
                "Are there any divergent behaviours between web and mobile?",
                "Could additional abstractions reduce duplication?",
            ],
        },
        {
            "title": "Unit & Integration Tests",
            "area": "testing",
            "focus": "Ensure comprehensive test coverage for new features (mobile, MongoDB, Firebase).",
            "timebox": "~3 hours",
            "study": [
                {"name": "Vitest advanced usage", "url": "https://vitest.dev/guide/working-with-vitest.html"},
                {"name": "Integration testing patterns", "url": "https://blog.logrocket.com/guide-integration-testing-node-apps/"},
            ],
            "build": [
                "Add unit tests for MongoDB and Firebase modules (services, helpers).",
                "Expand integration tests to cover new endpoints and cross-service flows.",
                "Ensure tests handle offline and error scenarios appropriately.",
                "Use test containers or mocks for external services when necessary.",
            ],
            "assignments": [
                "Commit new unit and integration tests.",
                "Update test scripts and CI configuration to include new suites.",
            ],
            "dod": [
                "Test coverage for critical paths > 80%.",
                "Tests run reliably in CI without flakiness.",
                "Mocks or test containers handle external dependencies cleanly.",
            ],
            "commit_msg": "test: add unit and integration tests for new modules",
            "outcome": [
                "Expanded test coverage.",
                "CI configuration updated.",
            ],
            "review_questions": [
                "Are external dependencies adequately mocked or containerized?",
                "Do integration tests reflect realistic usage scenarios?",
            ],
        },
        {
            "title": "End-to-End Tests",
            "area": "testing",
            "focus": "Implement end-to-end tests for critical user flows across web and mobile.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Playwright documentation", "url": "https://playwright.dev/docs/intro"},
                {"name": "Cypress best practices", "url": "https://docs.cypress.io/guides/references/best-practices"},
            ],
            "build": [
                "Choose an E2E test framework (Playwright or Cypress) for web and mobile flows.",
                "Write tests covering login, task creation, editing, deletion, offline sync, and notifications.",
                "Ensure selectors are stable and tests are resilient to timing issues.",
                "Integrate E2E tests into the CI pipeline.",
            ],
            "assignments": [
                "Commit E2E test scripts and configuration.",
                "Update CI pipeline to run E2E tests in parallel with unit/integration tests.",
            ],
            "dod": [
                "E2E tests pass consistently across environments.",
                "Critical user flows are fully covered.",
                "E2E tests add value without excessive maintenance.",
            ],
            "commit_msg": "test(e2e): implement end-to-end tests for critical flows",
            "outcome": [
                "E2E test suite in `tests/e2e/`.",
                "CI updated to run E2E tests.",
            ],
            "review_questions": [
                "Do E2E tests catch regressions that unit tests miss?",
                "Are the tests maintainable and not overly brittle?",
            ],
        },
        {
            "title": "CI/CD Enhancements",
            "area": "devops",
            "focus": "Improve the CI pipeline, containerize the application, and set up preview deployments.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Docker documentation", "url": "https://docs.docker.com/get-started/"},
                {"name": "GitHub Actions advanced", "url": "https://docs.github.com/en/actions/using-workflows"},
            ],
            "build": [
                "Create a multi-stage Dockerfile for the API and optionally the web client.",
                "Add docker-compose configuration for local development (DB, cache, queue).",
                "Update GitHub Actions to build Docker images and run tests inside containers.",
                "Configure preview deployments (e.g., Vercel for web, Railway/Fly.io for API).",
            ],
            "assignments": [
                "Commit Dockerfile(s) and docker-compose file.",
                "Update CI workflow to build and push images (if using a registry).",
            ],
            "dod": [
                "Containers build successfully and run locally.",
                "CI pipeline completes within a reasonable time.",
                "Preview deployments work and provide accessible URLs.",
            ],
            "commit_msg": "ci/devops: containerize services and enhance CI with preview deployments",
            "outcome": [
                "Docker and compose files in the repository.",
                "CI updated for container builds and deployments.",
            ],
            "review_questions": [
                "Does containerization simplify local setup?",
                "Are preview deployments stable and reflective of production?",
            ],
        },
        {
            "title": "Review & Testing Day #5",
            "area": "testing",
            "focus": "Perform final testing pass and finalize any outstanding tasks.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Refactoring for testability", "url": "https://martinfowler.com/articles/refactoring-microservice-testability.html"},
                {"name": "Test coverage analysis", "url": "https://jestjs.io/docs/cli#--coverage"},
            ],
            "build": [
                "Review test coverage reports and add tests for uncovered critical paths.",
                "Address any flakiness or intermittent failures in E2E tests.",
                "Perform final refactoring for clarity and maintainability.",
            ],
            "assignments": [
                "Commit additional tests and refactor changes.",
                "Write a reflection in `notes/day-52.md` about overall testing strategy and learnings.",
            ],
            "dod": [
                "Coverage on critical paths > 85%.",
                "All tests pass reliably on CI and locally.",
                "Reflection note completed.",
            ],
            "commit_msg": "test(final): increase coverage and stabilize test suite",
            "outcome": [
                "Coverage reports indicating improvement.",
                "Final round of refactoring integrated.",
                "Reflection note in `/notes/day-52.md`.",
            ],
            "review_questions": [
                "Are there any remaining weak spots in the test pyramid?",
                "What future tests would you add with more time?",
            ],
        },
        {
            "title": "System Design & ADR Writing",
            "area": "system-design",
            "focus": "Consolidate architectural decisions and document them comprehensively.",
            "timebox": "~3 hours",
            "study": [
                {"name": "ADR template (MADR)", "url": "https://adr.github.io/madr/"},
                {"name": "Writing effective system design docs", "url": "https://www.pagerduty.com/blog/engineering-design-docs/"},
            ],
            "build": [
                "Write a full system design document (5–8 pages) covering all components: web, API, database, queue, MongoDB, Firebase, and mobile.",
                "Summarize major decisions made across the project in ADRs (auth strategy, RLS design, caching, offline sync, MongoDB/Firebase usage).",
                "Include diagrams (e.g., sequence, component, deployment) using Mermaid or similar syntax.",
            ],
            "assignments": [
                "Commit `docs/system-design.md` and ADRs into `/docs/adrs`.",
                "Review ADRs for completeness and clarity.",
            ],
            "dod": [
                "System design document explains architecture and trade-offs clearly.",
                "ADRs cover all major decisions with context and alternatives.",
                "Diagrams are readable and reflect the implementation accurately.",
            ],
            "commit_msg": "docs: finalize system design and ADRs",
            "outcome": [
                "Comprehensive system design doc.",
                "ADRs for all key decisions.",
            ],
            "review_questions": [
                "Are there any undocumented decisions that should be captured?",
                "Does the system design doc provide a clear onboarding path for new engineers?",
            ],
        },
        {
            "title": "Refactor & Code Review",
            "area": "system-design",
            "focus": "Improve structure and readability by refactoring and performing thorough code reviews.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Refactoring patterns", "url": "https://refactoring.guru/refactoring/techniques"},
                {"name": "Effective code reviews", "url": "https://mtlynch.io/human-code-reviews-1/"},
            ],
            "build": [
                "Identify modules with high complexity or poor organization and refactor them for clarity.",
                "Use a PR to showcase the refactor and include benchmarks or examples demonstrating improvements.",
                "Create a code review checklist focusing on correctness, performance, security, and readability.",
                "Apply the checklist retroactively to two earlier PRs and fix discovered issues.",
            ],
            "assignments": [
                "Commit refactored code and the review checklist.",
                "Document the refactor rationale and improvements in the PR description or separate doc.",
            ],
            "dod": [
                "Refactor merged without breaking existing functionality.",
                "Review checklist adopted for future code reviews.",
                "Benchmarks show tangible improvements (e.g., reduced complexity or improved performance).",
            ],
            "commit_msg": "refactor: improve module structure and add code review checklist",
            "outcome": [
                "Refactored modules.",
                "Review checklist documented.",
            ],
            "review_questions": [
                "Did the refactor reduce cognitive load for future maintenance?",
                "Were any performance regressions introduced?",
            ],
        },
        {
            "title": "Incident Simulation & Postmortem",
            "area": "devops",
            "focus": "Practice incident response and write a postmortem for a simulated outage.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Incident response guide", "url": "https://sre.google/sre-book/handling-overload/"},
                {"name": "Postmortem templates", "url": "https://www.atlassian.com/incident-management/postmortem"},
            ],
            "build": [
                "Simulate an incident (e.g., database outage, cache failure, queue backlog) by injecting faults in a non-production environment.",
                "Follow runbooks to reproduce, mitigate, and resolve the issue.",
                "Capture timeline, root cause, mitigation steps, and lessons learned.",
                "Write a postmortem including corrective actions and follow-up tasks.",
            ],
            "assignments": [
                "Commit the postmortem to `/docs/postmortems/incident-01.md`.",
                "Update runbooks based on new insights gained.",
            ],
            "dod": [
                "Incident reproduced in a controlled environment.",
                "Postmortem includes clear timeline and root cause analysis.",
                "Follow-up action items identified and scheduled.",
            ],
            "commit_msg": "docs(postmortem): simulate incident and document root cause and mitigations",
            "outcome": [
                "Postmortem document.",
                "Updated runbooks reflecting new procedures.",
            ],
            "review_questions": [
                "How quickly was the incident identified and mitigated?",
                "What preventive measures can reduce recurrence?",
            ],
        },
        {
            "title": "Security Audit",
            "area": "security",
            "focus": "Audit dependencies and configurations for security vulnerabilities and harden the application.",
            "timebox": "~3 hours",
            "study": [
                {"name": "OWASP Dependency Check", "url": "https://owasp.org/www-project-dependency-check/"},
                {"name": "OWASP cheat sheets", "url": "https://cheatsheetseries.owasp.org/"},
            ],
            "build": [
                "Run automated vulnerability scans on dependencies (e.g., npm audit, OWASP Dependency Check).",
                "Identify and update vulnerable packages.",
                "Review and harden security configurations (CSP headers, cookie settings, XSS prevention).",
                "Document findings and mitigation steps in `SECURITY_AUDIT.md`.",
            ],
            "assignments": [
                "Commit updated dependencies and security configurations.",
                "Publish the security audit report.",
            ],
            "dod": [
                "No high or critical vulnerabilities remain unaddressed.",
                "Security best practices (e.g., output encoding【56951667337192†L293-L317】) are applied across the codebase.",
                "Audit report details findings and remediation.",
            ],
            "commit_msg": "security: audit dependencies and strengthen security configurations",
            "outcome": [
                "Updated dependencies (package.json, lockfile).",
                "Improved security headers and settings.",
                "`SECURITY_AUDIT.md` with findings.",
            ],
            "review_questions": [
                "Are any known vulnerabilities still unresolved?",
                "Do all outputs undergo proper encoding and sanitization?",
            ],
        },
        {
            "title": "System Design Checkpoint #4",
            "area": "system-design",
            "focus": "Finalize architecture documentation and prepare the project for presentation.",
            "timebox": "~2 hours",
            "study": [
                {"name": "Design review checklist", "url": "https://github.com/joelparkerhenderson/design-review-checklist"},
                {"name": "Architecture doc examples", "url": "https://engineering.atspotify.com/2020-04-07-the-spotify-squad-health-check/"},
            ],
            "build": [
                "Prepare a final architecture diagram summarizing all components and interactions.",
                "Identify remaining risks and document mitigation strategies.",
                "Ensure all design docs, ADRs, and runbooks are up-to-date.",
            ],
            "assignments": [
                "Commit final architecture diagram and updated docs.",
                "Write a reflection in `notes/day-57.md` summarizing design evolution.",
            ],
            "dod": [
                "Diagram reflects the current implementation accurately.",
                "All relevant docs are up-to-date and consistent.",
                "Reflection note captures personal insights and future considerations.",
            ],
            "commit_msg": "docs(design): finalize architecture and reflect on system design evolution",
            "outcome": [
                "Final architecture diagram and updated documentation.",
                "Reflection note in `/notes/day-57.md`.",
            ],
            "review_questions": [
                "Are there any inconsistencies between docs and the actual implementation?",
                "What design decisions would you revisit given more time?",
            ],
        },
        {
            "title": "Portfolio Packaging: Docs & Video",
            "area": "docs",
            "focus": "Package the project with polished documentation and a demo video.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Writing a great README", "url": "https://www.makeareadme.com/"},
                {"name": "Recording technical demos", "url": "https://www.loom.com/blog/how-to-record-a-great-video-presentation"},
            ],
            "build": [
                "Polish the main README with installation instructions, feature overview, architecture summary, and screenshots.",
                "Write `Architecture.md` with deeper technical explanations and diagrams suitable for recruiters and hiring managers.",
                "Record a 5-minute video walkthrough demonstrating the app’s features (web and mobile) and key technical points.",
                "Compile a cheat sheet summarizing design decisions and interview-ready talking points.",
            ],
            "assignments": [
                "Commit polished README and Architecture.md.",
                "Upload the demo video (or provide a link) and reference it in the README.",
            ],
            "dod": [
                "README provides a clear, professional introduction to the project.",
                "Architecture.md includes diagrams and technical depth.",
                "Demo video is concise and showcases critical features.",
            ],
            "commit_msg": "docs(portfolio): polish README, add architecture doc, and record demo video",
            "outcome": [
                "Updated README and Architecture.md.",
                "Demo video linked in documentation.",
            ],
            "review_questions": [
                "Is the documentation easy to follow for someone new to the project?",
                "Does the video clearly communicate both business and technical value?",
            ],
        },
        {
            "title": "Portfolio Packaging: Deploy & Demo",
            "area": "docs",
            "focus": "Deploy the application and ensure all components are accessible for demonstration.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Vercel deployment docs", "url": "https://vercel.com/docs"},
                {"name": "Railway deployment guide", "url": "https://docs.railway.app/deploy/"},
            ],
            "build": [
                "Deploy the web front-end to a platform like Vercel with environment variables configured.",
                "Deploy the API to a cloud service (e.g., Railway, Fly.io) with a separate database instance.",
                "Deploy the mobile app as a preview build (Expo EAS) and generate installation links.",
                "Test the deployed environments thoroughly to ensure features work as expected.",
            ],
            "assignments": [
                "Commit deployment configurations and update documentation with deployment URLs.",
                "Ensure environment variables are secure and documented.",
            ],
            "dod": [
                "Web, API, and mobile deployments are publicly accessible.",
                "Features work end-to-end in the deployed environments.",
                "Deployment instructions documented for future updates.",
            ],
            "commit_msg": "deploy: deploy front-end, API, and mobile app; update docs with links",
            "outcome": [
                "Deployment configuration files.",
                "Updated docs with live URLs and deployment notes.",
            ],
            "review_questions": [
                "Are there any environment differences that could cause issues?",
                "Is the deployment process repeatable and documented?",
            ],
        },
        {
            "title": "Capstone Handoff & Interview Prep",
            "area": "system-design",
            "focus": "Finalize the project, tag a release, and prepare for interviews.",
            "timebox": "~3 hours",
            "study": [
                {"name": "Preparing for technical interviews", "url": "https://interviewing.io/blog/how-to-prepare-for-your-next-interview"},
                {"name": "Writing a great portfolio", "url": "https://towardsdatascience.com/creating-an-impressive-portfolio-that-gets-you-hired-6a4184e5f09d"},
            ],
            "build": [
                "Tag the final release of the project and ensure version numbers are updated.",
                "Collect metrics (test coverage, performance numbers) for portfolio presentation.",
                "Write an interview cheat sheet summarizing the project, key decisions, and trade-offs.",
                "Rehearse a short talk track explaining the project end-to-end (problem, solution, architecture, lessons).",
            ],
            "assignments": [
                "Commit release tag and update CHANGELOG.",
                "Add the cheat sheet to `/docs/interview-pack.md`.",
            ],
            "dod": [
                "Release tag created and repository tidy.",
                "Interview pack contains succinct explanations and Q&A topics.",
                "Personal reflection summarizing the 60-day journey recorded in `notes/day-60.md`.",
            ],
            "commit_msg": "chore: finalize capstone release and prepare interview materials",
            "outcome": [
                "Tag or release in version control.",
                "`docs/interview-pack.md` summarizing project and potential interview topics.",
                "Reflection note in `/notes/day-60.md`.",
            ],
            "review_questions": [
                "What are the proudest achievements of this project?",
                "How would you improve the project with more time or resources?",
            ],
        },
    ]

    # Generate READMEs for each day
    for i, day_data in enumerate(days_data, start=1):
        day_str = f"day-{i:02d}"
        day_dir = days_dir / day_str
        day_dir.mkdir(parents=True, exist_ok=True)
        readme_path = day_dir / "README.md"
        with readme_path.open("w", encoding="utf-8") as f:
            f.write(build_readme(i, day_data))

    # Create empty note placeholders
    for i in range(1, 61):
        note_path = notes_dir / f"day-{i:02d}.md"
        note_path.parent.mkdir(parents=True, exist_ok=True)
        if not note_path.exists():
            note_path.write_text("<!-- Reflection notes for day {:02d} -->\n".format(i), encoding="utf-8")

    # Create placeholder files in templates, resources, and assignments
    (templates_dir / "README.md").write_text(
        "# Templates\n\nThis directory contains reusable templates for issues, pull requests, or documentation.\n\n", encoding="utf-8"
    )
    (resources_dir / "README.md").write_text(
        "# Resources\n\nA curated list of references and learning materials used throughout the 60‑day plan.\n\n", encoding="utf-8"
    )
    (assignments_dir / "README.md").write_text(
        "# Assignments\n\nDetailed project briefs and additional exercises will be placed here.\n\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
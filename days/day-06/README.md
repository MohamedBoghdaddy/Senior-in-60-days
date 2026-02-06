# Day 06 — State Management & Query Setup
![Day](https://img.shields.io/badge/Day-06-blue) ![Area](https://img.shields.io/badge/Area-frontend-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Implement data fetching and caching with TanStack Query and define state ownership.
### Timebox

~3 hours
### Study

- [TanStack Query documentation](https://tanstack.com/query/v4/docs/react/overview)
- [React state management guide](https://react.dev/learn/state-a-complete-guide)
- [useMemo & useCallback hooks](https://react.dev/reference/react)
### Build

1. Install TanStack Query and wrap application with `QueryClientProvider`.
1. Create an API client wrapper for fetch requests.
1. Implement a simple `useQuery` hook for fetching a tasks list from the API (mock endpoint).
1. Define an ADR discussing state ownership (local vs context vs server state).
### Assignments

- Commit query setup and state ownership ADR.
- Ensure tasks list re-renders only when data changes.
### DoD Checklist

- [ ] Queries cache properly with defined `staleTime` and `retry` policies.
- [ ] ADR explains reasoning for state placement.
- [ ] API client wrapper handles base URL and error parsing.
### Commit Message

`feat(state): configure TanStack Query and document state ownership decisions`
### Outcome Artifacts

- Added `QueryClient` provider in the app.
- Created `apiClient.ts` in shared package.
- ADR document in `/docs/adrs`.
### Self‑Review Questions

- Are you using React Query features effectively (cache, refetch)?
- Does the ADR capture trade-offs clearly?

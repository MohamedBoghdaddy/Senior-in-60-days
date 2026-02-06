# Day 11 — Performance Profiling
![Day](https://img.shields.io/badge/Day-11-blue) ![Area](https://img.shields.io/badge/Area-performance-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Diagnose and optimize rendering performance for the tasks list.
### Timebox

~3 hours
### Study

- [React DevTools Profiler](https://react.dev/learn/profile-performance-with-the-devtools-profiler)
- [Optimizing performance in React](https://react.dev/learn/optimizing-performance)
### Build

1. Use React DevTools Profiler to record renders while interacting with the tasks list.
1. Identify components with unnecessary re-renders and memoize them appropriately using `React.memo`, `useMemo`, and `useCallback`.
1. Implement list virtualization using `react-window` for large lists.
1. Write a performance note summarizing before/after results and decisions.
### Assignments

- Commit performance optimizations.
- Add `docs/performance.md` capturing findings and decisions.
### DoD Checklist

- [ ] Measured improvement in render times captured in the note.
- [ ] List virtualization reduces DOM nodes for large data sets.
- [ ] No broken functionality after optimization.
### Commit Message

`perf(list): profile and optimize rendering and add virtualization`
### Outcome Artifacts

- Performance report in `docs/performance.md`.
- Optimized list component using virtualization.
### Self‑Review Questions

- Which components caused the most re-renders and how were they optimized?
- Does virtualization produce any scroll flicker or UI bug?

# Day 45 — FlatList Performance
![Day](https://img.shields.io/badge/Day-45-blue) ![Area](https://img.shields.io/badge/Area-mobile-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Optimize large lists rendering in the mobile app using FlatList tuning.
### Timebox

~2 hours
### Study

- [FlatList performance guide](https://reactnative.dev/docs/optimizing-flatlist)
- [React Native performance overview](https://reactnative.dev/docs/performance)
### Build

1. Provide stable `keyExtractor` for list items.
1. Implement `getItemLayout` where possible to optimize measurement.
1. Memoize row components using `React.memo` and avoid re-renders.
1. Tune `initialNumToRender`, `maxToRenderPerBatch`, and window sizes to balance performance and responsiveness.
### Assignments

- Commit FlatList optimizations.
- Write performance notes detailing measured improvements.
### DoD Checklist

- [ ] Scrolling remains smooth with large data sets.
- [ ] No noticeable flicker or layout jank.
- [ ] Performance notes with before/after metrics committed.
### Commit Message

`perf(mobile): optimize FlatList rendering for smooth scrolling`
### Outcome Artifacts

- Updated mobile list components with optimization props.
- Performance report in `/docs/performance-rn.md`.
### Self‑Review Questions

- How do the tuning parameters impact memory usage?
- Are there any trade-offs in delaying initial rendering?

# Day 33 — Load Testing
![Day](https://img.shields.io/badge/Day-33-blue) ![Area](https://img.shields.io/badge/Area-performance-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Benchmark and identify performance bottlenecks under load.
### Timebox

~3 hours
### Study

- [k6 load testing tool](https://k6.io/docs/)
- [Interpreting performance metrics](https://docs.k6.io/docs/test-analysis)
### Build

1. Write k6 scripts to simulate realistic traffic on key endpoints (e.g., list tasks, create task).
1. Run load tests locally and record metrics such as p95 latency, throughput, and error rate.
1. Identify performance bottlenecks and propose optimizations.
1. Document results and recommended changes in `docs/load-testing.md`.
### Assignments

- Commit load testing scripts and results documentation.
- Implement at least one performance improvement based on findings.
### DoD Checklist

- [ ] Load testing script runs successfully.
- [ ] Report includes baseline metrics and analysis.
- [ ] Identified improvements documented and at least one implemented.
### Commit Message

`perf(test): add k6 load tests and address key bottlenecks`
### Outcome Artifacts

- `tests/load/` directory with k6 scripts.
- `docs/load-testing.md` summarizing results and improvements.
### Self‑Review Questions

- Which endpoints experience the highest latency under load?
- Are the improvements validated by a second test run?

# Bug Log

Every bug you find — in the existing system, in your code, during Break Days — gets an entry here.
This is your debugging history. It is evidence that you think in production terms.

**Rule:** Log the bug before you fix it. If you fix it without logging it, the learning is lost.

---

## Log format

```markdown
## Bug #XXX — [Short title]

- **Date:** YYYY-MM-DD
- **Found during:** [Day N / Break Day / Normal development / Code Review]
- **Component:** [backend / dotnet / k8s / docker-compose / sql / redis / etc.]
- **File(s):** [path]

### Symptom
[What you observed. Not the cause — what you saw from the outside.]

### Root cause
[What actually caused this. Be specific.]

### Impact
[Who/what would this affect in production? Data loss? Downtime? Silent error?]

### Fix
[What you changed. Link to the commit or file if applicable.]

### How to detect earlier
[What test, log, alert, or code review check would have caught this sooner?]

### Category
[ ] Logic error  [ ] Async/timing issue  [ ] Null/undefined  [ ] Missing validation
[ ] Security gap  [ ] Performance issue  [ ] Config error  [ ] Dependency failure
[ ] Race condition  [ ] Type error  [ ] Missing error handling  [ ] Deployment issue
```

---

## Bugs found

<!-- Add entries below. Most recent at the top. -->

---

## Bug pattern analysis (fill in at each phase review)

At the end of each phase, look at all bugs and answer:

**Phase 1 (Day 30) — What categories dominated?**

**Phase 2 (Day 60) — What categories dominated?**

**Phase 3 (Day 90) — What categories dominated?**

**What does the pattern tell me about my blind spots?**

**What would I add to my code review checklist based on these bugs?**

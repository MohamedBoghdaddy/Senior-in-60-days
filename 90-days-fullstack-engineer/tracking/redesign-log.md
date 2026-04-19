# Redesign Log

Every time you go back and change something you already built, log it here.
This is your engineering judgment history.

The ability to look at your own work critically and improve it is what separates engineers who grow from engineers who plateau.

**Rule:** Before you change something, write the "before" entry. After you change it, write the "after" and "why."

---

## Log format

```markdown
## Redesign #XXX — [Component name] — Week XX (Day N)

- **Date:** YYYY-MM-DD
- **Originally built:** Day N (Week W)
- **What changed:** [High-level description]
- **Files changed:** [paths]

### Before
[What it looked like. Code snippet or description.]

### After
[What it looks like now. Code snippet or description.]

### Why I changed it
[What did you learn between Day N and now that made this change obvious?
Be honest — was the original design wrong, or just not yet complete?]

### What I needed to know to build it right the first time
[This is the real lesson. One paragraph. This is what experience builds.]

### Tradeoff accepted
[What did this change cost? More lines of code? More complexity? Slower build time?
Every redesign has a cost. Name it.]

### What I would NOT change
[What did you get right the first time that you kept?
Acknowledging what worked is as important as acknowledging what didn't.]
```

---

## Redesigns

### Scheduled redesigns (from SCHEDULE-OVERLAY.md)

| Day | What to redesign | Status |
|-----|-----------------|--------|
| 14 | E-commerce schema (Day 8) — after transactions and indexes | |
| 28 | Node.js error handling (Day 6) — after 4 weeks of building | |
| 42 | CleanShop domain model (Day 33) — after auth and CRUD | |
| 55 | Node.js auth (Day 17) — after .NET auth and security audit | |
| 67 | docker-compose (Day 62) — after networking and security | |
| 74 | K8s manifests (Day 69) — after HPA, Secrets, Ingress | |
| 81 | Logging stack (Day 75) — after tracing and CI/CD | |
| 85 | Health/metrics endpoint (Day 26) — after Prometheus and tracing | |

<!-- Add log entries below when completing each redesign -->

---

## Unscheduled redesigns

<!-- Sometimes you see something that needs fixing outside the scheduled days. Log those here too. -->

---

## Redesign pattern analysis (fill in at each phase review)

**What component has been redesigned the most?**

**What does that tell me about where I build too fast without thinking?**

**What component stayed stable across all redesigns?**

**What does that tell me about where I think carefully upfront?**

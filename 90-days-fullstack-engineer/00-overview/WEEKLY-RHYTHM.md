# Weekly Rhythm

Every week of the 90-day plan has the same four discipline slots.
These are non-negotiable regardless of which week you are in.
They apply to any user following this plan.

Read [CORE-SYSTEM-RULE.md](../03-fullstack-system/CORE-SYSTEM-RULE.md) first.
See [SCHEDULE-OVERLAY.md](SCHEDULE-OVERLAY.md) to find which specific day each slot lands on.

---

## Discipline 1: BREAK THE SYSTEM day
**Frequency:** Once per week
**Duration:** Full day (3–4 hours)

### What it is

You deliberately break the system you have been building.
Then you fix it and write an incident report.

This is not optional. This is how senior engineers are made.
The best time to learn incident response is when the stakes are low and the failure is yours.

### What to break (rotate through these)

| Category | What to do |
|----------|-----------|
| API failure | Kill the backend process mid-request. Observe what the frontend does. |
| Database disconnection | Stop the Postgres container. Watch how the backend behaves. Does it crash or degrade? |
| Endpoint overload | Hit an endpoint with 1000 concurrent requests using `k6` or `ab`. What breaks first? |
| Memory pressure | Run the Node.js backend with `--max-old-space-size=64`. Does it OOM? When? |
| Dependency failure | Set the Redis URL to a wrong address. Does the backend start? Does it serve requests? |
| Bad deployment | Deploy a version with an intentional bug (wrong env var, broken SQL query). Find it. |
| Data corruption | Insert malformed data into the database directly. Does the API handle it gracefully? |
| Queue failure | Kill Redis while BullMQ has queued jobs. What happens to those jobs? |
| Auth failure | Expire all JWT secrets (change the secret). What does the frontend see? |
| Network partition | Add a firewall rule blocking backend → Postgres (using `iptables` or `docker network disconnect`). |

### Required output

For each Break Day, produce an entry in `05-production-thinking/incidents/` named `break-day-WXX.md`:

```markdown
## Break Day — Week XX — [Date]

### What I broke
[What component, what action]

### How I detected it
[Alert? 500 errors? Frontend behavior? Manual observation?]

### Timeline
- HH:MM - Introduced the failure
- HH:MM - First visible symptom
- HH:MM - Identified root cause
- HH:MM - Recovered

### Root cause
[Why did this happen?]

### How the system behaved
[Did it fail gracefully or catastrophically? What logged? What didn't?]

### What I fixed
[Code change, config change, or runbook addition]

### What I would add to prevent this in production
[Specific: what alert, what probe, what fallback]

### Senior insight
[One paragraph: what does this break day teach about production systems?]
```

---

## Discipline 2: REDESIGN day
**Frequency:** Every 2 weeks (on the even-week boundary)
**Duration:** 2–3 hours of the day + 1 hour writing

### What it is

You go back to something you built and improve it.
Not refactor for refactoring's sake.
You improve it because you have learned something since you built it.

This is how engineering judgment develops.
If you have never gone back and said "I would not build this the same way now," you have not learned.

### What to redesign (rotate through these)

| Category | Example |
|----------|---------|
| API structure | Restructure routes, change naming convention, add/remove versioning |
| Database schema | Add a missing index, fix a normalization problem, add a constraint |
| Error handling | Upgrade error hierarchy, improve error messages, fix status code mapping |
| Caching strategy | Change TTL, change cache keys, add or remove a cache layer |
| Auth architecture | Improve token rotation, fix a security gap, add refresh token family tracking |
| Queue/job design | Add retry logic, add a dead letter queue, improve job type separation |
| Service boundary | Extract something that grew too large, or merge something that was over-split |
| Testing approach | Add tests that were skipped, fix tests that tested implementation not behavior |
| Logging | Add fields that were missing, fix log levels, add correlation IDs |
| Docker/K8s | Improve resource limits, add health checks, improve startup sequence |

### Required output

For each Redesign Day, add an entry in `tracking/redesign-log.md`:

```markdown
## Redesign — Week XX — [Date]

### What I redesigned
[File(s), component name]

### What it looked like before
[Brief description or code snippet]

### What it looks like after
[Brief description or code snippet]

### Why I changed it
[Specific: what did I learn between when I built it and now that made this change obvious?]

### What I would have needed to know to build it right the first time
[This is the learning. Be honest.]

### Tradeoff I accepted
[What did this redesign cost? Speed? Complexity? Lines of code?]
```

---

## Discipline 3: CODE REVIEW day
**Frequency:** Once per week
**Duration:** 1–2 hours of the day

### What it is

You review your own code (or the existing code in the repo) as if you are a senior engineer reviewing a junior's PR.
You use the code review template and you produce written comments.

This is not "did I write clean code?" This is "what would I say if someone submitted this to me as a PR?"

### How to do it

1. Pick a file or set of files you recently changed or that you will be changing soon.
2. Read it as if you are seeing it for the first time.
3. Use the checklist below.
4. Write your comments as if you are leaving them on a GitHub PR review (file + specific feedback + reason).
5. Fix the top 2 issues you found.

### Code review checklist

**Correctness (must fix):**
- [ ] Does this code do what it is supposed to do?
- [ ] Are edge cases handled (null, empty, overflow, concurrent writes)?
- [ ] Are errors handled and propagated correctly?
- [ ] Are database queries safe (no SQL injection, no missing transactions)?
- [ ] Could this cause data loss?

**Security (must fix):**
- [ ] Is user input validated and sanitized?
- [ ] Are secrets not hardcoded?
- [ ] Is authentication enforced on endpoints that require it?
- [ ] Are error messages safe to expose to clients?

**Reliability (should fix):**
- [ ] Does this fail gracefully when a dependency is down?
- [ ] Is there retry logic for transient failures?
- [ ] Does this produce useful logs?
- [ ] Could this cause a memory leak or resource exhaustion?

**Performance (should check):**
- [ ] Is there an N+1 query hiding here?
- [ ] Is this indexed correctly?
- [ ] Is this result cacheable? Is it currently cached?
- [ ] What happens at 10× current load?

**Maintainability (good to fix):**
- [ ] Are names clear without needing comments to explain them?
- [ ] Is this function/method doing one thing?
- [ ] Are there tests for the non-obvious behavior?
- [ ] Would a new engineer understand this in 5 minutes?

### Required output

Add to your weekly notes file (`notes/week-XX-review.md`) a section:

```markdown
## Code Review this week

**Files reviewed:** [list]
**Reviewer mindset:** "I am a senior engineer reviewing a junior's PR."

### Must-fix findings
1. [File:line] — [Issue] — [Why it matters]
2. ...

### Should-fix findings
1. [File:line] — [Issue]

### What I fixed
- [Description of the 2 fixes applied]

### One thing I got right
- [Something you wrote that you would not change]
```

---

## Discipline 4: SYSTEM THINKING OUTPUT
**Frequency:** Once per week
**Duration:** 1–2 hours of the day

### What it is

Every week, you produce one structured document that demonstrates you are thinking about the system as a whole — not just the feature in front of you.

Senior engineers hold the entire system in their head. They know the failure modes, the bottlenecks, the scaling limits. They write these down. They share them. This discipline builds that habit.

### Output types (rotate, do not repeat the same type two weeks in a row)

| Type | What it is | Where to put it |
|------|-----------|-----------------|
| Architecture diagram | Text-based or drawn: components, connections, data flows | `06-writing-thinking/design-docs/` |
| Scaling plan | "What breaks first at 10× traffic and how to fix it" | `05-production-thinking/scaling/` |
| Tradeoff document | "We chose X over Y. Here is why, and here is what we accepted." | `06-writing-thinking/tradeoffs/` |
| Performance analysis | "This query takes Xms. Here is why. Here is the fix." | `06-writing-thinking/design-docs/` |
| Security threat model | "These are the 5 ways this system can be attacked and what we do about each." | `06-writing-thinking/design-docs/` |
| Failure mode analysis | "What happens when each component fails. Does the system degrade or crash?" | `05-production-thinking/` |

### Minimum quality bar

A System Thinking Output must:
- Be specific to the real system (not generic)
- Reference real file paths, real queries, real components
- Include at least one "and here is what I would change" conclusion
- Be something you could send to a technical interviewer as evidence

A System Thinking Output does NOT need to be long.
400–700 words is enough. Clear thinking beats word count.

---

## Weekly schedule template

Here is how a typical week maps to the four disciplines.
Exact day assignments are in [SCHEDULE-OVERLAY.md](SCHEDULE-OVERLAY.md).

```
Day 1 of week: Regular learning + build day
Day 2 of week: Regular learning + build day
Day 3 of week: Regular learning + build day  + CODE REVIEW (1h block)
Day 4 of week: Regular learning + build day  + SYSTEM THINKING OUTPUT (1.5h block)
Day 5 of week: Regular learning + build day
Day 6 of week: BREAK THE SYSTEM day (full day)
Day 7 of week: Regular learning + REDESIGN (every 2 weeks) or review/consolidation
```

This means most days are still "regular days" — the disciplines are additions, not replacements.
A Break Day is a full replacement. A Redesign Day adds ~2h to a regular day.
Code Review and System Thinking Output are blocks added to regular days.

---

## What happens if you skip a discipline

| Skipped discipline | What you lose |
|-------------------|---------------|
| BREAK THE SYSTEM | You will meet this failure in production instead. It will be worse there. |
| REDESIGN | You will build on a weak foundation and not notice. Technical debt accumulates silently. |
| CODE REVIEW | Your code quality standard stays frozen at "it works." |
| SYSTEM THINKING OUTPUT | You will understand your components but not your system. Interviewers notice. |

Missing one in a week is recoverable. Missing three or more in a phase means you are not following the plan.

# Getting Started

This guide is for anyone picking up this repo for the first time.
Follow these steps before Day 1. Do not skip them.

---

## Who this plan is for

This plan is NOT for beginners starting from zero.

It is for engineers who:
- Can already build APIs and full-stack applications
- Have at least 1 year of professional or project experience
- Want to move from junior/mid execution toward senior-level thinking
- Are weak in: consistency, production depth, system design, testing, DevOps

If you are a complete beginner, this plan will feel overwhelming. Start with Node.js fundamentals first, then return.

---

## What this plan builds

Over 90 days you will evolve ONE system — the multi-service platform in `03-fullstack-system/`:

- A Node.js API with auth, caching, queues, and production patterns
- A FastAPI AI microservice
- A React frontend
- A PostgreSQL + MongoDB + Redis data layer
- A .NET Clean Architecture service (added in Phase 2)
- Docker + Kubernetes infrastructure
- CI/CD pipeline
- Observability (Prometheus, Grafana, distributed tracing)

You will also solve 80+ LeetCode problems (Python + C++) and produce 12 system design documents.

---

## Before Day 1: Setup checklist

Complete all of these before you touch the phase plans.

### 1. Fork the repository

Fork this repository to your own GitHub account.
You will be committing evidence every single day. It must be your repo.

### 2. Start the system

```bash
cd 90-days-fullstack-engineer/03-fullstack-system/infra
docker-compose up
```

Check these pass:
```bash
curl http://localhost:5000/health   # should return {"status":"ok"}
curl http://localhost:8000/health   # AI service health
open http://localhost:3000          # frontend
```

If something is broken, fix it. Document what you fixed in `notes/day-00-setup.md`.
A broken system before Day 1 means you will skip setup problems and never learn infrastructure.

### 3. Read these 4 files — in order

1. [CORE-SYSTEM-RULE.md](90-days-fullstack-engineer/03-fullstack-system/CORE-SYSTEM-RULE.md) — the most important rule
2. [WEEKLY-RHYTHM.md](90-days-fullstack-engineer/00-overview/WEEKLY-RHYTHM.md) — the 4 weekly disciplines
3. [roadmap.md](90-days-fullstack-engineer/00-overview/roadmap.md) — 3-phase overview
4. [SCHEDULE-OVERLAY.md](90-days-fullstack-engineer/00-overview/SCHEDULE-OVERLAY.md) — which day is which type

### 4. Set up your tracking files

Open and fill in the baseline sections:
- [tracking/habit-tracker.md](90-days-fullstack-engineer/tracking/habit-tracker.md) — write today's date as Day 1
- [tracking/senior-behavior-checklist.md](90-days-fullstack-engineer/tracking/senior-behavior-checklist.md) — score yourself now (Day 0 column)
- [00-overview/baseline.md](90-days-fullstack-engineer/00-overview/baseline.md) — add your own honest self-assessment

### 5. Install required tools

Make sure these are installed before Day 1:

| Tool | Purpose | Version |
|------|---------|---------|
| Node.js | Run backend | 20 LTS |
| Python | LeetCode + AI service | 3.11+ |
| .NET SDK | Phase 2 | 8.0 |
| Docker Desktop | Containers | Latest |
| minikube or k3s | Phase 3 K8s | Latest |
| VS Code | Editor + debugger | Latest |
| kubectl | K8s CLI | Matches cluster version |
| k6 or wrk | Load testing (Break Days) | Latest |
| Postman or Insomnia | API testing | Latest |

### 6. Configure your note template

Every day you will fill in `notes/day-XX.md`. The template is already there.
Your first task on Day 1 is to fill in `notes/day-01.md` at the end of the day.

If you end a day and the note is empty, you have not finished the day.

---

## Daily rhythm

A typical day (2–4 hours):

```
[0:00] Open the phase plan for today's day number
[0:05] Read the full day entry (objective, study, build, LeetCode, reflection)
[0:10] Start study resource (max 50% of your time)
[1:00] Start build task — modify the real system
[2:30] LeetCode (45 min) — follow SOLUTIONS-README.md format
[3:15] Write notes/day-XX.md — do not skip this
[3:30] Commit everything: git add . && git commit -m "day-XX: [what you did]"
```

On **Break Days**: replace build task with the failure scenario. Still do LeetCode. Still write notes.
On **Redesign Days**: add 1.5–2h to the build block. The redesign is in addition to the normal day.
On **weekly review days**: fill in `notes/week-XX-review.md` using the template.

---

## How to use the phase plans

Each phase has a detailed day-by-day file:
- [Phase 1 (Days 1–30)](90-days-fullstack-engineer/00-overview/phase-1-days-01-30.md)
- [Phase 2 (Days 31–60)](90-days-fullstack-engineer/00-overview/phase-2-days-31-60.md)
- [Phase 3 (Days 61–90)](90-days-fullstack-engineer/00-overview/phase-3-days-61-90.md)

Each day entry has:
- **Objective** — what you are trying to understand or build
- **Study** — what to read/watch (time-boxed)
- **Build task** — what to add/change in the real system
- **LeetCode** — which problems, which language
- **Reflection output** — what to write in your notes (often a specific question to answer)
- **Estimated time** — realistic target
- **Why this day matters** — context

The [SCHEDULE-OVERLAY.md](90-days-fullstack-engineer/00-overview/SCHEDULE-OVERLAY.md) tells you what role each day plays (Regular, Break, Redesign, Code Review, System Thinking).

---

## What counts as "done" each day

- [ ] Build task complete and committed to git
- [ ] LeetCode problems written in the correct format (both brute force and optimized)
- [ ] `notes/day-XX.md` is non-empty and answers the reflection question
- [ ] If it was a Break Day: incident report committed to `05-production-thinking/incidents/`
- [ ] If it was a Redesign Day: entry added to `tracking/redesign-log.md`
- [ ] If it was Code Review day: review section added to weekly notes
- [ ] If it was System Thinking Output day: document committed to appropriate folder

---

## The only metric that matters

At the end of 90 days, open `tracking/habit-tracker.md`.
Count the days marked C (committed).

If the number is below 70: the plan was not followed consistently.
If the number is 70–80: solid execution with some gaps.
If the number is above 80: the plan worked.

The content of what was committed matters. But consistency is the prerequisite.
You cannot produce senior-level artifacts without senior-level consistency.

---

## Questions that come up

**"Can I skip a Break Day?"**
No. If you cannot simulate a failure in your own development environment, you will not know how to respond to one in production.

**"Can I adapt a day's objective?"**
Yes, if the system reveals a different problem. Document the change and why. A detour that produced a real artifact is better than a forced task that produced nothing.

**"Can I do days out of order?"**
No. The days are sequential. Each day builds context for the next. Day 5 (debugging) requires Day 1–4 (understanding what you are debugging).

**"What if I fall behind?"**
Skip the LeetCode on catch-up days. Do not skip the build tasks or Break Days. LeetCode can be made up. Production thinking cannot.

**"The system is already built — am I just maintaining it?"**
No. You are taking something that was scaffolded and making it real. The difference between "code that exists" and "a system that works in production" is everything you do in these 90 days.

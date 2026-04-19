# CORE SYSTEM RULE

This rule applies to every user who follows this plan.
Read this before Day 1. Re-read it at the start of every phase.

---

## The rule

**All 90 days of engineering work target ONE system.**

That system is the multi-service platform in this folder (`03-fullstack-system/`).

You do not build isolated mini-projects.
You do not build demo apps for individual concepts and abandon them.
You build one system, and you evolve it continuously for 90 days.

---

## What the system is

The platform is a multi-service backend system with:

| Service | Language | Role |
|---------|----------|------|
| `backend/` | Node.js (Express) | Main API — auth, listings, search, caching |
| `ai-services/` | Python (FastAPI) | AI microservice — enrichment, insights |
| `frontend/` | React | UI shell |
| `infra/` | Docker + K8s | Container definitions, orchestration |

Supporting stores:
- PostgreSQL — relational business data (users, listings, organizations)
- MongoDB — unstructured AI artifacts and documents
- Redis — caching, rate limiting, job queues
- BullMQ — background jobs (ingest, notifications)

---

## How each phase evolves this system

| Phase | What happens to the system |
|-------|---------------------------|
| Phase 1 (Days 1–30) | You study the system deeply. You understand every component. You audit it, critique it, and improve specific pieces (error handling, validation, logging, SQL schemas). |
| Phase 2 (Days 31–60) | You add to the system. .NET service joins the platform. You stress-test architecture decisions. You add tests, metrics, and design docs. |
| Phase 3 (Days 61–90) | You productionize the system. Docker hardens. K8s orchestrates. CI/CD automates. Observability is added. The system goes from "works locally" to "production-ready." |

---

## Rules for new users

If you are picking up this repo for the first time:

1. **Run the system first.** Before Day 1, do this:
   ```bash
   cd 90-days-fullstack-engineer/03-fullstack-system/infra
   docker-compose up
   ```
   Verify backend responds at `http://localhost:5000/health`.
   Verify frontend loads at `http://localhost:3000`.
   If something is broken, fix it before starting. Document what you fixed.

2. **Understand the system before changing it.** Days 1–7 include studying the existing Node.js backend. Do not refactor it before you understand it.

3. **Every build task modifies or extends this system.** If a day asks you to "add rate limiting," you add it to the actual backend in `02-backend-engineering/node/` or `03-fullstack-system/backend/`. Not in a new throwaway folder.

4. **Log every bug you find.** See [bug-log.md](../tracking/bug-log.md). Every real bug you encounter — in the system, in your code, during your breaks — gets an entry. This is your debugging history.

5. **Document every redesign.** See [redesign-log.md](../tracking/redesign-log.md). When you change something you already built, write why. This is your engineering judgment history.

---

## What counts as "the system"

All of these are part of the system:

- `03-fullstack-system/backend/` — Node.js main API
- `03-fullstack-system/ai-services/` — FastAPI AI service
- `03-fullstack-system/frontend/` — React UI
- `03-fullstack-system/infra/` — Docker, K8s, compose
- `02-backend-engineering/node/` — Node.js learning scaffold (feeds into the main backend)
- `02-backend-engineering/dotnet/CleanShop/` — .NET service (added in Phase 2, joins the platform)
- All ADRs, design docs, and architecture notes that describe the system
- All tests that protect the system

These do NOT count as the system:
- Throwaway scripts in notes/ (fine for learning, not the system)
- Isolated Hello World apps
- Code that is never connected to the platform

---

## The 4 weekly disciplines

Every week of all 90 days contains exactly these 4 discipline slots.
See [WEEKLY-RHYTHM.md](../00-overview/WEEKLY-RHYTHM.md) for the full definition.

| Discipline | Frequency | Purpose |
|------------|-----------|---------|
| BREAK THE SYSTEM day | 1× per week | Simulate failure, debug it, write an incident report |
| REDESIGN day | Every 2 weeks | Refactor or rethink something you already built |
| CODE REVIEW day | 1× per week | Review your own or the existing code using the checklist |
| SYSTEM THINKING OUTPUT | 1× per week | Produce one architecture diagram, scaling plan, tradeoff doc, or performance analysis |

---

## The 4 deployment milestones

| Day | Milestone | Definition of done |
|-----|-----------|-------------------|
| 30 | Local full system | `docker-compose up` runs all services, all health checks green |
| 60 | Deployed (basic) | System deployed to a free-tier cloud (Railway, Render, Fly.io) and accessible via URL |
| 75 | Improved deployment | K8s manifests applied to a local cluster with HPA, probes, and secrets |
| 90 | Production-style demo | CI pipeline runs, monitoring configured, runbooks written, system can be demoed |

---

## The failure condition

You have failed the CORE SYSTEM RULE if:
- You build a new "demo" instead of improving the existing system
- Your notes folder has scripts that were never connected to anything
- You skip a Break Day or Redesign Day because you were "not in the mood"
- The system cannot be started from scratch by running `docker-compose up`
- The system has no tests

You have not failed if:
- A day's build task is notes/documentation/design (as long as it's about the real system)
- You adapt a day's objective because the system exposed a different problem (document the change)
- You find a bug on a non-Break Day and log it (good — log it and fix it)

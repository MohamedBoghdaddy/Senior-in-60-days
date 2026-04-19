# Deployment Milestones

There are 4 deployment milestones across the 90 days.
Each one creates real pressure — not just "the code is ready" but "the system actually runs."

Engineers who only build locally never develop the instinct for what breaks in deployment.
These milestones fix that.

---

## Milestone 1: Day 30 — Local Full System

**Definition of done:** Running `docker-compose up` from a clean clone starts the entire system.
All services must pass their health checks. No manual steps beyond `docker-compose up`.

### Checklist

- [ ] `cd 90-days-fullstack-engineer/03-fullstack-system/infra && docker-compose up` completes without errors
- [ ] `GET http://localhost:5000/health` returns `{ status: "ok" }` (backend)
- [ ] `GET http://localhost:8000/health` returns healthy response (AI service)
- [ ] `GET http://localhost:3000` loads the frontend without errors
- [ ] PostgreSQL accepts connections on port 5432
- [ ] Redis accepts connections on port 6379
- [ ] MongoDB accepts connections on port 27017
- [ ] Backend successfully connects to PostgreSQL (verify via health endpoint DB check)
- [ ] Backend successfully connects to Redis (verify via health endpoint Redis check)
- [ ] Creating a listing via `POST /api/listings` works end-to-end
- [ ] Fetching a listing via `GET /api/listings/:id` returns cached result on second call
- [ ] A new user can register and log in
- [ ] All containers are running as non-root users
- [ ] Sensitive values (JWT_SECRET, DB passwords) come from `.env` file, not hardcoded in docker-compose

### What to do if it fails

If `docker-compose up` does not reach done state, log every failure in the [bug log](bug-log.md) and fix it before moving to Phase 2.

A broken local system means Phase 2 builds on sand.

### Evidence to commit

- `notes/day-30-milestone-1.md` — a 200-word report: what worked, what broke, what you fixed, how long it took to reach green.

---

## Milestone 2: Day 60 — Basic Cloud Deployment

**Definition of done:** The backend API is accessible at a public URL on a free-tier cloud provider. Any team member with the URL can call it.

Suggested providers (pick one):
- **Railway.app** — easiest for Node.js + Postgres + Redis in one platform
- **Render.com** — free tier for web services + Postgres
- **Fly.io** — more control, similar to Docker, good free tier
- **Koyeb** — Docker-based, straightforward

You do NOT need to deploy the full system (frontend + AI service + backend + all databases). You need:
- Backend API (deployed, accessible)
- PostgreSQL (can use Railway's managed Postgres or Render's)
- Redis (can use Railway's managed Redis or Upstash)

### Checklist

- [ ] Backend API is accessible at a public URL (e.g., `https://myapp.railway.app`)
- [ ] `GET /health` returns 200 from the public URL
- [ ] `POST /auth/register` creates a new user
- [ ] `POST /auth/login` returns a JWT
- [ ] Secrets (JWT_SECRET, DB passwords) are set as environment variables in the deployment platform — NOT in code or committed files
- [ ] The deployment fails health check if the DB is not available (does not silently serve broken requests)
- [ ] Deployment can be triggered by pushing to a branch (basic CD)
- [ ] Logs are accessible via the platform's log viewer

### What to document

Write `notes/day-60-milestone-2.md`:
- Which platform you chose and why
- What broke during deployment and how you fixed it
- One thing that works differently in a deployed environment vs local
- The public URL (if comfortable sharing)
- Cost (it should be $0 on free tier)

### Evidence to commit

- `notes/day-60-milestone-2.md`
- Updated `03-fullstack-system/backend/README.md` with deployment instructions

---

## Milestone 3: Day 75 — Improved Deployment

**Definition of done:** The system runs in a local Kubernetes cluster with production-quality manifests.
This milestone is about K8s, not cloud — it can run in minikube or k3s.

### Checklist

- [ ] `kubectl apply -f 03-fullstack-system/infra/k8s/` deploys the full system without errors
- [ ] Backend deployment has: readiness probe, liveness probe, resource limits (CPU + memory)
- [ ] Backend deployment has: rolling update strategy with `maxUnavailable: 0`
- [ ] All sensitive values are in K8s Secrets (not ConfigMaps, not in manifest files)
- [ ] Non-sensitive config is in ConfigMaps
- [ ] HPA is configured: backend scales between 2–10 replicas based on CPU
- [ ] Ingress is configured: `/api/*` routes to backend, `/*` routes to frontend
- [ ] `kubectl get pods` shows all pods Running (not CrashLoopBackOff)
- [ ] A pod can be deleted manually and K8s reschedules it within 30 seconds
- [ ] `kubectl rollout undo deployment/backend` works (rollback tested and verified)

### What to document

Write `notes/day-75-milestone-3.md`:
- What was different between docker-compose and K8s deployment
- What broke first and how you fixed it
- What K8s gives you that docker-compose does not
- What docker-compose gives you that K8s does not

### Evidence to commit

- All K8s manifests in `03-fullstack-system/infra/k8s/` must pass `kubectl apply`
- `notes/day-75-milestone-3.md`

---

## Milestone 4: Day 90 — Production-Style Demo

**Definition of done:** The system can be demonstrated to a technical interviewer or hiring manager in 10 minutes. It is not "production ready" — it is "production-quality" for a portfolio demo.

### Checklist

**System:**
- [ ] `docker-compose up` still starts the full system cleanly (from a clean clone)
- [ ] CI pipeline passes on every commit to main (`Actions` tab shows green)
- [ ] Prometheus metrics are accessible at `/metrics`
- [ ] Grafana dashboard shows at least: request rate, error rate, p95 latency
- [ ] Structured logs include requestId, userId, duration on every request
- [ ] 3 incident runbooks exist and are specific (not generic)
- [ ] 1 detailed postmortem exists with 5 Whys and action items

**Documentation:**
- [ ] `07-showcase/portfolio-narrative.md` is written (not a template)
- [ ] `07-showcase/system-walkthrough.md` is a real 10-minute walkthrough guide
- [ ] All phase plan files reference real artifacts that actually exist
- [ ] `tracking/progress-tracker.md` shows honest completion status

**Code quality:**
- [ ] The backend has at least 10 integration tests
- [ ] The .NET CleanShop project has at least 10 tests
- [ ] The CI pipeline runs all tests and fails on failure

**LeetCode:**
- [ ] 55+ Python solutions committed with brute force + optimized + real-world mapping
- [ ] 28+ C++ solutions committed
- [ ] `01-core-engineering/leetcode/pattern-cheatsheet.md` written

**Evidence to commit:**

- `notes/day-90-milestone-4.md` — "Here is what I can demo and what it proves."
- Git tag: `v1.0` on the final commit

---

## Milestone gap analysis (fill in at each milestone)

| Milestone | Date achieved | What was not ready | Time to fix | Root cause of gap |
|-----------|--------------|-------------------|-------------|-------------------|
| 1: Local full system | | | | |
| 2: Cloud deployment | | | | |
| 3: K8s local | | | | |
| 4: Production demo | | | | |

The gap analysis is the most valuable part of this tracker.
If something was not ready, the reason is a senior-level learning.

# 2AM Incident Response — Quick Reference

When something breaks in production at 2AM, your brain is slow and the pressure is high.
This card is the protocol. Follow it in order. Do not skip steps.

---

## The 9-step protocol

### 1. CONFIRM — Is this actually broken?

Before anything else, verify the problem is real.

```
- Is the alert real or a flapping monitor?
- Can you reproduce the symptom?
- Is it isolated (one region, one user, one service)?
- What is the error rate? Is it 100% or 0.1%?
```

Do not wake people up for a flapping alert. Do not spend 20 minutes diagnosing a problem that resolved itself.

**Time budget: 2 minutes max.**

---

### 2. ASSESS — What is the blast radius?

Before you fix anything, know what is broken.

```
- Which users are affected? (all / subset / specific account)
- What functionality is broken? (login / checkout / read-only / write operations)
- Is data being lost or corrupted, or just unavailable?
- Is it getting worse, stable, or recovering on its own?
```

The blast radius determines urgency and who to wake up.

**Time budget: 3 minutes max.**

---

### 3. STOP THE BLEEDING — Not fix it, just stop it

Your first goal is to limit damage, not solve the root cause.

Options:
- Roll back the last deployment
- Disable the feature flag that was just enabled
- Increase timeout / add circuit breaker to protect downstream services
- Scale up to handle load spike
- Route traffic away from the broken region
- Put maintenance page for the affected flow

**You are buying time. A partial fix that reduces blast radius is better than the perfect fix that takes 2 hours.**

---

### 4. COMMUNICATE — Tell people what you know, not what you think

As soon as you know what is broken:

**Internal (Slack/Teams):**
```
🔴 Incident: [service] is [symptom]
Impact: [who/what is affected]
Started: ~[time]
Status: Investigating / Mitigating
Next update in: 15 minutes
```

**External (status page, if applicable):**
```
We are investigating reports of [vague description].
We will update within [timeframe].
```

**The rule:** Communicate what you *know*, not what you *think*.
Do not say "it's probably the database" when you have not confirmed that yet.
Do not wait until you have the root cause to communicate — that's too late.

---

### 5. INVESTIGATE — Now find the actual cause

With blast radius stopped and communication out, start root cause analysis.

Work backwards from the symptom:

```
1. Where is the error showing up? (service logs, APM alerts, error tracker)
2. When did it start? (compare with deployment timestamps, traffic graphs)
3. What changed? (recent deployments, config changes, cron jobs, external services)
4. Is there a pattern? (specific user IDs, specific endpoints, specific times)
5. What do the metrics show? (CPU, memory, database connections, cache hit rate, queue depth)
```

**Tools to use:**
- Application logs (`grep ERROR`, filter by time range)
- APM dashboard (error rates, latency percentiles, throughput)
- Database slow query log
- Kubernetes events: `kubectl get events --sort-by=.lastTimestamp`
- Recent deployments: `git log --since="2 hours ago"`

---

### 6. STABILIZE — Apply a durable fix or workaround

Once you know the cause, apply the minimal fix:

- If a recent deployment caused it: roll back
- If a config value is wrong: fix config and restart
- If a query is slow under load: add index or kill the query and disable the feature
- If a dependency is down: enable fallback behavior, serve stale data, or fail gracefully

**Document what you did as you do it.** Even one line in Slack: "Restarted the job processor at 02:47, error rate dropped to 0."

---

### 7. VERIFY — Confirm the fix worked

Do not assume the fix worked. Verify it.

```
- Error rate back to baseline?
- Latency back to normal?
- Affected users can now complete their actions?
- No new errors introduced by the fix?
- No data inconsistency created?
```

**Watch for 5 minutes minimum before declaring resolved.**

---

### 8. MONITOR — Stay on it

After the fix, watch the system for 15–30 minutes:

- Error rate stable at 0 (or baseline)?
- No secondary failures from the fix?
- Queue/backlog processing correctly?
- No data reconciliation needed?

---

### 9. POSTMORTEM — Write it down before you sleep

Do not skip this. This is the entire value of the incident.

At minimum, record:
```
- What happened
- When it started
- What the blast radius was
- What we did to stop it
- What the root cause was
- What we are changing to prevent recurrence
```

Full postmortem format is in: `05-production-thinking/postmortems/`

---

## Communication templates

### Incident declaration (Slack)

```
🔴 INCIDENT DECLARED — [SERVICE NAME]

Symptom: [what users see]
Impact: [who/how many affected]
Started: ~[HH:MM UTC]
IC: @[incident commander]
Bridge: [link if applicable]

We are investigating. Next update in 15 minutes.
```

### Status update (every 15 minutes)

```
📊 INCIDENT UPDATE — [HH:MM UTC]

Status: [Investigating / Identified / Mitigating / Resolved]
Current impact: [same / reduced / resolved]
What we've tried: [brief]
Next steps: [brief]
Next update in: [time]
```

### Resolution

```
✅ INCIDENT RESOLVED — [HH:MM UTC]

Duration: [X hours Y minutes]
Root cause: [one sentence]
Fix applied: [one sentence]
Postmortem scheduled: [date]
```

---

## What NOT to do

- **Do not guess publicly.** "I think it might be the database" in a public channel plants a wrong assumption.
- **Do not rush a fix without understanding it.** A bad fix at 2AM creates a second incident at 3AM.
- **Do not go silent.** No communication is worse than uncertain communication.
- **Do not close the incident before verifying.** "I think it's fixed" is not verified.
- **Do not skip the postmortem.** The value of an incident is the prevention of the next one.

---

## The senior mindset at 2AM

A junior engineer panics and starts changing things.
A senior engineer slows down, follows the protocol, and changes exactly one thing at a time.

When you are tired and the pressure is high:
- Slow down
- Follow the steps
- Change one thing at a time
- Verify each change before the next
- Communicate throughout

The protocol exists because your judgment degrades at 2AM.
Trust the protocol, not your instincts.

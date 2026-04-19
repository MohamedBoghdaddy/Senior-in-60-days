# Debugging Journal Template

Copy this file for each debugging session. Name it: `debugging-YYYY-MM-DD-[short-description].md`

Hypothesis-driven debugging is a senior skill. This journal forces you to think before you change things.
The rule: form a hypothesis before you touch anything.

---

## Debugging Session — [Short description of the problem]

**Date:** YYYY-MM-DD
**Time started:** HH:MM
**Time resolved:** HH:MM (fill in when done)
**Component:** [service / module / query / infrastructure]

---

## The symptom

What did you observe? Not the cause — what you saw from the outside.

```
[Describe exactly what you observed: error message, unexpected behavior, test failure, 
performance degradation, etc. Paste the actual error if one exists.]
```

**When does it occur?**
- [ ] Every time
- [ ] Sometimes (estimated __ % of the time)
- [ ] Under specific conditions: [describe]
- [ ] After a recent change: [what changed]

**What is the impact?**
- [ ] Crashes / throws exception
- [ ] Returns wrong result
- [ ] Performance degradation
- [ ] Silent failure (no error, wrong outcome)
- [ ] Affects users in production

---

## What I know before touching anything

List every fact you know:

```
1. 
2. 
3. 
```

List every assumption you are making (distinguish facts from guesses):

```
1. [assumption]
2. [assumption]
```

---

## Hypotheses

Before running any command or changing any code, write your hypotheses.
Order them by probability (most likely first).

**Hypothesis 1:** 
```
[What do I think is causing this?]
[Why do I think this is the most likely cause?]
[How will I test this hypothesis?]
[What result would confirm it?]
[What result would eliminate it?]
```

**Hypothesis 2:**
```
[Same structure]
```

**Hypothesis 3:**
```
[Same structure]
```

---

## Investigation log

Record each step. Do not skip steps or compress them — future you needs to see the exact sequence.

```
[HH:MM] Step 1: What I did
         Command / code / query:
         Result:
         What this tells me:

[HH:MM] Step 2: What I did
         Command / code / query:
         Result:
         What this tells me:

[HH:MM] Step 3: ...
```

**After each step:** Update the hypothesis table:

| Hypothesis | Status | Evidence |
|------------|--------|---------|
| H1 | Likely / Eliminated / Confirmed | |
| H2 | Likely / Eliminated / Confirmed | |
| H3 | Likely / Eliminated / Confirmed | |

---

## The fix

**Root cause:**
```
[One sentence. Be precise — "a null pointer" is not precise. 
"The user object is null when the JWT contains a userId that doesn't exist in the database" is precise.]
```

**Why this caused the symptom:**
```
[Connect the root cause to what you observed at the surface level.]
```

**The fix I applied:**
```
[What you changed. Include file and line number.]
```

**Why this fix is correct:**
```
[Not just "it makes the error go away" — explain why this addresses the root cause.]
```

**Verification:**
- [ ] Reproduced the original bug before the fix
- [ ] Confirmed the bug is gone after the fix
- [ ] Confirmed no new errors introduced
- [ ] Test added to prevent regression

---

## What I should have known

What knowledge gap made this harder to debug?

```
[What concept, tool, or domain knowledge would have made this obvious faster?]
```

What I would do differently next time:

```
[What would change about my process — not just the code.]
```

---

## Time breakdown

| Phase | Time spent |
|-------|-----------|
| Understanding the symptom | |
| Forming hypotheses | |
| Investigation / testing hypotheses | |
| Implementing the fix | |
| Verifying the fix | |
| **Total** | |

If investigation took more than 30 minutes: what slowed you down?

```
[Honest analysis. Was it a missing log? A wrong hypothesis held too long? Unfamiliar code?]
```

---

## Should this go in the bug log?

If this was a bug in code you wrote or in the system:
- [ ] Yes — add an entry to `tracking/bug-log.md`
- [ ] No — this was a configuration issue / environment issue / expected behavior

---

## Techniques used in this session

Check all that apply:

- [ ] Binary search (isolate which half of the system contains the problem)
- [ ] Rubber duck (explained the problem out loud before looking at code)
- [ ] Minimal reproduction (reduced to the smallest case that shows the bug)
- [ ] Bisect (git bisect or test isolation to find which change introduced it)
- [ ] Instrumentation (added temporary logging to observe state)
- [ ] Hypothesis elimination (formed and methodically ruled out hypotheses)
- [ ] Fresh eyes (walked away and came back)
- [ ] Checked the obvious first (version mismatch, wrong environment, stale build)

---

## Note for future sessions

One thing to remember the next time you debug something similar:

```
[One sentence. The most transferable insight from this session.]
```

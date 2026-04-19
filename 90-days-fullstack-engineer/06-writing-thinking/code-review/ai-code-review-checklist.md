# AI-Generated Code Review Checklist

Reviewing AI-generated code is a different skill from reviewing junior code.
Junior code fails in predictable ways. AI code fails in unpredictable ways.

A junior writes code they don't fully understand. AI writes code that *looks* like it is fully understood.
The surface quality is high. The hidden problems are deep.

---

## Why AI code needs a different review mindset

Junior code red flags are obvious: bad naming, deep nesting, no error handling, magic numbers.
AI code red flags are subtle:

| AI Code Pattern | What it signals |
|----------------|-----------------|
| Too polished, too fast | May have skipped the hard part and solved a simpler version |
| Every edge case "handled" | Check that the handling is correct, not just present |
| Very clean abstractions | May be over-engineered for the actual problem |
| Confident tone in comments | Comments describe intent — they don't prove correctness |
| All happy-path logic | Failure paths may be fake (logging an error but not propagating it) |
| Hallucinated library calls | Methods that don't exist, options that aren't valid |
| Fake completeness | `// TODO: handle this case` buried inside a function |
| Architecture drift | Doesn't follow the patterns already established in the codebase |

---

## The SCOPE framework

Review in this order. Every letter is a gate — if it fails, fix before moving on.

### S — Solves the right problem

Before reading any code:
- State the actual requirement in one sentence
- Does the code solve that requirement, or does it solve something adjacent?
- AI often solves the problem it thinks was asked, not the problem that was asked

Questions to ask:
- [ ] Does the function signature match what the caller actually needs?
- [ ] Does the output format match what downstream code expects?
- [ ] Are the edge cases the *real* edge cases, or the *obvious* edge cases?
- [ ] Would this break under realistic production data?

### C — Correctness

Read the logic, not the style. Does it actually work?

- [ ] Trace through at least 2 inputs manually — does it produce the right output?
- [ ] What happens with empty input, null, zero, negative numbers?
- [ ] Is there an off-by-one? (AI loves `<` vs `<=` errors in loops and pagination)
- [ ] Are async operations awaited correctly? Are race conditions possible?
- [ ] Does it modify input data it shouldn't? (mutation bugs)
- [ ] Are database transactions scoped correctly?
- [ ] Does error handling actually propagate the error, or swallow it?

Watch specifically for:
```javascript
// AI writes this often — looks correct, isn't
try {
  await doSomething();
} catch (e) {
  console.error(e);  // Error is logged but not re-thrown — caller gets undefined
}
```

### O — Organization

Does this code fit the existing system?

- [ ] Does it follow the naming conventions in the rest of the codebase?
- [ ] Does it use the existing patterns (repository pattern, service layer, error classes)?
- [ ] Does it import the right things (not create a second version of a utility that already exists)?
- [ ] Is the abstraction level appropriate — not too granular, not a 200-line function?
- [ ] Does it belong in this file/layer, or is it in the wrong layer?

AI-specific check: search the codebase for any function the AI used that you don't recognize.
AI will confidently call `db.query()` when the codebase uses `db.execute()`.

### P — Protection

Does it handle what can go wrong in production?

- [ ] Are all external inputs validated before use?
- [ ] Is user-controlled data ever used in a query, command, or path without sanitization?
- [ ] Are secrets, tokens, or credentials ever logged or returned in responses?
- [ ] Does it handle the service being down (database, Redis, external API)?
- [ ] Is there a timeout on external calls?
- [ ] Are there rate limits or size limits on inputs?
- [ ] Are authorization checks present — not just authentication?

AI-specific check: AI often adds `console.log(userData)` for debugging and forgets to remove it.
Check every log statement for PII.

### E — Evolution

Can someone (including you, in 6 months) read and change this?

- [ ] Would a new team member understand what this does without asking?
- [ ] Are the variable names accurate, not just short?
- [ ] Are comments explaining *why*, not *what*?
- [ ] Are there any "magic" values that should be constants?
- [ ] Is there a test? (AI skips tests unless explicitly asked)
- [ ] If this fails, will the error message explain *where* it failed?

---

## Red flags that require immediate investigation

Stop the review and investigate these before anything else:

**1. Hallucinated library methods**
```javascript
// Does this method actually exist?
await redis.getWithDefault(key, defaultValue);
// Check the actual Redis client docs — this might be invented
```

**2. Fake completeness**
```javascript
async function processPayment(data) {
  // TODO: validate card details
  const result = await stripe.charge(data);
  return result;
}
// The TODO is inside production code. The validation was the hard part.
```

**3. Error swallowing**
```javascript
try {
  return await db.query(sql);
} catch (e) {
  return null; // Caller cannot distinguish "no results" from "database is down"
}
```

**4. Over-confident auth**
```javascript
// AI sometimes generates this pattern
if (user.role === 'admin') {
  // no check that user is actually authenticated
}
```

**5. Async without await**
```javascript
// Missing await — no error thrown, silent failure
function deleteUser(id) {
  db.query('DELETE FROM users WHERE id = $1', [id]); // not awaited
  return { success: true }; // always returns success even if delete failed
}
```

**6. Correct algorithm, wrong scale**
```javascript
// Works on 10 records, fails on 100,000
const users = await db.query('SELECT * FROM users');
const active = users.filter(u => u.lastLogin > cutoff);
```

---

## The review output format

When you complete a review, record it:

```markdown
## Code Review — [component] — Day N

**Source:** AI-generated / PR #N / pair session
**Reviewer:** [you]
**Date:** YYYY-MM-DD

### SCOPE verdict

| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| S - Solves right problem | Pass/Fail | |
| C - Correctness | Pass/Fail | |
| O - Organization | Pass/Fail | |
| P - Protection | Pass/Fail | |
| E - Evolution | Pass/Fail | |

### Issues found

**Blocking (must fix before merge):**
- [issue, file, line]

**Non-blocking (fix in follow-up):**
- [issue, file, line]

### AI-specific red flags checked
- [ ] No hallucinated methods
- [ ] No error swallowing
- [ ] No fake completeness (buried TODOs)
- [ ] No unwaited async
- [ ] No PII in logs
- [ ] No missing auth checks
- [ ] Algorithm scales to production data size

### What the AI got right
[Be specific — this is as important as what it got wrong]

### What I changed and why
[List changes made during review]
```

---

## The meta-lesson

AI code is a draft, not a solution.

A senior engineer uses AI to generate the scaffolding and then applies judgment to every line.
The review is not a formality — it is the actual engineering work.

If you accepted AI code without doing SCOPE, you did not engineer anything.
You copy-pasted. The system will fail in the places you did not review.

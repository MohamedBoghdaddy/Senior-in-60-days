# Junior Code Review Guide

How to review code written by someone less experienced than you — and how to leave them better than you found them.

The goal is not to catch mistakes. The goal is to transfer judgment.
A review that says "this is wrong" teaches nothing. A review that says "this is wrong, here is why, here is the principle" builds an engineer.

---

## The review order

Read in this sequence. Each level builds on the previous. Do not jump to style before correctness.

### 1. Does it solve the right problem?

Before reading a single line of code:
- What was the requirement?
- Does the code satisfy the requirement as stated?
- Is there a simpler version that would also work?

This catches the most expensive kind of wrong: technically correct code that does the wrong thing.

### 2. Is the logic correct?

Run it mentally or trace it:
- Trace through the main path with realistic data
- Trace through edge cases: empty, null, 0, negative, max size
- Check all branches — does every `if` have the right `else` behavior?
- Look for off-by-one errors in loops and array indexing
- Check that all async operations are awaited

### 3. Is it readable?

Only after correctness:
- Can you understand what this does without running it?
- Are the names accurate? (A variable called `data` that holds a user object is wrong)
- Are functions doing one thing?
- Is the complexity appropriate for the problem?

### 4. Is responsibility placed correctly?

- Is this logic in the right layer? (Business logic shouldn't be in a controller)
- Is there a utility function that already does this?
- Would moving this to a helper make both files clearer?

### 5. Is it safe?

- Is user input validated before use?
- Is anything logged that shouldn't be (passwords, tokens, PII)?
- Are SQL queries parameterized?
- Are authorization checks present (not just authentication)?
- Are errors handled without leaking stack traces to the client?

### 6. Is it maintainable?

- Would this break in 6 months when someone changes a related system?
- Are magic numbers or strings named as constants?
- Are there hardcoded values that will need to change per environment?
- Is there duplication that will cause bugs when one copy is updated and the other isn't?

### 7. Is it testable?

- Can you write a unit test for this function?
- Does it have side effects that make testing difficult?
- Are external dependencies injected or hardcoded?

### 8. Is it aligned with the rest of the system?

- Does it follow the conventions in the rest of the codebase?
- Does it use the established patterns (error handling, logging, data access)?
- Would a new engineer looking at this and the rest of the codebase assume they were written by the same person?

---

## The SCOPE framework (quick reference)

Use this as a mental mnemonic during review:

| Letter | Gate | One-line description |
|--------|------|---------------------|
| **S** | Solves right problem | Does it actually do what was asked? |
| **C** | Correctness | Does the logic work for all inputs? |
| **O** | Organization | Does it fit into the codebase cleanly? |
| **P** | Protection | Does it handle what can go wrong? |
| **E** | Evolution | Can someone change this safely later? |

---

## How to write review comments

**Bad comment:**
> "This is wrong."

**Better comment:**
> "This will throw if `users` is empty — you need a guard before line 14."

**Best comment:**
> "This will throw if `users` is empty because `.reduce()` on an empty array with no initial value throws TypeError. Guard with `if (!users.length) return 0` or pass `0` as the second argument to reduce. This pattern shows up any time you reduce a collection that might be empty — worth remembering."

The "best" version:
1. States what will fail
2. Explains why it will fail
3. Shows how to fix it
4. Names the general principle so it sticks

---

## Blocking vs. non-blocking issues

**Blocking — must fix before merge:**
- Incorrect logic
- Missing security check (unvalidated input, missing auth)
- Unhandled error that will crash in production
- Breaks existing tests or API contracts
- Data loss risk

**Non-blocking — log in follow-up:**
- Naming that could be clearer
- Function that could be extracted
- Missing test for edge case
- Style inconsistency

Do not block a PR on naming preferences. Do not let security issues through as non-blocking.

---

## What NOT to do in a review

- Do not rewrite the code in the comment. Describe what to change, not the exact code.
- Do not approve code you do not understand. Ask a question instead.
- Do not comment on style if there is no linter rule for it — this is noise.
- Do not pile on every possible improvement in one review. Pick the most important issues.
- Do not be vague. "This could be better" is not a review comment.
- Do not approve code because you feel social pressure. Your approval is a signature.

---

## The 5-minute pre-review checklist

Before you read a single line:

- [ ] What is this PR supposed to do? (read the description, not just the diff)
- [ ] Is there a linked issue or ticket?
- [ ] Did the author write any tests?
- [ ] Does CI pass?
- [ ] Is the diff small enough to review effectively? (>400 lines: ask to split)

---

## Patterns that always need a second look

| Pattern | Why it's worth checking |
|---------|------------------------|
| `catch (e) {}` or `catch (e) { return null }` | Error is probably being swallowed |
| `any` type in TypeScript | Type safety is being bypassed |
| `SELECT *` in a query | Returns all columns, may include sensitive data, breaks on schema changes |
| `await` inside a loop | Usually should be `Promise.all()` |
| Long parameter list (>3) | Usually means a function is doing too much |
| Nested ternaries | Usually unreadable — suggest named variable |
| `setTimeout` for timing coordination | Fragile — will fail under load |
| Comparing with `==` instead of `===` | Type coercion surprises |
| `.env` values with no fallback | Will crash on startup if env var missing |
| `console.log` in production code | Remove before merge or convert to structured log |

---

## The tone rule

Code review is a conversation, not a verdict.

Use "we" not "you":
- "We usually handle this with..." instead of "You should have used..."
- "This pattern can cause..." instead of "You did this wrong"

A review that makes someone feel stupid is a failed review, even if all the issues were caught.
The junior engineer needs to trust your judgment enough to ask you questions tomorrow.

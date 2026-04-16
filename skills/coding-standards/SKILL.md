---
name: coding-standards-and-simplification
description: "Core quality baseline and code simplification guides. Use when writing code, reviewing for maintainability, or refactoring for clarity. Focuses on KISS, DRY, YAGNI, naming, async hygiene, and error handling."
---

# Coding Standards and Simplification

## Purpose

Define a minimal quality baseline and a systematic process for simplifying code. The goal is code that is easier to read, understand, modify, and debug.

---

## When to Activate

- Starting a new module and needing coding conventions
- Reviewing maintainability and readability
- Refactoring for clarity and lower complexity
- Enforcing naming, consistency, and code smell checks
- Setting lint and formatting expectations

---

## Scope Boundaries

Use this skill for:
- descriptive naming and consistency
- readability and simplicity (KISS)
- duplication control (DRY)
- avoid speculative abstractions (YAGNI)
- immutability-first state/data updates where practical
- baseline error-handling expectations

Do NOT use this skill as the primary source for:
- framework architecture and layering
- API contract/versioning details
- React rendering/composition specifics
- backend data access and tenant isolation rules
- security standards beyond baseline input and error hygiene

If available, defer to narrower skills for those areas.

---
---

## Core Principles

## 1) Readability First

- Prefer clear names over short names
- Make intent obvious from function and variable names
- Keep formatting consistent and predictable
- Prefer self-documenting code; comment only when intent is not obvious

## 2) KISS

- Choose the simplest correct design
- Avoid clever implementations that reduce clarity
- Optimize only when there is evidence

## 3) DRY

- Extract repeated logic into helpers/modules
- Centralize shared constants and validation patterns
- Do not over-abstract one-off logic

## 4) YAGNI

- Build for current requirements first
- Avoid speculative extension points
- Add abstraction only after repeat demand appears

## 5) Immutability-First

- Prefer non-mutating updates for objects/collections
- Avoid in-place changes unless there is a clear measured benefit
- When mutation is required for performance, isolate and document why

---
# The Principles of Simplicity

1. **Readability First**: Clear names over short names. Intent should be obvious.
2. **KISS (Keep It Simple, Stupid)**: Choose the simplest correct design. Avoid cleverness.
3. **DRY (Don't Repeat Yourself)**: Extract repeated logic, but don't over-abstract one-offs.
4. **YAGNI (You Ain't Gonna Need It)**: Build for current requirements only.
5. **Chesterton's Fence**: Understand WHY code exists before you simplify or remove it.
6. **Immutability-First**: Prefer non-mutating updates for objects/collections. Avoid in-place changes unless there is a clear benefit.

---

# The Simplification Process

1. **Understand Before Touching**: Read context, check git blame, and identify edge cases.
2. **Identify Opportunities**:
    - **Structural Complexity**: Nested logic (3+ levels), long functions (50+ lines).
    - **Naming**: Generic names (`data`, `temp`), abbreviations (`usr`, `cfg`).
    - **Redundancy**: Copy-pasted logic, dead code, unnecessary wrappers.
3. **Apply Incrementally**: One simplification at a time. Run tests after each change.
4. **Rule of 500**: For refactors > 500 lines, use automation (codemods) rather than manual edits.

### Structural Simplification
| Pattern | Simplification |
|---------|----------------|
| Deep nesting | Extract into guard clauses or helper functions |
| Long functions | Split into focused functions with descriptive names |
| Boolean flags | Replace with options objects or separate specialized functions |

### Naming & Readability
| Pattern | Simplification |
|---------|----------------|
| Generic names | Rename to describe context (`validationErrors`, `userProfile`) |
| Comments on "What" | Delete — the code should be clear enough |
| Comments on "Why" | Keep — code cannot always express intent |

---

# Naming Rules

- **Verb-Noun Intent**: Functions should use verb-noun naming (e.g., `fetchUserProfile`, `calculateScore`).
- **Predicates for Booleans**: Booleans should read as questions/predicates (`isReady`, `hasAccess`, `canRetry`).
- **Domain over Technical**: Prefer domain terms over technical placeholders.
- **Avoid Vague Identifiers**: No `data`, `value`, `temp` unless the scope is tiny/obvious.

---

# Function and Structure Rules

- **Single Responsibility**: Keep functions focused on one thing.
- **Early Returns**: Use guard clauses to reduce nesting.
- **Code Smell Checks**:
    - Long functions with mixed responsibilities.
    - Nested conditional chains.
    - Magic numbers/strings without named constants.
    - Broad catch blocks that hide root causes.

---

# Async and Concurrency Baseline

- Use async patterns consistently for I/O
- Run independent I/O concurrently where safe
- Avoid accidental sequential waits
- Protect shared mutable state when concurrency exists

---

## Review Checklist

Before finalizing code, verify:

- [ ] Names are descriptive and consistent
- [ ] Logic is simple and understandable
- [ ] No unnecessary abstraction or future-only code
- [ ] Duplication is removed where it improves clarity
- [ ] No high-risk code smells remain
- [ ] Error handling is explicit and safe
- [ ] Mutation is intentional and justified

---
- Use async patterns consistently for I/O
- Run independent I/O concurrently where safe
- Avoid accidental sequential waits
- Protect shared mutable state when concurrency exists

---

## Review Checklist

Before finalizing code, verify:

- [ ] Names are descriptive and consistent
- [ ] Logic is simple and understandable
- [ ] No unnecessary abstraction or future-only code
- [ ] Duplication is removed where it improves clarity
- [ ] No high-risk code smells remain
- [ ] Error handling is explicit and safe
- [ ] Mutation is intentional and justified

---

## Output Contract

When this skill is activated, return:

1. Key findings (or proposed conventions)
2. Concrete fixes with minimal change scope
3. Residual risks and follow-up checks

This keeps output practical and review-ready.


- Use `async/await` patterns consistently for I/O.
- Run independent I/O concurrently (e.g., `Task.WhenAll` or `Promise.all`) where safe.
- Avoid accidental sequential waits.
- Protect shared mutable state when concurrency exists.

---

# Error Handling Baseline

- **Validate at Boundaries**: Trust internal code; validate at system edges (API handlers, form inputs).
- **Fail Fast**: Stop execution as soon as a failure condition is met.
- **Safe Messages**: Provide actionable, non-sensitive error messages.
- **Don't Swallow Exceptions**: Never catch and ignore errors without logging or handling.

---

# Red Flags
- Simplification that requires modifying tests to pass (you changed behavior).
- "Simplified" code that is harder to follow than the original.
- Broad cleanup mixed with feature or bug fix work (Must be separate PRs).
- Removing error handling in the name of "cleanliness".

---

# Verification
- [ ] All existing tests pass without modification.
- [ ] Linter and Build pass.
- [ ] Refactoring is separate from feature/fix logic.
- [ ] No behavioral changes were introduced.
- [ ] Naming and Structure rules followed.

---
name: coding-standards-and-simplification
description: "Core quality baseline and code simplification guides. Use when writing code, reviewing for maintainability, or refactoring for clarity. Focuses on KISS, DRY, YAGNI, naming, async hygiene, and error handling."
---

# Coding Standards and Simplification

## Purpose

Define a minimal quality baseline and a systematic process for simplifying code. 

**Senior Mindset**: Code is written for **people** (teammates and your future self), not just for machines. Follow the **Kaizen** mindset and the **TDD Iron Law** (Write tests before code) to ensure quality by design.



---

## When to Activate

- **Readability Rules**: Clean Code by Robert C. Martin (Uncle Bob).
- **Naming Conventions**: Intention-revealing, pronounceable, and searchable.
- **Function Hygiene**: Small (< 20 lines), high cohesion, one level of abstraction.
- **Commenting Policy**: "Don't comment bad code—rewrite it."
- **Aesthetic Integrity**: Code structure and design must follow the **Diamond Standard Pillars**: Scalable, Secure, Aesthetic.
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

## 1) Readable First, Clever Later (Strict)

- **Prioritize Clarity**: Choose easy-to-understand code over "clever" or "hacky" implementations that save a few lines but increase cognitive load.
- **The 6-Month Rule**: Ask yourself: "Will I or my teammates understand this logic in 6 months without explanation?"
- Make intent obvious from function and variable names.
- Keep formatting consistent and predictable.
- Prefer self-documenting code; comment only to explain **WHY** (logic/intent), not **WHAT** (the code itself).

## 2) KISS & Trade-offs

- Choose the simplest correct design.
- Avoid premature optimization or abstraction.
- **Balanced Trade-offs**: For senior tasks, balance readability, performance, and deadlines. Don't over-engineer for scenarios that don't exist yet.


## 3) DRY (Don't Repeat Yourself)

- **Duplication = Technical Debt**: Extract repeated logic into shared helpers or modules to prevent maintenance silos.
- Centralize shared constants and validation patterns.
- Do not over-abstract one-off logic (avoid "premature DRY").


## 4) YAGNI

- Build for current requirements first
- Avoid speculative extension points
- Add abstraction only after repeat demand appears

## 5) Immutability-First

- Prefer non-mutating updates for objects/collections
- Avoid in-place changes unless there is a clear measured benefit
- When mutation is required for performance, isolate and document why

## 6) Poka-Yoke (Error Proofing)

- **Design for structural impossibility**: Make invalid states unrepresentable (e.g., use Discriminated Unions/Enums instead of free strings).
- **Validate at boundaries**: Trust internal code; strictly verify at system edges.
- **Fail Fast & Loudly**: Stop execution immediately on contract violation.

## 7) Just-In-Time (JIT) Optimization

- Implement only current requirements (YAGNI).
- **Optimize only after measurement**: Profile before optimizing. Never optimize based on intuition alone.


---
# The Principles of Simplicity

1. **Readability First**: Clear names over short names. Intent should be obvious.
2. **KISS (Keep It Simple, Stupid)**: Choose the simplest correct design. Avoid cleverness.
3. **DRY (Don't Repeat Yourself)**: Extract repeated logic, but don't over-abstract one-offs.
4. **YAGNI (You Ain't Gonna Need It)**: Build for current requirements only.
5. **TDD First**: No production code without a failing test first (Red-Green-Refactor).
6. **Chesterton's Fence**: Understand WHY code exists before you simplify or remove it.
7. **Immutability-First**: Prefer non-mutating updates.

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

### Aesthetic Integrity (The Diamond Pillar)
1. **Visual Balance**: Maintain consistent indentation, grouping related logic with whitespace.
2. **Harmonious Naming**: Use consistent patterns across the codebase to create a "rhythm".
3. **Explicit Design**: UI-related code (CSS/React) must aim for **Premium Aesthetics** as defined in `@frontend-design`.
4. **Code-as-Art**: Treat every block of code as if other master engineers will read it for inspiration.
- **Use Nouns for Classes**: `Customer`, `Order`, `WikiPage`. Avoid `Manager`, `Data`, `Info`.
- **Use Verbs for Methods**: `postPayment`, `deletePage`, `isValid`.

### Clean Code Principles (MANDATORY)
1. **Small Functions**: Functions should be shorter than you think. Aim for **< 20 lines**.
2. **Do One Thing (SRP)**: A function or class should have exactly one reason to change.
3. **One Level of Abstraction**: Don't mix high-level business logic with low-level details (like regex or array slicing) in the same function.
4. **Newspaper Metaphor**: Organize files with high-level concepts at the top and implementation details at the bottom.
5. **No Side Effects**: Functions should not secretly change global state or hidden parameters.
6. **Error Handling**: Use Exceptions instead of return codes. Don't return `null`; don't pass `null`.

### .NET Specific Rules
- **XML Documentation**: Provide comprehensive XML documentation for all public APIs, methods, and types. Use `<summary>`, `<param>`, and `<returns>` tags.
- **Code Analysis**: Follow `.editorconfig` rules strictly. Ensure your code passes all **Roslyn Analyzers** and style checks. Do not suppress warnings without a documented architectural reason.

---

# Function and Structure Rules

- **Single Responsibility (SRP)**: Each function should do **one thing well**. If you need a "step-by-step" comment inside a function, consider extracting those steps into smaller, named functions.
- **Early Returns**: Use guard clauses to reduce nesting.
- **The Kaizen (Boy Scout) Rule**: Always leave the code cleaner than you found it. Small, frequent improvements are the engine of quality.

- **Code Smell Checks**:
    - Long functions (>50 lines) with mixed responsibilities.
    - Nested conditional chains (3+ levels).
    - Magic numbers/strings without named constants.
    - Broad catch blocks that swallow context or hide root causes.


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
- [ ] No unnecessary abstraction or future-only code (YAGNI)
- [ ] Duplication is removed where it improves clarity (DRY)
- [ ] **Poka-Yoke**: Invalid states are unrepresentable
- [ ] **Kaizen**: Code is cleaner than before the change
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

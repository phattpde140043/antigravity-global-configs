---
name: performing-code-review
description: "Systematic multi-pass code review framework (5 Phases). Part of the review-master discipline."
---

# Performing Code Review (The Iron Law)

**NO VERDICT WITHOUT COMPLETING ALL REVIEW PASSES.**

## 🔄 The Review Pipeline
1. **Phase 1: Reconnaissance**: Understand WHAT changed and WHY. Build a change taxonomy.
2. **Phase 2: Security Pass**: Tenant isolation, Auth/AuthZ, Secret management, Information disclosure.
3. **Phase 3: Architecture Pass**: Separation of Concerns, Error handling (RFC 7807), DI lifetimes, Middleware order.
4. **Phase 4: Bug Hunt**: Call site vs Declaration mismatch, Async/await hygiene, Resource disposal.
5. **Phase 5: Grading & Verdict**: Assign severity (Critical/High/Medium/Low) and issue Verdict (APPROVE/REQUEST CHANGES).

## 🧩 Stack-Specific Checklists
- **.NET**: Blocking async (`.Result`), Nullable misuse, EF Core N+1.
- **Python/pytest**: Fixture scoping, Playwright context disposal, xfail rationale.
- **JS/React**: Stale closures, missing `useEffect` cleanup, infinite re-renders, hydration mismatch.

## 🏁 Verdict Contract
Every review must include an Executive Summary, Change Taxonomy, Detailed Findings, and a clear Verdict with "Must Fix" (blocking) items.

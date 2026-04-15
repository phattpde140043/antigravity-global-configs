---
name: coding-standards
description: "Use when reviewing or writing code quality baselines: naming, readability, immutability-first updates, simple design (KISS/DRY/YAGNI), code smell checks, and safe error-handling defaults across projects. USE WHEN: reviewing or writing code quality baselines: naming, readability, immutability-first updates, simple design (KISS/DRY/YAGNI), code smell checks, and safe error-handling defaults across projects. NOT FOR: framework architecture and layering; API contract/versioning details."
---

# Coding Standards (Core, Cross-Project)

## Purpose

Define a minimal, reusable quality baseline that works across projects and languages.
This skill is the common floor, not a framework playbook.

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

## Naming Rules

- Functions and methods should use verb-noun intent (for example: `fetchUserProfile`, `calculateScore`)
- Booleans should read as predicates (`isReady`, `hasAccess`, `canRetry`)
- Avoid vague identifiers (`data`, `value`, `temp`, `flag`) unless scope is tiny and obvious
- Prefer domain terms over technical placeholders

---

## Function and Structure Rules

- Keep functions focused on one responsibility
- Prefer early returns over deep nesting
- Split long functions into small composable units
- Remove dead code and stale comments

Code smell checks:
- long functions with mixed responsibilities
- nested conditional chains
- copy-paste blocks
- magic numbers/strings without named constants
- broad catch blocks that hide root cause

---

## Error Handling Baseline

- Validate external inputs at boundaries
- Fail with actionable, non-sensitive messages
- Preserve root cause in logs/telemetry when possible
- Do not swallow exceptions silently
- Normalize error shape per project conventions

---

## Async and Concurrency Baseline

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

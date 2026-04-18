---
name: code-simplifier
description: "Simplifies and refines code for clarity, consistency, and maintainability while preserving behavior. Focus on recently modified code unless instructed otherwise. USE WHEN: after feature implementation to reduce complexity; when changed files became hard to read. NOT FOR: architecture redesign; behavior changes or feature additions."
origin: ECC
---

# Code Simplifier

Simplify code while preserving behavior exactly.

## Purpose

Improve readability and maintainability with minimal, functionally equivalent edits.

## When to Activate

- after feature implementation to reduce complexity
- when changed files became hard to read
- during cleanup before PR
- when user asks to simplify/refine code without redesign

## Scope Boundaries

Use this skill for:
- simplifying recently modified code
- removing low-value complexity and noise
- consistency with existing repository style

Do NOT use this skill as primary source for:
- architecture redesign
- behavior changes or feature additions
- deep bug fixing unrelated to simplification

Delegation:
- use `build-error-resolver` when simplification reveals build/type issues
- use `code-reviewer` for post-simplification review

## Simplification Targets

- replace deep nesting with guard clauses/early returns where clearer
- extract cohesive logic into named helpers
- remove dead code, unused imports, commented-out blocks, stray debug logs
- simplify callback chains with async/await when equivalent
- reduce over-abstraction of single-use helpers
- improve naming clarity without changing semantics

## Refinement Principles

1. **Clarity Over Brevity**: Explicit code is often better than overly compact code. Prefer clear steps over dense one-liners.
2. **No Nested Ternaries**: Avoid nested ternary operators; prefer `if/else` chains or `switch` statements for multiple conditions.
3. **Remove Redundant Abstractions**: Eliminate "wrapper" functions or classes that don't add value beyond a direct check.
4. **Maintain Balance**: Avoid over-simplification that removes helpful abstractions or makes code harder to debug/extend.

## Process

1. read changed files first
2. identify safe simplification candidates
3. apply minimal behavior-preserving edits
4. run quick verification (build/tests if available)
5. summarize changes and any residual risks

## Safety Rules

- preserve public API behavior
- avoid changing side effects, order, or error semantics unless explicitly requested
- avoid broad file reformatting unrelated to simplification
- keep diffs small and reviewable

## Output Contract

When activated, return:

1. simplification opportunities found
2. applied behavior-preserving changes
3. verification status
4. remaining candidates not changed (if any)

---
name: tdd-workflow
description: "Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with practical coverage goals across unit, integration, and E2E tests. USE WHEN: adding new features; fixing bugs or regressions. NOT FOR: deep E2E framework patterns; post-implementation verification orchestration."
origin: ECC
---

# TDD Workflow

Use test-driven development to convert requirements into executable checks before implementation.

---

## Purpose

Increase delivery confidence by defining behavior in tests first, then implementing minimum code to pass.

---

## When to Activate

- adding new features
- fixing bugs or regressions
- refactoring risky logic
- adding API endpoints or core workflows
- improving reliability of unstable modules

---

## Scope Boundaries

Use this skill for:
- red/green/refactor execution
- test case design from user journeys
- coverage-driven completion criteria

Do NOT use this skill as primary source for:
- deep E2E framework patterns
- post-implementation verification orchestration

Delegation:
- use `e2e-testing` for Playwright suite architecture and flake handling
- use `verification-loop` for final build/lint/test gate before PR
- use `eval-harness` when measuring pass@k reliability across attempts

---

## Core Principles

1. tests before implementation
2. one behavior per test
3. include happy path, edge cases, and failure paths
4. keep tests deterministic and isolated
5. refactor only with tests green

---

## Workflow

## 1) Define User Journey and Acceptance Criteria

Express behavior from actor perspective and expected outcome.

## 2) Write Failing Tests (Red)

Create unit/integration/E2E tests appropriate to risk and scope.
Tests should fail for the right reason.

## 3) Implement Minimal Code (Green)

Write smallest change that makes tests pass.
Avoid speculative abstractions.

## 4) Refactor Safely (Refactor)

Improve readability/design while keeping test suite green.

## 5) Validate Coverage and Gaps

Target strong practical coverage, with critical paths fully covered.
Use explicit thresholds where project policy requires them.

---

## Test Mix Guidance

- Unit: pure logic, helpers, component behavior
- Integration: API/service/database interactions
- E2E: critical end-user workflows only

Default priority:
- heavy unit/integration coverage
- focused E2E on critical paths

---

## Quality Rules

- no brittle selector or timing assumptions in tests
- no test interdependence
- avoid mocking behavior you need to verify end-to-end
- ensure failure messages are diagnosable

---

## Common Anti-Patterns

Avoid:
- writing implementation before tests
- asserting internal implementation details instead of behavior
- over-mocking critical integration boundaries
- skipping negative-path tests
- accepting flaky tests as normal

---

## Completion Criteria

Before marking done:

- [ ] acceptance criteria mapped to tests
- [ ] all new tests pass
- [ ] regression tests for changed behavior exist
- [ ] critical error paths are covered
- [ ] coverage is acceptable for risk level and policy

---

## Output Contract

When activated, return:

1. user journeys and test map
2. red-phase test plan
3. implementation scope for green phase
4. refactor checklist
5. coverage gaps and next tests

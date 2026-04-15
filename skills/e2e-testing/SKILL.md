---
name: e2e-testing
description: "Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. USE WHEN: creating or refactoring Playwright E2E suites; setting up test architecture (folders, fixtures, POM). NOT FOR: unit/integration test strategy outside E2E scope; framework-specific frontend architecture decisions."
origin: ECC
---

# E2E Testing Patterns (Playwright)

Build stable, fast, and maintainable E2E suites with clear ownership, deterministic waits, and CI-ready artifacts.

---

## Purpose

This skill provides practical Playwright patterns for end-to-end testing quality at scale.
It focuses on reliability, execution speed, and debuggability.

---

## When to Activate

- creating or refactoring Playwright E2E suites
- setting up test architecture (folders, fixtures, POM)
- reducing flaky tests and intermittent CI failures
- integrating E2E into CI/CD pipelines
- defining artifact and report strategy

---

## Scope Boundaries

Use this skill for:
- Playwright test architecture and conventions
- Page Object Model and fixtures
- waiting strategy and flake reduction
- CI execution, retries, and artifact retention

Do NOT use this skill as primary source for:
- unit/integration test strategy outside E2E scope
- framework-specific frontend architecture decisions
- browser automation unrelated to Playwright

---

## Recommended Structure

```text
tests/
  e2e/
    auth/
    features/
    critical-flows/
  pages/
  fixtures/
  data/
playwright.config.ts
```

Guidelines:
- organize by user journey or domain flow
- keep pages reusable and intent-driven
- isolate test data fixtures from test logic

---

## Page Object Model Rules

- one page object per feature/page boundary
- expose business actions, not low-level selector choreography
- centralize selectors and avoid selector duplication
- keep assertions mostly in spec files unless reusable assertion helpers are needed

Example shape:
- `goto()`
- `search(query)`
- `createItem(input)`
- `getResultCount()`

---

## Test Authoring Rules

1. Prefer behavior-oriented test names.
2. Keep one core behavior per test.
3. Use deterministic waits (locator/response/state), never blind sleeps.
4. Use `data-testid` or stable semantic selectors.
5. Keep cleanup deterministic (API reset, fixture teardown, isolated user data).

Anti-patterns:
- `waitForTimeout` for synchronization
- deep copy-paste setup in each test
- assertions on volatile UI text not tied to behavior

---

## Wait and Synchronization Strategy

Preferred order:
1. locator auto-wait actions/assertions
2. explicit wait for response/request when network-driven
3. wait for URL/state transitions
4. `networkidle` only when appropriate for SPA behavior

Rule:
- every wait should map to a real state transition.

---

## Playwright Configuration Baseline

Recommended defaults:
- `retries`: CI > local
- `forbidOnly`: enabled in CI
- `trace`: `on-first-retry`
- `screenshot`: `only-on-failure`
- `video`: `retain-on-failure`
- `actionTimeout` and `navigationTimeout` explicitly configured
- browser project matrix only as needed by risk profile

Keep worker count conservative in unstable CI environments.

---

## Flaky Test Mitigation

1. Classify flakes by root cause: timing, data, environment, external dependency.
2. Reproduce with `--repeat-each` and targeted retries.
3. Replace timing assumptions with condition-based waits.
4. Quarantine only with linked issue and expiry review.
5. Remove quarantine once root cause is fixed.

Quarantine rule:
- any `fixme/skip` must include issue reference and owner.

---

## Artifact and Report Strategy

Capture at minimum:
- HTML report
- JUnit/XML or JSON for CI parsing
- trace on retry/failure
- screenshots/videos on failure

Retention guidance:
- PR runs: short retention
- nightly/regression runs: longer retention for diagnosis

Ensure artifact paths are deterministic and easy to discover.

---

## CI/CD Integration

Pipeline essentials:
1. install dependencies deterministically
2. install browser binaries
3. run tests with environment-specific `BASE_URL`
4. always upload artifacts (even on failure)
5. fail fast on infra setup errors, not on missing reports

Execution tiers:
- PR: smoke subset + fast checks
- main/nightly: broader regression matrix
- release gate: critical flow suite must pass

---

## Critical Flow Guardrails

For finance, auth, and other high-impact paths:
- avoid production-side effects unless explicitly approved
- use sandbox/staging with deterministic seed data
- verify preconditions and postconditions clearly
- increase trace and logging depth for these suites

For wallet/web3 flows:
- mock provider behavior deterministically when possible
- avoid real private keys in tests
- separate chain/network-dependent tests from core smoke suite

---

## Output Contract

When activated, return:

1. current E2E risk assessment (architecture, flake, CI reliability)
2. prioritized remediation plan
3. concrete Playwright config/spec/page updates
4. artifact/report policy
5. follow-up checklist for stabilization

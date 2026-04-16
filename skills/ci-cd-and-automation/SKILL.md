---
name: ci-cd-and-automation
description: "Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines, configuring test runners, or establishing deployment strategies (feature flags, canary)."
---

# CI/CD and Automation

## Overview

Automate quality gates so that no change reaches production without passing tests, lint, type checking, and build. CI/CD catches what humans and agents miss, and enforces standards consistently on every change.

**Shift Left:** Catch problems as early as possible. A bug caught in linting costs minutes; the same bug caught in production costs hours.

**Faster is Safer:** Smaller batches and more frequent releases reduce risk. A deployment with 3 changes is easier to debug than one with 30.

## When to Use

- Setting up a new project's CI pipeline.
- Adding or modifying automated checks (Lint, Type check, Test).
- Configuring deployment pipelines and feature flags.
- Debugging CI failure loops.

## The Quality Gate Pipeline

Every change must pass these gates:
1. **LINT CHECK**: Style and static analysis (eslint).
2. **TYPE CHECK**: Structural integrity (tsc).
3. **UNIT TESTS**: Logic verification (jest/vitest).
4. **BUILD**: Production bundle readiness.
5. **SECURITY AUDIT**: Dependency vulnerability scan (npm audit).

## Feature Flags & Deployment

- **Decouple Deployment from Release**: Use feature flags to ship code early and enable it only when ready.
- **Canary Rollouts**: Enable features for a small percentage of users first.
- **Emergency Rollbacks**: Ensure every deployment has a clear reversion path. Disable a flag instead of reverting code when possible.

## CI Optimization (If Pipeline > 10m)
- **Cache dependencies**: Use `actions/cache` for node_modules.
- **Parallelize jobs**: Run Lint, Types, and Tests in parallel.
- **Matrix Builds**: Shard test suites across multiple runners.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "CI is too slow, I'll bypass it" | Optimize the pipeline, don't skip it. Broken code is slower than any CI. |
| "The test is flaky, just re-run" | Flaky tests mask real bugs. Fix the root cause of the flake. |
| "Manual testing is enough" | Manual testing doesn't scale and isn't repeatable across commits. |

## Red Flags
- No CI pipeline or persistent failures ignored.
- Production deploys without a staging/preview environment.
- No rollback mechanism defined.
- Secrets stored in code or CI config files instead of a Secrets Manager.

## Verification
- [ ] Pipeline runs on every PR and push to main.
- [ ] Failures block merge (required status checks).
- [ ] Secrets are securely managed.
- [ ] Deployment has a clear rollback path.

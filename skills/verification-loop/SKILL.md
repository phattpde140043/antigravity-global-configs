---
name: verification-loop
description: "A comprehensive verification system for coding sessions: build, types, lint, tests, security checks, and final readiness gating before PR or handoff. USE WHEN: after a feature or significant change; before opening a PR. NOT FOR: writing test suites from scratch; deep security architecture audits."
origin: ECC
---

# Verification Loop

Run a repeatable quality gate before merge or handoff.

---

## Purpose

Provide a consistent verification sequence so changes are validated across correctness, quality, and security dimensions.

---

## When to Activate

- after a feature or significant change
- before opening a PR
- after refactoring
- when assessing release readiness

---

## Scope Boundaries

Use this skill for:
- final verification sequencing
- pass/fail reporting
- readiness decision with actionable blockers

Do NOT use this skill as primary source for:
- writing test suites from scratch
- deep security architecture audits

Delegation:
- use `tdd-workflow` for test-first development process
- use `security-review` for implementation-time security checklist
- use `securities-audit` for deep vulnerability assessment

---

## Verification Phases

1. Build verification
2. Type check/static analysis
3. Lint/style checks
4. Test suite and coverage
5. Security quick scan
6. Diff sanity review

Stop rule:
- if a blocking phase fails, stop and fix before continuing.

---

## Recommended Commands

Use project-appropriate commands (npm/pnpm/yarn, dotnet, python, etc.) and capture concise output.

Examples:
- build: project build command
- types: TypeScript/Python type checker
- lint: language linter
- tests: full or targeted suites with coverage
- security: secret pattern scan + dependency audit
- diff: changed files/stat review

---

## Security Quick Scan Baseline

- detect obvious secret patterns
- detect debug logging in sensitive code paths
- check dependency vulnerability status where available

Note:
- quick scan is not a substitute for full security audit.

---

## Reporting Format

Use a compact readiness report:

- Build: PASS/FAIL
- Types: PASS/FAIL (+count)
- Lint: PASS/FAIL (+count)
- Tests: PASS/FAIL (+summary + coverage)
- Security: PASS/FAIL (+issues)
- Diff review: file count + risk notes
- Overall: READY/NOT READY

Include numbered blocker list with next actions.

---

## Continuous Cadence

For long sessions:
- run partial verification after each milestone
- run full verification before final handoff

---

## Quality Gate

Before declaring READY:

- [ ] build is green
- [ ] no critical type/lint failures remain
- [ ] relevant tests pass with acceptable coverage
- [ ] no high-severity security blockers unresolved
- [ ] diff reviewed for unintended changes

---

## Output Contract

When activated, return:

1. phase-by-phase status
2. blockers and severity
3. remediation actions
4. final READY/NOT READY decision
5. minimal rerun plan after fixes

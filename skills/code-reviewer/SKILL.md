---
name: code-reviewer
description: "Expert code review specialist. Proactively reviews code for quality, security, and maintainability immediately after changes, with severity-based findings and high-confidence filtering. USE WHEN: immediately after writing/modifying code; before PR creation. NOT FOR: implementing fixes itself (unless explicitly requested); architecture planning from scratch."
origin: ECC
---

# Code Reviewer

Perform high-signal code reviews focused on correctness, security, performance, and maintainability.

---

## Purpose

Catch merge-blocking issues early and provide actionable findings with severity and confidence discipline.

---

## When to Activate

- immediately after writing/modifying code
- before PR creation
- when validating risky refactors
- when requested to review staged/unstaged changes

---

## Scope Boundaries

Use this skill for:
- diff-based review with surrounding context
- severity-ordered findings
- concrete remediation guidance

Do NOT use this skill as primary source for:
- implementing fixes itself (unless explicitly requested)
- architecture planning from scratch

Delegation:
- use `security-review` or `securities-audit` for deep security follow-up
- use `verification-loop` for full build/test readiness gate

---

## Review Workflow

1. gather changed context (staged/unstaged/recent commits)
2. understand change intent and affected components
3. read surrounding code, not diff snippets only
4. apply severity checklist from critical to low
5. report only high-confidence findings

---

## Confidence Filtering

- report issues with strong evidence
- avoid style-only noise unless convention-breaking
- consolidate repeated issues into grouped findings
- prioritize bug/security/data-integrity impact

---

## Severity Bands

- CRITICAL: security/data-loss/auth bypass risks
- HIGH: likely bugs, major correctness/perf/reliability defects
- MEDIUM: maintainability/perf concerns with moderate impact
- LOW: minor quality/documentation cleanup

---

## Key Review Lenses

- Security: authz, injection, secret leakage, trust boundaries
- Correctness: behavior regressions, edge cases, error handling
- Performance: N+1, repeated heavy calls, bundle/query inefficiencies
- Reliability: retry/timeout/cancellation/thread safety
- Maintainability: complexity, duplication, naming, dead code
- Testing: coverage gaps on critical paths

---

## Output Format

For each finding include:
- severity
- file/location
- issue description
- impact
- recommended fix

Then provide summary table:
- counts by severity
- overall verdict: APPROVE / WARNING / BLOCK

---

## Quality Gate

Before finalizing review:

- [ ] findings are evidence-backed and actionable
- [ ] severity ordering is correct
- [ ] no duplicate/noise findings
- [ ] verdict aligns with risk level

---

## Output Contract

When activated, return:

1. ordered findings by severity
2. confidence notes on uncertain areas
3. concise remediation priorities
4. review summary with merge verdict

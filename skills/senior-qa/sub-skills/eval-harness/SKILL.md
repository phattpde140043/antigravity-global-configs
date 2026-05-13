---
name: eval-harness
description: "Formal evaluation framework for AI coding sessions implementing eval-driven development principles: capability evals, regression evals, pass@k metrics, grader design, and release gating. USE WHEN: setting up EDD for an AI-assisted project; defining objective completion criteria for agent tasks. NOT FOR: framework-specific test implementation details; replacing unit/integration/e2e test strategy."
origin: ECC
tools: Read, Write, Edit, Bash, Grep, Glob
---

# Eval Harness

Implement eval-driven development (EDD) for AI-assisted coding workflows using explicit pass/fail criteria, repeatable graders, and reliability metrics.

---

## Purpose

Treat evals as test infrastructure for agent behavior and output quality.
Define success before implementation, run checks continuously, and gate delivery by measured reliability.

---

## When to Activate

- setting up EDD for an AI-assisted project
- defining objective completion criteria for agent tasks
- tracking reliability with pass@k and pass^k
- creating regression protection for prompt, model, or workflow changes
- benchmarking behavior across model/harness versions

---

## Scope Boundaries

Use this skill for:
- eval design and execution workflow
- grader strategy (code-based, model-based, human)
- reliability metrics and release gating
- eval artifact structure and reporting

Do NOT use this skill as primary source for:
- framework-specific test implementation details
- replacing unit/integration/e2e test strategy
- architecture decisions unrelated to evaluation methodology

---

## Core Philosophy

1. Define expected behavior before implementation.
2. Prefer deterministic evaluation whenever possible.
3. Track regression on every meaningful change.
4. Separate capability gains from regression safety.
5. Measure reliability, not only single-run success.

---

## Eval Types

## Capability Eval

Use to verify new behavior exists.

Template:

```markdown
[CAPABILITY EVAL: name]
Task: [what should be accomplished]
Success Criteria:
- [ ] criterion 1
- [ ] criterion 2
- [ ] criterion 3
Expected Output: [observable result]
```

## Regression Eval

Use to ensure existing behavior still works.

Template:

```markdown
[REGRESSION EVAL: name]
Baseline: [commit/checkpoint]
Checks:
- check-1: PASS/FAIL
- check-2: PASS/FAIL
- check-3: PASS/FAIL
Result: X/Y passed (baseline Y/Y)
```

---

## Grader Strategy

## 1) Code-Based Grader (Default)

Use deterministic commands and assertions first.
Examples:
- pattern checks via grep/glob
- build/test/lint command outcomes
- file existence and schema checks

## 2) Model-Based Grader

Use only when deterministic grading is insufficient.
Require explicit rubric and structured scoring.

Recommended rubric:
- task completion
- correctness
- edge-case handling
- error handling
- maintainability

## 3) Human Review Gate

Require manual approval for high-risk areas:
- security-sensitive flows
- production data handling
- financial/critical operations
- policy and compliance implications

---

## Metrics

## pass@k

At least one success in k attempts.
- pass@1: first-attempt quality
- pass@3: short-horizon reliability

## pass^k

All k attempts succeed consecutively.
Use for high-confidence release gates.

Default targets (suggested):
- capability evals: pass@3 >= 90%
- regression evals on critical paths: pass^3 = 100%

---

## Workflow

## Step 1: Define (Before Coding)

Create eval definition with:
- capability checks
- regression checks
- metrics target
- risk level

## Step 2: Implement

Make changes guided by defined evals only.
Avoid unrelated scope expansion.

## Step 3: Evaluate

Run capability and regression graders.
Record pass/fail and attempt count.

## Step 4: Report

Publish summary with:
- score by eval group
- pass@k and pass^k
- failures and root cause notes
- ship recommendation

---

## Eval Artifacts

Recommended structure:

```text
.claude/
  evals/
    feature-name.md
    feature-name.log
    baseline.json
```

If the repo uses a different conventions folder, keep names stable and machine-readable.

---

## Report Template

```markdown
EVAL REPORT: [feature-name]

Capability Evals:
- [name]: PASS/FAIL (pass@attempt)
- ...

Regression Evals:
- [name]: PASS/FAIL
- ...

Metrics:
- pass@1: X%
- pass@3: Y%
- pass^3: Z%

Open Failures:
- [failure], [impact], [owner], [next action]

Status:
- READY / NOT READY
```

---

## Release Gating Rules

Ship only when all are true:
1. regression gate passes at required threshold
2. no unresolved high-risk failure
3. capability targets are met or exceptions documented
4. human review completed for required risk classes

If any gate fails, output NOT READY with concrete remediation actions.

---

## Best Practices

1. Keep evals fast enough to run frequently.
2. Version eval definitions with code changes.
3. Prefer small eval units with clear observability.
4. Track trend over time, not single snapshot.
5. Avoid rubric drift by reusing stable grader templates.

---

## Hard Bans

Delete and rewrite if present:
- success claims without measured evidence
- reliance on only one open-ended model grader
- changing success criteria after seeing failures
- regression checks omitted for critical flows

---

## Output Contract

When activated, return:

1. eval plan (capability + regression)
2. grader mapping and metric targets
3. execution summary
4. pass@k/pass^k metrics
5. ship decision with explicit rationale

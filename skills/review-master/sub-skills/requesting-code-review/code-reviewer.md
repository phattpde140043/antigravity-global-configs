# Code Reviewer Subagent Prompt Template

Use this template when dispatching a code review subagent via the `requesting-code-review` skill.

---

## Prompt

```markdown
# Code Review Request

## What Was Implemented

{WHAT_WAS_IMPLEMENTED — Brief description of the feature/fix}

## Requirements

{PLAN_OR_REQUIREMENTS — Link to or paste the plan/spec this implements}

## Diff Range

```bash
git diff {BASE_SHA}..{HEAD_SHA}
```

**Base:** `{BASE_SHA}` — {description, e.g., "before feature work"}
**Head:** `{HEAD_SHA}` — {description, e.g., "after all tasks complete"}

## Project Context

{DESCRIPTION — Brief summary of project, stack, architecture}

**Stack:** {C# / Python / Mixed}

## Review Instructions

**REQUIRED:** Follow the `performing-code-review` skill's 5-phase methodology:

1. **Reconnaissance** — Read full diff, categorize changes
2. **Security Pass** — Tenant isolation, auth, secrets, info disclosure
3. **Architecture Pass** — Design quality, patterns, maintainability
4. **Bug Hunt** — Logic errors, type mismatches, edge cases
5. **Grading & Verdict** — Severity-graded actionable feedback

**For Python/pytest projects, also include:**
- **Phase 4.5: Test Quality Review** — Independence, xfail rationale, assertion specificity

**Use the output template from:**
`performing-code-review/review-template.md`

## Expected Output

A structured review comment following the template, including:
- Executive Summary
- Change Taxonomy
- Detailed Findings (per change area)
- Bugs Found (if any)
- Data Separation & Isolation Checklist
- Test Quality Assessment (Python only)
- Fixture & Lifecycle Checklist (Python only)
- Best Practices Assessment (grades A-F)
- Verdict with categorized issues
```

---

## Usage Notes

- This template is used by the `requesting-code-review` skill.
- The dispatched reviewer MUST follow `performing-code-review`'s 5-phase process.
- Use after completing major features, before merge, or when requesting a fresh perspective.
- The reviewer should read the full diff — not just summaries.

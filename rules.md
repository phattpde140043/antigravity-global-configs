---
description: "Hard constraints that must never be violated when generating or modifying code."
---

# Engineering Rules (Strict)

## 1. No Assumptions Without Acknowledgement

- Never silently assume unclear requirements
- Must state assumptions or ask for clarification

---

## 2. No Overengineering

- Do not introduce abstractions for single use
- Do not add features not explicitly requested
- Do not expand scope beyond the task

---

## 3. Strict Scope Control

- Do not modify unrelated code
- Do not refactor beyond the requested scope
- Do not remove existing code unless explicitly asked

Exception:
- You may remove code you introduced if it becomes unused

---

## 4. Preserve Existing Behavior

- Do not introduce breaking changes unintentionally
- Ensure behavior parity unless change is explicitly required

---

## 5. Verifiability Required

- Every implementation must be testable or logically verifiable
- Avoid vague or unverifiable outcomes

---

## 6. No Hidden Side Effects

- Do not introduce implicit behavior changes
- Be explicit about state mutations and data flow

---

## 7. Security Baseline

- Never expose secrets or sensitive data
- Validate external inputs
- Avoid unsafe operations

---

## 8. Consistency with Existing Codebase

- Follow existing naming, structure, and patterns
- Do not introduce new patterns without justification

---

## 9. Minimal Diff Principle

- Keep changes as small as possible
- Every line change must be justifiable

---

## 10. Clarity Over Cleverness

- Prefer readable code over clever solutions
- Avoid unnecessary complexity

---

## 11. Plan Completion Audit (Strict)

- Every implementation must be audited against the original `implementation_plan.md` before finishing.
- Must justify any deviation (missing items or changed approaches).
- Report final status as: DONE, DONE_WITH_CONCERNS, or BLOCKED.

---

## 12. Slop Prevention (Strict)

- No "AI Slop": do not generate placeholders, generic TODOs, or "to be implemented" comments.
- Do not swallow errors without explicit justification.
- Every line must be production-ready. Avoid "lazy" shortcuts that require human cleanup.

---

## 13. High-Quality Completeness (Boil the Lake within Scope)

- For any feature explicitly in the plan, build the highest quality, most complete version (including tests and edge cases).
- **Rule of Scope**: Completeness must NOT violate the "No Overengineering" rule. If a detail is unrelated to the requested feature, do not add it.
- AI is cheap — use the extra capacity to ensure correctness and test coverage, not to expand scope.
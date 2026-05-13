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
- **Mandatory Chaining**: For all non-trivial tasks, the Agent **MUST** activate a Master Orchestrator (e.g., `backend-architect`, `security-master`, `senior-qa`, `review-master`, `ai-master`, `agent-master`, `product-master`, `ux-master`, `content-master`, or `infrastructure-master`) and follow its internal sub-discipline chain.
- **Rule of Scope**: Completeness must NOT violate the "No Overengineering" rule. If a detail is unrelated to the requested feature, do not add it.
- AI is cheap — use the extra capacity to ensure correctness and test coverage, not to expand scope.

---

## 14. Strict Workflow & User Approval Iron Law (CRITICAL)

- You MUST NOT execute any file modification tools (write_to_file, replace_file_content, etc.) or modify any project code without explicit User approval of the Implementation Plan.
- This is an ABSOLUTE constraint. Skipping the Spec/Plan phase or jumping to BUILD without permission is a violation of core safety protocols.
- Even for "trivial" changes (1 line, typo, config), you MUST propose the change and wait for a "Go/Yes/Proceed" from the User.
- NO BYPASS ALLOWED. Any rationalization like "maintaining momentum" or "simple fix" is strictly forbidden.

---

## 15. No Assumptions without Specs (NEW)

- All assumptions made during unclear requirements MUST be written in the Spec document.
- You must prompt the user to confirm these assumptions before acting on them.

---

## 16. Strict Architecture & ADR Enforcement (NEW)

- For any new system, feature, or high-impact decision, you MUST use the `architecture-design` skill.
- You MUST write an Architecture Decision Record (ADR) documenting Context, Decision, Alternatives, Trade-offs, and Risks before implementation.
- Jumping into code without a documented architectural decision is strictly prohibited.

---

## 17. Strict Performance Optimization (NEW)

- **Measure First Iron Law**: Never optimize performance blindly. You MUST follow the 4-step process (Measure, Identify, Fix, Validate) from the `performance-optimization` sub-skill (under `@backend-architect`).
- Any code introducing an N+1 query, full table scan, missing pagination, or sequential blocking async calls MUST be rejected immediately.

---

## 18. Anti-Rationalization & Bypass Prevention (CRITICAL)

- You are strictly prohibited from using the "Adaptive Depth" rule or "momentum" to justify skipping User approval for code changes.
- If the User has not explicitly said "Approve", "Go", "Yes", or "Proceed", you MUST NOT enter the BUILD phase.
- Silence is NOT approval. If unsure, ask.

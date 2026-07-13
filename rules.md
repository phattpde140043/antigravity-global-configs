---
description: "Hard constraints that must never be violated when generating or modifying code."
---

# Engineering Rules (Strict)

## 🧭 The Spine — 5 Core Principles

The memorable index to everything below. Structured after [Andrej Karpathy's coding guidelines](https://x.com/karpathy). The **numbered rules that follow are the authoritative detail** — this spine is how to hold them in your head, not a replacement for them. Bias toward caution over speed; for trivial tasks, use judgment.

1. **Think before coding.** Surface assumptions, name confusion, present tradeoffs, and get approval before you touch code — never pick a path silently. → *Rules 1, 15, 16.*
2. **Simplicity first.** The minimum code that solves the problem, nothing speculative. If 200 lines could be 50, rewrite it. No slop, no cleverness. → *Rules 2, 10, 12, 13.*
3. **Surgical changes.** Touch only what the request requires; preserve existing behavior and style; clean up only your own mess. Every changed line traces to the ask. → *Rules 3, 4, 6, 8, 9.*
4. **Goal-driven & verified.** Turn the task into a checkable success criterion, then loop until it passes — including performance and plan-completion. Weak criteria ("make it work") are not done. → *Rules 5, 11, 17.*
5. **Guardrails are non-negotiable.** Security baseline, the user-approval iron law, no rationalizing past a rule, and skill-registry integrity hold under every pressure. → *Rules 7, 14, 18, 19, 20.*

---

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

---

## 19. Aggressive Skill Activation (The 1% Rule)

- If you think there is even a **1% chance** a skill might apply to what you are doing, you **ABSOLUTELY MUST** invoke the skill.
- This is not negotiable. This is not optional. You cannot rationalize your way out of this.
- Invoke relevant skills BEFORE any response or action, including clarifying questions. Skills tell you HOW to gather information and approach the task.

## 20. Skill Registry Integrity — Router Must Not Lie (NEW)

Rule 19 governs *invoking* skills (be liberal at runtime). This rule governs *authoring* them (be disciplined when you add/rename/remove/relocate one).

- **Router-must-not-lie:** whenever you add, rename, remove, or relocate a skill, in the SAME change re-sync `skill-router.md` and the parent master's `SKILL.md`. A router that references a missing skill (dangling link) or omits a present one (orphan), or a master that lists a moved sub-skill, is a defect — fix it before finishing.
- **Single source of truth:** a given capability lives in exactly one canonical skill. If two masters need it, one holds the skill and the other cross-references it (`../<master>/sub-skills/<name>/SKILL.md`) — never a second divergent copy.
- **Split only when the cut earns it:** add a new skill only when it has a distinct trigger or another skill must reach it. Prefer extending or disambiguating an existing skill over creating a near-duplicate. No empty master orchestrators — a master with zero sub-skills belongs in `archive/`, not `skills/`.
- **Prune, don't just add:** when editing a skill, hunt no-ops and duplication and remove them. See [Writing Skills → Skill Architecture & Pruning](skills/agent-master/sub-skills/writing-skills/SKILL.md) for the authoring standard.

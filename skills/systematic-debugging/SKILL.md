---
name: systematic-debugging
description: "Elite debugging framework based on the Iron Law: No fixes without root cause. Incorporates structural tracing and defense-in-depth."
---

# Systematic Debugging (Tier 2)

Transform debugging from intuitive guesswork into a high-discipline investigative process.

## ⚡ Quick References (MANDATORY)
- **[Debugging Playbook](references/debugging-playbook.md)**: 4-Phase process and Multi-Agent Review.
- **[Root Cause Tracing](references/root-cause-tracing.md)**: Backward tracing techniques from symptom to trigger.
- **[Defense-in-Depth](references/defense-in-depth.md)**: Building multi-layered protection to prevent bug recurrence.
- **[Condition-Based Waiting](references/condition-based-waiting.md)**: Handling non-deterministic (flaky) and asynchronous errors.

---

## ⚖️ The Iron Law
**NEVER propose a solution without identifying the Root Cause.**
If you haven't identified the exact code and state that triggered the failure, you are "guessing." Guessing is unacceptable.

---

## 🛑 The Stop-the-Line Rule
When a bug or regression is detected:
1. **STOP** adding new features.
2. **PRESERVE** evidence (logs, stack traces).
3. **ISOLATE** the environment.
4. **INVESTIGATE** until root cause is found.

---

## 🛠️ Operating Pipeline (4 Phases)

### Phase 1: Observation & Reproduction (Proof)
Create a test case or scenario that reproduces the error 100% of the time. "You don't have a bug until you have a failing test."

### Phase 2: Structural Investigation (Source)
Utilize **Root Cause Tracing** and **5 Whys**. Do not stop at the first error message.

### Phase 3: The Atomic Fix (Precise Repair)
Implement the minimum required change to solve the issue at its root. Adhere to the **Surgical Changes** principle.

### Phase 4: Defense-in-Depth (Hardening)
Implement protection at 4 layers: Input validation, Business logic invariants, Environment guards, and High-signal logging.

---
name: agent-introspection-debugging
description: "Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports. USE WHEN: Maximum tool call or loop-limit failures; Repeated retries with no forward progress. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Agent Introspection Debugging

## Purpose

Enable the agent to **debug its own execution** when it is failing repeatedly, looping, or drifting from the intended task.

This is a **meta-skill** — it governs agent behavior, not system/code quality.

---

# When to Activate

- Maximum tool call or loop-limit failures
- Repeated retries with no forward progress
- Context growth or prompt drift degrading output quality
- File-system or environment state mismatch between expectation and reality
- Tool failures that are likely recoverable with diagnosis

---

# Scope Boundaries

**This skill covers:**
- Capturing agent failure state before retrying blindly
- Diagnosing agent-specific failure patterns (loops, drift, stale state)
- Applying contained recovery actions at the agent level
- Producing a structured debug report for the human

**This skill does NOT cover** (use the referenced skill instead):
- System resilience patterns (retry, circuit breaker, timeout) → `resilience-patterns`
- Code quality self-review after generating code → `code-generation` (Self-Review phase)
- Pre-code risk analysis → `implementation-planning`
- Security vulnerability detection → `securities-audit`

---

# Four-Phase Workflow

## Phase 1 — Failure Capture

Before attempting recovery, record the failure precisely.

Capture:
- Error type, message, and stack trace (when available)
- Last meaningful tool call sequence (what succeeded, what failed)
- What the agent was trying to accomplish
- Context pressure signals: repeated prompts, oversized logs, duplicated plans
- Environment assumptions: cwd, branch, expected files, service state

Template:

```markdown
## Failure Capture
- Task:
- Goal in progress:
- Error:
- Last successful step:
- Last failed tool / command:
- Repeated pattern (if any):
- Environment assumptions to verify:
```

---

## Phase 2 — Root-Cause Diagnosis

Match the failure to a known agent-level pattern before changing anything.

| Pattern | Likely Cause | Diagnostic Check |
|---------|-------------|-----------------|
| Same tool called 3+ times with similar input | Loop — no exit condition or wrong assumption | Inspect last N tool calls for repetition |
| Context keeps growing, reasoning quality drops | Unbounded notes, duplicated plans, oversized pasted output | Identify low-signal bulk in recent context |
| File missing after write / stale diff | Wrong cwd, branch drift, or race condition | Re-check path, `pwd`, `git status`, actual file existence |
| Tests still failing after "fix" applied | Wrong hypothesis — fix targeted the wrong root cause | Isolate the exact failing assertion and re-derive the bug |
| Tool returns unexpected schema or empty result | Environment changed or wrong tool parameters | Verify tool input, re-read source file, check preconditions |
| Agent optimizing a subtask that no longer matters | Objective drift — lost the real goal | Restate the original user request in one sentence |

Diagnosis questions:
- Is this a **logic failure** (wrong reasoning), **state failure** (stale assumption), **environment failure** (tool/service issue), or **policy failure** (hitting a guardrail)?
- Is the failure deterministic or transient?
- What is the smallest reversible action that would validate the diagnosis?

---

## Phase 3 — Contained Recovery

Recover with the **smallest action** that changes the diagnostic surface.

### Recovery Priority Order

1. **Restate the real objective** in one sentence
2. **Verify world state** instead of trusting memory (re-read files, check cwd, git status)
3. **Shrink the failing scope** to one file, one test, or one command
4. **Trim low-signal context** — keep only active goal, blockers, and evidence
5. **Run one discriminating check** — a single command that proves or disproves the hypothesis
6. **Only then retry** the original action
7. **Escalate to human** when failure is high-risk, externally blocked, or persists after one recovery cycle

### Anti-Patterns

- Retrying the same action 3+ times with slightly different wording
- Adding more context/notes hoping the next attempt will "just work"
- Switching to a completely different approach without diagnosing the current failure
- Claiming recovery without evidence (e.g., "I fixed it" with no verification)

Template:

```markdown
## Recovery Action
- Diagnosis:
- Smallest action taken:
- Why this is safe/reversible:
- Evidence that would prove success:
```

---

## Phase 4 — Introspection Report

End every recovery cycle with a structured report. Never end with just "I fixed it."

```markdown
## Agent Self-Debug Report
- Task:
- Failure pattern:
- Root cause:
- Recovery action:
- Result: success | partial | blocked
- Token/effort burn estimate: low | medium | high
- Follow-up needed: (yes/no + what)
- Lesson: (one-line insight to avoid recurrence)
```

---

# Integration with Existing Skills

| Situation after recovery | Next skill to use |
|-------------------------|-------------------|
| Code was changed during recovery | `code-generation` Self-Review phase |
| Recovery revealed a design ambiguity | `architecture-design` or `implementation-planning` |
| Recovery revealed a security concern | `securities-audit` |
| Failure pattern is worth remembering | Store in `/memories/` for future reference |

---

# Enforcement

- Do NOT retry more than once without running Phase 1–2 first
- Do NOT claim recovery without providing Phase 4 report
- Do NOT use this skill as a substitute for code self-review — that belongs in `code-generation`
- Do NOT diagnose system resilience issues (retry storms in production, circuit breakers) — that belongs in `resilience-patterns`

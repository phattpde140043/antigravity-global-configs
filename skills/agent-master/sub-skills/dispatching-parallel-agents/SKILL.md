---
name: dispatching-parallel-agents
description: "Parallel debugging and investigation strategies. Part of the agent-master discipline."
---

# Dispatching Parallel Agents

## 🧭 Strategy
- **One Agent per Domain**: Dispatch independent agents for unrelated failures (e.g., Subsystem A vs Subsystem B).
- **Concurrent Investigation**: Parallelize root cause analysis to save time.
- **Review & Integrate**: Review all findings concurrently and integrate changes once the full suite is verified.

## 🛑 HARD LIMIT: No Parallel Building
**NEVER** use parallel agents for implementation plan execution (BUILD phase).
- **Reason**: Causes file conflicts, inconsistent state, and broken integrations.
- **Alternative**: Use `subagent-driven-development` (sequential subagent-per-task).

## ✅ Use When
- 3+ test files failing with different root causes.
- Multiple subsystems broken independently.
- No shared state between investigations.

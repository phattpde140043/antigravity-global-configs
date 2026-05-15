---
name: executing-plans
description: "Execution logic for implementation plans. Part of the agent-master discipline."
---

# Executing Plans

## 🧭 Execution Logic
Select the optimal execution model based on task independence:

| Condition | Recommended Skill |
| :--- | :--- |
| Tasks are independent & subagents available | `subagent-driven-development` |
| Tasks are tightly coupled | `executing-plans` (Manual/Sequential) |
| Requirements are vague | `brainstorming` |

## ⚙️ Process
1. **Load & Review**: Identify concerns before starting.
2. **Execute**: Mark tasks as `in_progress`, follow steps exactly, and run verifications.
3. **Finish**: Use `finishing-a-development-branch` protocol.

## 🛑 STOP Rule
Stop immediately if:
- Hit a blocker or missing dependency.
- Verification fails repeatedly.
- Plan has critical gaps.

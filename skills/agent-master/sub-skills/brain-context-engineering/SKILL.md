---
name: brain-context-engineering
description: "Unified orchestrator for high-fidelity project memory and context engineering. Mandatory for complex projects (>2,000 LOC). Part of the agent-master discipline."
---

# Brain Context Engineering (Unified Chain)

Holistic "Total Context" strategy that prevents information loss and maximizes reasoning quality for complex systems.

## 🔗 The Skill Chain

1.  **Fundamental Grounding**: Manage token budgets and attention curves.
2.  **Storage & Persistence**: Sync `.brain/`, `memory/`, and `scratch/` directories.
3.  **Performance & Efficiency**: Apply observation masking and iterative compaction.
4.  **Quality Control**: Verify generated code aligns with all loaded context.

## ⚙️ Mandatory Execution Routine

### Phase 1: Context Setup (DEFINE/PLAN)
- **Initialize**: Sync persistent memory and load previous decisions from the filesystem.
- **Budgeting**: Calculate current token capacity and prioritize relevant files.

### Phase 2: Implementation Focus (BUILD)
- **Optimization**: Condense large documents into semantic snapshots.
- **Signal**: Ensure tool outputs are high-signal and low-token.

### Phase 3: Validation & Handoff (VERIFY/REVIEW)
- **Verification**: Check implementation against the entire context history.
- **Consolidation**: Update `memory/handoff.json` and ADRs to reflect the new state.

> [!IMPORTANT]
> Never operate in isolation. Always verify if siblings in the context chain are required for the current task level.

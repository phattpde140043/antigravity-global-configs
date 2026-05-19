---
name: brain-context-engineering
description: "Unified orchestrator for high-fidelity project memory and context engineering. Mandatory for complex projects (>2,000 LOC). Part of the agent-master discipline."
---



# Brain Context Engineering (Unified Chain)
Holistic "Total Context" strategy that prevents information loss and maximizes reasoning quality for complex systems.

This master skill orchestrates the ensemble of 14 specialized context engineering components. By activating `@brain-context-engineering`, the Agent commits to a holistic "Total Context" strategy that prevents information loss and maximizes reasoning quality for complex backend developments.

## 🔗 The Skill Chain
1.  **Fundamental Grounding**: Manage token budgets and attention curves.
2.  **Storage & Persistence**: Sync `.brain/`, `memory/`, and `scratch/` directories.
3.  **Performance & Efficiency**: Apply observation masking and iterative compaction.
4.  **Quality Control**: Verify generated code aligns with all loaded context.

## ⚙️ Mandatory Execution Routine


### Phase 1: Context Setup (DEFINE/PLAN)
- **Initialize**: Sync persistent memory and load previous decisions from the filesystem.
- **Budgeting**: Calculate current token capacity and prioritize relevant files.

- **Invoke `@filesystem-context`**: Initialize/Sync `.brain/`, `memory/`, and `scratch/` directories.
- **Invoke `@context-fundamentals`**: Calculate the current token budget and attention curve impacts.
- **Invoke `@memory-systems`**: Load pertinent previous decisions from the filesystem.

### Phase 2: Implementation Focus (BUILD)
- **Optimization**: Condense large documents into semantic snapshots.
- **Signal**: Ensure tool outputs are high-signal and low-token.

- **Invoke `@context-optimization`**: Apply observation masking and iterative compaction.
- **Invoke `@tool-design`**: Ensure tool outputs are high-signal/low-token.
- **Invoke `@context-compression`**: Condense large documents into semantic snapshots.

### Phase 3: Validation & Handoff (VERIFY/REVIEW)
- **Verification**: Check implementation against the entire context history.
- **Consolidation**: Update `memory/handoff.json` and ADRs to reflect the new state.

> [!IMPORTANT]
> Never operate in isolation. Always verify if siblings in the context chain are required for the current task level.

- **Invoke `@evaluation`**: Verify that the generated code aligns with all loaded context.
- **Invoke `@multi-agent-patterns`**: (If applicable) partition the review across specialized sub-agents.
- **Invoke `Post-Task Memory Consolidation`**: Update persistent memory files to reflect the new system state.
---

## The Skill Chain (Mandatory Loading)
When this skill is triggered, the Agent **MUST** recursively apply the principles from the following sub-skills:

1.  **Fundamental Grounding**: `@brain-context-engineering/context-fundamentals`
2.  **Storage & Persistence**: `@brain-context-engineering/filesystem-context` & `@brain-context-engineering/memory-systems`
3.  **Performance & Efficiency**: `@brain-context-engineering/context-optimization` & `@brain-context-engineering/context-compression`
4.  **Failure Mitigation**: `@brain-context-engineering/context-degradation` & `@brain-context-engineering/latent-briefing`
5.  **Architecture & Tooling**: `@brain-context-engineering/multi-agent-patterns` & `@brain-context-engineering/tool-design`
6.  **Quality Control**: `@brain-context-engineering/evaluation` & `@brain-context-engineering/advanced-evaluation`
7.  **Specialized Reasoning**: `@brain-context-engineering/project-development`, `@brain-context-engineering/bdi-mental-states`, & `@brain-context-engineering/hosted-agents`

---

## Mandatory Execution Routine
To ensure "all skills are called" as requested, follow this sequence for every non-trivial task:

## Recursive Trigger Logic
> [!IMPORTANT]
> If any sub-skill folder is accessed directly, the Agent must treat it as a trigger for this Master Chain. Do not operate in isolation; verify if siblings in the chain (e.g., `evaluation` after `optimization`) are also required for the current task.

---

## Skill Metadata
- **Version**: 1.0.0 (Unified Chain)
- **Relationship**: Parent to 14 Granular Sub-skills.
- **Last Updated**: 2026-04-19

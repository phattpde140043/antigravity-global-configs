---
name: context-rehydration
description: "Advanced semantic memory rehydration for AI agents. Strategies for restoring complex project context using temporal decay, decision weights, and multi-modal embedding logic."
---

# Semantic Context Rehydration

Restore high-fidelity project context across multi-agent or multi-session workflows.

## 🏗️ Rehydration Strategies

### 1. Relevance Scoring (Ranking)
Rank context components using a composite score:
- **Temporal Relevance**: Recent work and decisions are more critical.
- **Decision Weight**: High-impact architectural pivots get priority.
- **Semantic Similarity**: Aligning context with the immediate task goals.

### 2. Multi-Modal Retrieval
- **Text & Code**: Traditional RAG on codebase and docs.
- **Architectural Diagrams**: Restoring structural mental models.
- **Decision Trails**: Auditing `overview.txt` and ADRs for the "Why".

### 3. Token Budget Management
- **Incremental Loading**: Rehydrate in stages (Summary -> Critical Files -> History).
- **Dynamic Pruning**: Discard low-signal logs once a consolidated summary is restored.

## 🛠️ Restoration Patterns
- **Full Restoration**: For project resumption after long breaks.
- **Incremental Update**: For syncing new changes into existing mental models.
- **Context Merging**: Resolving semantic conflicts between parallel agent branches.

## 📋 Verification Checklist
- [ ] Is the current task aligned with the restored project overview?
- [ ] Are all critical architectural decisions (ADRs) loaded?
- [ ] Is the token budget optimized for high-signal context?
- [ ] Are there any semantic conflicts in the restored memory?
- [ ] Is the decision trail traceable back to the previous session?

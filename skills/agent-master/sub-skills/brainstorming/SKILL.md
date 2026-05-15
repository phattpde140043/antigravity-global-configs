---
name: brainstorming
description: "Mandatory protocol for creative work, feature design, and requirement exploration. Part of the agent-master discipline."
---

# Brainstorming Ideas Into Designs

Turn abstract ideas into fully formed designs and specs through structured dialogue.

## 🛑 HARD-GATE
**Do NOT** invoke any implementation skill, write any code, or scaffold any project until the design is presented and **APPROVED BY THE USER**. This applies to EVERY project, regardless of simplicity.

## 📋 Execution Checklist

1.  **Explore Context**: Check files, docs, and recent commits.
2.  **Clarifying Questions**: Ask one at a time to understand purpose, constraints, and success criteria.
3.  **Propose Approaches**: Present 2-3 options with trade-offs and a recommendation.
4.  **Present Design**: Scale sections to complexity; get approval after each section.
5.  **Write Spec**: Save to `docs/specs/` and run the Spec Review Loop.

## 🖼️ Visual Companion
When questions involve UI/UX, layouts, or architecture diagrams, offer the **Visual Companion** (browser-based mockups).
- **Offer Rule**: The offer to use the browser MUST be its own message.
- **Decision**: Use browser for visual content (mockups); use terminal for text content (logic/requirements).

## 🔗 Transition
The ONLY skill to invoke after successful brainstorming is `implementation-planning`.

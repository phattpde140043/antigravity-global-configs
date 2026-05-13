---
name: agent-master
description: "Master Agent Orchestrator. Coordinates Core Capabilities, Debugging, Planning, and Context Engineering."
category: automation
metadata:
  category: master-orchestrator
  triggers: [debugging, planning, code-generation, context-engineering]
---

# 🧠 Agent Master Orchestrator

The operational lead for agent efficiency and reliability. This master skill coordinates the core loops that allow an agent to function effectively within a workspace. Expert in autonomous agent coordination, multi-agent systems, and specialized tool orchestration.

## 🧭 Agentic Strategy
- **Computer Use (Visual Agents)**: Implement the **Perception-Reasoning-Action** loop for direct computer interaction (mouse/keyboard) within sandboxed environments (Docker/Xvfb).
- **Parallel Workspace Orchestration**: Configure isolated coding environments (ports, Redis DBs, secrets) for parallel agent execution (Conductor pattern).
- **Contextual Intelligence**: Master **Context Window Management**, **Context Restoration** (save/restore state), and **Contextual Chunking** for high-precision memory.
- **Autonomous Loop**: Follow the **Think-Decide-Act-Observe** cycle for self-correcting task execution.

## 🧭 Intent Discovery (Vague Requests)
When a user is unsure where to start, use these **Funnel Questions** to identify the best Master Discipline:
1. **Area**: Is this about Coding, Security, AI, DevOps, or Planning?
2. **Specificity**: Do you have a clear spec, or are we starting from scratch?
3. **Stack**: What technologies are involved (React, Python, AWS, etc.)?
4. **Mode**: Should I work autonomously or collaboratively with you?

## 🚀 Orchestration Strategy
- **Master-First**: Always trigger a Master Discipline for non-trivial tasks.
- **Sub-Skill Delegation**: Use Master Orchestrators to chain specialized expertise.
- **Verification Loop**: Ensure every autonomous step is validated before proceeding.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing core agent tasks, you **MUST** chain to the following sub-skills:

### 1. Planning & Execution
- For **Implementation Planning**:
  👉 **[Implementation Planning](sub-skills/implementation-planning/SKILL.md)**
- For **Task Breakdown** and Management:
  👉 **[Planning and Task Breakdown](sub-skills/planning-and-task-breakdown/SKILL.md)**
- For **Workflows** (DMUX):
  👉 **[DMUX Workflows](sub-skills/dmux-workflows/SKILL.md)**

### 2. Debugging & Error Handling
- For **Systematic Debugging**:
  👉 **[Systematic Debugging](sub-skills/systematic-debugging/SKILL.md)**
- For **Error Analysis**:
  👉 **[Error Detective](sub-skills/error-detective/SKILL.md)**
- For **Build Failures**:
  👉 **[Build Error Resolver](sub-skills/build-error-resolver/SKILL.md)**
- For **Agent Introspection**:
  👉 **[Agent Introspection Debugging](sub-skills/agent-introspection-debugging/SKILL.md)**

### 3. Code Crafting
- For **Code Generation**:
  👉 **[Code Generation](sub-skills/code-generation/SKILL.md)**
- For **Code Exploration**:
  👉 **[Code Explorer](sub-skills/code-explorer/SKILL.md)**
- For **Simplification**:
  👉 **[Code Simplifier](sub-skills/code-simplifier/SKILL.md)**
- For **Source-Driven Development**:
  👉 **[Source Driven Development](sub-skills/source-driven-development/SKILL.md)**
- For **Spec-Driven Development**:
  👉 **[Spec Driven Development](sub-skills/spec-driven-development/SKILL.md)**

### 4. Infrastructure & Context
- For **CI/CD and Automation**:
  👉 **[CI/CD and Automation](sub-skills/ci-cd-and-automation/SKILL.md)**
- For **Context Engineering**:
  👉 **[Context Engineering](sub-skills/context-engineering/SKILL.md)**
- For **Brain Context**:
  👉 **[Brain Context Engineering](sub-skills/brain-context-engineering/SKILL.md)**
- For **Migrations**:
  👉 **[Deprecation and Migration](sub-skills/deprecation-and-migration/SKILL.md)**

---

## 🏗️ Operating Pipeline
1. **Intake**: Audit workspace surface area and clarify requirements.
2. **Planning**: Break down tasks and create implementation plans.
3. **Execution**: Generate code following spec-driven or source-driven patterns.
4. **Correction**: Systematically debug and resolve any errors found.

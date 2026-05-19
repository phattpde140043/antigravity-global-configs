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

When performing core agent tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure structured planning, development, and systematic debugging:

### 🔄 Sequential Sub-Skill Pipeline
```
[Brainstorming] ──→ [Implementation Planning] ──→ [Code Generation] ──→ [Systematic Debugging] ──→ [Handoff]
```


### 1. Planning & Execution
- For **Brainstorming & Design** (HARD-GATE, Visual Companion):
  👉 **[Brainstorming](sub-skills/brainstorming/SKILL.md)**
- For **Implementation Planning**:
  👉 **[Implementation Planning](sub-skills/implementation-planning/SKILL.md)**
- For **Task Breakdown** and Management:
  👉 **[Planning and Task Breakdown](sub-skills/planning-and-task-breakdown/SKILL.md)**
- For **Workflows** (DMUX):
  👉 **[DMUX Workflows](sub-skills/dmux-workflows/SKILL.md)**
- For **Using Superpowers** (Aggressive Skill Activation & Discovery):
  👉 **[Using Superpowers](sub-skills/using-superpowers/SKILL.md)**
- For **Prototype** (Rapid throwaway prototyping for validation):
  👉 **[Prototype](sub-skills/prototype/SKILL.md)**
- For **Finishing A Development Branch** (Completion and merge options for branches):
  👉 **[Finishing A Development Branch](sub-skills/finishing-a-development-branch/SKILL.md)**
- For **To Issues** (Breaking down plans into tracer-bullet issues):
  👉 **[To Issues](sub-skills/to-issues/SKILL.md)**
- For **Forensic Session Root Cause Analysis** (session deltas, severities):
  👉 **[Analyze Project](sub-skills/analyze-project/SKILL.md)**
- For **Autonomous Agent Loops** (ReAct, Plan-Execute, Reflection, Guardrails):
  👉 **[Autonomous Agents](sub-skills/autonomous-agents/SKILL.md)**
- For **First-Principles Assumption Auditing & Logic Audits** (Axiom, prosecuting assumptions):
  👉 **[Axiom](sub-skills/axiom/SKILL.md)**
- For **Adaptive AI Operating Modes** (BRAINSTORM, IMPLEMENT, DEBUG, REVIEW, TEACH, SHIP, EXPLORE, PEC):
  👉 **[Behavioral Modes](sub-skills/behavioral-modes/SKILL.md)**
- For **Multi-Session Construction Plans** (cold-start self-contained context briefs, adversarial plan gates):
  👉 **[Blueprint Construction Planning](sub-skills/blueprint/SKILL.md)**
- For **Phased Major Feature Development & Tracking** (research, implementation plans, PROGRESS log, phased delivery):
  👉 **[Phased Feature Build](sub-skills/build/SKILL.md)**
- For **Parallel Multi-Agent Coordination** (split-merge orchestrations, task delegation, map-reduce agent grids):
  👉 **[Parallel Agents](sub-skills/parallel-agents/SKILL.md)**
- For **Dynamic Personal Tool Building** (on-the-fly execution extensions, custom self-enrichment scripts):
  👉 **[Personal Tool Builder](sub-skills/personal-tool-builder/SKILL.md)**
- For **Multi-Session Cold-Start Plan Writing** (structured outlines, scope isolation, validation milestones):
  👉 **[Plan Writing](sub-skills/plan-writing/SKILL.md)**
- For **Gen-3 Multi-File Discovery & Planning** (scanning files, AST context maps, comprehensive implementation plan gates):
  👉 **[Planning With Files](sub-skills/planning-with-files/SKILL.md)**
- For **Social Media Automated Orchestrator** (coordinates multi-channel posting, schedules pipelines, updates analytics):
  👉 **[Social Orchestrator](sub-skills/social-orchestrator/SKILL.md)**
- For **Automated Spec & Diagram Updater** (keeps architectural specifications and system diagrams synced dynamically):
  👉 **[Speckit Updater](sub-skills/speckit-updater/SKILL.md)**
- For **Squirrel 8-Phase Full-Cycle Developer** (auto-detects project maturity, greenfield setup, reproduction loops, TDD):
  👉 **[Squirrel Developer](sub-skills/squirrel/SKILL.md)**

### 🤖 Claude & LLM Orchestration
- For **Clarity Gate Precision Intent Audits** (prompt intent filtering, target alignment verification):
  👉 **[Clarity Gate](sub-skills/clarity-gate/SKILL.md)**
- For **Claude API Direct Client Integration** (token usage metrics, system prompt boundaries, tool-calling structures):
  👉 **[Claude API Integration](sub-skills/claude-api/SKILL.md)**
- For **Claude Code Expert CLI Workflows** (advanced CLI commands, server-side caching optimizations):
  👉 **[Claude Code Expert](sub-skills/claude-code-expert/SKILL.md)**
- For **Claude Code Setup & Guides** (environment settings, standard configuration tutorials):
  👉 **[Claude Code Guide](sub-skills/claude-code-guide/SKILL.md)**
- For **Claude Chrome Extension Troubleshooting** (DOM injection limits, message bus latency resolution):
  👉 **[Claude Chrome Troubleshooting](sub-skills/claude-in-chrome-troubleshooting/SKILL.md)**
- For **Claude API Performance Monitoring** (token volume tracking, execution latency logging):
  👉 **[Claude API Monitor](sub-skills/claude-monitor/SKILL.md)**
- For **Claude Console Safety & Settings Auditing** (temperature configuration, safety filters audit):
  👉 **[Claude Settings Auditor](sub-skills/claude-settings-audit/SKILL.md)**
- For **RecallMax Long-Context Memory** (conversation adapters, intent/tone summaries, 14-turn to 800 tokens compression):
  👉 **[RecallMax Memory](sub-skills/recallmax/SKILL.md)**
- For **Recursive Context Pruning & Token Budgeting** (token cost reduction, recursive trim-down execution):
  👉 **[Recursive Context Pruning](sub-skills/recursive-context-pruning/SKILL.md)**
- For **Secure Sandboxing & Variables Lock** (Varlock execution scopes, secure key/value local storage):
  👉 **[Varlock Secure Variables](sub-skills/varlock/SKILL.md)**
- For **Claude Varlock Secure Integration** (Claude API bindings for local key storage):
  👉 **[Varlock Claude Hooks](sub-skills/varlock-claude-skill/SKILL.md)**
- For **Vibe Checks & Alignment Monitors** (Viboscope dynamic mood meters, user sentiment trajectory matching):
  👉 **[Viboscope Dynamic Monitor](sub-skills/viboscope/SKILL.md)**
- For **Prompting Capabilities & Superpowers** (invoking maximum capacity prompt configurations):
  👉 **[Superpowers Prompting](sub-skills/superpowers/SKILL.md)**
- For **Tokenwise Economy Tracking** (token density monitoring, context optimization indicators):
  👉 **[Tokenwise Economy](sub-skills/tokenwise/SKILL.md)**
- For **Technical Change Tracker inside Context** (mapping dynamic codebase diffs inside active model contexts):
  👉 **[Technical Change Tracker](sub-skills/technical-change-tracker/SKILL.md)**
- For **Task Intelligence & Objective Decomposition** (breaking complex requirements into task execution trees):
  👉 **[Task Intelligence](sub-skills/task-intelligence/SKILL.md)**
- For **Redesigning Existing Legacy Projects** (greenfield code audits, decoupled domain models, structural refactoring):
  👉 **[Redesign Existing Projects](sub-skills/redesign-existing-projects/SKILL.md)**
- For **Rich Elicitation Prompt Strategies** (elaborated target details, user criteria mapping):
  👉 **[Rich Elicitation](sub-skills/rich-elicitation/SKILL.md)**

### 2. Debugging & Error Handling
- For **Systematic Debugging**:
  👉 **[Systematic Debugging](sub-skills/systematic-debugging/SKILL.md)**
- For **Evidence-Based Bug Hunting & Diagnosis** (reproduction, root cause tracing, regression prevention):
  👉 **[Bug Hunter](sub-skills/bug-hunter/SKILL.md)**
- For **Multi-Phase Gated Debugging Loops** (repro scripts, evidence-first logs, verification verification):
  👉 **[Phase Gated Debugging](sub-skills/phase-gated-debugging/SKILL.md)**
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
- For **Zoom Out** (High-level map and structural codebase context):
  👉 **[Zoom Out](sub-skills/zoom-out/SKILL.md)**
- For **Andrej Karpathy Persona Simulation** (deep learning, Vibe Coding, Software 2.0):
  👉 **[Andrej Karpathy](sub-skills/ai-expert-personas/andrej-karpathy/SKILL.md)**
- For **Bill Gates Persona Simulation** (high-level system design, strategic technology scaling, enterprise MVP):
  👉 **[Bill Gates](sub-skills/ai-expert-personas/bill-gates/SKILL.md)**
- For **Sam Altman Persona Simulation** (strategic hypergrowth scaling, extreme product market fit, fundraising, AGI timelines):
  👉 **[Sam Altman](sub-skills/ai-expert-personas/sam-altman/SKILL.md)**
- For **Steve Jobs Persona Simulation** (premium aesthetic obsessive, product presentation showmanship, reality distortion field):
  👉 **[Steve Jobs](sub-skills/ai-expert-personas/steve-jobs/SKILL.md)**

### 4. Infrastructure & Context
- For **CI/CD and Automation**:
  👉 **[CI/CD and Automation](sub-skills/ci-cd-and-automation/SKILL.md)**
- For **Unified Context Engineering** (Brain Context Chain):
  👉 **[Brain Context Engineering](sub-skills/brain-context-engineering/SKILL.md)**
- For **Migrations**:
  👉 **[Deprecation and Migration](sub-skills/deprecation-and-migration/SKILL.md)**
- For **Wallet-based Agentic Micropayments Routing** (paying for image generation, Grok live X/Twitter search, GPT second opinions):
  👉 **[BlockRun Micropayments Wallet](sub-skills/blockrun/SKILL.md)**
- For **Pipecat Voice AI Real-Time Agents** (WebRTC voice pipelines, speech-to-text-to-speech low latency streams):
  👉 **[Pipecat Voice Agents](sub-skills/pipecat-friday-agent/SKILL.md)**

- For **Handoff** (Session handoff and state consolidation):
  👉 **[Handoff](sub-skills/handoff/SKILL.md)**

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the core implementation and verification of green tests:
- 👉 For frontend features, recommend calling **[UX & Design Master](../ux-master/SKILL.md)** next to polish premium aesthetics and accessibility.
- 👉 Otherwise, recommend calling **[Review Master](../review-master/SKILL.md)** to run the Code Review Council and evaluate production readiness.

---

## 🏗️ Operating Pipeline
1. **Intake**: Audit workspace surface area and clarify requirements.
2. **Planning**: Break down tasks and create implementation plans.
3. **Execution**: Generate code following spec-driven or source-driven patterns.
4. **Correction**: Systematically debug and resolve any errors found.

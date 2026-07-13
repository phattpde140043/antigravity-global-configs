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


Each sub-skill below lists its **function**, a concrete **Use when** trigger, and (where a real neighbor exists) a **Not for** boundary. Load a sub-skill only when its trigger matches.

### 1. Planning, Design & Task Breakdown
> 📝 **Planning — pick one:** rigorous plan for non-trivial code (arch + atomic TDD steps) → **Implementation Planning**; write the plan doc from a spec → **Writing Plans**; dependency-aware verifiable breakdown → **Plan Writing**; slice a clear spec into ordered tasks → **Planning and Task Breakdown**; durable on-disk to-do across long/multi-session work → **Planning With Files**; steps that must survive fresh agents/sessions → **Blueprint Construction Planning**; split a plan into tickets → **To Issues**.
- **[Brainstorming](sub-skills/brainstorming/SKILL.md)** — Mandatory creative-exploration protocol that pressure-tests requirements and design before code. **Use when:** starting feature design, exploring requirements, or the user says "brainstorm / explore ideas / what are the options". **Not for:** executing an agreed plan (use Executing Plans).
- **[Rich Elicitation](sub-skills/rich-elicitation/SKILL.md)** — Multi-round clarifying questions before ambiguous work begins. **Use when:** 2+ task dimensions each have 3+ viable answers, or requirements are underspecified/contradictory. **Not for:** tasks with a single clear interpretation.
- **[Axiom](sub-skills/axiom/SKILL.md)** — First-principles assumption auditor that classifies hidden assumptions (fact/convention/belief/interest) and rebuilds conclusions from verified premises. **Use when:** a plan rests on unverified assumptions or you need to prosecute "why do we believe this?" **Not for:** routine execution where premises are settled.
- **[Implementation Planning](sub-skills/implementation-planning/SKILL.md)** — High-rigor engineering plan pairing strategic architecture (security, tenancy, performance) with atomic TDD steps. **Use when:** writing new code or modifying non-trivial logic that warrants a rigorous plan. **Not for:** one-line edits.
- **[Writing Plans](sub-skills/writing-plans/SKILL.md)** — Produces the written implementation plan from a spec before any code is touched. **Use when:** you have a spec/requirements for a multi-step task and need the plan document first. **Not for:** executing the plan (use Executing Plans); turning it into tickets (use To Issues).
- **[Plan Writing](sub-skills/plan-writing/SKILL.md)** — Structured task plan with explicit breakdowns, dependencies, and verification criteria. **Use when:** implementing features or refactors that need dependency-aware, verifiable steps. **Not for:** single-step tasks.
- **[Planning and Task Breakdown](sub-skills/planning-and-task-breakdown/SKILL.md)** — Breaks a spec into ordered, implementable tasks with scope estimates. **Use when:** requirements are clear, a task feels too large to start, or parallel work is possible. **Not for:** exploring vague ideas (use Brainstorming).
- **[Planning With Files](sub-skills/planning-with-files/SKILL.md)** — Manus-style persistent markdown files as on-disk working memory across a long task. **Use when:** a task spans many steps/sessions and needs durable to-do/progress files. **Not for:** short single-session tasks.
- **[Blueprint Construction Planning](sub-skills/blueprint/SKILL.md)** — Turns a one-line objective into cold-executable steps, each with a self-contained context brief. **Use when:** a plan must survive fresh sessions/agents that never read prior steps. **Not for:** quick in-session plans (use Writing Plans).
- **[Task Intelligence](sub-skills/task-intelligence/SKILL.md)** — Pre-task intelligence protocol that activates all relevant ecosystem agents/skills before executing a request. **Use when:** you want a pre-flight scan of which capabilities apply before starting. **Not for:** mid-execution steps.
- **[To Issues](sub-skills/to-issues/SKILL.md)** — Splits a plan/spec/PRD into independently-grabbable vertical-slice (tracer-bullet) issues. **Use when:** converting a plan into tickets or breaking work for parallel pickup. **Not for:** writing the plan itself (use Writing Plans) or authoring a PRD.

### 2. Build & Execution Pipelines
- **[Executing Plans](sub-skills/executing-plans/SKILL.md)** — Execution logic for working an approved implementation plan step by step. **Use when:** a plan exists and you are ready to build it. **Not for:** writing the plan (use Writing Plans); delegating parallel tasks (use Subagent-Driven Development).
- **[Subagent-Driven Development](sub-skills/subagent-driven-development/SKILL.md)** — Executes a plan's independent tasks via sequential subagent-per-task in the current session. **Use when:** an implementation plan has independent tasks to delegate one at a time. **Not for:** parallel building (causes file conflicts) — investigate in parallel via Dispatching Parallel Agents instead.
- **[Phased Feature Build](sub-skills/build/SKILL.md)** — 4-phase major-feature pipeline (research, implementation, progress, phase) driven by subcommands with a PROGRESS log. **Use when:** carrying a large feature through named phases with status tracking. **Not for:** small standalone changes.
- **[Squirrel Developer](sub-skills/squirrel/SKILL.md)** — Full-cycle 8-phase developer that auto-detects project maturity, then plans, builds, tests, lints, fixes, and documents. **Use when:** you want one skill to carry a project end-to-end (greenfield or existing). **Not for:** targeted single-phase help.
- **[Prototype](sub-skills/prototype/SKILL.md)** — Builds a throwaway prototype to answer a design question before committing to real code. **Use when:** the user says "prototype this", wants to sanity-check a data model, or mock a UI. **Not for:** full implementation (use Executing Plans); ideation (use Brainstorming).
- **[Finishing a Development Branch](sub-skills/finishing-a-development-branch/SKILL.md)** — Presents structured merge/PR/cleanup options once work is complete and tests pass. **Use when:** implementation is done and you must decide how to integrate the branch. **Not for:** mid-implementation work.
- **[Verification Before Completion](sub-skills/verification-before-completion/SKILL.md)** — Final verification gate before claiming work done. **Use when:** about to say something is complete/fixed/passing, or before committing or opening a PR. **Not for:** early exploration.
- **[Behavioral Modes](sub-skills/behavioral-modes/SKILL.md)** — Adaptive AI operating modes (brainstorm, implement, debug, review, teach, ship, orchestrate). **Use when:** you need to switch the agent's behavior to match the current task type. **Not for:** a single fixed-mode task.
- **[Autonomous Agents](sub-skills/autonomous-agents/SKILL.md)** — Patterns for self-directed agents (ReAct, Plan-Execute, Reflection, guardrails) that decompose and act. **Use when:** designing or running a loop that plans and executes independently. **Not for:** simple one-shot prompts.
- **[Personal Tool Builder](sub-skills/personal-tool-builder/SKILL.md)** — Builds custom throwaway/personal tools and scripts to solve the task at hand. **Use when:** you need an on-the-fly script/tool to extend execution. **Not for:** production tool/product engineering.
- **[Social Orchestrator](sub-skills/social-orchestrator/SKILL.md)** — Unified cross-channel social publishing (Instagram/Telegram/WhatsApp) with scheduling and unified metrics. **Use when:** coordinating multi-channel posting, scheduling, or campaign management. **Not for:** non-social automation.
- **[Speckit Updater](sub-skills/speckit-updater/SKILL.md)** — Safely updates or installs GitHub SpecKit templates while preserving project customizations. **Use when:** updating/installing SpecKit, or needing an approval-gated update/rollback flow. **Not for:** editing your own architecture specs (use Spec-Driven Development).
- **[Analyze Project](sub-skills/analyze-project/SKILL.md)** — Forensic root-cause analyzer for Antigravity sessions: classifies scope deltas, rework, hotspots, and auto-improves prompts/health. **Use when:** reviewing a session's failures/rework or wanting prompt/health improvements. **Not for:** live code debugging (use Systematic Debugging).

### 3. Multi-Agent & Parallel Orchestration
- **[Parallel Agents](sub-skills/parallel-agents/SKILL.md)** — Multi-agent orchestration for independent tasks needing different domain expertise or multiple perspectives. **Use when:** several independent workstreams or a multi-lens analysis can run at once. **Not for:** tightly coupled sequential work.
- **[Dispatching Parallel Agents](sub-skills/dispatching-parallel-agents/SKILL.md)** — Dispatches one agent per independent problem domain for concurrent investigation/debugging. **Use when:** 3+ test files or subsystems fail with different, unrelated root causes. **Not for:** parallel implementation/build (run sequentially via Subagent-Driven Development).
- **[DMUX Workflows](sub-skills/dmux-workflows/SKILL.md)** — Multi-agent orchestration via dmux (tmux pane manager) across Claude Code, Codex, OpenCode, and other harnesses. **Use when:** the user wants divide-and-conquer work run in parallel tmux panes. **Not for:** framework-specific coding rules or architecture decisions.
- **[CrewAI Orchestration](sub-skills/crewai-orchestration/SKILL.md)** — Role-based multi-agent design with CrewAI (agent personas, task decomposition, Processes and Flows). **Use when:** building or debugging a CrewAI crew/workflow. **Not for:** other agent frameworks (use PydanticAI) or non-framework orchestration.
- **[Using Superpowers](sub-skills/using-superpowers/SKILL.md)** — Aggressive skill-discovery activator that requires invoking the Skill tool before any response. **Use when:** starting a conversation and you must find/activate the right skills first. **Not for:** mid-task steps once skills are already loaded.
- **[Superpowers Activation](sub-skills/superpowers/SKILL.md)** — Companion skill-activation entry point establishing how to find and use skills up front. **Use when:** bootstrapping skill discovery at conversation start. **Not for:** ongoing execution after skills are selected.

### 🤖 Claude, LLM Frameworks & Context/Memory Orchestration
- **[Claude API Integration](sub-skills/claude-api/SKILL.md)** — Build apps with the Claude API / Anthropic SDK / Agent SDK (tool use, system prompts, token usage). **Use when:** code imports `anthropic` / `@anthropic-ai/sdk` / `claude_agent_sdk`, or the user asks to use the Claude API. **Not for:** OpenAI or other AI SDKs; general programming.
- **[PydanticAI](sub-skills/pydantic-ai/SKILL.md)** — Build type-safe, production AI agents with PydanticAI (structured outputs, dependency injection, deterministic testing). **Use when:** building or testing a PydanticAI agent. **Not for:** CrewAI crews (use CrewAI Orchestration) or raw Claude SDK apps (use Claude API).
- **[Claude Code Expert](sub-skills/claude-code-expert/SKILL.md)** — Deep Claude Code CLI expertise (hooks, MCPs, CLAUDE.md, sub-agents, permissions, advanced workflows). **Use when:** maximizing Claude Code productivity or wiring advanced CLI configuration. **Not for:** first-time basic setup (use Claude Code Guide).
- **[Claude Code Guide](sub-skills/claude-code-guide/SKILL.md)** — Comprehensive reference and templates for configuring and using Claude Code. **Use when:** setting up Claude Code or looking up config best practices/templates. **Not for:** deep advanced tuning (use Claude Code Expert).
- **[Claude Chrome Troubleshooting](sub-skills/claude-in-chrome-troubleshooting/SKILL.md)** — Diagnoses and fixes Claude-in-Chrome MCP extension connectivity. **Use when:** `mcp__claude-in-chrome__*` tools fail, return "Browser extension is not connected", or behave erratically. **Not for:** non-Chrome MCP issues.
- **[Claude Monitor](sub-skills/claude-monitor/SKILL.md)** — Performance monitor for Claude Code and the local machine (CPU/RAM/disk, API latency, health reports). **Use when:** diagnosing slowness or measuring local/API performance. **Not for:** code-level bugs.
- **[Claude Settings Auditor](sub-skills/claude-settings-audit/SKILL.md)** — Analyzes a repo to recommend Claude Code settings.json permissions (detects stack, build tools, monorepo). **Use when:** setting up a new project or auditing which read-only bash commands to allow. **Not for:** runtime debugging.
- **[Clarity Gate](sub-skills/clarity-gate/SKILL.md)** — Pre-ingestion epistemic-quality verification for RAG: qualifies documents, produces CGDs, validates Source-of-Truth files. **Use when:** checking a doc for hallucination/equivocation risk before it enters a knowledge base ("cgd verify", "sot verify", "can an LLM read this safely"). **Not for:** clarifying a user's prompt intent (use Rich Elicitation).
- **[RecallMax Memory](sub-skills/recallmax/SKILL.md)** — Long-context memory that injects large clean context and compresses history with tone/intent preservation. **Use when:** you need durable conversation memory or to compress a long history into few tokens. **Not for:** one-off short chats.
- **[Recursive Context Pruning](sub-skills/recursive-context-pruning/SKILL.md)** — Prunes redundant context and enforces ultra-concise, token-budgeted responses. **Use when:** context is bloated or you must cut token cost recursively. **Not for:** tasks needing full verbose context.
- **[Tokenwise Economy](sub-skills/tokenwise/SKILL.md)** — Measurement-driven model router (Haiku/Sonnet/Opus) that logs real $ per task and A/B tests cheaper tiers. **Use when:** optimizing cost by routing tasks to the cheapest capable model. **Not for:** correctness-only tasks with no cost concern.
- **[Technical Change Tracker](sub-skills/technical-change-tracker/SKILL.md)** — Tracks code changes as structured JSON with state-machine enforcement and cross-session handoff. **Use when:** you need auditable change records and bot continuity across sessions. **Not for:** ad-hoc one-session edits.
- **[Varlock Secure Variables](sub-skills/varlock/SKILL.md)** — Secure-by-default environment-variable management for Claude Code sessions. **Use when:** loading or handling secrets/env vars safely in a session. **Not for:** non-secret config.
- **[Varlock Claude Hooks](sub-skills/varlock-claude-skill/SKILL.md)** — Ensures secrets are never exposed in Claude sessions, terminals, logs, or git commits. **Use when:** binding Varlock-managed secrets into Claude workflows. **Not for:** general env setup (use Varlock Secure Variables).
- **[Viboscope](sub-skills/viboscope/SKILL.md)** — Psychological compatibility matching via validated psychometrics (cofounders, collaborators, friends). **Use when:** matching people for compatibility or team fit. **Not for:** code, model, or context monitoring.

### 4. Debugging & Error Handling
> 🐞 **Debugging — pick one:** general defect with logs/telemetry → **Systematic Debugging**; reproducible bug to fix end-to-end → **Bug Hunter**; must force evidence-before-fix discipline → **Phase-Gated Debugging**; clue lives in logs/stack traces → **Error Detective**; build/type-checker failures → **Build Error Resolver**; the AI agent itself is looping/stuck → **Agent Introspection Debugging**.
- **[Systematic Debugging](sub-skills/systematic-debugging/SKILL.md)** — AI-assisted debugging using observability platforms and automated root-cause analysis. **Use when:** diagnosing a defect with logs/telemetry and a structured method. **Not for:** build/type-checker failures (use Build Error Resolver).
- **[Bug Hunter](sub-skills/bug-hunter/SKILL.md)** — Traces from symptom to root cause, implements the fix, and prevents regression. **Use when:** a reproducible bug needs finding and fixing end-to-end. **Not for:** unclear repros needing a gated protocol (use Phase-Gated Debugging).
- **[Phase-Gated Debugging](sub-skills/phase-gated-debugging/SKILL.md)** — 5-phase protocol that blocks code edits until root cause is confirmed. **Use when:** you must stop premature fix attempts and force evidence-first debugging. **Not for:** trivial known fixes.
- **[Error Detective](sub-skills/error-detective/SKILL.md)** — Hunts bugs through logs, stack traces, and anomaly/pattern detection. **Use when:** the clue lives in log output or stack traces and needs pattern analysis. **Not for:** build configuration failures.
- **[Build Error Resolver](sub-skills/build-error-resolver/SKILL.md)** — Resolves build and type-checker errors. **Use when:** the build fails or TypeScript/type errors block progress. **Not for:** architecture redesign or feature expansion.
- **[Agent Introspection Debugging](sub-skills/agent-introspection-debugging/SKILL.md)** — Structured self-debugging for AI-agent failures (capture, diagnose, contained recovery, introspection report). **Use when:** hitting max tool-call/loop limits or repeated retries with no forward progress. **Not for:** ordinary product-code bugs (use Systematic Debugging).

### 5. Code Crafting & Quality
- **[Code Generation](sub-skills/code-generation/SKILL.md)** — Generates production-ready backend code with enforced architecture, security, and performance, plus self-review. **Use when:** the request is to write backend code to a spec. **Not for:** reading/mapping existing code (use Code Explorer).
- **[Code Explorer](sub-skills/code-explorer/SKILL.md)** — Traces execution paths, maps architecture layers, and documents dependencies of existing features. **Use when:** before implementing in an unfamiliar area or debugging complex behavior paths. **Not for:** modifying/refactoring code or final architecture arbitration.
- **[Code Simplifier](sub-skills/code-simplifier/SKILL.md)** — Reviews a diff for clarity and safe simplifications, then optionally applies low-risk fixes. **Use when:** tidying a diff for readability without changing behavior. **Not for:** hunting correctness bugs (use Bug Hunter).
- **[Coding Standards](sub-skills/coding-standards/SKILL.md)** — Core quality baseline enforcing KISS, DRY, YAGNI, Poka-Yoke, and idempotency. **Use when:** writing or reviewing code to hold a minimum quality bar. **Not for:** large-scale architecture design (use Code Craftsmanship).
- **[Code Craftsmanship](sub-skills/code-craftsmanship/SKILL.md)** — Clean Code, SOLID, and Clean Architecture (Uncle Bob) for structure and boundary management. **Use when:** shaping module boundaries, dependencies, and sustainable architecture. **Not for:** quick line-level cleanups (use Coding Standards or Code Simplifier).
- **[Source-Driven Development](sub-skills/source-driven-development/SKILL.md)** — Grounds every decision in official documentation with source citations. **Use when:** you need authoritative, source-cited code free of outdated patterns for a framework/library. **Not for:** greenfield ideation.
- **[Spec-Driven Development](sub-skills/spec-driven-development/SKILL.md)** — Writes a specification before coding. **Use when:** starting a new project/feature/significant change with no spec, or requirements are vague. **Not for:** work that already has an approved spec/plan.
- **[Zoom Out](sub-skills/zoom-out/SKILL.md)** — Produces a high-level map of relevant modules and callers. **Use when:** the user says "zoom out" or is unfamiliar with how a code section fits the bigger picture. **Not for:** deep architecture refactoring.
- **[Redesign Existing Projects](sub-skills/redesign-existing-projects/SKILL.md)** — Audits generic UI patterns and applies premium design fixes to existing apps without rewrites. **Use when:** upgrading the look/feel of an existing website or app. **Not for:** greenfield builds or backend logic.
- **[Writing Skills](sub-skills/writing-skills/SKILL.md)** — Authoring workflow for creating, editing, and verifying skills. **Use when:** creating a new skill, editing an existing one, or checking a skill works. **Not for:** discovering/using skills at runtime (use Using Superpowers).
- **[AI Expert Personas](sub-skills/ai-expert-personas/SKILL.md)** — Library index of expert personas for architectural review, technical debate, and philosophical critique. **Use when:** you want a named expert lens to critique a design or decision. **Not for:** hands-on implementation.
  - **[Andrej Karpathy](sub-skills/ai-expert-personas/andrej-karpathy/SKILL.md)** — Deep-learning / "Software 2.0" / Vibe Coding lens. **Use when:** debating ML system design or neural-net-first approaches.
  - **[Bill Gates](sub-skills/ai-expert-personas/bill-gates/SKILL.md)** — High-level system design, enterprise MVP, strategic scaling lens. **Use when:** critiquing product/technology strategy at scale.
  - **[Sam Altman](sub-skills/ai-expert-personas/sam-altman/SKILL.md)** — Hypergrowth scaling, product-market fit, fundraising, AGI-timeline lens. **Use when:** stress-testing growth or startup strategy.
  - **[Steve Jobs](sub-skills/ai-expert-personas/steve-jobs/SKILL.md)** — Premium aesthetics, product presentation, uncompromising-taste lens. **Use when:** critiquing product polish and presentation.

### 6. Infrastructure, Context & Handoff
- **[CI/CD and Automation](sub-skills/ci-cd-and-automation/SKILL.md)** — Automates CI/CD pipeline setup (test runners, deployment strategies, feature flags, canary). **Use when:** setting up or modifying build/deploy pipelines. **Not for:** application feature code.
- **[Using Git Worktrees](sub-skills/using-git-worktrees/SKILL.md)** — Isolates feature work in dedicated git worktrees. **Use when:** starting feature work that needs isolation, or before executing an implementation plan in parallel. **Not for:** single-branch quick edits.
- **[Context Engineering](sub-skills/context-engineering/SKILL.md)** — Curates rules, specs, and source files to optimize the agent's context for focused execution. **Use when:** starting a new session, switching tasks, or output quality degrades. **Not for:** deep long-term project memory (use Brain Context Engineering).
- **[Brain Context Engineering](sub-skills/brain-context-engineering/SKILL.md)** — Unified orchestrator for high-fidelity project memory and context engineering (its own sub-chain). **Use when:** on complex projects (>2,000 LOC) needing durable, structured memory. **Not for:** quick per-session context tuning (use Context Engineering).
- **[Deprecation and Migration](sub-skills/deprecation-and-migration/SKILL.md)** — Manages code removal and system/API migration, moving users safely between implementations. **Use when:** replacing an old system/API/feature or migrating users. **Not for:** greenfield builds.
- **[BlockRun Micropayments Wallet](sub-skills/blockrun/SKILL.md)** — Wallet-based agentic micropayments routing (pay for image generation, Grok live X/Twitter search, GPT second opinions). **Use when:** the agent must pay per-use for external paid services. **Not for:** free local tooling.
- **[Pipecat Voice Agents](sub-skills/pipecat-friday-agent/SKILL.md)** — Builds a low-latency voice assistant (F.R.I.D.A.Y.) with Pipecat + Gemini + OpenAI (WebRTC speech-to-text-to-speech). **Use when:** building a real-time voice/WebRTC agent. **Not for:** text-only agents.
- **[Handoff](sub-skills/handoff/SKILL.md)** — Compacts the current conversation into a handoff document for a fresh session/agent to continue. **Use when:** ending a long session, switching context, or handing work to another agent. **Not for:** writing plans (use Writing Plans) or PRDs.

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

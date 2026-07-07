---
name: review-master
description: "Master Review Orchestrator. Coordinates Code Audit, Language-specific Diagnostics, and Production Readiness through specialized sub-disciplines."
metadata:
  category: master-orchestrator
  triggers: code-review, pr-review, quality-audit, readiness-score, ai-slop-scan
---

# 🛡️ Review Master Orchestrator

The final authority for craftsmanship and production readiness. This master skill orchestrates the Review Council and deep-dive diagnostics to ensure the Diamond Standard.

---

## 🧭 Audit Strategy
- **Uncompromising Quality**: Reject mediocrity and "AI Slop."
- **Evidence-Based**: Every finding must be backed by data or logic.
- **Mentoring-First**: Feedback should empower and educate.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing reviews, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure comprehensive code quality auditing:

### 🔄 Sequential Sub-Skill Pipeline
```
[Workspace Surface Audit] ──→ [Code Reviewer (Framework)] ──→ [Code Review Excellence] ──→ [Vibe Code Auditor]
```


### 1. Core Review Frameworks & Methodology
- **[Code Reviewer (Framework)](sub-skills/code-reviewer/SKILL.md)** — senior general-purpose review across five dimensions (correctness, readability, architecture, security, performance). **Use when:** you need a thorough all-round review of a change before merge. **Not for:** language-specific deep dives or performance-gated audits (use the specialized skills below).
- **[Performing Code Review](sub-skills/performing-code-review/SKILL.md)** — systematic 5-phase reviewer methodology (Recon → Security → Architecture → Bug Hunt → Verdict) that forbids any verdict before all passes complete. **Use when:** you are the reviewer and need a repeatable multi-pass process to reach a verdict. **Not for:** requesting a review or reacting to feedback (see the Feedback Loop group).
- **[Code Review Excellence](sub-skills/code-review-excellence/SKILL.md)** — constructive-feedback and mentoring layer with severity labels and conventional-commit conventions. **Use when:** writing review comments, coaching, or applying severity/feedback standards. **Not for:** locating the defects themselves — pair it with a diagnostic skill.
- **[Brooks Lint](sub-skills/brooks-lint/SKILL.md)** — classic-software-engineering reviewer catching design smells, coupling, and architectural risk (DRY, APOSD complexity, Clean Code, Release It stability, DDIA). **Use when:** auditing design quality, coupling, or architectural stability rather than line-level bugs.

### 2. Language-Specific & Specialized Diagnostics
- **[C# Reviewer](sub-skills/csharp-reviewer/SKILL.md)** — expert C#/.NET review of async safety, nullable handling, injection, and idiomatic conventions. **Use when:** reviewing C#/.NET changes. **Not for:** non-.NET languages.
- **[Vibe Code Auditor](sub-skills/vibe-code-auditor/SKILL.md)** — audits AI-generated/prototype code for "slop" and technical debt and scores Production Readiness (0-100). **Use when:** vetting AI-generated or prototype code and needing a readiness score.
- **[Differential Security Review](sub-skills/differential-review/SKILL.md)** — security-focused review via Git-history/blame risk analysis and Blast Radius impact scoring. **Use when:** assessing the security impact and reach of a change set from commit history and dependencies.
- **[Performance AI Auditor](sub-skills/performance-testing-review/ai-review/SKILL.md)** — AI-assisted review combining static-analysis platforms (SonarQube/CodeQL/Semgrep) to flag bugs, vulnerabilities, and performance issues. **Use when:** you want automated AI + static-analysis gating of latency budgets, pool sizing, and N+1 queries.
- **[Performance Multi-Agent Auditor](sub-skills/performance-testing-review/multi-agent-review/SKILL.md)** — multi-agent orchestration for split-opinion, adversarial performance review gates. **Use when:** you want consensus/adversarial multi-agent gating of a performance-sensitive change.
- **[Clarvia AEO Auditor](sub-skills/clarvia-aeo-check/SKILL.md)** — scores an MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). **Use when:** evaluating a tool or MCP server for agent-readiness before adoption. **Not for:** reviewing application source code.
- **[Vibers Human Review](sub-skills/vibers-code-review/SKILL.md)** — human review workflow for AI-generated GitHub projects: spec-based feedback, security review, and follow-up fix PRs via the Vibers service. **Use when:** you pushed an AI-generated project and want spec-based human review with returned fix PRs.

### 3. Review Feedback Loop (Requesting & Receiving)
- **[Requesting Code Review](sub-skills/requesting-code-review/SKILL.md)** — systematic delegation that dispatches a code-reviewer subagent to follow the 5-phase methodology. **Use when:** handing off a change for review ("review early, review often"). **Not for:** doing the review yourself (use Performing Code Review).
- **[Receiving Code Review](sub-skills/receiving-code-review/SKILL.md)** — protocol for acting on review feedback: technical action over performative agreement (bans "you're absolutely right"-style replies). **Use when:** you receive review comments and must respond and revise.
- **[Requesting Review (Pre-Merge Variant)](sub-skills/code-review-feedback/requesting/SKILL.md)** — dispatch a code-reviewer subagent on completing tasks or major features before merging. **Use when:** finishing a task/feature and verifying it meets requirements pre-merge. **Not for:** distinct from the discipline-level Requesting Code Review above; use whichever your workflow references.
- **[Receiving Review (Reception Mindset Variant)](sub-skills/code-review-feedback/receiving/SKILL.md)** — treat review as technical evaluation, not emotional performance; verify before implementing, ask before assuming. **Use when:** processing reviewer feedback and deciding what to implement. **Not for:** distinct from the discipline-level Receiving Code Review above; use whichever your workflow references.

### 4. Workflow & Artifact Management
- **[PR Review](sub-skills/pr-review/SKILL.md)** — deep production-grade PR review across five axes (Architecture, Security, Performance, Correctness, Readability) with change-sizing guardrails (~100 lines). **Use when:** reviewing a pull request or diff and enforcing PR hygiene and size limits.
- **[Codex Review](sub-skills/codex-review/SKILL.md)** — enforces CHANGELOG.md upkeep and Conventional Commits, plus Codex-reasoning review of large refactors. **Use when:** verifying changelog entries, commit-message conventions, or reviewing large-scale refactoring.
- **[Unslop](sub-skills/unslop/SKILL.md)** — post-processes AI-generated text through the `unslop` CLI to strip AI writing patterns before publishing. **Use when:** cleaning AI-written prose or docs prior to publishing. **Not for:** source-code refactoring — it targets text, not code.

### 5. Context & Surface Analysis
- **[Workspace Surface Audit](sub-skills/workspace-surface-audit/SKILL.md)** — audits and classifies Copilot instructions and skills into project-level vs user-level scope using codebase evidence, flagging gaps and stale surfaces. **Use when:** deciding scope for a workspace's instructions/skills or auditing surface coverage.
- **[Comment Analyzer](sub-skills/comment-analyzer/SKILL.md)** — evaluates code comments for accuracy, completeness, maintainability, and comment-rot risk. **Use when:** after refactors or behavior changes, or when reviewing heavily commented modules.
- **[Conversation Analyzer](sub-skills/conversation-analyzer/SKILL.md)** — analyzes conversation transcripts to turn repeated assistant misbehaviors into enforceable hook rules. **Use when:** the user repeatedly corrects assistant behavior or hook-policy design is requested. **Not for:** tasks unrelated to hook policy.

### 6. Team Collaboration
- **[Collaboration Issue Standards](sub-skills/collaboration/issues/SKILL.md)** — GitHub issue-resolution workflow spanning triage, root-cause analysis, TDD fixes, and PR management. **Use when:** turning vague bug reports or feature requests into actionable, tracked issues and fixes.
- **[Collaboration Standup Notes](sub-skills/collaboration/standup/SKILL.md)** — async-first standup notes generated from commit history for remote-team coordination. **Use when:** producing daily standup/progress logs or tracking blockers asynchronously.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the code review audit and scoring:
- 👉 Recommend calling **[Content Master](../content-master/SKILL.md)** next to update code documentation, record final architectural decisions (ADRs), and compile release notes.

---

## 🛡️ Review Council Protocol
This Orchestrator operates the **[Agent Review Framework](file:///Users/macos/.antigravity-global/agent_review_framework.md)** Phases 6-11.
1. Perform Level 1 PHC.
2. Delegate to relevant Sub-Disciplines.
3. Consolidate into a **Readiness Score (>85 required)**.

---

## 📊 Summary Contract
When activated, the Orchestrator MUST return:
1. Severity-ordered findings.
2. Readiness Score.
3. **Verdict**: APPROVE / REQUEST CHANGES / BLOCK.

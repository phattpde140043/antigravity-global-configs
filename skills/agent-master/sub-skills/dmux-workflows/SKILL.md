---
name: dmux-workflows
description: "Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other harnesses. USE WHEN: user asks to run work in parallel; complex task benefits from divide-and-conquer. NOT FOR: framework-specific coding rules; architecture decisions unrelated to orchestration."
origin: ECC
---

# dmux Workflows

Orchestrate parallel AI agent sessions with clear boundaries, merge discipline, and low conflict risk.

---

## Purpose

This skill defines operational patterns for multi-agent execution in parallel.
It focuses on task decomposition, pane/session roles, and merge strategy.

---

## When to Activate

- user asks to run work in parallel
- complex task benefits from divide-and-conquer
- coordinating multiple agent sessions across harnesses
- prompts like: split this work, multi-agent, use dmux

---

## Scope Boundaries

Use this skill for:
- deciding what can run in parallel safely
- assigning lane ownership to each pane/agent
- merge and integration order
- conflict prevention and recovery patterns

Do NOT use this skill as primary source for:
- framework-specific coding rules
- architecture decisions unrelated to orchestration
- replacing built-in subagent workflows when in-process tools are enough

---

## What is dmux

dmux is a tmux-based pane manager for agent sessions.
Core interaction model:
- `n`: create new pane with prompt
- `m`: merge pane output into main context

Typical install:
- `npm install -g dmux`

If `tmux` is missing, install via package manager for the OS first.

---

## Operational Rules

1. Parallelize only independent tasks.
2. Assign one owner per file area when possible.
3. Define a merge order before execution.
4. Keep pane prompts explicit about boundaries and outputs.
5. Limit active panes to sustainable token budget.

---

## Workflow

## Step 1: Partition the Work

Split the objective into lanes by concern:
- research
- implementation
- tests
- docs/review

Reject parallel split if lanes mutate the same files without isolation.

## Step 2: Define Contracts per Lane

Each lane must declare:
- scope (files or subsystem)
- output format
- done criteria
- no-touch boundaries

## Step 3: Execute in Parallel

Use dmux panes (or equivalent multi-session setup) to run lanes concurrently.
Keep prompts short, specific, and test-oriented.

## Step 4: Merge Strategically

Merge low-risk lanes first:
1. research/spec outputs
2. isolated code changes
3. tests
4. integration and cleanup

Review before merge; do not blindly merge pane output.

## Step 5: Final Integration

Run build/tests once all merges are complete.
Resolve conflicts in main lane with explicit decisions.

---

## Recommended Patterns

## Pattern A: Research + Implement

- Lane 1: gather constraints and best practices
- Lane 2: implement baseline
- Merge research back before final hardening

## Pattern B: Multi-File Feature

- lane per independent module/file group
- main lane performs integration and end-to-end verification

## Pattern C: Test + Fix Loop

- lane 1 watches tests and summarizes failures
- lane 2 applies fixes and requests rerun

## Pattern D: Parallel Review

- lane per review lens: security, performance, testing gaps
- merge into one prioritized report

---

## Conflict Control

Use git worktrees when lanes may touch overlapping areas.
Suggested flow:
1. create isolated worktree per lane
2. execute lane in its own worktree
3. merge branches back in controlled order

If worktrees are not available, reduce lane overlap to near zero.

---

## Tooling Fallbacks

If dmux is unavailable:
- use built-in subagent orchestration for read-heavy discovery
- run sequential mini-batches with strict lane contracts
- prefer fewer lanes over unmanaged concurrency

Rule:
- orchestration quality matters more than tool choice.

---

## Troubleshooting

- pane appears idle: check waiting-for-input state and prompt for next action
- merge conflicts spike: reduce lane overlap or switch to worktrees
- token burn is high: reduce active lanes and tighten prompts
- inconsistent outputs: enforce output template per lane

---

## Output Contract

When activated, return:

1. parallelization decision (yes/no and why)
2. lane plan (owner, scope, outputs)
3. merge order
4. risk controls (conflicts, token budget, validation)
5. final integration checklist

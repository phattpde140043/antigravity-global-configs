---
name: using-git-worktrees
description: Use when starting feature work that needs isolation or before executing implementation plans.
---

# Using Git Worktrees

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches without switching.

**Core principle:** Isolation prevents context pollution and accidentally committing unrelated changes.

## Directory Selection

1. Check for `.worktrees/` or `worktrees/` in project root.
2. Check for preferences in `CLAUDE.md`, `GEMINI.md`, or `AGENTS.md`.
3. Ask user if no convention exists.

## Safety Rules

- **Ignore Verification**: MUST verify the worktree directory is in `.gitignore` before creation.
- **Clean Baseline**: Run tests in the new worktree to ensure it starts clean.
- **Report Location**: Announce the worktree path and test status to the user.

## Creation Steps

```bash
# Create worktree
git worktree add .worktrees/branch-name -b branch-name

# Setup environment
npm install # or equivalent

# Verify baseline
npm test # or equivalent
```

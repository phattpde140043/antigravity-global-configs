# Defense-in-Depth Validation

## Overview

Fixing a bug at the source is step one. Ensuring it can never happen again—even if new bugs are introduced—is elite engineering.

**Formula:** Fix at the source + Guard at every layer.

---

## The 4 Layers of Defense

### Layer 1: Entry Point (The Filter)
Intercept bad data before it enters your business logic.
- **Tools**: schema validation, DTOs, type checks.
- **Action**: Throw or reject immediately if input is invalid.

### Layer 2: Business Logic (The Invariant)
Your core logic must remain valid regardless of how it was called.
- **Tools**: `assert()`, preconditions, invariant checks.
- **Action**: Validate parameters *inside* internal methods.

### Layer 3: Environment & Global (The Box)
Use the runtime environment to limit possible damage.
- **Tools**: Environment variables, file system permissions, network isolation.
- **Action**: Refuse to execute dangerous operations (e.g., `git init`) outside of `NODE_ENV=test` or specific directories.

### Layer 4: Instrumentation (The Beacon)
If a bug gets through all guards, make it loud and clear.
- **Tools**: Stack trace logging, health checks, observability alerts.
- **Action**: Log full context and stack trace *before* a dangerous or uncertain operation.

---

## Case Study: Git Init Pollution

**The Bug**: `.git` directory created in the source code folder during tests.

**Fix**: Ensure `projectDir` is never empty.

**Defense-in-Depth Implementation**:
1. **Layer 1 (DTO)**: `CreateProjectRequest` validates that `tempDir` is a valid, existing path string.
2. **Layer 2 (Invariant)**: `Project.create()` throws if the target directory is empty or resolves to a sensitive path.
3. **Layer 3 (Env Guard)**: `WorktreeManager` checks `process.env.STRICT_SANDBOX` and refuses to run `git init` in any path that isn't a child of `OS.tmpdir()`.
4. **Layer 4 (Instrumentation)**: `execFileAsync` logs the command, CWD, and stack trace to `stderr` if the operation belongs to a test suite.

---

## Implementation Prompt
"I've identified the root cause. Now, how do we implement 4 layers of defense so this class of bug is structurally impossible in the future?"

---
**Next Step in Debugging Workflow:**
👉 **[Handling Flakiness & Races: Condition-Based Waiting](./condition-based-waiting.md)**

[Back to Systematic Debugging Master Skill](./SKILL.md)


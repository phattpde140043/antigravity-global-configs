---
name: workspace-surface-audit
description: "Audit and classify Copilot instructions and skills for a specific workspace using evidence from the actual codebase. Determine what should be project-level (auto-load) vs user-level (on-demand), and identify gaps or stale surfaces. USE WHEN: the request clearly matches the workspace-surface-audit domain. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Workspace Surface Audit

## Purpose

Classify Copilot instructions and skills into the right scope for a specific workspace, backed by evidence from the actual codebase — not guesswork.

---

# When to Use

- A workspace has grown instructions/skills organically and needs cleanup
- Setting up Copilot surfaces for a new repo
- Suspecting stale or misplaced instructions (project-level rule that doesn't match the stack)
- Wanting a repeatable audit instead of manual curation
- After major stack changes (new framework, dropped language, architecture shift)

---

# Classification Model

Two buckets only:

## PROJECT (auto-load every session)

Location: `.github/instructions/` and `.github/skills/`

Qualifies when:
- The repo clearly uses the matching stack/framework
- The rule or skill applies to every coding session in this workspace
- The `applyTo` pattern matches files that actually exist in the repo

## GLOBAL (on-demand, available across all workspaces)

Location: `~/.copilot/skills/` and `~/.copilot/instructions/`

Qualifies when:
- The skill is framework-agnostic or meta-level (agent workflow, planning, review)
- The repo might need it situationally but not every session
- It applies equally to all workspaces, not just this one

---

# Workflow

## Step 1 — Read the Repo Stack

Establish the actual stack before classifying anything:

```bash
# File extensions distribution
find . -type f -name '*.cs' -o -name '*.ts' -o -name '*.py' -o -name '*.java' -o -name '*.yml' | head -50

# Package managers and frameworks
ls -la *.csproj *.sln package.json tsconfig.json pom.xml pyproject.toml go.mod 2>/dev/null

# Build and test config
ls -la Dockerfile docker-compose* azure-pipelines.yml .github/workflows/ 2>/dev/null
```

Record:
- Languages in use
- Frameworks in use
- Package manager(s)
- Test stack
- Deployment surface
- External dependencies (search, AI, databases)

---

## Step 2 — Inventory Current Surfaces

List all instructions and skills at both scopes:

| Path | Type | Scope | `applyTo` | Status |
|------|------|-------|-----------|--------|
| `.github/instructions/X.md` | instruction | project | `**/*.cs` | ? |
| `.github/skills/Y/SKILL.md` | skill | project | — | ? |
| `~/.copilot/skills/Z/SKILL.md` | skill | global | — | ? |
| `~/.copilot/instructions/W.md` | instruction | global | — | ? |

---

## Step 3 — Build Evidence Table

For every surface, record repo evidence supporting or opposing its placement:

```text
Component                              | Type        | Current Scope | Proposed | Evidence                                    | Justification
engineering-guardrails.instructions.md | instruction | project       | PROJECT  | 200+ .cs files, applyTo=**/*.cs matches     | Active C# codebase
search-query-design/SKILL.md          | skill       | project       | PROJECT  | Azure Search used in 5+ services             | Core domain skill
distributed-system/SKILL.md           | skill       | global        | GLOBAL   | No multi-service architecture in this repo   | Reference only
pr-review/SKILL.md                    | skill       | global        | GLOBAL   | Applies to all repos equally                 | Meta-workflow skill
```

---

## Step 4 — Classify Each Surface

### Promote to PROJECT when:

- The repo has files matching the skill's domain (e.g., `.cs` files for ASP.NET rules)
- The instruction's `applyTo` pattern matches real files in the workspace
- The skill addresses this repo's core domain (search, AI, tenant isolation)

### Keep as GLOBAL when:

- The skill is meta-level (planning, review, debugging, architecture design)
- The repo doesn't actively use the skill's domain
- The skill applies identically across all workspaces

### Flag as STALE when:

- The instruction references frameworks/patterns not present in the repo
- The `applyTo` pattern matches zero files
- The skill duplicates another surface at a different scope

### Flag as GAP when:

- The repo uses a framework/pattern with no corresponding instruction or skill
- A critical domain (security, performance, tenant isolation) has no coverage

---

## Step 5 — Produce the Audit Plan

Actions:
- **Keep** — surface is correctly placed, no change
- **Move** — surface is at wrong scope (global ↔ project)
- **Update** — surface content is stale or `applyTo` needs fixing
- **Create** — gap identified, new surface needed
- **Remove** — surface is duplicated or obsolete

---

## Step 6 — Verify

After applying changes, verify:

- Every PROJECT instruction has an `applyTo` that matches real files
- No duplicate coverage between project and global scope
- No stale framework references remain
- Gaps identified in Step 4 are addressed or documented

---

# Output Format

```text
STACK SUMMARY
- Languages, frameworks, runtime, deployment surface

CURRENT INVENTORY
- Count of project instructions, project skills, global skills, global instructions

CLASSIFICATION TABLE
- Full evidence table from Step 3

AUDIT PLAN
- Actions: keep / move / update / create / remove with justification

VERIFICATION
- Checks run
- Remaining gaps
- Open questions for the user
```

---

# Scope Boundaries

**This skill covers:**
- Auditing instruction/skill placement and relevance for a workspace
- Identifying gaps and stale surfaces
- Producing an evidence-backed reclassification plan

**This skill does NOT cover:**
- Writing the actual content of new instructions/skills → use the appropriate domain skill
- Agent runtime debugging → `agent-introspection-debugging`
- Architecture or code design decisions → `architecture-design`
- Security auditing of application code → `securities-audit`

---
name: documentation-and-adrs
description: "Records architectural decisions and project documentation. Use when making significant design choices, changing public APIs, or recording context for future maintenance."
---

# Documentation and ADRs

## Overview

Document decisions, not just code. Code shows *what* was built; documentation explains *why* and what alternatives were rejected.

## Architecture Decision Records (ADRs)
ADRs capture reasoning for expensive-to-reverse decisions (database choice, auth strategy, library selection).

### ADR Template
1. **Title**: ADR-00X [Short description]
2. **Status**: Proposed / Accepted / Superseded
3. **Context**: Requirements and constraints.
4. **Decision**: What we're doing and why.
5. **Alternatives**: What we rejected and why.
6. **Consequences**: Trade-offs and follow-up work.

## Inline Documentation
- **Comment "Why", not "What"**: Don't restate the code. Explain non-obvious intent or hacky workarounds.
- **Rules Files (CLAUDE.md)**: Primary source for project-specific conventions and commands.
- **Gotchas**: Document known traps or lifecycle requirements (e.g. "must call X before Y").

## Red Flags
- Significant architectural choices with no written rationale.
- Public APIs with no type documentation or usage examples.
- Commented-out code instead of deletion (Git has history).
- TODOs left standing for weeks.

## Verification
- [ ] ADRs exist for major architectural decisions.
- [ ] README covers quick start and commands.
- [ ] No commented-out code remains.
- [ ] Rules files are up to date.

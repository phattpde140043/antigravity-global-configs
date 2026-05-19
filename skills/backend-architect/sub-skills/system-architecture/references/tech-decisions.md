# Tech Decision Framework

## When to Make a Tech Decision

Any decision that:
- Affects more than one team or service
- Is difficult/expensive to reverse
- Introduces a new technology or pattern
- Changes the build/deploy pipeline

→ MUST go through this framework and be documented as an **ADR** (see `resources/adr-playbook.md`).

## Decision Process

### 1. Define the Problem
- What specific problem are we solving?
- What happens if we do nothing?
- What constraints exist? (budget, timeline, team skills)

### 2. Identify Options
- List at least 2-3 alternatives
- Include "do nothing" as an option
- Research each option enough to understand trade-offs

### 3. Evaluate Against Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Team familiarity** | High | Can the team use this effectively today? |
| **Ecosystem maturity** | High | Is it production-proven? Active community? |
| **Operational cost** | Medium | Total cost of ownership (hosting, licensing, maintenance) |
| **Reversibility** | High | How hard is it to switch if this doesn't work? |
| **Security posture** | High | CVE history, update cadence, dependency chain |
| **Integration** | Medium | How well does it fit existing stack? |

### 4. Make the Decision
- Choose the option that best fits constraints
- **Prefer boring technology** — proven tools over shiny new ones
- Document WHY other options were rejected

### 5. Record as ADR
- Use the templates in `resources/adr-playbook.md`
- Include context, decision, alternatives, and trade-offs
- Store in `docs/decisions/` directory

## Anti-Patterns

- **Resume-Driven Development** — Choosing tech to learn it, not because it fits
- **Cargo Culting** — "Google uses it so we should too"
- **Analysis Paralysis** — Spending more time deciding than the decision is worth
- **Implicit Decisions** — Making tech choices without documenting them

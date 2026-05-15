---
name: writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work.
---

# Writing Skills (TDD for Process)

**Writing skills is Test-Driven Development applied to process documentation.**

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

## TDD Mapping

- **RED (Fail)**: Agent violates a rule or fails a task without the skill (baseline).
- **GREEN (Pass)**: Agent complies or succeeds with the skill present.
- **REFACTOR**: Refine the skill to close loopholes and improve clarity.

## Skill Structure (SKILL.md)

1. **YAML Frontmatter**: `name` and `description` (Start with "Use when...").
2. **Overview**: Core principle in 1-2 sentences.
3. **When to Use**: Triggering symptoms and contexts.
4. **Implementation**: Patterns, code, and references.
5. **Common Mistakes**: Loopholes and rationalizations.

## Red Flags in Skill Writing

- **Workflow Summary in Description**: NEVER summarize "how" in the description; only "when".
- **Narrative Storytelling**: Keep it as a reference guide, not a diary.
- **Untested Skills**: Deploying a skill without watching an agent use it first.

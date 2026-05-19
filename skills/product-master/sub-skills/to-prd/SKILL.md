---
name: to-prd
description: "Convert conversation context and codebase understanding into a structured Product Requirements Document (PRD). USE WHEN: user wants to create a PRD, formalize requirements, or crystallize what to build. NOT FOR: initial brainstorming (use `brainstorming`); writing implementation plans (use `writing-plans`)."
---

# To PRD

This skill takes the current conversation context and codebase understanding and produces a PRD. Do NOT interview the user — synthesize what you already know.

## Scope Boundaries

Use this skill for:
- Converting conversation insights into a formal PRD
- Crystallizing requirements after brainstorming or grilling sessions
- Publishing structured requirements to GitHub Issues

Do NOT use this skill for:
- Initial ideation — use `brainstorming`
- Stress-testing a plan — use `grill-with-docs`
- Writing implementation plans — use `writing-plans`
- Breaking a plan into issues — use `to-issues`

## Process

### 1. Explore the repo
Understand the current codebase state if you haven't already. Use the project's domain glossary vocabulary throughout the PRD, and respect any ADRs in the area you're touching.

### 2. Sketch modules
Sketch out the major modules you will need to build or modify. Actively look for opportunities to extract deep modules that can be tested in isolation.

Check with the user that these modules match their expectations. Check which modules they want tests written for.

### 3. Write the PRD

Use the template below:

---

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story in the format:

1. As an <actor>, I want a <feature>, so that <benefit>

This list should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made:
- Modules that will be built/modified
- Interfaces that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts

Do NOT include specific file paths or code snippets — they go stale quickly.

## Testing Decisions

- What makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (similar tests in the codebase)

## Out of Scope

Things that are explicitly out of scope for this PRD.

## Further Notes

Any further notes about the feature.

---

### 4. Publish
Publish the PRD to the project issue tracker or save to `docs/specs/` depending on the project's convention.

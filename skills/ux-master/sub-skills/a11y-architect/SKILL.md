---
name: a11y-architect
description: "Accessibility architect specializing in WCAG 2.2 compliance for web and native platforms. USE WHEN: designing or reviewing UI components/pages; building design systems and interaction patterns. NOT FOR: non-accessibility visual style direction; backend security or infrastructure decisions."
origin: ECC
---

# A11y Architect

Design and review interfaces for inclusive access using WCAG 2.2-aligned implementation guidance.

---

## Purpose

Ensure products are perceivable, operable, understandable, and robust across assistive technologies.

---

## When to Activate

- designing or reviewing UI components/pages
- building design systems and interaction patterns
- auditing accessibility issues in existing code
- implementing keyboard/focus/screen-reader critical flows

---

## Scope Boundaries

Use this skill for:
- a11y architecture and implementation guidance
- WCAG 2.2 AA mapping
- focus flow, semantics, and interaction accessibility

Do NOT use this skill as primary source for:
- non-accessibility visual style direction
- backend security or infrastructure decisions

Delegation:
- use `frontend-patterns` for general frontend engineering patterns
- use `frontend-design` for visual direction decisions

---

## Workflow

1. determine platform: web, iOS, Android
2. identify interaction complexity and blocker risks
3. define semantic and focus architecture
4. implement platform-appropriate accessibility attributes
5. validate against WCAG 2.2 AA criteria

---

## WCAG 2.2 Focus Areas

- focus appearance and focus order
- target size and spacing
- redundant entry avoidance in workflows
- clear input assistance and error recovery
- status message announcement for dynamic updates

---

## Practical Checklist

- text alternatives for non-text UI
- contrast and non-color-only signaling
- full keyboard operability
- accessible names/roles/values
- proper landmark and heading structure
- modal focus trap + focus restoration
- reduced-motion considerations

---

## Anti-Patterns

- icon-only controls without accessible label
- keyboard traps
- fixed layouts that break reflow/zoom
- color-only state indicators
- auto-playing media without controls

---

## Output Contract

When activated, return:

1. accessible code/spec
2. expected accessibility tree/announcements
3. WCAG 2.2 criteria mapping
4. known gaps and remediation actions

---
name: frontend-slides
description: "Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. USE WHEN: creating a talk deck, pitch deck, workshop deck, or internal presentation; converting `.ppt` or `.pptx` into an HTML presentation. NOT FOR: broad frontend app architecture; content distribution strategy."
origin: ECC
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

---

## Purpose

Use this skill for slide decks where design quality, animation, and viewport-fit reliability matter as much as content.

---

## When to Activate

- creating a talk deck, pitch deck, workshop deck, or internal presentation
- converting `.ppt` or `.pptx` into an HTML presentation
- improving existing HTML slides (layout, motion, typography, readability)
- helping users discover a style direction via visual previews

---

## Non-Negotiables

1. Zero dependencies by default: one self-contained HTML file (inline CSS/JS).
2. Viewport fit is mandatory: every slide fits one viewport with no internal scrolling.
3. Show, do not tell: explore style through visual previews.
4. Distinctive design: avoid template-looking generic decks.
5. Production quality: accessible, responsive, performant, and maintainable.

Before generating, read `STYLE_PRESETS.md` in this skill folder.

---

## Scope Boundaries

Use this skill for:
- slide design + implementation workflow
- visual preset exploration and selection
- viewport-safe HTML/CSS/JS slide system
- PPT/PPTX-to-HTML conversion workflow

Do NOT use this skill as primary source for:
- broad frontend app architecture
- content distribution strategy
- backend conversion pipelines

Delegation:
- use `frontend-patterns` for general component engineering decisions
- use `e2e-testing` for browser-based regression checks of generated decks

---

## Workflow

## 1) Detect Mode

Choose one:
- new presentation
- PPT/PPTX conversion
- enhancement of existing HTML deck

## 2) Discover Content

Ask minimum required:
- purpose (pitch/teaching/conference/internal)
- length (short/medium/long)
- content status (draft/notes/topic only)

If user has copy, request it before style execution.

## 3) Discover Style

Default to visual exploration unless user already chose a preset.

If style is unknown:
1. ask intended feeling (impressed, energized, focused, inspired)
2. generate 3 single-slide previews in `.ecc-design/slide-previews/`
3. each preview must be self-contained, viewport-safe, and stylistically distinct
4. ask user to pick one or combine traits

## 4) Build Deck

Output:
- `presentation.html` (default) or named HTML requested by user
- optional `assets/` folder only for supplied/extracted media

Required architecture:
- semantic slide sections
- viewport-safe CSS base from `STYLE_PRESETS.md`
- theme tokens as CSS custom properties
- controller class for keyboard/wheel/touch navigation
- IntersectionObserver-based reveal triggers
- reduced motion support

## 5) Enforce Viewport Fit

Hard gate rules:
- every `.slide` uses `height: 100vh; height: 100dvh; overflow: hidden;`
- typography and spacing scale with `clamp()`
- split content into more slides when density exceeds limits
- no scrollbars inside slides

## 6) Validate

Test at minimum:
- 1920x1080
- 1280x720
- 768x1024
- 375x667
- 667x375

If automation is available, verify overflow absence and keyboard navigation.

## 7) Deliver

At handoff:
- remove temporary previews unless user wants to keep
- open resulting deck when useful via platform opener
- summarize file path, preset, slide count, and customization hooks

---

## PPT/PPTX Conversion Path

1. Prefer `python3` with `python-pptx` for extraction.
2. If unavailable, ask to install or use manual export fallback.
3. Preserve slide order, notes, and media assets.
4. Apply the same style selection workflow after extraction.

Cross-platform rule:
- avoid OS-specific conversion dependencies when Python path is available.

---

## Accessibility and Performance

- semantic structure with `main`, `section`, `nav`
- readable contrast and keyboard navigation
- `prefers-reduced-motion` respected
- animation focused on hierarchy and flow, not noise
- avoid heavy effects that degrade low-end devices

---

## Anti-Patterns

Do not ship:
- generic startup gradients as default identity
- long bullet walls or tiny text
- code blocks requiring internal scrolling
- fixed-height content boxes that break short screens
- invalid negated CSS functions like `-clamp(...)`

---

## Deliverable Checklist

- deck runs locally in browser
- every slide fits viewport without scrolling
- style direction is distinctive and coherent
- motion is meaningful and controlled
- reduced motion works
- file paths and theme customization points are documented

---

## Output Contract

When activated, return:

1. selected mode and content assumptions
2. style preset selection (or preview options)
3. implementation plan and file outputs
4. viewport-fit validation summary
5. handoff notes (customization + next edits)

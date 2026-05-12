---
name: browser-automation
description: "Functional browser automation using Playwright, Skyvern, and AWT. Use for task execution, multi-tenant verification, and visual testing."
metadata:
  category: tool
  triggers: browser, playwright, skyvern, awt, browser-automation
risk: safe
source: community
date_added: "2026-05-12"
---

# Browser Automation (Functional)

## Overview

Execute programmatic browser interactions for testing, data extraction, or system verification. This skill provides the "hands and eyes" for the agent in a live browser environment.

## When to Use

- Executing multi-tenant isolation checks (L3 Stage 2/3).
- Automating repetitive UI tasks or data gathering.
- Performing visual verification or OCR-based interaction.
- Debugging UI flows that cannot be captured by static unit tests.

## Iron Law

**ALWAYS verify the final state. Never assume a click or navigation succeeded without a follow-up assertion or screenshot.**

## Tooling & Techniques

### 1. Playwright (Core)
- Use for deterministic, selector-based automation.
- Leverage `lib/helpers.js` for safe interaction patterns.
- **Reference**: `e2e-testing` for deep POM architecture.

### 2. Skyvern (AI-Powered)
- Use for complex, dynamic, or visually ambiguous sites.
- Best for "Intent-based" automation where selectors are brittle.
- **Reference**: **[references/skyvern.md](references/skyvern.md)** (CLI & MCP Guide).

### 3. AWT (Visual Matching)
- Use for platforms like Flutter or Canvas where DOM selectors don't exist.
- Leverages OpenCV and OCR for interaction.
- **Reference**: **[references/awt.md](references/awt.md)**.

## Step-by-Step

1. **Detect**: Check for a running dev server using `lib/helpers.js`.
2. **Initialize**: Start the browser session (Headless by default in CI).
3. **Act**: Execute steps (navigate, click, type).
4. **Assert**: Verify success via `expect`, `screenshot`, or `validate`.
5. **Report**: Save traces and logs for failure analysis.

---

## 🔗 Related Skills
- **e2e-testing**: Strategy, POM, and Architecture.
- **browser-testing-with-devtools**: Live inspection and debugging.
- **testing-workflow**: Overall QA lifecycle management.

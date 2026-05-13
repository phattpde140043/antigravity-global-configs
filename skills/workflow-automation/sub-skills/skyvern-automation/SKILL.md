---
name: skyvern-automation
description: "Expert in AI-powered browser automation using Skyvern. Focuses on visual navigation, structured data extraction, and complex multi-page workflow automation."
---

# Skyvern AI Browser Automation

Master the use of Skyvern for intelligent, vision-based web automation.

## 🏗️ Automation Classification
1. **Validation**: Use `skyvern browser validate` for simple boolean checks (e.g., "Is user logged in?").
2. **Extraction**: Use `skyvern browser extract` with JSON schemas for high-fidelity data scraping.
3. **Actions (Act)**: Use `skyvern browser act` when labels are clear and the flow is simple.
4. **Workflows**: Use `skyvern workflow create` for multi-page, reusable, and complex production automations.

## 🚀 Key Patterns
- **Hybrid Targeting**: Combine deterministic selectors (`--selector`) with AI intent (`--intent`) for maximum reliability.
- **Session Management**: Reuse sessions across commands to maintain state (login, cookies).
- **Safe Login**: Always use `skyvern browser login` with stored credentials; NEVER type passwords directly.
- **Verification**: Always take a `screenshot` or run a `validate` check after page-changing actions.

## 🛡️ Error Recovery & Optimization
- **Action Failure**: If a click fails, add more context to the prompt or switch to a hybrid selector.
- **Empty Extraction**: Implement waits for content visibility before extracting.
- **Workflow Blocks**: Split complex flows into one block per page/step for better debugging and caching.

## 📋 Verification Checklist
- [ ] Is the correct command used (Validate vs Extract vs Act)?
- [ ] Are passwords handled through the secure credential vault?
- [ ] Is a screenshot or validation check performed after key actions?
- [ ] Are complex flows split into discrete workflow blocks?
- [ ] Does the automation include error recovery logic (Waits, context)?

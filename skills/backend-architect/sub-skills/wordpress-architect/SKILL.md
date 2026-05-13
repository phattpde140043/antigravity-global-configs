---
name: wordpress-architect
description: "Expert in high-fidelity codebase conversion (React/HTML/Next.js) to WordPress. Focuses on pixel-perfect UI preservation, ACF dynamic mapping, and technical SEO."
---

# WordPress Architecture & Conversion

Master the transition from static/React frontends to dynamic, CMS-driven WordPress themes.

## 🏗️ Forensic Conversion Process
1. **Phase 1: UI Comparison**: Side-by-side audit of source components vs. WordPress templates.
2. **Phase 2: Full Audit**: Deep dive into SEO, CMS editability, and performance.
3. **Phase 3: Strategic Mapping**: Map static content to `get_field()` (ACF) or standard WP functions.
4. **Phase 4: Iterative Validation**: Fix one issue at a time with "Zero UI/DOM Change" verification.

## 🛡️ Absolute UI Lock (Principles)
- **Zero Structure Change**: No extra `div` wrappers; preserve original nesting exactly.
- **Class Integrity**: Maintain original CSS/Tailwind class names without "cleaning up".
- **Asset Pathing**: Use `get_template_directory_uri()` for all assets to ensure portability.

## ⚡ Technical Implementation
- **Navigation**: Use custom Walkers to preserve complex Tailwind structures in `wp_nav_menu`.
- **Dynamic Content**: Replace static text with `the_title()`, `the_content()`, or ACF fields.
- **Hooks**: Always include `wp_head()` and `wp_footer()` at exact boundaries.

## 📋 Verification Checklist
- [ ] Is the UI a 1:1 pixel-perfect match with the original?
- [ ] Are all static paths replaced with dynamic WordPress functions?
- [ ] Is technical SEO (Meta, Schema, Hierarchy) preserved?
- [ ] Are dynamic menus using the original HTML/CSS structure?
- [ ] Does the theme pass a full audit with zero DOM regressions?

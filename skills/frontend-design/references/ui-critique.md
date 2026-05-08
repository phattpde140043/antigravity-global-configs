# UI Critique & Accessibility Checklist

Use this checklist to evaluate any UI modification or new feature.

## 👁️ Visual Hierarchy
- [ ] Is there a clear focal point?
- [ ] Can the eye easily navigate from the primary action to secondary information?
- [ ] Is spacing consistent (using a 4px or 8px grid)?

## ♿ Accessibility (WCAG 2.1 AA)
- [ ] **Contrast**: Text ratio at least 4.5:1 (use a contrast checker).
- [ ] **Touch Targets**: Minimum 44x44px for mobile interactions.
- [ ] **Screen Readers**: All interactive elements have descriptive `aria-labels` and `roles`.
- [ ] **Keyboard Nav**: Focus states are clearly visible and the tab order is logical.

## 🧠 Cognitive Design
- [ ] **Affordance**: Do clickable elements look clickable?
- [ ] **Feedback**: Does every action have an immediate visual/haptic response?
- [ ] **Errors**: Are error messages helpful and actionable (not just "An error occurred")?

## 🚀 Perceived Performance
- [ ] **Skeleton Screens**: Used instead of blank loading states.
- [ ] **Optimistic UI**: Are actions (like "Like" or "Save") reflected immediately before the server confirms?

## 📱 Responsiveness
- [ ] Does the layout break at standard breakpoints (320px, 768px, 1024px)?
- [ ] Are images optimized and responsive (`srcset`)?

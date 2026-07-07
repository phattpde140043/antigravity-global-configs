---
name: ux-master
description: "Master UX & Design Orchestrator. Coordinates Frontend Design, UI Patterns, and Accessibility."
category: engineering
metadata:
  category: master-orchestrator
  triggers: [frontend, ui-ux, design-systems, accessibility, slides]
---

# 🎨 UX & Design Master Orchestrator

The visual and interaction lead. This master skill coordinates the creation of beautiful, accessible, and high-performance user interfaces.

---

## 🧭 Design Strategy
- **Rich Aesthetics**: WOW the user with premium design (glassmorphism, gradients, micro-animations).
- **Framework Excellence**: Master **Angular** (state management, migration, UI patterns) and **Next.js** for enterprise web.
- **Mobile Mastery**: Implement high-end mobile UIs using **Android Jetpack Compose** and **Apple HIG** standards.
- **Immersive Experiences**: Create **3D Web Experiences** using **Three.js** and **Anime.js** for high-end visual impact.
- **Accessibility-First (A11y)**: Prioritize contrast (4.5:1), focus states, and aria-labels as non-negotiable.
- **Performance Excellence**: Optimize for Core Web Vitals (LCP < 2.5s, FID < 100ms, CLS < 0.1).
- **Visual Validation**: Systematically check for layout shifts, brand consistency, and professional polish.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing UX or frontend tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure stunning visual quality, performance, and complete accessibility:

### 🔄 Sequential Sub-Skill Pipeline
```
[Baseline UI Standards] ──→ [Frontend Design] ──→ [Frontend Patterns] ──→ [Animejs Animations] ──→ [A11y Architect]
```


### 1. Visual Design & UI

**Visual design foundations**
- **[Frontend Design](sub-skills/frontend-design/SKILL.md)** — Apple-level product design, UX flows, and high-end visual systems. **Use when:** setting art direction, visual language, or premium UI aesthetics for a product. **Not for:** React implementation patterns (see Frontend Patterns) or backend/API design.
- **[UX/UI Principles](sub-skills/uxui-principles/SKILL.md)** — Evaluate interfaces against 168 research-backed UX/UI principles and detect antipatterns. **Use when:** auditing a design for principle violations or injecting UX context into an AI coding session. **Not for:** producing final mockups or copy.
- **[Frontend Patterns](sub-skills/frontend-patterns/SKILL.md)** — React/Next.js component, state-management, and performance patterns. **Use when:** building React components/feature modules or deciding a state-management approach. **Not for:** high-concept art direction (see Frontend Design) or backend/API contracts.
- **[Baseline UI Standards](sub-skills/baseline-ui/SKILL.md)** — Enforces animation durations, typography scale, component a11y, and anti-pattern checks in Tailwind projects. **Use when:** building or reviewing Tailwind/React UI to enforce design consistency. **Not for:** data-fetching logic or non-Tailwind styling stacks.

**Motion & animation**
- **[Anime.js Animations](sub-skills/animejs-animation/SKILL.md)** — Complex, high-performance DOM/SVG timeline animations with Anime.js. **Use when:** adding scripted micro-animations, staggered sequences, or SVG motion. **Not for:** scroll-driven storytelling (see Scroll Experience Design).
- **[Scroll Experience Design](sub-skills/scroll-experience/SKILL.md)** — Immersive scroll-driven parallax and cinematic narratives (GSAP ScrollTrigger, Framer Motion). **Use when:** building scroll-triggered storytelling like NYT interactives or Apple product pages. **Not for:** standard timeline animations (see Anime.js Animations).

**3D, canvas & imagery**
- **[Spline 3D Integration](sub-skills/spline-3d/SKILL.md)** — Embed and control interactive 3D scenes from Spline.design in web/React projects. **Use when:** adding a Spline 3D scene with runtime control to a page. **Not for:** hand-coded Three.js/WebGL or 2D canvas drawing.
- **[Canvas Design Philosophy](sub-skills/canvas-design/SKILL.md)** — Create a visual design philosophy / aesthetic movement, then express it as artwork output as `.md`, `.pdf`, and `.png`. **Use when:** defining a bold art-direction manifesto and producing visual expression pieces. **Not for:** coding interactive HTML `<canvas>`/WebGL apps (the name is misleading).
- **[Unsplash Integration](sub-skills/unsplash-integration/SKILL.md)** — Search and fetch free professional photography via the Unsplash API. **Use when:** sourcing responsive hero/section imagery for a design. **Not for:** generating original artwork or icon systems.

**Presentations & generated media**
- **[Frontend Slides](sub-skills/frontend-slides/SKILL.md)** — Build animation-rich HTML presentations from scratch or from PowerPoint. **Use when:** creating a talk/pitch/workshop deck or converting `.ppt`/`.pptx` to HTML. **Not for:** broad frontend app architecture.
- **[Remotion Core](sub-skills/remotion/core/SKILL.md)** — Generate programmatic videos in React with transitions, zoom, and text overlays (e.g. Stitch-project walkthroughs). **Use when:** composing a video from React components and timeline interpolation. **Not for:** real-time interactive UI.
- **[Remotion Performance](sub-skills/remotion/best-practices/SKILL.md)** — Remotion best practices for reliable, fast rendering (concurrency, frame caching, Lambda). **Use when:** optimizing or troubleshooting Remotion renders. **Not for:** initial composition setup (see Remotion Core).

**UX research, flows & writing**
- **[UX Persuasion Engineering](sub-skills/ux-persuasion/SKILL.md)** — Apply behavioral psychology and choice architecture to reduce friction and guide user behavior. **Use when:** conversion friction comes from interaction design, layout, or sequencing rather than copy. **Not for:** copy-only fixes (see UX Copywriting).
- **[UX Wireframe Flows](sub-skills/ux-flow/SKILL.md)** — Design user flows and screen structure with StyleSeed patterns (progressive disclosure, hub-and-spoke, information pyramids). **Use when:** mapping multi-screen navigation and information hierarchy before visual design. **Not for:** pixel-level component styling.
- **[UX Usability Feedback](sub-skills/ux-feedback/SKILL.md)** — Add loading, empty, error, and success feedback states to components and pages. **Use when:** implementing state feedback with mobile-first rules on StyleSeed components. **Not for:** heuristic scoring (see UX Auditing).
- **[UX Copywriting](sub-skills/ux-copy/SKILL.md)** — Generate microcopy in StyleSeed's Toss-inspired voice for buttons, empty states, errors, toasts, confirmations, and forms. **Use when:** writing or refining in-product microcopy. **Not for:** long-form marketing content.
- **[UX Auditing](sub-skills/ux-audit/SKILL.md)** — Audit screens against Nielsen's heuristics and mobile UX best practices in the StyleSeed Toss language. **Use when:** running a usability/heuristic review of existing screens. **Not for:** designing new flows from scratch (see UX Wireframe Flows).

**Components & widgets**
- **[Chat Widget](sub-skills/chat-widget/SKILL.md)** — Build a real-time support chat with a floating user widget and admin dashboard. **Use when:** adding live chat, customer-support chat, or in-app messaging. **Not for:** general notification or toast UIs.

**Browser extensions**
- **[Browser Extension Builder](sub-skills/browser-extension-builder/SKILL.md)** — Build cross-browser (Chrome/Firefox) extensions end to end: Manifest V3, popup UIs, monetization, and Web Store publishing. **Use when:** scoping, building, or shipping a browser-extension product. **Not for:** deep Chrome-specific service-worker/messaging internals (see Chrome Extension Developer).
- **[Chrome Extension Developer](sub-skills/chrome-extension-developer/SKILL.md)** — Deep Chrome Manifest V3 engineering: background/service workers, content scripts, and cross-context messaging. **Use when:** implementing or debugging Chrome extension internals and message passing. **Not for:** cross-browser packaging or store-launch strategy (see Browser Extension Builder).

**Mobile & Telegram**
- **[Building Native UI](sub-skills/building-native-ui/SKILL.md)** — Build React Native apps with Expo Router (styling, navigation, animations, native tabs). **Use when:** building or structuring an Expo Router mobile app. **Not for:** native Kotlin/Swift or web-only UI.
- **[Telegram Mini Apps](sub-skills/telegram-mini-apps/SKILL.md)** — Build Telegram Mini Apps (TWA) — web apps that run inside the Telegram webview. **Use when:** building an in-Telegram web app with React wrappers and state sync. **Not for:** chat-only bot interfaces (see Telegram Bots UI).
- **[Telegram Bots UI](sub-skills/telegram-bots-ui/SKILL.md)** — Build Telegram bots with conversational UX, inline keyboards, webhooks, and monetization. **Use when:** designing bot menus and inline-button flows via the Telegram Bot API. **Not for:** full webview apps (see Telegram Mini Apps).

**Reasoning companion (catalog outlier)**
- **[Satori Wisdom Companion](sub-skills/satori/SKILL.md)** — Clinically informed psychology + philosophy thinking partner (IFS, DBT, Stoicism, Jungian). **Use when:** seeking a structured philosophical/psychological conversation partner or exploring internal conflicts. **Not for:** generating OG/SVG images (despite the "Satori" name) or any visual/UI task.

### 2. Implementation & Performance

**Tailwind & design systems**
- **[Tailwind Patterns](sub-skills/tailwind-patterns/SKILL.md)** — Tailwind CSS v4 CSS-first configuration, container queries, and design-token architecture. **Use when:** writing Tailwind v4 utilities or migrating config to the CSS-first model. **Not for:** building a full component-variant library (see Tailwind Design System).
- **[Tailwind Design System](sub-skills/tailwind-design-system/SKILL.md)** — Production design systems in Tailwind with tokens, component variants, responsive patterns, and a11y. **Use when:** standing up a reusable, token-driven component library. **Not for:** one-off utility styling (see Tailwind Patterns).

**Frameworks, data & build**
- **[Nextjs Turbopack](sub-skills/nextjs-turbopack/SKILL.md)** — Next.js 16+ and Turbopack bundling, FS caching, and dev-speed tuning. **Use when:** developing Next.js 16+ or diagnosing slow dev startup/HMR. **Not for:** Next.js API semantics (routing/server actions) or general frontend architecture.
- **[TanStack Query Expert](sub-skills/tanstack-query/SKILL.md)** — TanStack Query async state: fetching, stale-time, mutations, optimistic updates, and Next.js App Router SSR. **Use when:** managing server state, cache invalidation, or optimistic mutations. **Not for:** client-only UI state or backend API design.
- **[Expo Upgrades](sub-skills/expo/upgrade/SKILL.md)** — Upgrade Expo SDK versions and resolve React Native dependency locks. **Use when:** bumping an Expo SDK major version or fixing upgrade dependency conflicts. **Not for:** greenfield app UI (see Building Native UI).

**TypeScript**
- **[TypeScript Pro](sub-skills/typescript/pro/SKILL.md)** — Advanced application-level TypeScript: generics, decorators, strict safety, enterprise patterns. **Use when:** writing strongly-typed app/library code with complex generics. **Not for:** compiler-internals or type-level metaprogramming (see TypeScript Expert).
- **[TypeScript Expert](sub-skills/typescript/expert/SKILL.md)** — Type-level programming, monorepo management, migration strategies, and tooling/performance. **Use when:** authoring advanced type-level utilities, tuning compiler performance, or migrating a codebase/monorepo. **Not for:** everyday typed feature code (see TypeScript Pro).

**Accessibility**
- **[A11y Architect](sub-skills/a11y-architect/SKILL.md)** — WCAG 2.2 accessibility architecture for web and native platforms. **Use when:** designing or reviewing UI components, pages, or design-system interaction patterns. **Not for:** non-a11y visual style direction or backend/infrastructure security.
- **[Screen Reader Testing](sub-skills/screen-reader-testing/SKILL.md)** — Test web apps with NVDA/JAWS/VoiceOver for real screen-reader behavior. **Use when:** validating actual assistive-tech output and ARIA behavior. **Not for:** automated contrast/lint checks or design-time a11y architecture (see A11y Architect).

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the user interface design and accessibility implementation:
- 👉 Recommend calling **[Review Master](../review-master/SKILL.md)** next to perform the final code readiness audit and ensure zero technical debt.

---

## 🏗️ Operating Pipeline
1. **Inspiration**: Draw from modern, premium web designs.
2. **Foundation**: Build the core design system and tokens.
3. **Components**: Create reusable, focused, and accessible components.
4. **Assembly**: Implement responsive layouts with smooth transitions.

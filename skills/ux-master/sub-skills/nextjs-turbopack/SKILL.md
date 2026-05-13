---
name: nextjs-turbopack
description: "Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack. USE WHEN: developing or debugging Next.js 16+ applications; diagnosing slow dev startup or HMR updates. NOT FOR: framework API semantics (routing, server actions, etc.); general frontend architecture decisions."
origin: ECC
---

# Next.js and Turbopack

Use this skill for practical Next.js bundling/runtime decisions with Turbopack-first development workflows.

---

## Purpose

Improve developer feedback loops and bundling reliability by choosing the right dev/build mode and diagnosing common performance bottlenecks.

---

## When to Activate

- developing or debugging Next.js 16+ applications
- diagnosing slow dev startup or HMR updates
- deciding Turbopack vs webpack fallback in development
- investigating production bundle behavior and build output size

---

## Scope Boundaries

Use this skill for:
- Turbopack/webpack mode decisions
- incremental bundling and cache behavior
- dev speed troubleshooting
- bundle analysis workflow selection

Do NOT use this skill as primary source for:
- framework API semantics (routing, server actions, etc.)
- general frontend architecture decisions
- stale assumptions about version-specific defaults

Delegation:
- use `documentation-lookup` for exact Next.js version behavior and flags
- use `frontend-patterns` for component/state/rendering architecture

---

## Operating Model

- Turbopack is the preferred default for modern Next.js dev workflows.
- Webpack fallback is for compatibility/debug scenarios only.
- Build/runtime behavior can vary by Next.js version; verify against current docs.

Version discipline:
- confirm command flags and build semantics for the exact installed version.

---

## Decision Guide

Use Turbopack when:
- standard day-to-day development
- large app where startup/HMR speed matters
- no blocking webpack-only plugin constraints

Use webpack fallback when:
- confirmed Turbopack bug/regression
- dev dependency requires webpack-only behavior
- isolating bundler-specific issues

Production note:
- verify `next build` bundling path for current version before making assumptions.

---

## Performance Workflow

1. confirm active bundler mode
2. measure baseline startup and update latency
3. inspect cache behavior and invalidation patterns
4. analyze heavy dependencies/chunks
5. apply targeted fixes and re-measure

Typical bottlenecks:
- oversized client bundles
- broad file invalidation triggering large rebuild scope
- unnecessary cache busting
- large dependency graphs in hot paths

---

## Practical Optimization Rules

- keep dependencies lean in client-side code paths
- prefer server-first patterns where applicable
- split heavy modules and defer non-critical imports
- avoid clearing `.next` cache unless troubleshooting requires it
- pin and test Next.js minor upgrades before team-wide rollout

---

## Troubleshooting Playbook

- slow startup: verify bundler mode, inspect dependency load, compare cold/warm starts
- slow HMR: identify broad invalidation surfaces and large shared modules
- plugin incompatibility: validate plugin support matrix, use webpack fallback if needed
- inconsistent build behavior: confirm version-specific flags and experimental settings

---

## Quality Gate

Before recommending changes:

- [ ] current Next.js version confirmed
- [ ] active bundler mode confirmed
- [ ] baseline and post-change measurements compared
- [ ] fallback path documented when compatibility issues exist
- [ ] recommendations are version-aware and source-backed

---

## Output Contract

When activated, return:

1. detected context (version, mode, symptoms)
2. bundler decision (Turbopack vs webpack) with rationale
3. prioritized optimization actions
4. fallback/compatibility plan
5. verification checklist with expected outcomes

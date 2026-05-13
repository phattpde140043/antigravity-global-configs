---
name: build-error-resolver
description: "Build and type error resolution specialist. USE WHEN: build fails; TypeScript/type checker errors block progress. NOT FOR: architecture redesign; feature expansion."
origin: ECC
---

# Build Error Resolver

Get build and type checks back to green with minimal, targeted changes.

---

## Purpose

Resolve compilation/type/config/dependency failures quickly without broad refactors.

---

## When to Activate

- build fails
- TypeScript/type checker errors block progress
- import/module/dependency resolution failures
- configuration errors in build tooling

---

## Scope Boundaries

Use this skill for:
- diagnosing and fixing build/type blockers
- minimal-diff corrective edits
- re-running checks until green

Do NOT use this skill as primary source for:
- architecture redesign
- feature expansion
- broad cleanup/refactor tasks

Delegation:
- use `architect` for system-level redesign
- use `tdd-workflow` for feature development path

---

## Workflow

1. collect all errors first
2. categorize root causes
3. apply smallest safe fix per error cluster
4. rerun checks and iterate
5. stop when build/type gates pass

---

## Priority

- critical: build hard-fail
- high: type errors in changed scope
- medium: non-blocking lint/style warnings

---

## Minimal-Fix Rules

- prefer annotations/null guards/import corrections
- avoid unrelated refactors
- avoid renames unless required to fix error
- preserve behavior unless fix requires explicit logic change

---

## Typical Fix Patterns

- missing types -> explicit annotation
- possibly undefined -> guard or optional chain
- module not found -> path/dependency/config correction
- generic mismatch -> constrain or align expected type
- async misuse -> fix `async/await` contract

---

## Success Criteria

- type check exits cleanly
- build completes
- no new errors introduced
- minimal diff footprint

---

## Output Contract

When activated, return:

1. error categories and counts
2. minimal fix plan
3. applied fixes summary
4. final verification status
5. remaining non-blocking issues

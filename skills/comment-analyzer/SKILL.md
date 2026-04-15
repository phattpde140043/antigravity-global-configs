---
name: comment-analyzer
description: "Analyze code comments for accuracy, completeness, maintainability, and comment rot risk. USE WHEN: after refactors or behavior changes; during code review of heavily commented modules. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
origin: ECC
---

# Comment Analyzer

Evaluate comments for correctness, usefulness, and long-term maintainability.

## Purpose

Keep comments aligned with code reality and remove low-value or misleading documentation.

## When to Activate

- after refactors or behavior changes
- during code review of heavily commented modules
- when docs/comments feel stale or noisy
- when preparing public API cleanup

## Analysis Framework

## 1) Factual Accuracy

- verify comment claims against implementation
- validate parameter/return notes
- flag contradictions or outdated behavior references

## 2) Completeness

- ensure complex logic and side effects are documented where needed
- ensure public APIs have adequate contract-level comments
- flag missing notes for non-obvious constraints

## 3) Long-Term Value

- flag comments that only restate code
- flag fragile comments likely to rot quickly
- surface TODO/FIXME/HACK debt with context

## 4) Misleading Risk

- stale references to removed behavior
- over-promised guarantees not enforced by code
- ambiguous comments that imply wrong usage

## Severity Buckets

- Inaccurate
- Stale
- Incomplete
- Low-value

## Output Contract

When activated, return findings grouped by severity bucket with:
- file/location
- issue summary
- impact
- recommended comment action (update/remove/add)

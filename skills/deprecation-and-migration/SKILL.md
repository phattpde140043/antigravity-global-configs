---
name: deprecation-and-migration
description: "Manages code removal and system migration. Use when replacing old systems, APIs, or features, and when moving users safely from one implementation to another."
---

# Deprecation and Migration

## Overview

Code is a liability, not an asset. Every line has maintenance, security, and onboarding costs. Deprecation is the discipline of removing code that no longer earns its keep.

## Core Principles
- **Code is a Liability**: When functionality can be provided with less code or better abstractions, the old code should go.
- **Hyrum's Law**: Every observable behavior is a contract. Users depend on undocumented quirks, making removal hard.
- **The Churn Rule**: If you own the infrastructure being deprecated, you are responsible for migrating your users.

## The Migration Process
1. **Replacement Ready**: Don't deprecate without a working, documented alternative.
2. **Advisory Notice**: Announce early with a clear migration guide.
3. **Incremental Migration**: Use patterns like **Strangler** (parallel systems) or **Adapter** (translate old calls to new implementation).
4. **Zero Usage Verification**: Confirm zero active usage via logs/telemetry before deletion.

## Patterns
- **Strangler Pattern**: Route traffic incrementally from old to new.
- **Adapter Pattern**: Keep the legacy interface while replacing the backend executor.
- **Feature Flag Migration**: Switch users one by one using toggles.

## Red Flags
- Deprecation without a replacement.
- No migration tooling or documentation provided.
- "Zombie code": Code that nobody owns but everything depends on (Must be assigned or sunsetted).

## Verification
- [ ] Replacement covers all critical use cases.
- [ ] Migration guide exists with concrete steps.
- [ ] All consumers migrated (verified by metrics).
- [ ] Old code, tests, and config fully removed.

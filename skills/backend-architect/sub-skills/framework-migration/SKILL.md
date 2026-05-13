---
name: framework-migration
description: "Expert framework and code migration engineer. Covers: legacy system modernization (Strangler Fig), framework-to-framework code migration (React→Vue, REST→GraphQL, SQL→NoSQL), safe dependency upgrades (semver batching, breaking change detection, rollback), and language version upgrades (Python 2→3). USE WHEN: migrating codebase to new framework/language/platform, upgrading major dependencies, modernizing legacy systems, or designing migration roadmaps. NOT FOR: greenfield development; minor bug fixes; infrastructure-only changes."
risk: high
origin: consolidated
date_created: "2026-04-24"
consolidated_from:
  - framework-migration-legacy-modernize
  - framework-migration-deps-upgrade
  - framework-migration-code-migrate
---

# Framework & Code Migration

Expert-level guide for migrating codebases across frameworks, languages, platforms, and dependency versions with minimal disruption, validated rollback strategies, and comprehensive testing.

## When to Use

Activate this skill when:
- Modernizing a legacy system (Strangler Fig, incremental replacement)
- Migrating between frameworks (React→Vue, Angular→React, jQuery→modern JS)
- Upgrading major library versions (React 17→18, Angular 14→17, .NET 6→8)
- Changing language version (Python 2→3, Node 16→20, TypeScript 4→5)
- Migrating API paradigms (REST→GraphQL, monolith→microservices)
- Migrating databases (SQL→NoSQL, MySQL→PostgreSQL)
- Planning safe dependency batch upgrades

**Do NOT use for:**
- Greenfield development (no legacy to migrate from)
- Minor bug fixes or configuration changes
- Infrastructure-only changes

---

## Risk Gate — BFRI Before ANY Migration

Before starting ANY migration work, score using BFRI (from `@backend-architect`):

```
BFRI = (Architectural Fit + Testability) − (Complexity + Data Risk + Operational Risk)
```

| BFRI | Migration Decision |
| --- | --- |
| **6–10** | Proceed — standard migration plan |
| **3–5** | Proceed with caution — mandate parallel system + rollback plan |
| **0–2** | Risky — require Strangler Fig approach, no big-bang |
| **< 0** | **STOP** — Decompose into smaller migrations first |

**Rule:** BFRI < 0 means the migration scope is too broad. Break it into smaller increments until each piece scores ≥ 3.

---

## Part 1 — Legacy System Modernization (Strangler Fig)

### Phase Overview

```
Phase 1: Assessment & Risk Analysis
    ↓
Phase 2: Test Coverage Establishment (Gate: ≥80% coverage before touching code)
    ↓
Phase 3: Incremental Migration Implementation (Strangler Fig)
    ↓
Phase 4: Performance Validation & Progressive Rollout
    ↓
Phase 5: Legacy Decommissioning & Documentation
```

### Phase 1 — Assessment

**Mandatory outputs before proceeding:**
1. **Technical debt inventory**: outdated dependencies, deprecated APIs, security vulns, performance bottlenecks, architectural anti-patterns
2. **Component complexity score** (1–10) for each module
3. **Dependency graph**: internal modules, external services, shared DB schemas, cross-system data flows
4. **Business impact matrix**: Business Criticality × Traffic Volume × Data Sensitivity × Regulatory Risk

**Prioritization formula:**
```
Migration Priority = (Business Value × 0.4) + (Technical Risk × 0.3) + (Quick Win Potential × 0.3)
```

### Phase 2 — Test Coverage Gate

**BLOCKER: < 40% coverage → do NOT modify the component.**

For under-covered components, write **characterization tests** first:
- Tests that capture CURRENT behavior without modifying logic
- Goal: safety net for refactoring, not specification
- These are temporary — replace with proper unit tests post-migration

```bash
# Measure coverage before touching anything
dotnet test --collect:"XPlat Code Coverage"   # .NET
npm run test -- --coverage                    # Node.js
pytest --cov=src --cov-report=html            # Python
```

Also implement **contract tests** for all integration points:
- Consumer-driven contracts for APIs
- Message queue interaction contracts
- Database schema contracts
- Performance baselines (P95 latency, throughput)

### Phase 3 — Strangler Fig Implementation

**Core principle:** New code runs in parallel with old code. Traffic is gradually shifted. Never big-bang.

```
                        ┌─────────────────┐
Traffic →  API Gateway  →  Feature Flag   →  New System (5% → 25% → 50% → 100%)
                        └─────────────────┘
                                ↓ fallback
                          Legacy System
```

**Setup checklist:**
- [ ] API gateway with routing rules (URL patterns, headers, user segments)
- [ ] Feature flags for gradual rollout control
- [ ] Circuit breakers on new system (fail → fallback to legacy)
- [ ] Dual observability dashboard (monitor both systems simultaneously)
- [ ] Dual-write or event sourcing for data consistency during transition

**Progressive rollout triggers:**
- Start at 5% traffic for 24h
- Automatic rollback if: error rate > 1%, latency > 2× baseline, or business metric degradation
- Advance only when 24h observation period passes with clean metrics
- Path: 5% → 25% → 50% → 100%

### Phase 4 — Performance Validation

Validate modernized components against baselines captured in Phase 2:

| Metric | Gate |
| --- | --- |
| P95 response time | ≤ 110% of legacy baseline |
| Error rate | ≤ 0.1% |
| Throughput | ≥ 95% of legacy |
| Memory usage | ≤ 120% of legacy |

**Performance regression > 10% = rollback trigger.**

### Phase 5 — Decommission

**Rule:** Minimum 30 days at 0% traffic before decommissioning legacy components.

Checklist:
- [ ] Traffic analysis confirms 0 requests to legacy for 30+ days
- [ ] Archive legacy code with behavior documentation
- [ ] Remove from CI/CD pipelines
- [ ] Clean up: DB tables, deprecated endpoints, unused config
- [ ] Document sunset timeline for any retained legacy pieces

**Success criteria for full modernization:**
- ≥ 80% test coverage on all migrated components
- Zero unplanned downtime during migration
- Security vulnerabilities reduced ≥ 90%
- Technical debt score improved ≥ 60%
- 30 days stable post-migration without rollback

---

## Part 2 — Code Migration (Framework / Language / API)

### Migration Complexity Assessment

Before writing a migration plan, assess complexity:

| Factor | Low (1) | Medium (3) | High (5) |
| --- | --- | --- | --- |
| **Codebase size** | < 5k LOC | 5–50k LOC | > 50k LOC |
| **Architectural fit** | Same paradigm | Similar paradigm | Fundamentally different |
| **Dependency overlap** | > 70% compatible | 30–70% compatible | < 30% compatible |
| **Business logic complexity** | CRUD only | Some domain rules | Deep domain rules |
| **Data complexity** | Simple schema | Normalized relations | Complex joins / transformations |

```
Overall Complexity = Average of all factors
< 3: Simple migration (direct port)
3–4: Moderate (adapter + incremental)
> 4: Complex (Strangler Fig or big-bang with extensive testing)
```

### Framework Migration Patterns

#### React → Vue (Component Mapping)

| React | Vue 3 Equivalent |
| --- | --- |
| `className` | `class` |
| `onClick={handler}` | `@click="handler"` |
| `{condition && <X />}` | `<X v-if="condition" />` |
| `arr.map((x, i) => <X />)` | `<X v-for="(x, i) in arr" :key="i" />` |
| `componentDidMount` | `onMounted()` |
| `componentWillUnmount` | `onBeforeUnmount()` |
| `useState` | `ref()` / `reactive()` |
| `useEffect` | `watch()` / `watchEffect()` |
| `useContext` | `provide()` / `inject()` |
| `React.memo` | `defineComponent` with `shallowRef` |

#### REST → GraphQL Migration

1. Inventory all REST endpoints (method, path, request schema, response schema)
2. Map resources → GraphQL types
3. Map `GET` → Query; `POST/PUT/PATCH` → Mutation; `DELETE` → Mutation
4. Implement resolvers as wrappers around existing REST handlers (adapter pattern)
5. Run REST and GraphQL in parallel — consumer migration is independent of server migration
6. Deprecate REST endpoints individually as consumers migrate

#### SQL → NoSQL Design Decisions

| SQL Relationship | NoSQL Strategy |
| --- | --- |
| One-to-One | Embed sub-document |
| One-to-Many (small, bounded) | Embed array |
| One-to-Many (large / unbounded) | Reference by ID |
| Many-to-Many | Reference + denormalize if read-heavy |

**Key rule:** Design for query patterns, not for normalization. In NoSQL, the data model follows the access pattern.

### Language Version Upgrades

#### Python 2 → 3 Quick Reference

| Python 2 | Python 3 |
| --- | --- |
| `print x` | `print(x)` |
| `unicode(x)` | `str(x)` |
| `.iteritems()` | `.items()` |
| `.iterkeys()` | `.keys()` |
| `xrange` | `range` |
| `raise Exception, "msg"` | `raise Exception("msg")` |
| `except E, e:` | `except E as e:` |

Run `2to3 -w .` for automated transformation, then review diffs manually.

#### Node.js Version Upgrades

```bash
# Check breaking changes for your upgrade
npx node-check-usage   # detects deprecated API usage

# Use nvm to test across versions
nvm install 20 && nvm use 20
npm test

# Common breaking changes Node 16 → 18:
# - fetch() native (remove node-fetch)
# - URL parsing changes
# - Stricter DNS resolution order
```

### Automated Testing Strategy

For every migration, you MUST have comparison tests:

```
Pre-Migration Baseline         Post-Migration Verification
─────────────────────         ───────────────────────────
Capture: unit test results  → Compare: same tests still pass
Capture: P95 latency        → Compare: within 110% of baseline
Capture: error rate         → Compare: no regression
Capture: bundle size        → Compare: not significantly larger
Capture: API responses      → Compare: output equivalent (contract)
```

**Rollback trigger thresholds:**
- Any P0 feature non-functional
- Error rate increase > 5%
- Response time increase > 50%
- Any data integrity issue

---

## Part 3 — Dependency Upgrades

### Upgrade Priority Matrix

```
SECURITY   → Immediate. Do not batch. Upgrade isolated on its own branch.
PATCH      → Batch all patches together. Smoke test only. Low risk.
MINOR      → Group by domain (testing libs together, HTTP libs together). Regression test.
MAJOR      → One at a time. Full test suite + integration test + 24h soak.
```

### Semver Risk Classification

```
patch (x.y.Z) → Safe. Backwards-compatible bug fixes.
minor (x.Y.z) → Moderate. New features, no breaking changes by spec. Verify peer deps.
major (X.y.z) → High. Breaking changes likely. Read full CHANGELOG. Write migration guide.
```

### Incremental Upgrade Process

For **major version upgrades**:

1. **Create isolated branch**: `git checkout -b upgrade/{package}-v{version}`
2. **Capture baseline**: run full test suite, record coverage + performance metrics
3. **Update**: `npm install pkg@{version}` or `dotnet add package Pkg --version {version}`
4. **Run codemod** (if available): `npx react-codemod ...`, `ng update @angular/core`
5. **Fix compiler/linter errors** — these are the breaking changes made visible
6. **Run tests** — failures = behavioral breaking changes
7. **Record rollback point**: `git tag pre-upgrade-{pkg}-{datetime}`
8. **Review performance**: compare bundle size, startup time, P95 latency
9. **Soak in staging 24h** before merging to main

### Framework-Specific Upgrade Commands

```bash
# Angular
ng update @angular/core@{version} --dry-run   # Preview changes
ng update @angular/core@{version}              # Apply

# React
npm install react@{version} react-dom@{version}
npx react-codemod rename-unsafe-lifecycles src/

# Vue 2 → 3
npm install vue@3 @vue/migration-tool
npx @vue/migration-tool analyze

# .NET
dotnet add package Microsoft.AspNetCore --version {version}
# Check: https://learn.microsoft.com/aspnet/core/migration

# Python
pip install --upgrade {package}
pip-check   # verify no dependency conflicts
```

### Rollback Procedure

```bash
#!/bin/bash
# Rollback any dependency upgrade

# 1. Restore manifest
git checkout package.json package-lock.json   # npm
# OR
git checkout requirements.txt                 # pip
# OR
git checkout {project}.csproj                 # .NET

# 2. Restore lockfile and reinstall
npm ci                    # npm
pip install -r requirements.txt   # pip
dotnet restore            # .NET

# 3. Verify rollback succeeded
npm test
curl -f http://localhost:{port}/health || exit 1
```

### Post-Upgrade Health Monitoring

Monitor for 24h after every major upgrade:

| Metric | Alert Threshold |
| --- | --- |
| Error rate | > 1% (absolute) or > 2× pre-upgrade |
| API P95 latency | > 110% of baseline |
| Memory usage | > 120% of baseline |
| Bundle size (frontend) | > 15% increase |

---

## Migration Checklist (Universal)

Run before finalizing any migration:

- [ ] BFRI scored — migration complexity is acceptable
- [ ] Baseline metrics captured (latency, error rate, test coverage, bundle size)
- [ ] Characterization tests cover changed modules (≥ 80%)
- [ ] Contract tests in place for all integration points
- [ ] Rollback plan documented with explicit trigger conditions
- [ ] Rollback tested in staging (not just documented)
- [ ] Progressive rollout configured (not big-bang unless scope < 1 file)
- [ ] Observability in place for both old and new systems during transition
- [ ] Performance validated against baseline
- [ ] Security audit run on migrated code (`@securities-audit`)
- [ ] Legacy code archived with behavior documentation
- [ ] Team notified and runbook distributed

---

## Resources

- [legacy-modernization.md](resources/legacy-modernization.md) — Full Strangler Fig playbook, agent coordination, decommission checklist
- [code-migration-playbook.md](resources/code-migration-playbook.md) — Framework migrators, language transformations, comparison testing framework, rollback manager
- [dependency-upgrade-playbook.md](resources/dependency-upgrade-playbook.md) — Dep audit scripts, breaking change detection, batch planner, compatibility matrix, post-upgrade monitoring

## Delegation

| Need | Use Instead |
| --- | --- |
| Security audit of migrated code | `securities-audit` + `backend-security-coder` |
| Performance profiling | `performance-optimization` |
| Test strategy design | `test-driven-development` + `test-engineer` |
| Architecture design for new system | `backend-architect` + `distributed-system` |
| API contract design | `api-design` + `spec-driven-development` |

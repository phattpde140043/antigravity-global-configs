---
name: reviewing-cicd-pipelines
description: Use when reviewing GitHub Actions workflows, CI/CD pipeline changes, or deployment configurations — covers workflow syntax, secret injection, environment targeting, and pipeline security
---

# Reviewing CI/CD Pipelines

## Overview

CI/CD pipeline changes are infrastructure code with security implications. A broken pipeline blocks the entire team. A misconfigured secret leaks credentials.

**Core principle:** Pipeline changes get the same rigor as production code. Validate syntax, verify secret bindings, and confirm environment targeting.

## When to Use

- Reviewing GitHub Actions workflow changes (`.github/workflows/`)
- Auditing secret injection patterns
- Validating deployment target configurations
- Reviewing pipeline security (OIDC, permissions, artifacts)

## Review Checklist

### 1. Workflow Syntax Validation

| Check | What to Verify |
|-------|--------------------|
| **YAML syntax** | Valid YAML — indentation, quoting, multiline strings |
| **Action versions** | Pinned to SHA or major version (`actions/checkout@v4`), not `@latest` |
| **Job dependencies** | `needs:` graph is correct — no circular dependencies, correct ordering |
| **Matrix strategy** | Matrix combinations produce expected permutations |
| **Timeout** | `timeout-minutes` set on long-running jobs (prevents stuck runners) |
| **Concurrency** | `concurrency:` group prevents parallel deploys to same environment |
| **Trigger conditions** | `on:` triggers match intent — `push` vs `pull_request` vs `workflow_dispatch` |
| **Path filters** | `paths:` / `paths-ignore:` correctly scoped — not triggering on unrelated files |

### 2. Secret Management

| Check | What to Verify |
|-------|--------------------|
| **Secret references** | `${{ secrets.NAME }}` matches what's configured in GitHub Settings |
| **Environment secrets** | Environment-specific secrets use `environment:` block, not repo-level secrets |
| **Secret masking** | Secrets never echoed in `run:` steps — no `echo ${{ secrets.X }}` |
| **OIDC federation** | If using OIDC (Azure/AWS/GCP), verify audience, subject, and trust policy match |
| **Env var mapping** | `env:` block maps secrets to env vars with correct names for the application |
| **No hardcoded creds** | No tokens, passwords, or connection strings in workflow files |
| **Secret rotation** | Secrets can be rotated without code changes — no version/value coupling |

### 3. Environment & Deployment Security

| Check | What to Verify |
|-------|--------------------|
| **Environment protection** | Production environments have required reviewers and wait timers |
| **Deployment target** | Correct resource group, subscription, region for each environment |
| **Shared deployment names** | Deployments in shared resource groups use unique names (avoid ARM conflicts) |
| **Permissions block** | `permissions:` uses least privilege — `id-token: write` only when OIDC needed |
| **Runner selection** | Correct runner label (`ubuntu-latest` vs self-hosted) for security requirements |
| **Artifact handling** | Artifacts uploaded with appropriate retention — no PII in artifacts |

### 4. Test Pipeline Integration

| Check | What to Verify |
|-------|--------------------|
| **Test command** | Correct `pytest` / `npm test` command with appropriate markers |
| **Environment variables** | All required env vars from `.env` are mapped from secrets |
| **Browser installation** | `playwright install` runs before browser tests |
| **Test reporting** | JUnit XML or similar format for CI test result visibility |
| **Failure handling** | `if: always()` on reporting steps to capture results even on failure |
| **Timeout-minutes** | Appropriate timeouts for test types (5min unit, 15min integration, 30min E2E) |

### 5. OSP Search E2E Specific

| Check | What to Verify |
|-------|--------------------|
| **Tenant secrets** | `ALPHA_TENANT_*` and `BETA_TENANT_*` all mapped from secrets |
| **Base URL** | Points to correct environment (staging vs production) |
| **Internal secret** | `INTERNAL_SECRET` injected from secrets, never hardcoded |
| **Keycloak URL** | `KEYCLOAK_TOKEN_URL` points to correct Keycloak instance |
| **Swagger URL** | For schemathesis (Scope 12), `SWAGGER_URL` targets backend directly (not Kong) |
| **Locust config** | Performance tests (Scope 9) have separate workflow with extended `timeout-minutes` |

## Severity Classification

| Severity | Examples |
|----------|---------|
| 🚨 **CRITICAL** | Secret exposed in logs, credentials hardcoded, OIDC misconfigured |
| 🔴 **HIGH** | Wrong deployment target, missing environment protection, no timeout |
| 🟡 **MEDIUM** | Unpinned action versions, missing concurrency control, no test reporting |
| 🟢 **LOW** | Non-standard naming, missing path filters, verbose logging |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `@latest` for actions | Pin to SHA or major version: `actions/checkout@v4` |
| `echo ${{ secrets.X }}` for debugging | Never echo secrets — use `***` masking or dedicated debug tools |
| Missing `timeout-minutes` | Always set — prevents stuck runners consuming hours |
| Same deployment name in shared RG | Use environment-specific prefixes: `s365dev-deploy` vs `test-deploy` |
| `permissions: write-all` | Use least privilege: only `id-token: write` if OIDC needed |
| Hardcoded `runs-on: ubuntu-latest` | Consider self-hosted for security-sensitive workloads |

## Integration

**Called by:**
- `performing-code-review` — when PR touches `.github/workflows/`
- `requesting-code-review` — when dispatching review of pipeline changes

**Pairs with:**
- `building-e2e-tests` — test pipeline configuration
- `verification-before-completion` — verify pipeline runs before claiming success

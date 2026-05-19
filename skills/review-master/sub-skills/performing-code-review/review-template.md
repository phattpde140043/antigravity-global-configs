# Code Review Output Template

Use this template when producing the final review comment. Fill in all sections.
Delete sections that genuinely don't apply (e.g., "Bugs Found" if no bugs exist).
**For Python test projects:** Include the "Test Quality" and "Fixture & Lifecycle" sections.
**For C#/.NET projects:** Include the "Data Separation" and "Middleware" sections.
**For JavaScript/React.js projects:** Include the "Frontend Security" and "Component & Hooks" sections.

---

```markdown
# PR #{{NUMBER}} — Security & Architecture Review

**PR**: [{{TITLE}}]({{URL}})
**Author**: `{{AUTHOR}}` | **Branch**: `{{HEAD}}` → `{{BASE}}`
**Files Changed**: {{FILE_COUNT}} | **+{{ADDITIONS}} / -{{DELETIONS}}** | **Commits**: {{COMMIT_COUNT}}
**Stack**: {{C# / Python / Mixed}}

---

## Executive Summary

{{One paragraph: what this PR does, scope of changes, overall quality verdict.}}

---

## Change Taxonomy

| # | Change Area | Files | Impact |
|---|---|---|---|
| 1 | {{Area name}} | {{N}} {{new/modified}} | 🟢/🟡/🔴 {{Brief}} |
| 2 | ... | ... | ... |

---

## {{N}}. {{Change Area Name}} — {{EMOJI}} {{GRADE}}

### What Changed
{{Brief description of the change in this area}}

### Assessment
{{Detailed analysis with:}}
- ✅ What's done well (with evidence)
- ⚠️ Concerns (with code snippets)
- 🚨 Critical issues (with fix suggestions)

---

## 🚨 BUGS FOUND

### Bug #{{N}}: {{File}} — {{Brief Description}}

```{{language}}
// Current (buggy)
{{code showing the bug}}
```

**Problem:** {{Explain why this is wrong}}

**Fix:**
```{{language}}
// Corrected
{{code showing the fix}}
```

---

## Data Separation & Isolation Checklist

| Security Concern | Status | Evidence |
|---|---|---|
| Tenant isolation preserved | ✅/❌ | {{Brief evidence}} |
| Cross-tenant attack detection | ✅/❌ | {{Brief evidence}} |
| Auth checks preserved | ✅/❌ | {{Brief evidence}} |
| No internal details leaked | ✅/❌ | {{Brief evidence}} |
| Secrets properly managed | ✅/❌ | {{Brief evidence}} |
| Thread-safe shared state | ✅/❌ | {{Brief evidence}} |

---

## Test Quality Assessment (Python test projects only)

| Dimension | Status | Evidence |
|---|---|---|
| Test independence (no ordering deps) | ✅/❌ | {{Brief evidence}} |
| xfail rationale on all expected failures | ✅/❌ | {{Brief evidence}} |
| Assertion specificity (descriptive messages) | ✅/❌ | {{Brief evidence}} |
| Marker accuracy (matches Implementation Plan) | ✅/❌ | {{Brief evidence}} |
| Scope isolation (one concern per test) | ✅/❌ | {{Brief evidence}} |
| CRUD cleanup in teardown | ✅/❌ | {{Brief evidence}} |
| No hardcoded tenant data | ✅/❌ | {{Brief evidence}} |

---

## Fixture & Lifecycle Checklist (Python test projects only)

| Concern | Status | Evidence |
|---|---|---|
| Fixture scopes correct (session vs function) | ✅/❌ | {{Brief evidence}} |
| `yield` fixtures have teardown | ✅/❌ | {{Brief evidence}} |
| Playwright contexts disposed | ✅/❌ | {{Brief evidence}} |
| conftest.py hierarchy clean | ✅/❌ | {{Brief evidence}} |
| No fixture shadowing | ✅/❌ | {{Brief evidence}} |
| Settings via `get_settings()` only | ✅/❌ | {{Brief evidence}} |
| `SecretStr` for passwords | ✅/❌ | {{Brief evidence}} |
| `.env` not committed | ✅/❌ | {{Brief evidence}} |

---

## Frontend Security Checklist (JavaScript/React.js projects only)

| Concern | Status | Evidence |
|---|---|---|
| No tokens in `localStorage` | ✅/❌ | {{Brief evidence}} |
| No `dangerouslySetInnerHTML` without sanitization | ✅/❌ | {{Brief evidence}} |
| No secrets in client-exposed env vars | ✅/❌ | {{Brief evidence}} |
| CSP headers configured | ✅/❌ | {{Brief evidence}} |
| Source maps disabled in production | ✅/❌ | {{Brief evidence}} |
| No `eval()` or `new Function()` | ✅/❌ | {{Brief evidence}} |
| Auth guards on protected routes | ✅/❌ | {{Brief evidence}} |
| `package-lock.json` committed | ✅/❌ | {{Brief evidence}} |
| No SSR data leaks (`__NEXT_DATA__`) | ✅/❌ | {{Brief evidence}} |

---

## Component & Hooks Checklist (JavaScript/React.js projects only)

| Concern | Status | Evidence |
|---|---|---|
| Components under ~200 lines | ✅/❌ | {{Brief evidence}} |
| Custom hooks follow `use*` convention | ✅/❌ | {{Brief evidence}} |
| `useEffect` cleanup implemented | ✅/❌ | {{Brief evidence}} |
| Dependency arrays correct (no stale closures) | ✅/❌ | {{Brief evidence}} |
| No direct state mutation | ✅/❌ | {{Brief evidence}} |
| Server state via data-fetching library | ✅/❌ | {{Brief evidence}} |
| Stable `key` props (no array index) | ✅/❌ | {{Brief evidence}} |
| TypeScript `any` minimized | ✅/❌ | {{Brief evidence}} |
| E2E selectors use `data-testid` | ✅/❌ | {{Brief evidence}} |

---

## Best Practices Assessment

| Category | Grade | Notes |
|---|---|---|
| Security | **{{A-F}}** | {{Brief justification}} |
| Architecture | **{{A-F}}** | {{Brief justification}} |
| Error Handling | **{{A-F}}** | {{Brief justification}} |
| Code Quality | **{{A-F}}** | {{Brief justification}} |
| Logging | **{{A-F}}** | {{Brief justification}} |
| Test Quality | **{{A-F}}** | {{Python only — xfail rationale, assertions, independence}} |
| Fixture Design | **{{A-F}}** | {{Python only — scoping, lifecycle, teardown}} |
| Component Design | **{{A-F}}** | {{JS/React only — SRP, hooks, prop drilling, composition}} |
| Bundle & Build | **{{A-F}}** | {{JS/React only — tree-shaking, code splitting, env var safety}} |

---

## Verdict: **{{APPROVE / APPROVE with comments / REQUEST CHANGES}}**

### 🚨 Must Fix Before Merge

| # | Issue | File | Severity |
|---|---|---|---|
| 1 | {{Description}} | `{{file.ext}}` | 🔴 {{Bug/Security}} |

### ⚠️ Should Fix (Security Hardening)

| # | Issue | File | Severity |
|---|---|---|---|
| 1 | {{Description}} | `{{file.ext}}` | 🟡 {{Category}} |

### 💡 Non-Blocking Suggestions

| # | Item |
|---|---|
| 1 | {{Suggestion}} |
```

---

## Usage Notes

- **Every section must have evidence** — code snippets, file references, or specific line numbers
- **Grades must be justified** — a grade without explanation is useless
- **Bugs need fixes** — don't just point out problems, show the solution
- **Verdicts must match findings** — if you found bugs, the verdict MUST be REQUEST CHANGES
- **Checklist items must be verified** — don't mark ✅ without checking
- **For Python test projects** — always include Test Quality and Fixture & Lifecycle sections
- **For C#/.NET projects** — always include Data Separation and Middleware sections
- **Test Quality and Fixture grades** — omit these rows from Best Practices for C#/.NET reviews
- **For JavaScript/React.js projects** — always include Frontend Security and Component & Hooks sections
- **Component Design and Bundle grades** — omit these rows from Best Practices for C#/.NET and Python reviews

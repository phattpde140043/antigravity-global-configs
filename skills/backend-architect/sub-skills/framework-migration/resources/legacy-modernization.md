# Legacy Modernization — Full Strangler Fig Playbook

Detailed reference for the 5-phase legacy modernization workflow from `framework-migration` SKILL.md.

## Phase 1 — Comprehensive Legacy Assessment

### Technical Debt Inventory Template

For each component, document:

```markdown
## Component: [Name]

### Complexity Score: [1–10]
- 1–3: Simple — direct port feasible
- 4–6: Moderate — adapter pattern required
- 7–10: Complex — Strangler Fig mandatory

### Technical Debt Items
- [ ] Outdated dependencies (list with current vs latest)
- [ ] Deprecated API usage (list each API)
- [ ] Security vulnerabilities (CVE IDs if known)
- [ ] Performance bottlenecks (profiling data)
- [ ] Architectural anti-patterns (God classes, circular deps, etc.)

### Coupling Analysis
- External services: [list]
- Shared databases: [list with table names]
- Message queues: [list]
- Circular dependencies: [list]

### Quick Win Potential: [High/Medium/Low]
Rationale: [why this is or isn't a quick win]
```

### Business Impact Matrix

| Component | Business Criticality | Traffic (req/day) | Data Sensitivity | Regulatory | Rollback Complexity | Priority Score |
| --- | --- | --- | --- | --- | --- | --- |
| [Name] | [1–5] | [metric] | [Low/Med/High] | [Y/N] | [1–5] | [(BV×0.4)+(TR×0.3)+(QW×0.3)] |

**Sort by Priority Score descending — highest score = migrate first.**

---

## Phase 2 — Test Coverage Establishment

### Characterization Test Pattern

When coverage < 40%, write characterization tests to capture CURRENT behavior:

```typescript
// Characterization test — describes what the code DOES (not what it SHOULD do)
describe('LegacyOrderProcessor (characterization)', () => {
    it('processes standard order with expected output snapshot', () => {
        const processor = new LegacyOrderProcessor();
        const result = processor.process({ id: 1, items: [{sku: 'A', qty: 2}], discount: 0 });

        // Snapshot captures current behavior — update only after intentional change
        expect(result).toMatchSnapshot();
    });

    it('applies discount in specific order (legacy behavior)', () => {
        // Document quirky legacy behavior explicitly
        const processor = new LegacyOrderProcessor();
        // Legacy applies discount BEFORE tax (business later decided this was wrong)
        // PRESERVE this behavior until business formally decides to change it
        const result = processor.process({ items: [{price: 100}], discount: 0.1 });
        expect(result.total).toBe(90 + (90 * 0.1)); // discount then tax
    });
});
```

### Contract Test Template

```typescript
// Consumer-driven contract — what the consumer expects from the provider
const contract = {
    provider: 'UserService',
    consumer: 'OrderService',
    interactions: [
        {
            description: 'Get user by ID',
            request: { method: 'GET', path: '/users/123' },
            response: {
                status: 200,
                body: { id: '123', email: Matchers.string(), isActive: Matchers.boolean() }
            }
        }
    ]
};

// This contract is verified against the real UserService in CI
// Both consumer and provider must pass contract tests before migration
```

### Performance Baseline Script

```bash
#!/bin/bash
# capture-baseline.sh — run before ANY migration

ENDPOINTS=(
    "GET /api/orders"
    "POST /api/orders"
    "GET /api/users/{id}"
)

echo "Capturing performance baselines..."

for endpoint in "${ENDPOINTS[@]}"; do
    method=$(echo $endpoint | cut -d' ' -f1)
    path=$(echo $endpoint | cut -d' ' -f2)

    # Measure P50, P95, P99 with 100 requests
    result=$(hey -n 100 -c 10 -m $method http://localhost:${PORT}${path} 2>&1)

    echo "## $endpoint" >> baseline.md
    echo "\`\`\`" >> baseline.md
    echo "$result" | grep -E "(Requests/sec|50th|95th|99th)" >> baseline.md
    echo "\`\`\`" >> baseline.md
done

echo "Baseline captured → baseline.md"
```

---

## Phase 3 — Strangler Fig Infrastructure

### API Gateway Routing Configuration (NGINX example)

```nginx
# nginx.conf — route by feature flag header
upstream legacy_backend { server legacy:8080; }
upstream new_backend    { server new:8081; }

server {
    location /api/ {
        # Check feature flag cookie
        set $upstream legacy_backend;

        if ($cookie_ff_new_system = "true") {
            set $upstream new_backend;
        }

        # Check percentage rollout (using shared_dict from lua)
        # 5% → new, 95% → legacy
        # access_by_lua_block { ... }

        proxy_pass http://$upstream;

        # Circuit breaker: on upstream error, try legacy
        proxy_next_upstream error timeout http_500 http_502 http_503;
        proxy_next_upstream_tries 1;
        error_page 500 502 503 504 = @fallback;
    }

    location @fallback {
        proxy_pass http://legacy_backend;
    }
}
```

### Feature Flag Registration

```typescript
// Register migration flags
const flags = {
    'new-order-processor':  { rollout: 5,  enabled: true },
    'new-user-service':     { rollout: 0,  enabled: false },
    'new-payment-gateway':  { rollout: 0,  enabled: false },
};

// Evaluate per request
function shouldUseNewSystem(featureName: string, userId: string): boolean {
    const flag = flags[featureName];
    if (!flag?.enabled) return false;

    // Deterministic bucketing — same user always gets same system
    const hash = murmurhash(userId) % 100;
    return hash < flag.rollout;
}
```

### Progressive Rollout Runbook

| Step | Action | Wait | Rollback Trigger |
| --- | --- | --- | --- |
| 0 | Deploy new system (0% traffic) | 1h | Any deployment error |
| 1 | Route 5% to new | 24h | Error rate > 1% OR latency > 2× baseline |
| 2 | Route 25% to new | 24h | Same as above |
| 3 | Route 50% to new | 48h | Same as above |
| 4 | Route 75% to new | 24h | Same as above |
| 5 | Route 100% to new | 30 days | Same as above |
| 6 | Decommission legacy | — | N/A (irreversible — ensure 30d clean) |

**Auto-rollback configuration:**

```yaml
# Deployment monitoring rules
alerts:
  - name: migration-error-spike
    condition: error_rate > 0.01  # 1%
    action: set_feature_flag(rollout=0)  # immediate rollback to 0%
    notify: [on-call-engineer]

  - name: migration-latency-spike
    condition: p95_latency > baseline_p95 * 2
    action: set_feature_flag(rollout=0)
    notify: [on-call-engineer]
```

---

## Phase 4 — Performance Validation

### Comparison Test Suite

```typescript
describe('Migrated component performance validation', () => {
    const BASELINE = {
        p50: 45,   // ms (from baseline.md)
        p95: 120,  // ms
        errorRate: 0.002,
    };

    it('p95 latency within 110% of baseline', async () => {
        const metrics = await loadTest({ url: '/api/orders', requests: 1000, concurrency: 50 });
        expect(metrics.p95).toBeLessThanOrEqual(BASELINE.p95 * 1.1);
    });

    it('error rate does not regress', async () => {
        const metrics = await loadTest({ url: '/api/orders', requests: 1000 });
        expect(metrics.errorRate).toBeLessThanOrEqual(BASELINE.errorRate * 1.5);
    });
});
```

---

## Phase 5 — Decommission Checklist

```markdown
## Legacy Component Decommission: [Component Name]

### Prerequisites (ALL must be checked before decommission)
- [ ] 30-day traffic analysis shows 0 requests to legacy component
- [ ] All contract tests pass on new system
- [ ] All consumer services confirmed migrated (team sign-off)
- [ ] Performance baselines met for 30+ days
- [ ] No open incidents related to this component in last 30 days

### Decommission Steps
- [ ] Remove traffic routing rules (set weight to 0)
- [ ] Archive legacy code: `git tag legacy-[component]-archived-[date]`
- [ ] Remove from CI/CD pipeline
- [ ] Drop or rename legacy DB tables (after backup): `ALTER TABLE users_legacy RENAME TO users_legacy_archived_[date]`
- [ ] Remove feature flags
- [ ] Update DNS/load balancer configs
- [ ] Notify all consumer teams
- [ ] Update architecture documentation
- [ ] Close migration ticket

### Rollback Window
After decommission, legacy code remains archived for **90 days** before permanent deletion.
```

---

## Agent Coordination Reference

For AI-assisted migration workflows, the recommended agent specialization:

| Phase | Agent Role | Responsibility |
| --- | --- | --- |
| Assessment | `legacy-modernizer` | Technical debt inventory, complexity scoring |
| Assessment | `architect-review` | Dependency graph, integration point mapping |
| Test Coverage | `test-automator` | Characterization tests, contract tests, performance baselines |
| Infrastructure | `backend-architect` | API gateway, feature flags, circuit breakers |
| Security | `security-auditor` | OWASP audit on migrated components |
| Performance | `performance-engineer` | Load tests, optimization recommendations |
| Deployment | `deployment-engineer` | Progressive rollout, automated rollback |
| Documentation | `docs-architect` | Architecture diagrams, runbooks, lessons learned |

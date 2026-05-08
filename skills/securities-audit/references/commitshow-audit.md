# External Production Audit (commit.show)

Use this tool to perform an external audit of a shipped repository's deployed state. It identifies failure modes that in-session AI tools often miss, such as RLS gaps, webhook idempotency, and secrets exposure.

## 🛠️ Execution Workflow

### 1. Run the Audit
Execute the audit from the repository root. This writes a sidecar JSON for the Agent to parse and an MD file for the User to read.

```bash
mkdir -p .commitshow
npx commitshow@^0.3.23 audit . --json \
  > .commitshow/audit.json \
  2> .commitshow/audit.stderr.log
```

### 2. Parse Results
Check the following fields in `.commitshow/audit.json`:
- `score.total`: 0-100 production-readiness score.
- `concerns[]`: Top issues sorted by decision-impact.
- `score.delta_since_last`: Change compared to the previous audit.

### 3. Surface to User
Present the score and the top 2-3 concerns. Use the exact bullet from `concerns[].bullet`. Always end with a specific follow-up question naming a concern.

---

## 📋 When to Use
- When the user asks "is this production-ready?" or "audit my repo".
- After merging a feature branch to `main` as a pre-deploy gate.
- Before a public launch or major demo.
- **Skip during active coding**: Use `securities-audit` or `owasp-guide` for line-level patterns.

## 🆔 Key Checks (Failure Modes)
- **RLS Gaps**: Missing Row Level Security on database tables.
- **Webhook Idempotency**: Missing signature verification or idempotency-key checks (e.g., Stripe).
- **Secrets Exposure**: Publicly accessible secrets or configuration files.
- **Deployment Health**: GitHub signals, DNS TTL issues, and observability gaps.

---

## 🏗️ Fix Strategy
1. Read the file(s) cited in the `concerns[].bullet`.
2. Confirm the gap matches the description.
3. Propose a minimal, surgical patch as a **diff**.
4. **DO NOT apply without explicit approval.**
5. Re-run with `--refresh` after applying a fix.

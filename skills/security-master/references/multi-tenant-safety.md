# Multi-Tenant Safety & Data Isolation (SaaS)

Protecting customer data isolation is the highest priority in multi-tenant SaaS systems. Data leakage between tenants is a critical security failure.

## 🥇 The Golden Rules
1. **Enforce at the Database (RLS)**: Application-layer filtering is a suggestion; Database-level RLS is enforcement.
2. **Never Use Sequential IDs**: Use UUIDs for all tenant-scoped resources to prevent enumeration attacks.
3. **No Unscoped Queries**: Every raw query MUST include `WHERE tenant_id = $1`.

---

## 🛡️ PostgreSQL Row-Level Security (RLS)
RLS acts as a database-level safety net. Even if application code forgets a filter, RLS blocks the cross-tenant read.

```sql
-- 1. Enable RLS
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;
ALTER TABLE projects FORCE ROW LEVEL SECURITY;

-- 2. Create Isolation Policy
CREATE POLICY tenant_isolation ON projects
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- 3. Create Insert Policy
CREATE POLICY tenant_insert ON projects
  FOR INSERT
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id')::uuid);
```

---

## 🛠️ Tenant-Aware Middleware
Extract the `tenant_id` from the JWT at the start of every request and bind it to the database connection.

```typescript
async function tenantMiddleware(req, res, next) {
  const tenantId = req.auth?.tenantId; 
  if (!tenantId) return res.status(403).json({ error: "No tenant context" });

  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    // Bind tenant_id to the transaction session
    await client.query("SELECT set_config('app.current_tenant_id', $1, true)", [tenantId]);
    req.db = client;
    
    res.on("finish", async () => {
      client.release(); // Connection returns to pool with context reset
    });
    next();
  } catch (err) {
    client.release();
    next(err);
  }
}
```

---

## 🚫 Never Do This (Anti-Patterns)
- **Unscoped Admin Access**: Never allow a regular tenant JWT to access admin aggregation endpoints (`GET /admin/all-stats`).
- **Shared Connection Pools without Reset**: If using `SET LOCAL`, always ensure the connection is reset or released within a transaction to avoid context leakage.
- **Auto-incrementing IDs**: `invoice #1042` allows an attacker to guess `invoice #1043` for another tenant. Use UUIDs.
- **Client-Side Tenant Filtering**: Never trust the client to tell you which `tenant_id` they belong to; always derive it from a verified server-side session or JWT claim.

## 📋 Isolation Checklist
- [ ] Is `tenant_id` the first column in every composite index?
- [ ] Is RLS enabled and tested for all tenant-scoped tables?
- [ ] Are background jobs scoped explicitly to a `tenant_id`?
- [ ] Is there a CI check to prevent migrations from creating unscoped tables?


---

## 🔗 Related References
- **[Threat Modeling](threat-modeling.md)**
- **[API Security](api-security.md)**

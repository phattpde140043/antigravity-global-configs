# Multi-Tenant Safety: The Golden Rules

Protecting customer data isolation is the highest priority in multi-tenant systems.

## 🥇 The Golden Rule
Every database query and resource access MUST be filtered by `TenantId`.

## 🛡️ Implementation Patterns
- **Database Level**: Use Row Level Security (RLS) or Query Interceptors to automatically inject `WHERE TenantId = @CurrentTenant`.
- **API Level**: Extract `TenantId` from the verified JWT claim, NOT from a user-provided header (unless for specific admin tasks).
- **Caching**: Ensure Cache Keys are prefixed with `TenantId` (e.g., `tenant1:user:123`).

## 📋 Isolation Checklist
- [ ] Are all database queries filtered by `TenantId`?
- [ ] Is `TenantId` validated against the User's access token?
- [ ] Does the UI/Frontend handle tenant switching securely?
- [ ] Are background jobs scoped to a single tenant at a time?

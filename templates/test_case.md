# 🧪 Automation Test Case: [Title]

## 1. Objective
Describe what this test validates (e.g., "Verify that Tenant A cannot delete Tenant B's search profile").

## 2. Requirements & Context
- **Feature**: [Link to Feature Doc/Spec]
- **Tenant Isolation**: [YES/NO]
- **Required Skills**: `e2e-testing`, `test-engineer`
- **Pre-requisites**: [e.g., Auth token, Pre-existing entities]

## 3. Test Data (Seeding)
| Entity | Properties | Tenant |
| :--- | :--- | :--- |
| UserA | Admin | Tenant_Alpha |
| UserB | Member | Tenant_Beta |
| Resource1 | Private | Tenant_Alpha |

## 4. Execution Steps (The Flow)
1. **Setup**: Login as UserA, create Resource1.
2. **Action**: Login as UserB, attempt `DELETE /api/resources/{Resource1.id}`.
3. **Verification**: 
   - HTTP Status: `403 Forbidden` or `404 Not Found`.
   - DB Check: Query `Resources` where `id = {Resource1.id}` should still exist.

## 5. Teardown
- Delete Resource1 as UserA.
- Logout.

## 6. Failure Analysis (Expected Errors)
- If `401`, check auth token expiration.
- If `200`, **HIGH RISK: Isolation Failure detected.**

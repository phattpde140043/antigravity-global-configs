# Secrets Infrastructure & CI/CD Management

Implement secure secrets management in CI/CD pipelines and runtime environments. Avoid hardcoding sensitive information and ensure least-privilege access.

## 🛡️ Core Principles
1. **Never Commit Secrets**: Use `.gitignore` and pre-commit hooks (TruffleHog/GitGuardian).
2. **Environment Separation**: Use distinct secrets for Dev, Staging, and Production.
3. **Least Privilege**: Only grant access to the specific secrets a service needs.
4. **Auto-Rotation**: Enable automatic secret rotation for Databases and API Keys.

---

## 🛠️ Tooling & Integration

### HashiCorp Vault
- **Best For**: Multi-cloud, dynamic secrets, and high-compliance environments.
- **Workflow**:
  - `vault kv put secret/db config=...`
  - Retrieve via CLI or `vault-action` in GitHub Actions.

### Cloud Native Managers (AWS/Azure/GCP)
- **AWS Secrets Manager**: Integrated with RDS; supports automatic rotation via Lambda.
- **Azure Key Vault**: Managed identities for secret-less access from Azure services.
- **GCP Secret Manager**: Versioned secrets with IAM-based access control.

### GitHub / GitLab Secrets
- **GitHub Secrets**: Scoped to Repository, Organization, or Environment.
- **Masking**: Automatically mask secrets in logs using `::add-mask::$SECRET`.

---

## 📋 CI/CD Secret Scanning
Add a scanning stage to your pipeline to prevent accidental leaks:

```yaml
secret-scan:
  image: trufflesecurity/trufflehog:latest
  script:
    - trufflehog filesystem .
```

## 🔄 Rotation Strategy
1. **Trigger**: Time-based (e.g., 90 days) or Event-based (e.g., person leaves team).
2. **Execution**:
   - Generate new secret.
   - Update Secret Manager.
   - Trigger app restart or config reload.
   - Revoke old secret after a short grace period.

## 🏁 Secrets Checklist
- [ ] Are secrets encrypted at rest in the backend?
- [ ] Is audit logging enabled for secret access?
- [ ] Are secrets masked in CI/CD logs?
- [ ] Is there a pre-commit hook to block secrets?
- [ ] Are all hardcoded secrets removed and rotated?


---

## 🔗 Related References
- **[API Security](api-security.md)**
- **[Memory Security](memory-security.md)**

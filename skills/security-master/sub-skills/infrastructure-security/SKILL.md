---
name: infrastructure-security
description: "Cloud infrastructure security reference for AWS compliance (CIS, PCI-DSS, HIPAA), IAM hardening, and secrets management. Use as a lookup guide for cloud auditing and identity governance."
---

# Infrastructure Security Reference

This skill serves as a condensed reference guide for cloud infrastructure security and compliance.

## AWS Compliance Benchmarks

### CIS AWS Foundations Highlights
- **IAM (1.x)**: Check root MFA, credential reports, and console login without MFA.
- **Logging (2.x)**: Verify CloudTrail multi-region logging and log file validation.
- **Monitoring (3.x)**: Check metric filters for unauthorized API calls and IAM changes.
- **Networking (4.x)**: Audit security groups for unrestricted SSH (22) or RDP (3389) access.

**Key CLI Commands:**
- `aws iam get-credential-report`
- `aws iam get-account-summary`
- `aws cloudtrail describe-trails`
- `aws ec2 describe-security-groups --filters Name=ip-permission.cidr,Values='0.0.0.0/0'`

---

## IAM Hardening & Governance

### Core Principles
- **Least Privilege**: Grant only necessary permissions.
- **Role-Based Access (RBAC)**: Use IAM roles for services; avoid static access keys.
- **Policy Guardrails**: Use Service Control Policies (SCPs) for organization-wide restrictions.

### Audit Checklist
- [ ] Users without MFA.
- [ ] Access keys older than 90 days.
- [ ] Overly permissive wildcards (`*`) in policies.
- [ ] Cross-account trust relationships in roles.

---

## Secrets Management & Rotation

### Rotation Lifecycle
Automated rotation via AWS Secrets Manager and Lambda:
1.  **Creation**: Generate new credential.
2.  **Deployment**: Update target service (RDS, API Gateway).
3.  **Testing**: Verify connection with new secret.
4.  **Finalization**: Move `AWSCURRENT` label to new version.

**Key CLI Commands:**
- `aws secretsmanager rotate-secret --secret-id <id>`
- `aws secretsmanager describe-secret --secret-id <id>`

---

## Data Protection Framework

### Multi-Layer Encryption
- **At Rest**: Enforce AES-256 for EBS, RDS, and S3.
- **In Transit**: Enforce TLS 1.2+ for all API calls and data transfers.
- **Key Management**: Use AWS KMS with periodic key rotation enabled.

---

## Operational Security Monitoring
- **AWS Config**: Continuous monitoring of resource configuration.
- **Security Hub**: Unified view of security alerts and compliance status.
- **GuardDuty**: Threat detection for AWS accounts and workloads.

---

## Supply Chain Security

### Dependency Scanning
Automated vulnerability detection for package manifests:
- **NPM**: `npm audit` (check for critical/high).
- **Python**: `safety check` or `pip-audit`.
- **Go**: `govulncheck ./...`.
- **Rust**: `cargo audit`.

### SBOM (Software Bill of Materials)
Generate and maintain SBOMs for compliance (CycloneDX/SPDX):
1. **Inventory**: List all direct and transitive dependencies.
2. **Scan**: Correlate inventory with NVD/GitHub Advisory databases.
3. **Verify**: Check for restrictive or non-compliant licenses.

**Reference Tools**: `trivy`, `syft`, `cyclonedx-cli`.


---

## Constraints
- **Reference-Only**: This file provides architectural and CLI patterns. Implementation must be tailored to environment specifics.
- **Security Gates**: Any infrastructure change must be validated against the **Adversarial Tracer** mindset in `securities-audit`.

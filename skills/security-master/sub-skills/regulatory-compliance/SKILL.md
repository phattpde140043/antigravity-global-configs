---
name: regulatory-compliance
description: "Business logic implementations and checklists for GDPR, HIPAA, and PCI-DSS compliance. Use for designing privacy controls, audit trails, and healthcare/payment data handling."
---

# Regulatory Compliance Implementation

Practical code patterns for meeting legal and industry security standards.

## 1. GDPR (Privacy by Design)

### Consent Management
```csharp
public class ConsentManager {
    // Record user consent with full audit trail
    public async Task RecordConsent(string userId, string type, bool granted) {
        var record = new ConsentAudit {
            UserId = userId,
            Type = type,
            Granted = granted,
            Timestamp = DateTime.UtcNow,
            IpAddress = GetRequestIp(),
            PolicyVersion = "v2.1"
        };
        await _db.ConsentLogs.AddAsync(record);
    }
}
```

### Right to Erasure (Article 17)
1. **Identify**: Locate all PII across DBs, Logs, and Backups.
2. **Remove/Anonymize**: Hard delete profile data; Anonymize user-generated content (e.g., replace name with "Deleted User").
3. **Notify**: Inform third-party processors of the erasure request.

---

## 2. HIPAA (Healthcare Data)

### PHI Protection Safeguards
- **Minimum Necessary Rule**: Grant access only to the specific data needed for a treatment purpose.
- **Audit Logs**: Every read/write to Protected Health Information (PHI) MUST be logged with `userId` and `patientId`.

### Technical Controls
- **Encryption**: FIPS 140-2 validated encryption for PHI at rest.
- **Automatic Logoff**: Enforce session timeouts on systems accessing PHI.

---

## 3. PCI-DSS (Payment Data)

### Cardholder Data Environment (CDE)
- **Never Store**: CVV/CVC, full magnetic stripe data, or PIN blocks.
- **Tokenization**: Replace PAN (Primary Account Number) with a token immediately.
- **Storage**: If PAN must be stored, it must be rendered unreadable (e.g., strong hash/encryption).

### Network Segmentation
Isolate the CDE from the rest of the corporate network using firewalls and strict ACLs.

---

## Audit Trail Requirements
Every compliance framework requires a tamper-evident audit log:
- **Who**: Unique identifier of the actor.
- **What**: The action performed (Read/Write/Delete).
- **When**: UTC timestamp.
- **Where**: Source IP and system component.
- **Success/Failure**: Result of the attempt.

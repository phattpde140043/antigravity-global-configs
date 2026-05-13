---
name: framework-migration
description: "Master of system modernization and framework transition. Expert in the Strangler Fig Pattern, legacy code refactoring, and gradual cutover strategies."
---

# Framework Migration & Modernization

Expertise in transforming legacy systems into modern architectures while maintaining business continuity.

## 🏗️ The Strangler Fig Pattern
The gold standard for risk-managed legacy modernization:
1. **Identify**: Isolate a small piece of legacy functionality.
2. **Implement**: Build the new version using modern technologies.
3. **Intercept**: Route traffic for that functionality to the new version (using API Gateway or Proxy).
4. **Iterate**: Repeat until the legacy host is fully replaced and "strangled".

## 🚀 5-Phase Modernization Workflow
1. **Assessment**: Audit technical debt, dependencies, and risk. Identify "Quick Wins".
2. **Test Coverage**: Establish characterization tests for legacy code to ensure parity.
3. **Incremental Migration**: Extract business logic into adapters/facades. Implement modern patterns.
4. **Validation**: Load testing, security hardening, and progressive rollout (Canary).
5. **Decommissioning**: Safe removal of legacy components and database tables.

## 🛡️ Best Practices
- **Facade/Adapter**: Use to bridge the gap between legacy and modern code.
- **Contract Testing**: Ensure integration points remain stable during transition.
- **Feature Flags**: Enable gradual traffic shifting and instant rollbacks.
- **Data Parity**: Use dual-writes or event sourcing to sync data between systems.

## 📋 Verification Checklist
- [ ] Is the migration plan using the Strangler Fig Pattern (Incremental)?
- [ ] Are characterization tests covering the legacy behavior?
- [ ] Is there a rollback strategy for every migrated component?
- [ ] Are contract tests validating integration boundaries?
- [ ] Has performance parity (SLA) been verified post-migration?

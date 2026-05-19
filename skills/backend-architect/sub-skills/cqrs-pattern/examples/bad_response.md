# Example: Bad Response (Anti-Patterns to Avoid)

This file demonstrates the common AI slop, shortcuts, and structural errors under cqrs-pattern.

## ❌ Rejected Patterns
- Mixing architectural layers in a single mega-file.
- Swallowing exceptions or lacking boundary validation.
- Missing rate-limiting, tenant isolation, or explicit contracts.

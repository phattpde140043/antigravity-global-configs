---
name: sast-engineering
description: "Expert in Static Analysis Security Testing (SAST). Focuses on creating custom Semgrep rules to detect vulnerabilities, dangerous patterns, and enforce security standards."
---

# SAST Engineering (Semgrep)

Master the art of proactive security through automated static analysis.

## 🏗️ The SAST Workflow
1. **Analyze**: Identify the dangerous pattern (e.g., `eval(user_input)`).
2. **Test-First**: Write positive cases (vulnerable code) and negative cases (safe/sanitized code) with `# ruleid` and `# ok` annotations.
3. **AST Analysis**: Use the Abstract Syntax Tree to understand how the code is structured.
4. **Rule Creation**: Write the Semgrep rule (Pattern matching or Taint mode).
5. **Iterate**: Run `semgrep --test` until all cases pass.

## 🚀 Taint Mode (Priority)
Use Taint Mode for data-flow vulnerabilities (Injection, XSS):
- **Sources**: Where untrusted data enters (e.g., `request.args.get`).
- **Sinks**: Where dangerous operations occur (e.g., `os.system`, `eval`).
- **Sanitizers**: Functions that make data safe (e.g., `html.escape`).

## 🛡️ Best Practices
- **Explicit over Generic**: Avoid broad patterns like `$F(...)`. Be specific to the language and framework.
- **AST Visibility**: Patterns must account for syntactic variations that Semgrep's AST-based engine sees.
- **False Positive Management**: Always include negative tests (`# ok`) to ensure rules don't break developer velocity.

## 📋 Verification Checklist
- [ ] Is a test file with `# ruleid` and `# ok` annotations provided?
- [ ] Does the rule use Taint Mode for data-flow issues?
- [ ] Are language-specific AST variations considered?
- [ ] Have safe alternatives/sanitizers been verified as "OK"?
- [ ] Is the rule specific enough to avoid noise (False Positives)?

---
name: conversation-analyzer
description: "Analyze conversation transcripts to identify repeated assistant behaviors worth preventing with hooks. USE WHEN: user repeatedly corrects assistant behavior; hook policy design is requested. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
origin: ECC
---

# Conversation Analyzer

Analyze conversation history to discover recurring assistant misbehaviors and convert them into hook rules.

## Purpose

Turn repeated correction patterns into enforceable guardrails.

## When to Activate

- user repeatedly corrects assistant behavior
- hook policy design is requested
- /hookify is invoked without explicit target rules
- long sessions show recurring avoidable mistakes

## What to Detect

- explicit corrections ("don't do that", "use X instead")
- frustration signals and repeated reversions
- repeated tool misuse patterns
- user undoing/reverting assistant edits

## Prioritization

Rank by:
1. frequency
2. severity/impact
3. preventability via hooks

## Output Format

```yaml
behavior: "What went wrong"
frequency: "observed count/pattern"
severity: high|medium|low
suggested_rule:
  name: "rule-name"
  event: bash|file|stop|prompt
  pattern: "regex or matcher"
  action: block|warn
  message: "user-facing guidance"
```

## Rule Quality Checklist

- rule is specific and testable
- pattern avoids broad false positives
- action severity matches risk
- message gives clear correction path

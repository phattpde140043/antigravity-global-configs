# Code Review Excellence Playbook

Detailed patterns, checklists, and templates for professional code reviews.

---

## Language-Specific Patterns

### 1. Python Review
❌ **BAD (Mutable Default Arguments)**:
```python
def add_item(item, items=[]): # Bug! Shared across calls
    items.append(item)
    return items
```
✅ **GOOD**:
```python
def add_item(item, items=None):
    items = items or []
    items.append(item)
    return items
```

### 2. TypeScript/JavaScript Review
❌ **BAD (Using 'any')**:
```typescript
function process(data: any) { return data.value; }
```
✅ **GOOD**:
```typescript
interface DataPayload { value: string; }
function process(data: DataPayload) { return data.value; }
```

---

## High-Performance Feedback Patterns

### The "Modified Sandwich" Template
When providing difficult feedback:
1. **Context/Praise**: "I really appreciate the work on the [Feature X] logic, it handles the complex state transitions nicely."
2. **Specific Issue**: "🔴 [blocking] I noticed the payment loop performs a DB query for every item (N+1). With large orders, this will cause production timeouts."
3. **Actionable Solution**: "Could we use `.Include()` or a batch fetch here? I've seen this pattern work well in `PaymentService.cs:42`."

---

## PR Review Comment Template
Use this structure for your final review summary:

```markdown
## 🤖 Review Summary
**Verdict**: 🔴 REQUEST CHANGES | ✅ APPROVE

### 🎯 Overview
[Brief summary of the change and overall assessment]

### 🔴 Blocking Issues
- [File:Line] [Description + Fix]

### 🟡 Important Findings
- [File:Line] [Description + Suggestion]

### 🎉 What's Done Well
- [Highlight specific clean code or good logic]

### 💡 Suggestions & Learning
- [Nitpicks or educational links]
```

---

## Advanced Architecture Review
When reviewing major changes, ask these "Value-Based" questions:
- **Contract Integrity**: "Does this change an existing public API contract without a deprecation path?"
- **Ownership**: "Does this service boundary own its data or is it reaching into another service's DB?"
- **Testability**: "Is this logic easily testable in isolation, or does it require a full integration environment?"

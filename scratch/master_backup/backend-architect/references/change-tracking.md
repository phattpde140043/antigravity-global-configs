# Technical Change Tracking & Session Handoff

Maintain absolute continuity across AI sessions using a structured state machine and JSON-based handoff records. This prevents context loss when sessions expire or transfer.

## 🔄 Change State Machine
Every task or feature must progress through these states:
`planned` → `in_progress` → `implemented` → `tested` → `deployed`
*(Use `blocked` for external impediments)*

---

## 📋 Session Handoff Protocol (MANDATORY)
At the conclusion of every session or task, the Agent **MUST** update/create a handoff record in `memory/handoff.json`.

### Handoff Schema
```json
{
  "task_id": "TC-XXXX",
  "status": "in_progress | implemented | blocked",
  "progress_summary": "What was actually completed.",
  "next_steps": ["Step 1", "Step 2"],
  "blockers": ["Technical or requirement blockers"],
  "active_files": ["Paths to files currently being edited"],
  "context_keys": ["Key architectural decisions made in this session"],
  "last_updated": "YYYY-MM-DD HH:MM:SS"
}
```

---

## 🛠️ Operating Pipeline
1. **Init**: Create a new tracking record in `memory/` at the start of a feature.
2. **Update**: Move state from `planned` to `in_progress` once coding starts.
3. **Evidence**: When moving to `tested`, include snippets of successful test logs in the record.
4. **Handoff**: Ensure the `next_steps` are clear enough for a new Agent session to resume without asking the User.

## 📊 Change Dashboard (Optional)
For long-running projects, generate a `docs/CHANGELOG_TECHNICAL.md` that summarizes these JSON records into a human-readable format, focusing on:
- **What** changed.
- **Why** it changed (ADR link).
- **How** it was verified.

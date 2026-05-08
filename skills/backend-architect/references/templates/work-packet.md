# Work Packet Template

| Field | Description |
| :--- | :--- |
| **Packet ID** | Unique identifier (e.g., WP-001) |
| **Objective** | Short description of the refactor goal |
| **Owned Files** | Absolute paths of files this worker is allowed to edit |
| **Dependencies** | IDs of packets that must be completed first |
| **Risks** | Potential side effects or invariants to preserve |
| **Done Criteria** | Specific commands or state to verify completion |
| **Integration Notes** | Instructions for merging or post-processing |

## Success Gate
- [ ] Code builds without errors.
- [ ] Unit tests for owned files pass.
- [ ] No changes made to files outside the "Owned Files" list.

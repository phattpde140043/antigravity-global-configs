---
name: workflow-automation
description: "Master of automating business and development workflows using MCP (Composio), Rube, and third-party integrations (Calendly, Slack, GitHub)."
---

# Workflow Automation & Integration

Streamline processes by connecting tools and automating repetitive tasks.

## 🏗️ Automation via MCP (Composio/Rube)
- **Tool Discovery**: Always call `RUBE_SEARCH_TOOLS` to get the latest schemas.
- **Connection Management**: Use `RUBE_MANAGE_CONNECTIONS` to verify and authorize toolkits.
- **Sequence Orchestration**: Design multi-tool sequences (e.g., Get User -> List Events -> Filter -> Action).

## 📅 Scheduling Integrations (Calendly/Cal.com)
- **ID Resolution**: Always resolve full API URIs (e.g., `https://api.calendly.com/users/{uuid}`) instead of bare IDs.
- **Availability Queries**: Handle time-range constraints (e.g., max 7-day range for availability checks).
- **Idempotency**: Verify existing states (e.g., check for existing invitations) before creating new ones to avoid duplicates.

## 🛡️ Best Practices
- **Explicit Confirmation**: Always ask for user approval before executing destructive actions (Delete, Cancel, Send).
- **Time Handling**: Use UTC format (`yyyy-MM-ddTHH:mm:ss.ffffffZ`) for all timestamps.
- **Pagination**: Implement token-based pagination loops to ensure complete data retrieval.

## 📋 Verification Checklist
- [ ] Are tools searched and schemas verified before execution?
- [ ] Is the connection status checked and authenticated?
- [ ] Are timestamps in the correct UTC format?
- [ ] Is pagination handled for large datasets?
- [ ] Was user confirmation obtained for high-risk actions?

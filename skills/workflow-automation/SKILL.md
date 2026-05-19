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

- For **BambooHR Automation** (employees, time-off, benefits via Rube MCP):
  👉 **[BambooHR Automation](sub-skills/bamboohr-automation/SKILL.md)**
- For **Basecamp Project Management Automation** (todos, schedules, posts via Rube MCP):
  👉 **[Basecamp Automation](sub-skills/basecamp-automation/SKILL.md)**
- For **Stripe & Stripe Billing Automation** (invoices, subscriptions via Rube MCP):
  👉 **[Billing Automation](sub-skills/billing-automation/SKILL.md)**
- For **Box Storage Automation** (files, folders, metadata via Rube MCP):
  👉 **[Box Automation](sub-skills/box-automation/SKILL.md)**
- For **Bitbucket VCS Automation** (repositories, pull requests, issues via Rube MCP):
  👉 **[Bitbucket Automation](sub-skills/bitbucket-automation/SKILL.md)**
- For **Skyvern Browser-Automation** (LLM-driven visual web parsing and task execution):
  👉 **[Skyvern Automation](sub-skills/skyvern-automation/SKILL.md)**
- For **Brevo Email CRM Automation** (contacts, lists, campaigns via Rube MCP):
  👉 **[Brevo Automation](sub-skills/brevo-automation/SKILL.md)**
- For **Sales Outbound Outreach & CRM Automation** (HubSpot deals, custom CRM automations):
  👉 **[Sales Automator](sub-skills/sales-automator/SKILL.md)**
- For **Salesforce Outbound & Integration Automation** (Salesforce Process Builder, Salesforce Flows via Rube MCP):
  👉 **[Salesforce Automation](sub-skills/salesforce-automation/SKILL.md)**
- For **PagerDuty Incident Management Automation** (incident creation, on-call schedules, alert routing via Rube MCP):
  👉 **[PagerDuty Automation](sub-skills/pagerduty-automation/SKILL.md)**
- For **Pipedrive Sales CRM Automation** (deals, pipelines, organizations via Rube MCP):
  👉 **[Pipedrive Automation](sub-skills/pipedrive-automation/SKILL.md)**
- For **Square Point of Sale (POS) & Payment Automation** (transactions, checkout links, inventory updates via Rube MCP):
  👉 **[Square Automation](sub-skills/square-automation/SKILL.md)**
- For **Canva Automated Design & Media Generation** (design template retrieval, image generation, social asset creation via Rube MCP):
  👉 **[Canva Automation](sub-skills/canva-automation/SKILL.md)**
- For **Changelog Generating & Releases Automation** (git commit logs summaries, product changelogs, automated Slack notifications via Rube MCP):
  👉 **[Changelog Automation](sub-skills/changelog-automation/SKILL.md)**

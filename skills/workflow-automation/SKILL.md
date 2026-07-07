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

## 🧩 Sub-Skill Catalog

- **[BambooHR Automation](sub-skills/bamboohr-automation/SKILL.md)** — Automate BambooHR HR records (employees, time-off, benefits, dependents, employee updates) via Rube MCP. **Use when:** reading or updating employee data, filing/approving time-off, or managing benefits in BambooHR.
- **[Basecamp Automation](sub-skills/basecamp-automation/SKILL.md)** — Automate Basecamp project management (to-dos, messages, people, to-do list organization) via Rube MCP. **Use when:** creating or organizing Basecamp to-dos, posting messages, or managing project members.
- **[Billing Automation](sub-skills/billing-automation/SKILL.md)** — Design automated billing systems (recurring billing, invoice generation, dunning, proration, tax calculation). **Use when:** implementing SaaS subscription billing, automating invoicing/renewals, recovering failed payments, or handling usage-based and tax billing. **Not for:** one-off or manual invoices, or tasks unrelated to subscriptions.
- **[Box Automation](sub-skills/box-automation/SKILL.md)** — Automate Box storage (file upload/download, content search, folder management, collaboration, metadata, sign requests) via Composio's Box toolkit. **Use when:** uploading/retrieving Box files, searching content, managing folders or collaborators, or querying metadata.
- **[Bitbucket Automation](sub-skills/bitbucket-automation/SKILL.md)** — Automate Bitbucket VCS (repositories, pull requests, branches, issues, workspace management) via Rube MCP. **Use when:** managing Bitbucket repos, opening or reviewing pull requests, or tracking issues. **Not for:** local Git operations (use Git Worktrees).
- **[Skyvern Automation](sub-skills/skyvern-automation/SKILL.md)** — AI-powered browser automation with Skyvern for visual navigation, structured data extraction, and multi-page workflows. **Use when:** a task needs an LLM to visually navigate and act on a website that lacks an API, or to extract structured data across pages. **Not for:** platforms that expose a direct API or MCP toolkit (prefer the dedicated integration).
- **[Brevo Automation](sub-skills/brevo-automation/SKILL.md)** — Automate Brevo (formerly Sendinblue) email marketing (contacts, lists, campaigns) via Composio's Brevo toolkit. **Use when:** managing Brevo contacts and lists or running email marketing campaigns.
- **[Sales Automator](sub-skills/sales-automator/SKILL.md)** — Draft sales outreach content: cold emails, follow-up cadences, proposals, pricing pages, case studies, and sales scripts. **Use when:** writing cold-outreach or lead-nurturing copy and templates. **Not for:** CRM record operations (use Pipedrive or Salesforce automation).
- **[Salesforce Automation](sub-skills/salesforce-automation/SKILL.md)** — Automate Salesforce (leads, contacts, accounts, opportunities, SOQL queries) via Rube MCP. **Use when:** creating or updating Salesforce records, or running SOQL queries.
- **[PagerDuty Automation](sub-skills/pagerduty-automation/SKILL.md)** — Automate PagerDuty incident management (incidents, services, schedules, escalation policies, on-call rotations) via Rube MCP. **Use when:** creating or triaging incidents, configuring escalation policies, or managing on-call schedules.
- **[Pipedrive Automation](sub-skills/pipedrive-automation/SKILL.md)** — Automate Pipedrive CRM (deals, contacts, organizations, activities, notes, pipelines) via Rube MCP. **Use when:** managing Pipedrive deals and pipelines, logging activities, or updating contacts and organizations.
- **[Square Automation](sub-skills/square-automation/SKILL.md)** — Automate Square point-of-sale and payments (payments, orders, invoices, locations) via Rube MCP. **Use when:** processing Square payments or checkout, managing orders and invoices, or querying locations.
- **[Canva Automation](sub-skills/canva-automation/SKILL.md)** — Automate Canva design and media (designs, exports, folders, brand templates, autofill) via Rube MCP. **Use when:** generating or exporting Canva designs, applying brand templates, or autofilling social assets at scale.
- **[Changelog Automation](sub-skills/changelog-automation/SKILL.md)** — Generate changelogs from commits, PRs, and releases following the Keep a Changelog format. **Use when:** setting up release workflows, generating release notes, or standardizing commit conventions.
- **[Reddit Automation](sub-skills/reddit-automation/SKILL.md)** — Automate Reddit (search subreddits, create posts, manage comments, browse top content) via Rube MCP. **Use when:** posting to subreddits, monitoring or searching Reddit, or managing comments.
- **[Render Automation](sub-skills/render-automation/SKILL.md)** — Automate Render cloud (services, deployments, projects) via Rube MCP. **Use when:** deploying to Render, checking build/deploy status, or managing Render services and projects.
- **[X Twitter Scraper](sub-skills/x-twitter-scraper/SKILL.md)** — Automate X/Twitter (tweet search, follower export, posting, DMs, webhooks) via MCP and SDKs. **Use when:** searching tweets, exporting followers, posting or DMing, or feeding X data into a pipeline.
- **[Vercel Automation](sub-skills/vercel-automation/SKILL.md)** — Automate Vercel (deployments, domains, DNS, env vars, projects, teams) via Rube MCP. **Use when:** managing Vercel deployments, assigning domains or DNS, or updating environment variables.
- **[Telegram Core](sub-skills/telegram/SKILL.md)** — Set up the Telegram Bot API: BotFather registration, messages, webhooks, inline keyboards, groups/channels, with Node.js and Python boilerplates. **Use when:** building or configuring a Telegram bot from scratch (tokens, webhooks, command handlers). **Not for:** scheduled channel operations over an existing bot (use Telegram Automation).
- **[Telegram Automation](sub-skills/telegram-automation/SKILL.md)** — Automate Telegram operations (send messages, manage chats, share photos/documents, bot commands) via Rube MCP. **Use when:** auto-posting scheduled content, pushing alert feeds, or managing chats through an already-configured bot. **Not for:** initial bot setup (use Telegram Core).
- **[Git Worktrees](sub-skills/git/worktrees/SKILL.md)** — Use git worktrees to create isolated workspaces that share one repository for parallel branch work. **Use when:** you need to work on multiple branches simultaneously without stashing or switching, e.g. concurrent checkouts or separate build workspaces.

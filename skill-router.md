---
description: "Skill routing map with explicit USE WHEN and NOT FOR boundaries. Use this to pick the best matching skill(s) and avoid overlap."
---

# Skill Router

## Routing Rules

1. Select at most 1 primary skill and 1 supporting skill unless the task explicitly requires more.
2. Match user intent against the USE WHEN clause first.
3. If NOT FOR applies, skip that skill and choose a better match.
4. For security-sensitive implementation, pair with security-review when relevant.
5. For C# code changes, pair code modifications with csharp-reviewer when relevant.

## Skill Map

| Skill | Use When | Not For |
|---|---|---|
| a11y-architect | designing or reviewing UI components/pages; building design systems and interaction patterns | non-accessibility visual style direction; backend security or infrastructure decisions |
| agent-introspection-debugging | Maximum tool call or loop-limit failures; Repeated retries with no forward progress | unrelated tasks outside this scope |
| api-and-interface-design | Designing new API endpoints or resource URLs; Implementing pagination; defining type contracts between modules; establishing boundaries between frontend and backend | unrelated tasks outside this scope |
| architect | planning new cross-cutting features; refactoring large or tightly coupled systems | line-by-line implementation plans; build/type error fixing |
| architecture-design | designing new systems, features, or making high-level technical decisions | unrelated tasks outside this scope |
| browser-testing-with-devtools | Building/debugging UI; inspecting DOM/Console/Network; visual verification; performance profiling | backend-only changes; CLI tools; non-browser code |
| ci-cd-and-automation | Setting up pipelines; automated quality gates (lint/type/test); deployment strategies; feature flags | local debugging only; manual tasks unrelated to automation |
| article-writing | Drafting blog posts, essays, guides, tutorials; Turning notes into polished articles | unrelated tasks outside this scope |
| brand-voice | Writing for social media, email, launch posts, threads, or product updates | unrelated tasks outside this scope |
| build-error-resolver | build fails; TypeScript/type checker errors block progress | architecture redesign; feature expansion |
| code-architect | translating approved feature direction into concrete code structure; adding multi-file capabilities | deep system architecture alternatives; code review/audit of final diffs |
| code-explorer | before implementing features in unfamiliar areas; when debugging complex behavior paths | final architecture decision arbitration; code modification or refactor execution |
| code-generation | generating boilerplate, scaffolding, or repetitive code structures | unrelated tasks outside this scope |
| code-reviewer | thorough code review before merge; evaluating implementation quality | implementing fixes itself; architecture planning from scratch |
| coding-standards-and-simplification | Writing new code; reviewing for maintainability; refactoring for clarity (KISS/DRY/YAGNI); simplified logic patterns | framework architecture and layering; API contract/versioning details |
| context-engineering | Daily pair-programming; files < 2000 lines; focus on business logic instead of system management | complex systems; large-scale context optimization |
| brain-context-engineering/context-optimization | optimizing context; reducing token costs; KV-cache stabilization; observation masking | single-file changes; simple tasks |
| brain-context-engineering/filesystem-context | offloading context to files; scratch pads; plan persistence; multi-agent shared workspaces | short sessions; low-latency requirements |
| brain-context-engineering/multi-agent-patterns | partitioning complex tasks across multiple agents; coordinating sub-agent workflows | tasks that fit comfortably in a single window |
| idea-refine | raw concepts or vague ideas; startup concepts; process improvements; feature ideation | implementation-ready requirements; debugging existing code |
| planning-and-task-breakdown | breaking work into implementable units; estimating scope; parallelizing work; vertical slicing | single-file changes; obvious scope; pre-defined task lists |
| debugging-and-error-recovery | Systematic triage of test failures, build breaks, or runtime bugs; root-cause analysis | unrelated tasks outside this scope |
| deprecation-and-migration | Replacing old systems/APIs; sunsetting features; consolidating duplicate logic; zombie code cleanup | new feature development; initial implementation |
| documentation-and-adrs | Recording architectural decisions; writing public API docs; changelog maintenance; explaining "why" | documenting obvious code; throwaway prototypes |
| comment-analyzer | after refactors or behavior changes; during code review of heavily commented modules | unrelated tasks outside this scope |
| content-engine | writing X posts or threads; drafting LinkedIn posts or launch updates | deep voice derivation; long-form article craft |
| conversation-analyzer | user repeatedly corrects assistant behavior; hook policy design is requested | unrelated tasks outside this scope |
| crosspost | user wants to publish one idea across multiple platforms | deriving voice profile from scratch; shaping weak source material |
| csharp-reviewer | any C# code change (*.cs); PR review for .NET services/libraries | implementing large code rewrites; non-.NET language reviews |
| deep-research | user asks for in-depth research or investigation; competitive analysis, technology evaluation | brand voice derivation; social content adaptation |
| distributed-system | designing or troubleshooting distributed architectures, message queues, eventual consistency | unrelated tasks outside this scope |
| dmux-workflows | user asks to run work in parallel; complex task benefits from divide-and-conquer | framework-specific coding rules; architecture decisions unrelated to orchestration |
| documentation-lookup | setup or configuration questions for a specific library/framework; API reference lookups | architecture decisions unrelated to library API details; broad market research |
| dotnet-patterns | writing new C# code; refactoring .NET services and libraries | deep security audits or threat modeling; PR severity triage |
| e2e-testing | creating or refactoring Playwright E2E suites; setting up test architecture (folders, fixtures, POM) | unit/integration test strategy; frontend architecture decisions |
| eval-harness | setting up evaluation-driven development for AI-assisted projects; defining completion criteria | framework-specific test implementation; replacing unit/integration/e2e strategy |
| exa-search | user needs latest web/news information; finding code examples or API references | multi-theme research synthesis; framework documentation resolution |
| fal-ai-media | user asks to generate images from text prompts; create video from text or image | social campaign strategy; non-fal providers as default path |
| frontend-design | building a landing page, dashboard, or app shell from scratch; upgrading bland UI | framework-specific state/data architecture; backend/API concerns |
| frontend-patterns | building React components and feature modules; deciding state management approach | high-concept visual direction; backend/API contract design |
| frontend-slides | creating a talk deck, pitch deck, or internal presentation; converting ppt to HTML | broad frontend app architecture; content distribution strategy |
| framework-migration | modernizing legacy systems (Strangler Fig); migrating frameworks (React→Vue, REST→GraphQL); upgrading major dependencies (breaking changes, semver batching); language version upgrades (Python 2→3); SQL→NoSQL migration | greenfield development; minor bug fixes; infrastructure-only changes |
| implementation-planning | Writing new code; Modifying existing logic | unrelated tasks outside this scope |

| investor-materials | creating or revising a pitch deck; writing one-pagers and investor memos | investor outreach messaging; social/media content distribution |
| investor-outreach | writing cold outreach to investors; drafting warm intro requests | building core fundraising assets; voice profiling methodology |
| market-research | researching a market, category, company, or technology trend; building TAM/SAM/SOM estimates | framework/API documentation lookup; purely technical implementation |
| mcp-server-patterns | creating a new MCP server; adding or updating tools/resources/prompts | product-specific business logic; generic API design unrelated to MCP |
| nextjs-turbopack | developing or debugging Next.js 16+ applications; diagnosing slow dev startup or HMR | framework API semantics; general frontend architecture decisions |
| nodejs-backend | building or reviewing Node.js/Express/TypeScript microservices; Prisma data access; Zod validation; Sentry observability; Express middleware; background jobs | C#/.NET services (use dotnet-patterns); React/Next.js frontend (use frontend-patterns); pure infrastructure |
| performance-optimization | profiling slow endpoints or queries; optimizing throughput, latency, or memory usage | architecture redesign; feature development |

| pr-review | reviewing pull requests for correctness, style, and risk before merge | implementing fixes; architecture planning |
| product-capability | PRD/roadmap note exists but implementation constraints are vague; feature crosses multiple services | unrelated tasks outside this scope |
| resilience-patterns | adding retry logic, circuit breakers, timeouts, or fallback strategies | unrelated tasks outside this scope |
| securities-audit | auditing for financial data handling, regulatory compliance, or sensitive data exposure | unrelated tasks outside this scope |
| security-and-hardening | handling user input; authentication/authorization; storing sensitive data; external integrations | high-level threat modeling; legal compliance interpretation |
| security-auditor | security-focused code review; threat analysis; hardening recommendations; vulnerability detection | broad architecture design unrelated to security |
| security-review | implementing authentication/authorization; handling user input or file uploads | deep architecture-level threat modeling; compliance legal interpretation |
| source-driven-development | framework-specific implementation; building boilerplate or starter patterns; verifying best practices | pure logic; renaming variables; speed-priority tasks |
| spec-driven-development | starting new projects or features; ambiguous requirements; architectural decisions | single-line fixes; typo corrections; self-contained requirements |
| strategic-compact | long sessions approaching context pressure; multi-phase tasks (research -> plan -> implement -> test) | runtime debugging or failure diagnosis; test/build verification workflows |
| tdd-workflow | adding new features; fixing bugs or regressions | deep E2E framework patterns; post-implementation verification orchestration |
| test-driven-development | implementing new logic; fixing bugs (Prove-It pattern); modifying existing functionality | pure configuration; documentation; static content |
| test-engineer | designing test suites; writing tests for existing code; evaluating test quality and coverage | implementing features or fixes itself |
| verification-loop | after a feature or significant change; before opening a PR | writing test suites from scratch; deep security architecture audits |
| workspace-surface-audit | auditing project structure, file layout, or surface-level code organization | unrelated tasks outside this scope |
| x-api | posting tweets or threads programmatically; reading timeline/mentions/user info | content strategy and editorial planning; cross-platform distribution |

## Notes

- This file guides selection; source-of-truth remains each SKILL.md.
- Keep descriptions concise and action-triggered to improve skill discovery.

## Delegation Chains

When a task exceeds a skill's scope, delegate using these chains:

| Current Skill | Exceeds Scope When | Delegate To |
|---|---|---|
| build-error-resolver | fix requires architectural change | architect |
| code-reviewer | review reveals need for full rewrite | code-architect |
| tdd-workflow | tests require E2E browser automation | e2e-testing |
| architect | needs line-by-line implementation | code-architect |
| code-architect | output needs post-implementation review | code-reviewer / csharp-reviewer |
| security-review | threat spans entire architecture | architect |
| performance-optimization | bottleneck is architectural | architect / distributed-system |
| frontend-design | needs component-level implementation | frontend-patterns |
| implementation-planning | plan needs E2E validation | verification-loop |
| verification-loop | gaps found require new tests | tdd-workflow / e2e-testing |

---
name: content-master
description: "Master Content & Knowledge Orchestrator. Coordinates Writing, Documentation, and Standards."
category: writing
metadata:
  category: master-orchestrator
  triggers: [writing, documentation, adrs, article-writing, standards]
---

# ✍️ Content & Knowledge Master Orchestrator

The authoritative lead for documentation and written communication. This master skill coordinates technical writing, knowledge management, and coding standards.

---

## 🧭 Content Strategy
- **Clarity & Precision**: Use clear, concise language for technical topics.
- **Structured Knowledge**: Organize documentation for easy discovery.
- **Standardized Excellence**: Enforce consistent coding and writing standards.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing writing or documentation tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure structured technical writing and governance:

### 🔄 Sequential Sub-Skill Pipeline
```
[Writing Skills] ──→ [Documentation and ADRs] ──→ [Coding Standards]
```


### 1. Technical Writing & Style
- **[Writing Skills](sub-skills/writing-skills/SKILL.md)** — authoring guide for creating and refining agent skills themselves. **Use when:** building or improving a SKILL.md, its frontmatter, or delegation structure. **Not for:** writing end-user prose or documentation (use the style and docs skills below).
- **[Beautiful Prose Guidelines](sub-skills/beautiful-prose/SKILL.md)** — a strict style contract for clean, forceful English free of AI cadence, filler, and therapeutic tone. **Use when:** a draft or rewrite must read as timeless, concrete human prose. **Not for:** structured reference or API docs where terseness beats voice.
- **[Avoid AI Writing](sub-skills/avoid-ai-writing/SKILL.md)** — audits and rewrites copy against 21 categories of AI writing tells using a 43-entry replacement table. **Use when:** text sounds AI-generated and needs humanizing before publish. **Not for:** first-draft generation from scratch.
- **[Bulletmind Structured Thinking](sub-skills/bulletmind/SKILL.md)** — converts input into clean, hierarchical bullet points. **Use when:** summarizing, note-taking, or compressing content into nested bullets. **Not for:** flowing narrative prose.

### 2. Documentation, ADRs & References
- **[Documentation and ADRs](sub-skills/documentation-and-adrs/SKILL.md)** — records architectural decisions and project documentation. **Use when:** making a significant design choice, changing a public API, or capturing context for future maintainers. **Not for:** looking up existing library docs (use Documentation Lookup).
- **[Documentation Lookup](sub-skills/documentation-lookup/SKILL.md)** — pulls up-to-date library/framework docs via Context7 MCP instead of training data. **Use when:** setup/config questions, API reference lookups, or the user names a framework (React, Next.js, Prisma). **Not for:** architecture decisions or market research unrelated to library API details.
- **[Grill With Docs](sub-skills/grill-with-docs/SKILL.md)** — stress-tests an existing plan against the domain model, glossary, and ADRs. **Use when:** validating a plan's terminology and decisions against documented project language. **Not for:** initial ideation or writing the plan itself.
- **[System README Standards](sub-skills/readme/SKILL.md)** — produces exhaustively thorough project README documentation and onboarding structure. **Use when:** writing or overhauling a repository README or codebase onboarding guide. **Not for:** decision records (use Documentation and ADRs).
- **[Reference Builder](sub-skills/reference-builder/SKILL.md)** — generates comprehensive technical references, parameter listings, and configuration guides. **Use when:** building searchable API/reference material or a full config catalog. **Not for:** narrative tutorials or blog posts.

### 3. Long-form & Content Engines
- **[Article Writing](sub-skills/article-writing/SKILL.md)** — drafts long-form content in a distinctive voice derived from supplied examples or brand guidance. **Use when:** writing blog posts, essays, launch posts, guides, tutorials, or newsletter issues, or turning notes/transcripts/research into polished articles. **Not for:** short social copy or reference docs.
- **[Blog Writing Guide](sub-skills/blog-writing-guide/SKILL.md)** — enforces Sentry's blog writing standards and Hook-Body-CTA structure. **Use when:** drafting a Sentry blog post or product announcement. **Not for:** non-Sentry voice or other platforms.
- **[Content Engine](sub-skills/content-engine/SKILL.md)** — builds platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. **Use when:** producing posts/threads or a multi-platform repurposing campaign. **Not for:** deep voice fingerprinting or long-form editorial polish (use Article Writing).
- **[Podcast Generation](sub-skills/podcast-generation/SKILL.md)** — generates real audio narratives from text via Azure OpenAI's Realtime API. **Use when:** turning written content into a scripted/spoken podcast segment. **Not for:** text-only deliverables.

### 4. Social, SEO & Structured Data
- **[Social Copywriting](sub-skills/social-content/SKILL.md)** — social strategy plus engaging posts tied to goals and audience across major networks. **Use when:** planning or drafting social posts to build audience and engagement. **Not for:** keyword/SEO optimization (use Social SEO Writing) or long-form articles.
- **[Social SEO Writing](sub-skills/social-post-writer-seo/SKILL.md)** — writes clear, SEO-aware social posts for Instagram, LinkedIn, and Facebook. **Use when:** you need keyword-integrated posts with organic-reach templates. **Not for:** schema/structured-data markup.
- **[Schema Markup SEO](sub-skills/schema-markup/SKILL.md)** — designs, validates, and optimizes schema.org / JSON-LD structured data. **Use when:** adding rich-snippet markup for search eligibility and measurable SEO impact. **Not for:** writing the page copy itself.

### 5. Brand Voice & Persuasion Psychology
- **[Sentry Brand Guidelines](sub-skills/brand-guidelines/SKILL.md)** — writes copy in Sentry's Plain Speech (default) and Sentry Voice tones. **Use when:** writing UI text, error messages, empty states, onboarding, 404 pages, docs, or marketing copy for Sentry. **Not for:** another brand's voice.
- **[Anthropic Brand Guidelines](sub-skills/brand-guidelines-anthropic/SKILL.md)** — Anthropic's official visual identity: brand colors, typography, and styling. **Use when:** applying Anthropic brand colors, fonts, or visual formatting to output. **Not for:** voice/tone copywriting.
- **[Community Brand Guidelines](sub-skills/brand-guidelines-community/SKILL.md)** — community copy of the same Anthropic visual-identity resource (colors, typography). **Use when:** you need Anthropic brand styling and prefer the community-sourced variant. **Not for:** anything distinct from Anthropic Brand Guidelines — the two files are duplicates.
- **[Brand Perception Psychologist](sub-skills/brand-perception-psychologist/SKILL.md)** — diagnoses what a brand's identity signals subconsciously and prescribes realignment. **Use when:** auditing how a market perceives a brand or repositioning messaging/visuals to shift trust or status. **Not for:** producing the final copy or visual assets.
- **[Pitch Psychologist](sub-skills/pitch-psychologist/SKILL.md)** — structures sales, investor, and product pitches with desire-then-solution psychological sequencing. **Use when:** a deck, talk track, or one-pager needs stronger belief progression from attention to commitment. **Not for:** generic content unrelated to persuasion.
- **[Scarcity Urgency Psychologist](sub-skills/scarcity-urgency-psychologist/SKILL.md)** — engineers credible scarcity and urgency mechanics grounded in real limits. **Use when:** you need honest deadline/stock/access urgency that drives action without eroding trust. **Not for:** fabricated scarcity — the skill stops if the limit is not real.

### 6. Scientific, Research & SR&ED Writing
- **[Scientific Writing Standards](sub-skills/scientific-writing/SKILL.md)** — deep-research writing with verified citations and formatted academic outputs. **Use when:** producing research-backed documents, papers, abstracts, or LaTeX-formatted academic writing. **Not for:** casual or marketing content.
- **[Claude Scientific Writing](sub-skills/claude-scientific-skills/SKILL.md)** — general patterns for scientific research and analysis tasks. **Use when:** a task clearly involves scientific research or analysis workflows. **Not for:** work outside that scope; not a substitute for expert validation.
- **[Citation Management](sub-skills/citation-management/SKILL.md)** — manages citations systematically across the research and writing process (APA, IEEE, BibTeX). **Use when:** structuring, tracking, or formatting references and citation databases. **Not for:** the prose or research itself.
- **[SR&ED Project Organizer](sub-skills/sred-project-organizer/SKILL.md)** — organizes a list of projects and their documentation into the Canadian SR&ED submission format. **Use when:** structuring projects/docs into SR&ED tax-claim format. **Not for:** writing the technical work summaries (use SR&ED Work Summary).
- **[SR&ED Work Summary](sub-skills/sred-work-summary/SKILL.md)** — reviews a year of work and groups relevant links into projects as a Notion doc for SR&ED documentation. **Use when:** compiling technical progress and experimental methodology into SR&ED project summaries. **Not for:** top-level submission structuring (use SR&ED Project Organizer).

### 7. PDF Processing
- **[PDF Processing](sub-skills/pdf/SKILL.md)** — extract text/tables, merge/split, create, and fill PDFs via Python libs (pypdf, pdfplumber, ReportLab) and CLI tools. **Use when:** parsing, transforming, generating, or form-filling PDF files. **Not for:** authoring prose that merely ends up as a PDF (use the writing skills).
- **[PDF Processing (Official)](sub-skills/pdf-official/SKILL.md)** — the same PDF processing guide (extraction, generation, form filling). **Use when:** the same PDF tasks as above. **Not for:** anything distinct — this file is a duplicate copy of PDF Processing.

### 8. Governance — Coding Standards
- **[Coding Standards](sub-skills/coding-standards/SKILL.md)** — core code-quality baseline and simplification guide (KISS, DRY, YAGNI, naming, async hygiene, error handling). **Use when:** writing code, reviewing for maintainability, or refactoring for clarity. **Not for:** prose or documentation style.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of documentation and ADR writing:
- 👉 Recommend calling **[Infrastructure Master](../infrastructure-master/SKILL.md)** next to translate the architectural decisions into CDK or other IaC setup for deployment.

---

## 🏗️ Operating Pipeline
1. **Audit**: Review existing documentation or knowledge gaps.
2. **Draft**: Create structured content following established style guides.
3. **Review**: Validate technical accuracy and adherence to standards.
4. **Publish**: Organize and link new content within the knowledge graph.

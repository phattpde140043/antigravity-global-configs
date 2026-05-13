---
name: article-writing
description: "Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance. USE WHEN: Drafting blog posts, essays, launch posts, guides, tutorials, or newsletter issues; Turning notes, transcripts, or research into polished articles. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Article Writing

Write long-form content that sounds like an actual person with a point of view, not an LLM smoothing itself into paste.

---

# When to Activate

- Drafting blog posts, essays, launch posts, guides, tutorials, or newsletter issues
- Turning notes, transcripts, or research into polished articles
- Matching an existing founder, operator, or brand voice from examples
- Tightening structure, pacing, and evidence in already-written long-form copy

---

# Core Rules

1. Lead with the concrete thing: artifact, example, output, anecdote, number, screenshot, or code.
2. Explain after the example, not before.
3. Keep sentences tight unless the source voice is intentionally expansive.
4. Use proof instead of adjectives.
5. Never invent facts, credibility, or customer evidence.

---

# Voice Handling

If the user wants a specific voice, run `brand-voice` first and reuse its VOICE PROFILE.
Do not duplicate a second style-analysis pass here — `brand-voice` is the canonical source.

If no voice references are given, default to a **sharp operator voice**: concrete, unsentimental, useful.

---

# Banned Patterns

Delete and rewrite any of these on sight:
- "In today's rapidly evolving landscape"
- "game-changer", "cutting-edge", "revolutionary"
- "here's why this matters" as a standalone bridge
- Fake vulnerability arcs
- A closing question added only to juice engagement
- Biography padding that does not move the argument
- Generic AI throat-clearing that delays the point

---

# Writing Process

1. **Clarify** the audience and purpose.
2. **Outline** with one job per section — no section exists without a clear reason.
3. **Open sections** with proof, artifact, conflict, or example.
4. **Expand** only where the next sentence earns its space.
5. **Cut** anything that sounds templated, overexplained, or self-congratulatory.

---

# Structure Guidance

## Technical Guides

- Open with what the reader gets (outcome, not background)
- Use code, commands, screenshots, or concrete output in every major section
- End with actionable takeaways, not a soft recap

## Essays / Opinion

- Start with tension, contradiction, or a specific observation
- Keep one argument thread per section
- Make opinions answer to evidence

## Newsletters

- Keep the first screen doing real work
- Do not front-load diary filler
- Use section labels only when they improve scannability

---

# Quality Gate

Before delivering, verify:

- [ ] Factual claims are backed by provided sources — nothing invented
- [ ] Generic AI transitions are gone (no "furthermore", "it's worth noting", "let's dive in")
- [ ] Voice matches supplied examples or the agreed VOICE PROFILE
- [ ] Every section adds something new — no padding
- [ ] Formatting matches the intended medium (blog, newsletter, docs, etc.)
- [ ] Opening sentence does real work — no warm-up paragraph

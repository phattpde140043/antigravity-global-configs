---
name: brand-voice
description: "Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content and outreach workflows. USE WHEN: The user wants content or outreach in a specific voice; Writing for social media, email, launch posts, threads, or product updates. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Brand Voice

Build a durable voice profile from real source material, then use that profile everywhere instead of re-deriving style from scratch or defaulting to generic AI copy.

---

# When to Activate

- The user wants content or outreach in a specific voice
- Writing for social media, email, launch posts, threads, or product updates
- Adapting a known author's tone across channels
- The content needs a reusable style system instead of one-off mimicry

---

# Source Priority

Use the strongest real source set available, in this order:

1. Recent original social posts and threads
2. Articles, essays, memos, launch notes, or newsletters
3. Real outbound emails or DMs that worked
4. Product docs, changelogs, README framing, and site copy

Do not use generic platform exemplars as source material.

---

# Collection Workflow

1. Gather 5–20 representative samples when available.
2. Prefer recent material over old unless the user says older writing is more canonical.
3. Separate "public launch voice" from "private working voice" if the source set clearly splits.
4. If the user provides URLs, fetch and extract content before analysis.

---

# What to Extract

Analyze source material for:

- **Rhythm** — sentence length tendency (short/mixed/long)
- **Compression** — how much context is compressed vs spelled out
- **Capitalization** — conventional, all-lowercase, or mixed
- **Parentheticals** — frequency and purpose (qualification, aside, humor)
- **Questions** — frequency and purpose (rhetorical, structural, absent)
- **Claim sharpness** — hedged vs direct vs blunt
- **Evidence density** — how often numbers, mechanisms, or receipts show up
- **Transitions** — smooth connectors, abrupt jumps, earned turns
- **Avoidance list** — what the author never does

---

# Output: VOICE PROFILE

Produce a structured, reusable block that downstream skills consume directly.

```
## VOICE PROFILE: [Name or Brand]

**Sentence style:** [e.g., Short and punchy. Rarely exceeds 15 words.]
**Compression:** [e.g., High — assumes reader context, skips setup]
**Formality:** [e.g., Casual-professional. No slang, no stiffness.]
**Capitalization:** [e.g., Conventional sentence case]
**Parentheticals:** [e.g., Frequent — used for qualification and dry asides]
**Questions:** [e.g., Rare. Never used as engagement bait.]
**Claim style:** [e.g., Direct and specific. Backs claims with numbers.]
**Evidence density:** [e.g., High — mechanisms, metrics, and concrete examples]
**Transitions:** [e.g., Abrupt. Earns the next section by contrast, not connectors.]
**Never does:** [e.g., Fake vulnerability, LinkedIn cadence, warm-up paragraphs]
**Signature moves:** [e.g., Opens with the artifact, parenthetical qualifiers, dry humor]
```

Keep the profile short enough to fit in session context. The point is operational reuse, not literary criticism.

---

# Hard Bans

Delete and rewrite any of these on sight:

- Fake curiosity hooks
- "not X, just Y" framing
- "no fluff" (is itself fluff)
- Forced lowercase for aesthetics
- LinkedIn thought-leader cadence
- Bait questions
- "Excited to share"
- Generic founder-journey filler
- Corny parentheticals that add nothing

---

# Persistence Rules

- Reuse the latest confirmed VOICE PROFILE across related tasks in the same session.
- If the user asks for a durable artifact, save the profile to `/memories/` using the memory tool.
- Do not create repo-tracked files that store personal voice fingerprints unless the user explicitly asks.
- When resuming a session, check `/memories/session/` for an existing voice profile before re-deriving.

---

# Downstream Use

This skill is the **canonical source of truth** for voice profiles. Use it before or alongside:

- `article-writing` — for long-form content in a specific voice
- Any social media, email, or launch writing task
- Any workflow where voice consistency matters

If `article-writing` or another skill needs a voice profile, this skill produces it.

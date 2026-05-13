---
name: fal-ai-media
description: "Unified media generation via fal.ai MCP for image, video, and audio workflows. Covers text-to-image, text/image-to-video, text-to-speech, and video-to-audio generation. USE WHEN: user asks to generate images from text prompts; user asks to create video from text or image. NOT FOR: social campaign strategy and distribution; non-fal providers as the default path."
origin: ECC
---

# fal.ai Media Generation

Generate image, video, and audio assets through fal.ai MCP with predictable quality, cost control, and reproducible iteration.

---

## Purpose

Provide a single workflow for selecting fal.ai models, preparing inputs, estimating cost, running generation, and validating outputs.

---

## When to Activate

- user asks to generate images from text prompts
- user asks to create video from text or image
- user asks for speech/audio generation
- user asks for thumbnails, visual assets, promo clips, or narrated media

---

## Scope Boundaries

Use this skill for:
- fal.ai model discovery and selection
- media generation execution flow
- cost estimation and async job handling
- quality checks and iteration loops

Do NOT use this skill as primary source for:
- social campaign strategy and distribution
- non-fal providers as the default path
- long-form editing pipelines beyond generation handoff

Delegation:
- use content-engine for platform packaging and campaign adaptation
- use crosspost for distribution across social platforms

---

## MCP Requirement

fal.ai MCP must be configured in the active harness.
If unavailable, report the limitation and propose fallback with available media tooling.

---

## Core Tooling

- `search`: find candidate models by task keywords
- `find`: inspect model parameters and constraints
- `estimate_cost`: estimate generation cost before expensive runs
- `upload`: upload source files for image-to-video or editing inputs
- `generate`: run model generation
- `status` and `result`: monitor and retrieve async jobs
- `cancel`: stop expensive or incorrect jobs early
- `models`: list currently popular models

---

## Model Selection Playbook

## Image

- fast iteration: lightweight image model variants
- final quality: higher-fidelity image model variants
- editing/transform: image model with source image input

## Video

- text-to-video for concepting and first-pass motion
- image-to-video for tighter visual control and consistency
- audio-enabled video models when synchronized sound is required

## Audio

- text-to-speech for narration/voice lines
- video-to-audio for scene-matched sound generation

Rule:
- start with lower-cost/faster model for prompt exploration, then switch to high-quality model for final assets.

---

## Standard Workflow

## Step 1: Clarify Output Specs

Capture required constraints:
- medium: image, video, or audio
- target aspect ratio or duration
- tone/style and subject
- quality target and budget ceiling

## Step 2: Discover and Validate Model

Use `search` or `models`, then `find` for parameter contract.
Pick one primary model and one fallback model.

## Step 3: Estimate Cost First

Use `estimate_cost` before long video or multi-asset runs.
If estimate exceeds budget, reduce duration, count, or quality tier.

## Step 4: Prepare Inputs

For source-based generation, `upload` first and pass resulting URLs.
Validate prompt clarity before running expensive jobs.

## Step 5: Generate and Monitor

Run `generate`, then poll via `status` and `result`.
If output is clearly off-target, use `cancel` to limit spend.

## Step 6: Evaluate and Iterate

Check output against objective:
- visual/audio fidelity
- prompt adherence
- artifacts or temporal instability

Iterate with minimal controlled changes:
- one variable per rerun (prompt, seed, guidance, duration, ratio)

---

## Parameter Guidance

Prioritize these controls:
- `prompt`: specific scene/action/style instructions
- `seed`: reproducible iteration
- size/aspect settings: target platform fit
- duration: balance quality and cost in video
- number of outputs: broad exploration vs focused refinement

Prompt guidance:
- describe subject, style, camera/motion, lighting, and mood
- avoid contradictory constraints in one prompt
- keep action verbs explicit for video motion

---

## Cost and Reliability Rules

1. Always estimate cost before high-cost generations.
2. Cap first pass with low count/duration.
3. Use seeds for reproducible comparisons.
4. Cancel misconfigured runs early.
5. Log model and key parameters for reproducibility.

---

## Safety and Compliance

- do not generate disallowed content per policy
- do not include private identifiers without user confirmation
- do not expose secrets in prompts or metadata
- respect copyright/trademark constraints in requested output style

---

## Output Contract

When activated, return:

1. chosen model and rationale
2. generation parameters and estimated cost
3. run status and output summary
4. refinement suggestions for next iteration
5. handoff notes for downstream editing/distribution

---

## Related Skills

- content-engine for packaging assets into platform-native content
- crosspost for distribution variants and publishing adaptation

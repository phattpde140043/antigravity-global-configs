# Style Presets Reference

Curated visual styles for `frontend-slides`.
Use this file for viewport-safe CSS base, preset selection, and implementation guardrails.

## Viewport Fit Is Non-Negotiable

Each slide must fully fit in one viewport.

Golden rule:
- one slide equals one viewport height
- too much content means split into more slides
- never scroll inside a slide

## Density Limits

| Slide Type | Maximum Content |
|------------|-----------------|
| Title slide | 1 heading + 1 subtitle + optional tagline |
| Content slide | 1 heading + 4-6 bullets or 2 short paragraphs |
| Feature grid | 6 cards maximum |
| Code slide | 8-10 lines maximum |
| Quote slide | 1 quote + attribution |
| Image slide | 1 image, ideally under 60vh |

## Mandatory Base CSS

```css
html, body {
  height: 100%;
  overflow-x: hidden;
}

html {
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
}

.slide {
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  position: relative;
}

.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-height: 100%;
  overflow: hidden;
  padding: var(--slide-padding);
}

:root {
  --title-size: clamp(1.5rem, 5vw, 4rem);
  --h2-size: clamp(1.25rem, 3.5vw, 2.5rem);
  --h3-size: clamp(1rem, 2.5vw, 1.75rem);
  --body-size: clamp(0.75rem, 1.5vw, 1.125rem);
  --small-size: clamp(0.65rem, 1vw, 0.875rem);

  --slide-padding: clamp(1rem, 4vw, 4rem);
  --content-gap: clamp(0.5rem, 2vw, 2rem);
  --element-gap: clamp(0.25rem, 1vw, 1rem);
}

.card, .container, .content-box {
  max-width: min(90vw, 1000px);
  max-height: min(80vh, 700px);
}

.feature-list, .bullet-list {
  gap: clamp(0.4rem, 1vh, 1rem);
}

.feature-list li, .bullet-list li {
  font-size: var(--body-size);
  line-height: 1.4;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  gap: clamp(0.5rem, 1.5vw, 1rem);
}

img, .image-container {
  max-width: 100%;
  max-height: min(50vh, 400px);
  object-fit: contain;
}

@media (max-height: 700px) {
  :root {
    --slide-padding: clamp(0.75rem, 3vw, 2rem);
    --content-gap: clamp(0.4rem, 1.5vw, 1rem);
    --title-size: clamp(1.25rem, 4.5vw, 2.5rem);
    --h2-size: clamp(1rem, 3vw, 1.75rem);
  }
}

@media (max-height: 600px) {
  :root {
    --slide-padding: clamp(0.5rem, 2.5vw, 1.5rem);
    --content-gap: clamp(0.3rem, 1vw, 0.75rem);
    --title-size: clamp(1.1rem, 4vw, 2rem);
    --body-size: clamp(0.7rem, 1.2vw, 0.95rem);
  }

  .nav-dots, .keyboard-hint, .decorative {
    display: none;
  }
}

@media (max-height: 500px) {
  :root {
    --slide-padding: clamp(0.4rem, 2vw, 1rem);
    --title-size: clamp(1rem, 3.5vw, 1.5rem);
    --h2-size: clamp(0.9rem, 2.5vw, 1.25rem);
    --body-size: clamp(0.65rem, 1vw, 0.85rem);
  }
}

@media (max-width: 600px) {
  :root {
    --title-size: clamp(1.25rem, 7vw, 2.5rem);
  }

  .grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.2s !important;
  }

  html {
    scroll-behavior: auto;
  }
}
```

## Viewport Checklist

- each `.slide` includes `100vh`, `100dvh`, and `overflow: hidden`
- typography uses `clamp()`
- spacing uses `clamp()` or viewport units
- media has max-height constraints
- short-height breakpoints include 700px, 600px, and 500px
- if crowded, split into more slides

## Mood to Preset Mapping

| Mood | Good Presets |
|------|--------------|
| Impressed / Confident | Bold Signal, Electric Studio, Dark Botanical |
| Excited / Energized | Creative Voltage, Neon Cyber, Split Pastel |
| Calm / Focused | Notebook Tabs, Paper and Ink, Swiss Modern |
| Inspired / Moved | Dark Botanical, Vintage Editorial, Pastel Geometry |

## Preset Catalog

1. Bold Signal - high-impact keynote style.
2. Electric Studio - clean agency polish.
3. Creative Voltage - energetic retro-modern contrast.
4. Dark Botanical - premium atmospheric elegance.
5. Notebook Tabs - editorial and structured.
6. Pastel Geometry - friendly and approachable.
7. Split Pastel - playful split-composition style.
8. Vintage Editorial - magazine-inspired storytelling.
9. Neon Cyber - futuristic tech aesthetic.
10. Terminal Green - developer-centric monospace deck.
11. Swiss Modern - minimal, grid-disciplined precision.
12. Paper and Ink - literary narrative style.

## Animation Feel Mapping

| Feeling | Motion Direction |
|---------|------------------|
| Dramatic / Cinematic | slow fades, parallax, large scale-ins |
| Techy / Futuristic | glow, particles, grid motion, scramble text |
| Playful / Friendly | spring easing, floating shapes |
| Professional / Corporate | subtle 200-300ms transitions |
| Calm / Minimal | restrained movement, whitespace-first |
| Editorial / Magazine | staggered text-image interplay |

## CSS Gotcha: Negating Functions

Never use:

```css
right: -clamp(28px, 3.5vw, 44px);
margin-left: -min(10vw, 100px);
```

Use:

```css
right: calc(-1 * clamp(28px, 3.5vw, 44px));
margin-left: calc(-1 * min(10vw, 100px));
```

## Validation Sizes

- 1920x1080
- 1440x900
- 1280x720
- 1024x768
- 768x1024
- 414x896
- 375x667
- 896x414
- 667x375

## Anti-Patterns

Avoid:
- generic purple-on-white startup visuals
- system-font identity by default
- bullet walls and tiny text
- scrolling code blocks
- fixed-height boxes that break on short screens

Generate **several radically different UI variations** on a single route, switchable from a floating bottom bar. The user flips between variants in the browser, picks one (or steals bits from each), then throws the rest away.

If the question is about logic/state rather than what something looks like — wrong branch. Use [LOGIC.md](LOGIC.md).

## When this is the right shape
- "What should this page look like?"
- "I want to see a few options for this dashboard before committing."
- "Try a different layout for the settings screen."

## Two sub-shapes — strongly prefer sub-shape A

### Sub-shape A — adjustment to an existing page (preferred)
The route already exists. Variants are rendered **on the same route**, gated by a `?variant=` URL search param. The existing data fetching, params, and auth all stay — only the rendering swaps.

### Sub-shape B — a new page (last resort)
Only use when the thing being prototyped genuinely has no existing page to live inside. Create a **throwaway route** following the project's routing convention.

### 1. State the question and pick N
Default to **3 variants**. More than 5 stops being radically different and starts being noise — cap there.

### 2. Generate radically different variants
Variants must be **structurally different** — different layout, different information hierarchy, different primary affordance, not just different colours. Three slightly-tweaked card grids isn't a UI prototype, it's wallpaper.

### 3. Wire them together
Create a single switcher component on the route:

```tsx
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

### 4. Build the floating switcher
A small fixed-position bar at the bottom-centre of the screen with:
- **Left/Right arrows** — cycle variants (also keyboard `←`/`→`)
- **Variant label** — shows current variant key and name
- Visually distinct from the page content
- Hidden in production builds

### 5. Hand it over
Surface the URL (and the `?variant=` keys). The interesting feedback is usually **"I want the header from B with the sidebar from C"** — that's the actual design they want.

### 6. Capture the answer and clean up
Once a variant has won, write down which one and why. Then:
- **Sub-shape A** — delete the losing variants and the switcher; fold the winner into the existing page.
- **Sub-shape B** — promote the winning variant to a real route, delete the throwaway.

**Don'ts:**
- Variants that differ only in colour or copy. That's a tweak, not a prototype.
- Sharing too much code between variants. Each variant should be free to throw out the layout.
- Wiring variants to real mutations. Read-only prototypes are fine.
- Promoting the prototype directly to production. Rewrite it properly.

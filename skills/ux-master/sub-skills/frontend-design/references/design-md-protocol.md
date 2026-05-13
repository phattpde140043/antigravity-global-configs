# DESIGN.md Protocol: Semantic Design Documentation

A `DESIGN.md` file serves as the "Source of Truth" for your product's visual language. It translates technical values (Tailwind/CSS) into descriptive, designer-friendly language that AI models can easily follow.

## 📄 Structure of DESIGN.md

### 1. Visual Theme & Atmosphere
Capture the "vibe" using evocative adjectives.
- **Examples**: "Airy & Minimalist," "Utilitarian & Dense," "Sophisticated High-Contrast Dark Mode."

### 2. Color Palette & Roles
List colors by Descriptive Name + Hex Code + Functional Role.
- **Example**: "Deep Muted Navy (#1A1A2E) - Used for primary background and branding."

### 3. Geometry & Shape
Translate `border-radius` into physical descriptions.
- **Pill-shaped** (`rounded-full`)
- **Generously rounded** (`rounded-2xl`)
- **Sharp/Professional** (`rounded-none` or `rounded-sm`)

### 4. Depth & Elevation
Describe how the UI handles layers and shadows.
- **Examples**: "Flat & Layer-less," "Whisper-soft diffused shadows," "Heavy, high-contrast elevation for modals."

---

## 🛠️ Synthesis Workflow (How to create DESIGN.md)

1. **Discovery**: Scan the codebase (Tailwind config, CSS variables) to extract core design tokens.
2. **Analysis**: Look for patterns in spacing, typography usage, and component shapes.
3. **Synthesis**: Write the `DESIGN.md` file using the structure above.
4. **Verification**: Compare the written descriptions against a screenshot or rendered UI to ensure accuracy.

## 📋 Usage in Prompting
When asking for a new screen or component, always provide the `DESIGN.md` file as context:
> *"Generate a new Checkout screen for the OSP project. Use the design language defined in the attached DESIGN.md."*

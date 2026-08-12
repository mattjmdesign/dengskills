---
name: ui-system-initializer
description: Use this skill when starting a new codebase or design file that needs a clean UI foundation before components or pages are built. Produces a minimal design system setup covering semantic color tokens, typography, spacing, radius, shadows, light/dark mode, token naming, and where the system should live in code or design tools.
---

# UI System Initializer

Use this skill before generating screens, components, or visual polish. Its job is to establish the smallest useful design system foundation so agents and humans stop inventing colors, spacing, and type styles one component at a time.

## Process

1. Identify the target environment: codebase, Figma/design file, or both.
2. Determine whether a design system already exists. If it does, inventory the existing tokens instead of replacing them.
3. Define a minimal semantic color system: background, foreground, muted, muted foreground, border, primary, primary foreground, destructive, success, warning, card, popover, sidebar, and accent tokens only when needed.
4. Define typography defaults: sans and mono font stacks, fluid text scale, semantic font weights, and line-height tokens.
5. Define a 4px-based spacing and sizing scale for padding, margin, gap, touch targets, and layout rhythm.
6. Define radius, border, shadow, and focus-ring tokens.
7. Establish light and dark mode from the start, preferably with OKLCH values and complete token coverage in both themes.
8. Specify where tokens live: `globals.css`, Tailwind `@theme`, `tailwind.config.ts`, Figma variables, or a shared token source.
9. Output implementation-ready tokens plus rules for how future UI should consume them.

## Output format

````markdown
## UI system foundation

**Target environment:**
**Existing system status:**
**Token source of truth:**

### Color tokens
- [token]: [purpose]

### Typography scale
- [token]: [value and use]

### Spacing and sizing scale
- [token]: [value and use]

### Radius, shadow, and focus tokens
- [token]: [value and use]

### Theme strategy
- [light/dark approach]

### Implementation snippet
```css
/* token setup */
```

### Usage rules for agents and designers
- [rule]

### Decisions to confirm
- [item]
````

## Worked example

## UI system foundation

**Target environment:** Next.js + Tailwind v4 codebase (no Figma file yet)
**Existing system status:** None — greenfield
**Token source of truth:** `src/styles/globals.css` @theme inline

### Color tokens
- `--color-background` / `--color-foreground` — app canvas and default text
- `--color-muted` / `--color-muted-foreground` — secondary surfaces and text
- `--color-border`, `--color-input`, `--color-ring`
- `--color-primary` / `--color-primary-foreground` — brand actions
- `--color-destructive`, `--color-success`, `--color-warning`
- `--color-card`, `--color-popover`

### Typography scale
- `--font-sans` (Inter), `--font-mono` (JetBrains Mono); `--text-base: clamp(1rem, 0.5rem + 1vw, 1.125rem)`

### Spacing and sizing scale
- 4px base: 4/8/12/16/24/32/48/64; touch targets min 44px

### Radius, shadow, and focus tokens
- `--radius-md: 8px` (outer = inner + padding); `--shadow-card`; 2px focus ring token

### Theme strategy
- OKLCH primitives; `:root` light and `.dark` overrides for every semantic token; system detection via next-themes

### Implementation snippet
```css
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
}
```

### Usage rules for agents and designers
- Component code references semantic tokens only — never raw hex or one-off spacing

### Decisions to confirm
- Brand hue/lightness range; whether a Figma variable set should mirror the CSS tokens

## Common mistakes to prevent

- Do not create a large enterprise token system before the project needs it.
- Do not introduce arbitrary hex values, one-off pixel values, or component-specific colors.
- Do not define light mode without dark mode coverage for the same semantic tokens.
- Do not use primitive color names directly in component code when semantic tokens should be used.
- Do not overwrite an existing token system without documenting what changed and why.

## Boundaries

- Do not use when a token system already exists — audit it with `$ui-system-governance` instead of replacing it.
- Do not use when the question is layout shells — use `$ui-layout-architect`.

## Validate before final

- The output defines a minimal but complete color, type, spacing, radius, shadow, and focus foundation.
- Every color token has a clear semantic purpose and light/dark coverage.
- The source of truth is explicit enough for future agents to update the same files instead of inventing new ones.
- The system can support primitives, layout shells, and page composition without new arbitrary values.

## See also

- [Design Engineering guide: Design System](https://frontendguide.dev/docs/design-system)

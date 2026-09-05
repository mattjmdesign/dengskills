---
name: tokens
description: "Create or extend a small token system with semantic roles, theme pairs, and concrete component usage. Use when starting a UI foundation, when colors or spacing multiply, or before building components or shells."
---

# Design tokens

Give repeated visual decisions a shared home. Inspect existing tokens and consumers before defining another palette or replacing the system.

## Work

- Establish audience, platform, brand constraints, and reading versus task density. Choose roles before values.
- Define only needed surface/text, action/foreground, border, focus, and status pairs; add type, spacing, radius, and motion scales where repetition warrants them.
- Reuse the current format and naming. OKLCH is useful for perceptual adjustment but does not guarantee contrast. Literal values are appropriate at the source; a one-off measured dimension does not automatically deserve a token.
- Support the themes the product actually needs. For each supported theme, verify actual foreground/background pairs and interactive states; do not mechanically invert colors.
- Show how one real primitive and one composed screen consume the roles. Use those examples to discover missing roles before growing the system.
- For existing work, explain additions and migrations, including consumers that may change visibly.

## Deliver

Give the source path, compact role/value table or implementation, usage example, and contrast/visual checks. For an authorized implementation task, update the source and its consumers.

```markdown
## Token foundation

**Source:**
**Roles:** surface/text, action/foreground, border, focus, status pairs
**Type / spacing / radius:** scales added where repeated
**Themes:** pairs verified per theme
**Usage:** one primitive + one screen consume the roles
**Checks:** contrast, focus, enlargement, theme transitions
```

Example: pair action background with action text; pair warning surface with warning text. A name such as “primary” does not prove either pairing is readable.

Check text enlargement, focus visibility, and theme transitions in context. Avoid compulsory dark mode, fixed type ratios, or a token for every pixel. Use `$system` for ongoing drift and migration review; `$craft` for broader visible design work.

## Worked example

## Token foundation

**Source:** `src/styles/globals.css` (`@theme inline`)
**Roles:** `--color-background` / `--color-foreground`; `--color-muted` / `--color-muted-foreground`; `--color-border`, `--color-ring`; `--color-primary` / `--color-primary-foreground`; `--color-destructive`, `--color-success`, `--color-warning`
**Type / spacing / radius:** `--font-sans` (Inter), `--font-mono` (JetBrains Mono); 4px scale 4/8/12/16/24/32/48; `--radius-md: 8px`; 2px focus ring
**Themes:** Light `:root` plus `.dark` overrides for every semantic role; verify each foreground/background pair, do not invert mechanically
**Usage:** Button consumes `--color-primary` pair; dashboard card consumes `--color-card` pair with `--radius-md` and `--shadow-card`
**Checks:** AA contrast per pair in both themes; focus ring visible on Button; 200% text enlargement without clipping

## Boundaries

- Do not use when a token system already exists — use `$system` to audit drift instead of replacing it.
- Do not use when the question is layout shells — use `$layout` instead.

---
name: tokens
description: "Create or extend a small token system with semantic roles, theme pairs, and concrete component usage."
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

Example: pair action background with action text; pair warning surface with warning text. A name such as “primary” does not prove either pairing is readable.

Check text enlargement, focus visibility, and theme transitions in context. Avoid compulsory dark mode, fixed type ratios, or a token for every pixel. Use `$system` for ongoing drift and migration review; `$craft` for broader visible design work.

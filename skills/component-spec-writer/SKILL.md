---
name: component-spec-writer
description: Use this skill when defining a UI component before code. Produces a component specification for React, Vue, or design-system work covering purpose, component type, variants, states, props/inputs, slots/composition, accessibility behavior, responsive behavior, design-token requirements, implementation boundaries, and acceptance criteria.
---

# Component Spec Writer

Use this skill before generating component code. Agents produce better components when the interface, states, and constraints are defined first.

## Process

1. Define the component purpose and where it appears.
2. Classify it as primitive, composed feature component, layout component, or page-level pattern.
3. Define variants, sizes, visual states, interaction states, and data states.
4. Define props/inputs, including controlled vs uncontrolled behavior if relevant.
5. Define slots and composition rules.
6. Define accessibility behavior: semantics, keyboard interaction, focus management, ARIA only when needed, target size, reduced motion.
7. Define responsive behavior and token usage expectations.
8. Write acceptance criteria for implementation and review.

## Output format

````markdown
## Component specification: [Name]

**Purpose:**
**Component type:**
**Used in:**

### Variants
- [item]

### States
- [item]

### Props / inputs
```ts
interface ComponentProps {
  // ...
}
```

### Slots / composition
- [item]

### Accessibility behavior
- [item]

### Responsive behavior
- [item]

### Design token requirements
- [item]

### Implementation boundaries
- [item]

### Acceptance criteria
- [ ] [criterion]
````

## Worked example

## Component specification: ProjectStatusBadge

**Purpose:** Shows a project's lifecycle status next to its name in lists and headers.
**Component type:** Primitive-level badge with domain variants (kept in primitives until 2+ features need it).
**Used in:** ProjectList, ProjectDetailHeader

### Variants
- status: active | paused | completed | archived (each maps to colour + label)
- size: sm | md (default md)

### States
- default, hover (no-op — non-interactive), label truncation at narrow widths

### Props / inputs
```ts
interface ProjectStatusBadgeProps {
  status: "active" | "paused" | "completed" | "archived"
  size?: "sm" | "md"
  className?: string
}
```

### Slots / composition
- No slots — label text derives from status; not meant for arbitrary children

### Accessibility behavior
- Semantic `<span>` (non-interactive); status conveyed by text, colour is decorative — no colour-only meaning; WCAG AA contrast for every status pair

### Responsive behavior
- Truncates label with ellipsis below 320px container; never wraps

### Design token requirements
- Uses `--color-success`, `--color-warning`, `--color-muted`, `--color-primary` and matching foreground tokens — no raw hex

### Implementation boundaries
- No click handlers, no tooltips (wrap externally if needed); not part of button primitives

### Acceptance criteria
- [ ] All four statuses render correct label + token colours
- [ ] WCAG 2.2 AA contrast in light and dark mode
- [ ] Does not wrap or break layout in a 320px container

## Common mistakes to prevent

- Do not code until states and accessibility behavior are specified.
- Do not turn every visual option into a prop; prefer composition when possible.
- Do not use raw colors, spacing, fonts, or shadows where semantic tokens should exist.
- Do not add ARIA when semantic HTML already provides the behavior.

## Boundaries

- Do not use when the design system has no tokens yet — establish them with `$ui-system-initializer` first.
- Do not use when the component already exists — check `$ui-system-governance` inventories before duplicating.

## Validate before final

- The spec includes variants, states, props, accessibility, responsive behavior, and acceptance criteria.
- The component type explains whether it belongs in primitives or feature code.

## See also

- [Design Engineering guide: Component Architecture](https://frontendguide.dev/docs/component-architecture)

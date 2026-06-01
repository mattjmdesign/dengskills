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

## Common mistakes to prevent

- Do not code until states and accessibility behavior are specified.
- Do not turn every visual option into a prop; prefer composition when possible.
- Do not use raw colors, spacing, fonts, or shadows where semantic tokens should exist.
- Do not add ARIA when semantic HTML already provides the behavior.

## Validate before final

- The spec includes variants, states, props, accessibility, responsive behavior, and acceptance criteria.
- The component type explains whether it belongs in primitives or feature code.

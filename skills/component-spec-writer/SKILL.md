---
name: component-spec-writer
description: Write a pre-implementation specification for a UI component. Use when defining a React, Vue, or component-system primitive or composed component, including purpose, variants, props, slots, states, accessibility behavior, responsive behavior, composition rules, acceptance criteria, and implementation boundaries before coding.
---

# Component Spec Writer

Use this skill before generating component code. Agents produce better components when the interface, states, and constraints are defined first.

## Process

1. Define the component purpose and where it appears.
2. Identify whether it is a primitive, composed feature component, layout component, or page-level pattern.
3. Define variants, sizes, visual states, interaction states, and data states.
4. Define props or inputs, including controlled/uncontrolled behavior if relevant.
5. Define slots/composition rules.
6. Define accessibility behavior: semantics, keyboard interaction, focus management, ARIA only when needed, target size, reduced motion.
7. Define responsive behavior and token usage expectations.
8. Write acceptance criteria for implementation and review.

## Output format

```markdown
## Component specification: [Name]

**Purpose:**

**Type:**

**Variants:**

**States:**

**Props / inputs:**

**Slots / composition:**

**Accessibility behavior:**

**Responsive behavior:**

**Design token requirements:**

**Acceptance criteria:**
```

## Guardrails

- Do not code until states and accessibility behavior are specified.
- Prefer composition over huge variant APIs.
- Use semantic design tokens instead of raw colors, spacing, fonts, or shadows.

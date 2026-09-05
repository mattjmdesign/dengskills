---
name: component
description: "Specify or revise a UI component\u2019s API, states, semantics, data ownership, and acceptance behavior. Use when defining props, variants, slots, keyboard behavior, or acceptance criteria before building a component."
---

# Component contract

Define the decisions a component owns. Inspect existing components and callers before proposing a duplicate or a universal abstraction.

## Work

- Name purpose, consumers, and ownership: product-agnostic primitive, domain component, or layout. Domain states belong near the feature even when reused across several screens.
- Define necessary inputs, events, controlled/uncontrolled behavior, defaults, and composition slots. Prefer explicit states over combinations of contradictory booleans.
- Specify reachable data and interaction states. Separate component behavior from server authorization and persistence responsibilities.
- Describe native semantics, accessible name, keyboard model, focus entry/return, and feedback. Follow the applicable platform pattern; not every control uses the same keys.
- Define content limits, wrapping, responsive behavior, supported themes, and token usage. Do not truncate essential status labels without an equivalent accessible path.
- For a revision, identify caller migrations and backward compatibility before changing the API.

## Deliver

A compact contract: **purpose/owner, API, meaningful states, interaction, resilience, acceptance**. Include types only when they resolve ambiguity. A simple badge does not need a full component RFC.

```markdown
## Component specification: [Name]

**Purpose:**
**Type:** primitive | feature | layout
**Used in:**
**Variants:**
**States:**
**Props:** inputs, events, defaults
**Accessibility:** semantics, keyboard, focus
**Tokens / responsive:**
**Acceptance:** [...]
```

Example: ProjectStatus composes a generic Badge but maps domain status to text in feature code. Its label conveys meaning independently of color; an unknown server value has an intentional fallback.

Verify behavior in its real parent, including long content and keyboard interaction. For implementation requests, build the component and run relevant checks. Use `$states` for gaps across a larger flow.

## Worked example

## Component specification: ProjectStatusBadge

**Purpose:** Show a project's lifecycle status next to its name in lists and headers.
**Type:** Primitive-level badge with domain variants; kept in primitives until two or more features need it.
**Used in:** ProjectList, ProjectDetailHeader
**Variants:** `status: active | paused | completed | archived`; `size: sm | md` (default md)
**States:** Default only; non-interactive with no hover action; label truncates with ellipsis below 320px, never wraps.
**Props:** `status` (required), `size?`, `className?`; label text derives from status; no arbitrary children slots.
**Accessibility:** Semantic `span`; status conveyed by text, color decorative; AA contrast for every pair in both themes.
**Tokens / responsive:** Uses `--color-success`, `--color-warning`, `--color-muted`, `--color-primary` pairs; no raw hex.
**Acceptance:** All four statuses render correct label and colors; passes contrast in both themes; holds layout in a 320px container.

## Boundaries

- Do not use when the product has no tokens yet — use `$tokens` first.
- Do not use when the component already exists — check `$system` inventories before duplicating.

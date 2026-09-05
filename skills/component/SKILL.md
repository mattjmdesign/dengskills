---
name: component
description: "Specify or revise a UI component\u2019s API, states, semantics, data ownership, and acceptance behavior."
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

Example: ProjectStatus composes a generic Badge but maps domain status to text in feature code. Its label conveys meaning independently of color; an unknown server value has an intentional fallback.

Verify behavior in its real parent, including long content and keyboard interaction. For implementation requests, build the component and run relevant checks. Use `$states` for gaps across a larger flow.

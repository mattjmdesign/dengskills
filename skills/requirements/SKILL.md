---
name: requirements
description: "Turn a brief or existing feature into testable behavior, quality constraints, and explicit data and permission contracts."
---

# Requirements

Write requirements about outcomes and observable behavior. Keep explicit user choices; do not replace their product with a preferred solution.

## Work

- Extract the user goal, initiating event, allowed actor, inputs, result, and failure behavior from the brief or running product.
- Give requirements stable IDs only when traceability helps. Prefer “An editor can rename a project; a viewer cannot” to legalistic filler.
- For each write, identify server authorization, validation, persistence, duplicate submission behavior, and what happens if the result is unknown after a timeout.
- Specify applicable quality constraints with conditions: target devices, input methods, content size, latency measurement, supported languages, privacy, and availability. Mark proposed targets as proposals.
- Name dependencies, unresolved contract questions, and excluded scope. Do not invent APIs or imply they exist.
- When revisiting implementation, report which requirements are met, changed, missing, or unverified, with evidence.

## Deliver

Use **requirement → acceptance example → dependency/unknown**. Add only enough examples to distinguish correct behavior from a plausible implementation.

Example: Given a viewer sends a rename request directly, the server rejects it and the stored name remains unchanged. Hiding the edit button alone does not satisfy this requirement.

Include a failure or boundary case for consequential behavior. “Accessible,” “fast,” and “secure” need scoped verification criteria. Use `$flow` when branch order is the open question; `$component` when a reusable interaction needs a contract.

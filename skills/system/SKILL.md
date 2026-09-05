---
name: system
description: "Audit or maintain existing tokens, components, and shared layouts; resolve drift with evidence and a migration path."
---

# Design system review

Keep a useful system coherent without treating every exception as a defect. Inspect actual consumers and documentation; rendered behavior outranks a naming preference.

## Work

- Locate token, primitive, feature-component, layout, and documentation sources. Inventory only the areas relevant to the request.
- Distinguish accidental drift from intentional differences in task, density, platform, or brand. A raw value or arbitrary utility is a review candidate, not a severity rating.
- Find duplicated behavior, inaccessible variants, missing theme pairs, unstable shared layouts, and undocumented ownership.
- Prioritize by user consequence and spread: a broken keyboard path outranks two inconsistent colors.
- For each change, decide reuse, extension, or new component; identify consumers and compatibility impact. Retire APIs only with a migration route.
- Update DESIGN.md or existing guidance when an authorized change creates a durable convention. Do not create a duplicate registry just to satisfy a template.

## Deliver

For audit: **finding → evidence → impact → suggested fix → verification**, with confirmed facts separated from hypotheses. For implementation: make scoped fixes, update consumers/docs, and recheck affected siblings.

Example: two dialog wrappers may legitimately differ in destructive confirmation behavior. Consolidate their shared focus and surface treatment without erasing the distinction.

Verify representative consumers across supported themes, sizes, and states. Do not claim visual improvement from source checks alone. Use `$tokens` for a missing token foundation and `$component` for one component's contract.

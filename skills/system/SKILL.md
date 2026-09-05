---
name: system
description: "Audit or maintain existing tokens, components, and shared layouts; resolve drift with evidence and a migration path. Use when auditing drift, deduplicating components, fixing theme or focus gaps, or updating DESIGN.md before new UI."
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

```markdown
## System review

**Sources:** token, component, layout, docs locations
**Maturity:** ...

### Drift issues
| Issue | Evidence | Impact | Fix | Verification |
|---|---|---|---|---|
|  |  |  |  |  |

### Priority fixes
1. ...

### Guardrails
- ...
```

Example: two dialog wrappers may legitimately differ in destructive confirmation behavior. Consolidate their shared focus and surface treatment without erasing the distinction.

Verify representative consumers across supported themes, sizes, and states. Do not claim visual improvement from source checks alone. Use `$tokens` for a missing token foundation and `$component` for one component's contract.

## Worked example

## System review

**Sources:** Tokens in `src/styles/globals.css`; components in `src/components/ui/`; no DESIGN.md yet.
**Maturity:** Evolving — tokens plus 40 components with no registry.

### Drift issues
| Issue | Evidence | Impact | Fix | Verification |
|---|---|---|---|---|
| Inline hex in feature code | `#3b82f6` twice in `features/reports` | Breaks theming | Replace with `--color-primary` | Render both themes; search for remaining hex |
| LegacyCard duplicates Card | Two callers | Divergent behavior | Deprecate LegacyCard with migration path | Update callers; confirm no visual regression |
| Page-specific gutters | `dashboard/settings` uses custom padding | Inconsistent rhythm | Use shell gutter `px-6` | Compare routes at fixed width |

### Priority fixes
1. Replace stray hex values
2. Deprecate LegacyCard
3. Align settings page gutters

### Guardrails
- Register new components in the inventory before merge; new tokens need light/dark pairs.

## Gotchas

- Inspect actual consumers and docs first; do not treat every exception as drift.
- Separate evidence from hypotheses; do not claim visual improvement from source checks alone.
- Prioritize by user consequence and spread; fix broken keyboard paths before minor color variance.
- Decide reuse, extension, or new component per change; do not silently rewrite or duplicate registries.
- Retire APIs only with a migration route; record durable conventions in existing guidance.

## Boundaries

- Do not use on a brand-new project with no UI yet — use `$tokens` instead.
- Do not use when the question is one component's behavior — use `$component` instead.

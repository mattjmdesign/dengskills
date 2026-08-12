---
name: ui-system-governance
description: Use this skill when a project already has UI work and needs its design system documented, maintained, or audited. Produces or updates DESIGN.md guidance, inventories tokens/components/layout shells, catches token drift and duplicate components, identifies missing states and responsive gaps, and proposes system-safe changes before new UI is added.
---

# UI System Governance

Use this skill once a UI system exists or starts evolving. Its job is to keep humans and agents aligned by documenting what exists, where it lives, what rules future UI must follow, and what inconsistencies need correction.

## Process

1. Locate existing design documentation: `DESIGN.md`, `AGENTS.md`, Storybook docs, component READMEs, Figma handoff notes, or design-system pages.
2. Inventory tokens: colors, typography, spacing, radius, shadows, motion, breakpoints, and theme overrides.
3. Inventory primitives, composites, organisms/feature sections, and layout shells. Note source paths, variants, sizes, and intended use.
4. Audit for token drift: inline hex values, hardcoded pixels, arbitrary Tailwind values, unmatched dark-mode colors, and component-specific one-off styles.
5. Audit for component drift: duplicate buttons/inputs/cards, variant explosion, wrappers that do not add behavior, and feature components placed in primitive folders.
6. Audit for layout drift: duplicate dashboard shells, inconsistent max widths, mismatched header/sidebar dimensions, and page-specific gutters.
7. Audit for quality gaps: missing loading/empty/error states, weak focus states, poor responsive behavior, inaccessible interactions, and missing reduced-motion handling.
8. Generate or update `DESIGN.md` with the current source of truth, rules for future additions, and a change log of system decisions.
9. Propose fixes in priority order. Do not silently rewrite the design system without explaining the impact.

## Output format

````markdown
## UI system governance report

**Documentation status:**
**System maturity:**
**Primary source of truth:**

### Token inventory
- [token group]: [location and notes]

### Component inventory
| Component | Layer | Location | Variants / states | Notes |
| --- | --- | --- | --- | --- |

### Layout shell inventory
- [shell]: [dimensions, routes, responsive behavior]

### Drift and consistency issues
| Issue | Severity | Evidence | Recommended fix |
| --- | --- | --- | --- |

### DESIGN.md update
```markdown
# Design System
...
```

### Priority fixes
1. [fix]

### Guardrails for future agents
- [rule]
````

## Worked example

## UI system governance report

**Documentation status:** No DESIGN.md exists
**System maturity:** Evolving — tokens + 40 components, no registry
**Primary source of truth:** `src/styles/globals.css` (tokens) + `src/components/ui/` (components)

### Token inventory
- Colors: complete semantic set; 2 stray hex values in feature code
- Typography: `--text-*` scale defined; 1 hardcoded `text-[15px]`
- Spacing: 4px scale in use; 3 arbitrary values

### Component inventory
| Component | Layer | Location | Variants / states | Notes |
| --- | --- | --- | --- | --- |
| Button | Primitive | components/ui/button | 4 variants, 3 sizes, loading | Matches spec |
| Badge | Primitive | components/ui/badge | 4 statuses | Missing empty-state guidance |
| LegacyCard | Primitive | components/ui/legacy-card | 2 variants | Duplicates Card — deprecate |

### Layout shell inventory
- DashboardLayout: 256px sidebar, 56px header; one page defines its own gutters (drift)

### Drift and consistency issues
| Issue | Severity | Evidence | Recommended fix |
| --- | --- | --- | --- |
| Inline hex in feature code | High | `#3b82f6` × 2 in features/reports | Replace with `--color-primary` |
| LegacyCard duplicates Card | Medium | 2 callers | Deprecate with migration path |
| Page-specific gutters | Low | dashboard/settings | Use shell gutter `px-6` |

### DESIGN.md update
(Concrete DESIGN.md content listing token groups, the component inventory, and usage rules.)

### Priority fixes
1. Replace stray hex values
2. Deprecate LegacyCard
3. Align settings page gutters

### Guardrails for future agents
- New components register in the inventory before merge; new tokens need light/dark pairs

## Common mistakes to prevent

- Do not treat documentation as a one-time setup file. It must change when tokens, components, or layout shells change.
- Do not add new components without updating the component inventory or usage guidance.
- Do not fix drift by introducing another abstraction that hides the inconsistency.
- Do not rename or remove tokens/components without noting migration impact.
- Do not let agents create visual exceptions without documenting the reason.

## Boundaries

- Do not use on a brand-new project with no UI yet — use `$ui-system-initializer`.
- Do not use when the question is one component's behaviour — use `$component-spec-writer`.

## Validate before final

- The report identifies the current token, component, and layout sources of truth.
- `DESIGN.md` guidance is concrete enough for the next agent to follow.
- Drift issues include evidence and recommended fixes, not vague criticism.
- Priority fixes distinguish urgent consistency problems from optional polish.
- Future additions have clear guardrails for when to reuse, extend, or add new primitives.

## See also

- [Design Engineering guide: Design System Governance](https://frontendguide.dev/docs/design-system-governance)

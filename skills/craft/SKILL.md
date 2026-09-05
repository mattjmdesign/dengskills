---
name: craft
description: "Build, improve, or audit interfaces through product-specific composition, responsive layout, interaction states, accessibility, and rendered verification. Use for visible UI work on web, mobile, or desktop. Use when repairing scanning on a dense screen, refining hierarchy before review, or auditing a flow for state and keyboard support."
---

# Craft Interfaces

Make an interface that helps a specific person do a specific job and feels deliberately designed. Strong work resolves composition, typography, behavior, and resilience together. More decoration or a larger diff is not proof of improvement.

## Choose the task

**Build** creates an interface. **Improve** changes existing work while preserving intent, useful behavior, brand, and explicit constraints. **Audit** returns findings; it does not authorize edits.

For each surface, choose **preserve**, **repair** a bounded defect, **refine** hierarchy and treatment, or **recompose** regions and reading order. Broad improvement includes high-value visual opportunities, not only bugs. Do not replace strong work to manufacture novelty.

Scale the process to the task. A button fix needs local evidence and a focused check; a site redesign needs coverage of its route families and shared regions. Do not turn every change into a scorecard or require new approval for work already authorized.

## Load guidance when needed

Paths are relative to this skill. Read only what changes the current decision:

| Decision | Reference |
| --- | --- |
| Composition, character, choosing an intervention | [Design authorship](references/design-authorship.md) |
| Type, spacing, color, density, tokens | [Foundations](references/foundations.md) |
| Grids, navigation, wrapping, scroll and route stability | [Responsive layout](references/responsive-layout.md) |
| Controls, forms, async states, feedback, copy | [Components and states](references/components-and-states.md) |
| Native apps, adaptive windows, platform input | [Platform adaptation](references/platform-adaptation.md) |
| Semantics, keyboard, focus, contrast, text scaling | [Accessibility](references/accessibility.md) |
| Generic composition or a final visual critique | [Visual quality](references/visual-quality.md) |
| Review evidence, acceptance, optional formal scorecards | [Review and verification](references/review-and-verification.md) |

For substantial visible work, start with authorship and foundations. Read accessibility before completing interactive UI, and responsive layout when structure changes. Load the formal scorecard schema only when producing a scorecard; its schema remains strict when used.

## Frame and compose

1. Inspect the brief, real content, routes, components, tokens, and rendered baseline. Identify the user, primary task, success condition, target platform, and constraints. Resolve facts from the workspace before asking questions.
2. Inventory the stated scope. For whole-product work, cover discoverable route families and shared regions; a representative record can verify a family but cannot silently exclude another. Keep a compact coverage note for multi-surface work.
3. State a short design direction: primary action, reading order, intended tone, and the compositional choice that expresses it. Choose a useful product-specific signature or deliberate restraint. Avoid borrowing a category template without a content reason.
4. If a primary surface needs a new composition, compare two materially different region maps or quick renders before committing. Compare order, proportions, density, focal point, and narrow-screen behavior, not merely fonts or colors. Small repairs do not need alternatives.
5. Rank information and actions; establish key alignments, widths, grouping, scroll ownership, and supported states. Define what should become visibly or behaviorally better.

Use real content early. Do not invent customers, metrics, testimonials, pricing, research, or capabilities. Missing media should produce an intentional text-led layout or a useful empty state. Do not expose drafts, personal data, or dormant fields merely because code can access them.

## Implement and interrogate

Work from task blockers and inaccessible behavior through structure, responsive behavior, state recovery, and visual craft. Continue through the requested visual improvement; technical cleanup alone does not satisfy it.

- Reuse sound primitives and token roles. Check consumers before changing shared components.
- Group with proximity and alignment before adding containers. Let page families differ when their jobs differ.
- Keep DOM, reading, and focus order aligned. Use semantic controls with names, visible focus, and non-hover access.
- Let real content determine wrapping and topology. Do not hide page overflow or truncate essential information to disguise a sizing defect.
- Model loading, empty, error, success, permission, and interrupted-write states when reachable. A pending response is not proof of a failed write; recovery must respect the server contract.
- Verify supported themes and actual color pairs. A semantic token name does not guarantee contrast.
- Add motion for orientation or feedback; preserve reduced-motion alternatives and immediate access to content.

For substantial builds, refinements, and recompositions, capture the rendered result, critique it, and revise the highest-value residual issue. Inspect first at thumbnail scale for balance and hierarchy, then actual size for reading and operation, then fine detail for alignment, wrapping, and state transitions. Compare with the baseline; do not force churn when the result is already strong.

## Verify the result

Use a local or designated test environment and safe fixtures. Test the critical task with the relevant input methods, narrow/intermediate/wide sizes, supported themes, long content, and text enlargement. Check focus, contrast, target size, reduced motion, local scroll regions, and recovery.

For changing routes or overlays, compare persistent anchors at the same viewport. A full reload is not evidence of stable client routing: confirm the runtime is attached and the transition stays in the same document. Record actual geometry or observed movement, not only a CLS score. Recheck affected sibling surfaces after shared fixes.

Tools support judgment:

```bash
python3 scripts/ui_source_audit.py /path/to/project --format markdown
python3 scripts/analyze_layout_stability.py stability.json --format markdown
```

Run these from the skill directory, or resolve their absolute paths. The source scanner reports candidates, not confirmed defects; the stability helper validates supplied measurements and cannot capture them. For a requested formal audit, read the schema reference and use `scripts/score_ui_audit.py`; never fabricate evidence to satisfy it.

Do not perform real payments, messages, deletions, publication, or permission changes merely to test UI. Follow the user's existing scope and authorization.

## Report with evidence

Lead with the material result. For implementation, state visible decisions, behavior/system changes, scope covered, rendered checks, and remaining gaps. Link a coverage artifact when detail would swamp the answer. For audits, use **observation → evidence → user impact → cause → fix → verification**, ordered by consequence; keep severity separate from confidence.

Completion requires the intended task to work, the requested visual improvement to be visible, and the relevant resilience/interaction checks to pass. Mark blocked or unverified areas explicitly. Source inspection, a successful build, or a numerical score alone cannot establish visual quality or accessibility conformance.

## Worked example

Repair scanning on a day-scheduling screen: technicians missed reassigned shifts in a 40-row list. Left-align start times in a fixed-width slot, place the change badge above the assignment title, keep row actions in a fixed trailing slot, and preserve DOM and focus order. Check narrow/wide renders, keyboard traversal, and text enlargement. Remaining gap: filter no-results copy still needs operations approval.

## Gotchas

- Verify actual foreground/background pairs; a semantic token name does not guarantee contrast.
- Treat a pending response as unconfirmed; it is not proof of a failed write — respect the server contract on retry.
- Confirm stable client routing by checking the runtime stays attached in the same document; a full reload is not evidence.
- Do not hide page overflow or truncate essential content to disguise a sizing defect.
- Keep DOM, reading, and focus order aligned; do not reorder visually without reordering semantically.
- Treat scanner output as candidates, not confirmed defects; do not fabricate evidence to satisfy a scorecard.

## Boundaries

- Do not use when the question is page shells, reading order, or responsive structure only — use `$layout` instead.
- Do not use when the question is token roles or theme pairs only — use `$tokens` instead.
- Do not use when the question is one component API or contract only — use `$component` instead.
- Do not use when the question is missing-state coverage only — use `$states` instead.

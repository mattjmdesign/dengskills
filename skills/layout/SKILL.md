---
name: layout
description: "Design or revisit page shells, reading order, responsive structure, and scroll ownership using real content. Use when planning landing, dashboard, auth, or docs shells, or when responsive behavior and scroll ownership diverge."
---

# Layout

Choose the structure that serves the user's task. Inventory actual routes, shared regions, tokens, and primitives before creating a new shell.

## Work

- Name the primary task and rank its content. Separate reading surfaces, comparison surfaces, and workspaces instead of applying one dashboard template everywhere.
- Map regions in DOM/reading order, key alignments, width limits, and scroll ownership. Identify what persists across routes.
- Choose whether to preserve, repair, refine, or recompose the existing layout. A broad improvement request permits meaningful restructuring while preserving product constraints.
- Define narrow-screen changes by content pressure: what wraps, stacks, moves into a drawer, or remains scrollable. Keep essential actions and data accessible.
- Use intrinsic sizing, shrinkable grid/flex children, and local overflow for wide data. Do not hide page overflow to conceal a sizing defect.
- Reuse primitives and shared dimensions. Add a shell only when it owns a real repeated relationship.

## Deliver

A region map or implementation with responsive behavior, shared ownership, and acceptance checks. Do not invent testimonials, metrics, or pricing to fill a section skeleton.

```markdown
## Layout plan

**Surface:**
**Shells:**
**Regions in reading order:**
**Shared dimensions:**
**Responsive behavior:**
**Acceptance checks:**
```

Test real long labels, sparse and dense content, narrow/intermediate/wide sizes, and text enlargement. At a fixed width, compare short and long routes and open overlays for movement of persistent regions.

A planning request needs a clear structure; a build request needs a rendered result. Use `$craft` when composition, typography, and visual character also need development. It is not required for a small sizing repair.

## Worked example

## Layout plan

**Surface:** Dashboard plus public site; detected primitives reused, no new shell library
**Shells:** Detected marketing, dashboard, and auth preserved; no new shell added
**Regions in reading order:** Dashboard: nav → header → main; marketing: nav → hero → proof → features → footer; auth: centered card with no chrome
**Shared dimensions:** Reuse detected shell tokens; limits set from actual table width and longest labels
**Responsive behavior:** Nav becomes drawer at narrow widths from content pressure; sections stack; tables scroll locally with shrinkable cells
**Acceptance checks:** Long labels wrap without breaking headers; empty and error states hold shell size; persistent regions do not shift when overlays open

## Gotchas

- Inventory real routes, tokens, and primitives first; do not create a new shell without a repeated relationship.
- Derive limits from actual content; do not hardcode shared dimensions in multiple places.
- Map regions in reading order with scroll ownership; do not hide page overflow to conceal a sizing defect.
- Define narrow-screen behavior by content pressure; do not apply one template to reading, comparison, and workspace surfaces.
- Use real labels and empty/loading/error states for checks; do not invent testimonials or metrics to fill sections.

## Boundaries

- Do not use when per-page content priority is undecided — use `$hierarchy` for key pages first.
- Do not use when no token or library decision exists — use `$tokens` or the existing-library audit first.

---
name: layout
description: "Design or revisit page shells, reading order, responsive structure, and scroll ownership using real content."
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

Test real long labels, sparse and dense content, narrow/intermediate/wide sizes, and text enlargement. At a fixed width, compare short and long routes and open overlays for movement of persistent regions.

A planning request needs a clear structure; a build request needs a rendered result. Use `$craft` when composition, typography, and visual character also need development. It is not required for a small sizing repair.

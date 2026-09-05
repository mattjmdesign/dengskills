---
name: git
description: "Plan or refine Git collaboration, reviewable changes, worktrees, and dependency-update ownership."
---

# Git workflow

Keep concurrent work understandable and the integration branch usable. Read the repository's branch and release policy before proposing another.

## Work

- Identify contributors, active edits, integration/deploy branches, CI, and preview environments. Do not assume a long-lived dev branch is required.
- Prefer short-lived changes organized around a reviewable user outcome. Visual, behavior, and data changes may belong together when separating them obscures correctness.
- Use worktrees for independent edits or side-by-side comparisons when helpful. Shared ownership notes are coordination aids, not actual file locks.
- State who owns shared files such as tokens, schemas, manifests, and lockfiles during parallel work. Preserve unrelated changes.
- Update lockfiles with the package manager for authorized dependency changes. Resolve competing dependency edits by reconciling manifests and regenerating, not hand-splicing dependency hashes.
- Follow the established commit, branch, merge, and approval rules. Do not invent blanket prohibitions on rebase or require approval for every local edit.

## Deliver

A compact plan naming base branch, change boundaries, shared-file ownership, checks, preview/review path, and integration order. Do not execute pushes, merges, or branch deletion merely because a planning request mentions them.

For a redesign, a shared token change may affect every route: review its consumers together before splitting page-specific work. A small feature may be clearest as one vertical slice.

Validate that the plan preserves others' work and lets a reviewer reproduce the relevant behavior. Use `$context` only if the resulting conventions need durable documentation.

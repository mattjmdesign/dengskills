---
name: git
description: "Plan or refine Git collaboration, reviewable changes, worktrees, and dependency-update ownership. Use when planning branches, slicing reviewable PRs, coordinating parallel agents, or assigning lockfile ownership."
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

```markdown
## Git workflow plan

**Base / integration branches:**
**Change boundaries:**
**Shared-file ownership:**
**Checks:**
**Preview / review path:**
**Integration order:**
```

For a redesign, a shared token change may affect every route: review its consumers together before splitting page-specific work. A small feature may be clearest as one vertical slice.

Validate that the plan preserves others' work and lets a reviewer reproduce the relevant behavior. Use `$context` only if the resulting conventions need durable documentation.

## Worked example

## Git workflow plan

**Base / integration branches:** Detected from repo policy; preserved, no new long-lived branch proposed
**Change boundaries:** Token change separate from behavior/data; small demoable work ships as one short-lived change
**Shared-file ownership:** Design lead owns tokens during redesign; each agent states scope in review; regenerate lockfile via package manager
**Checks:** Detected lint plus smoke on touched flow
**Preview / review path:** Per-change preview; merge after human review; integration branch stays deployable
**Integration order:** Shared token change first with consumer review, then page-specific work

## Gotchas

- Read the repo branch and release policy first; do not assume a long-lived dev branch is required.
- Prefer short-lived changes around reviewable outcomes; do not prescribe fixed branch names.
- Plan only; do not push, merge, or delete branches on a planning request.
- Update lockfiles through the package manager; do not hand-edit hashes.
- State shared-file ownership explicitly; do not treat coordination notes as file locks.
- Follow established merge and approval rules; do not invent blanket rebase or approval bans.

## Boundaries

- Do not use for a solo throwaway prototype — keep git trivial with no branch or review policy.
- Do not use to write context-file content — use `$context` for AGENTS.md or CLAUDE.md.

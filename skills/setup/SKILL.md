---
name: setup
description: "Plan or improve a repository foundation: ownership, commands, configuration, tokens, and a runnable first slice. Use when starting a repository, when fresh checkout install or env setup fails, or when feature ownership is unclear."
---

# Project setup

Make the next feature easy to locate, run, and verify. Inspect the repository, manifests, lockfile, and local instructions first. Improve existing conventions before introducing new ones.

## Work

- Confirm runtime, package manager, framework, deploy target, and actual commands. Distinguish existing tooling from proposed additions.
- Place route composition, feature logic, reusable primitives, validation, and data access near their owners. Do not create empty folders for hypothetical scale.
- Choose one token source and identify how primitives consume it. Reuse an existing UI library; a new repository does not require a custom Button.
- Document environment variable names and safe placeholders. Keep secret validation and access server-side; never import a secret-bearing environment object into browser code.
- Set the smallest useful verification path: types/lint/build and a meaningful check of the first critical flow. Add infrastructure when it addresses a concrete risk.
- On existing projects, preserve user edits and change only the foundation implicated by the task. Explain migration effects on consumers.

## Deliver

For planning, give actual/proposed paths, commands, and an ordered setup sequence. For implementation, create the authorized foundation and run its checks rather than stopping at a checklist.

```markdown
## Foundation plan

**Stack assumption:**
**Package manager:**
**Deploy target:**
**Structure:** actual/proposed paths
**Commands:** install, dev, check, test
**Env:** names + placeholders + validation
**Tokens / data / checks:** locations and commands

### Setup sequence
1. ...
2. ...
```

A usable result lets a fresh checkout install reproducibly, run a slice, and locate tokens, data access, and verification commands. Update the package-manager lockfile through the package manager when dependencies change.

Use `$context` to record durable repository facts and `$git` for collaboration policy when those are needed.

## Worked example

## Foundation plan

**Stack assumption:** Detected Vue 3 + Vite from manifest; preserved
**Package manager:** Detected npm from lockfile; preserved
**Deploy target:** Detected host from repo config; preserved
**Structure:** `app/` routes; `ui/` primitives; `features/` per feature; `lib/` data and validation; existing token file preserved
**Commands:** Detected install, dev, check, test from manifest; no new tooling added
**Env:** `.env.example` checked in; server-side validation module; secrets stay server-side
**Tokens / data / checks:** Reuse detected token file; data in `lib/data/`; detected check before PRs

### Setup sequence
1. Record detected stack and commands
2. Repair missing env example
3. Reuse token source
4. Build first slice + check
5. Record facts with `$context`

## Gotchas

- Repair the detected foundation; do not propose a new stack when the task is foundation repair.
- Verify runtime, package manager, and commands from manifests and lockfiles; do not invent tooling.
- Preserve existing conventions and user edits; change only the implicated foundation.
- Place code near its owner; do not create empty folders for hypothetical scale.
- Keep secrets server-side; do not import secret-bearing env objects into browser code.
- Reuse one token source and existing primitives; do not add a second system without need.

## Boundaries

- Do not use to choose the framework — use `$stack` first.
- Do not use to audit UI drift or duplicate components — use `$system` for that review.

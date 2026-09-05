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

**Stack assumption:** Next.js App Router, TypeScript, Tailwind v4
**Package manager:** pnpm
**Deploy target:** Vercel
**Structure:** `src/app/` routes; `src/components/ui/` primitives; `src/components/features/` per feature; `src/lib/` data and validation; `src/styles/globals.css` tokens
**Commands:** `pnpm install`, `pnpm dev`, `pnpm check` (Biome), `pnpm test` (Vitest)
**Env:** `.env.example` checked in; `env.ts` validates with zod at startup; secrets stay server-side
**Tokens / data / checks:** Tokens in `src/styles/globals.css`; data hooks in `src/lib/data/`; `pnpm check` before PRs

### Setup sequence
1. Scaffold app + layout
2. Add Biome + strict TS
3. Add env example + validation
4. Create token globals
5. Build first primitive + test
6. Record facts with `$context`

## Boundaries

- Do not use to choose the framework — use `$stack` first.
- Do not use to audit UI drift or duplicate components — use `$system` for that review.

---
name: context
description: "Create or revise repository instructions using verified commands, paths, architecture constraints, and review expectations. Use when creating AGENTS.md or CLAUDE.md, when agents invent commands or paths, or when instructions drift stale."
---

# Agent context

Record what an agent would otherwise guess incorrectly. Read existing context files and their scope before editing; keep one authoritative home for each rule.

## Work

- Verify project purpose, commands, runtime, paths, and architecture from the workspace. Never invent a test command or an existing component.
- Capture consequential boundaries: where secrets and authorization live, who owns cached data, token/component sources, and generated files.
- Include the actual checks and observable evidence expected for the work. Distinguish lint/build from rendered or behavioral verification.
- Separate durable conventions from task-specific plans. Link focused supporting docs instead of embedding complete manuals.
- Reconcile contradictions and stale instructions, including blanket lockfile bans, duplicate formatting stacks, and obsolete paths. Preserve explicit user policies unless asked to change them.
- Match the client and file format already in use. If adding client-specific discovery rules, verify current client documentation; do not claim every client loads every filename.

## Deliver

Update the requested file, or provide a ready-to-use draft when edits were not requested. Usually include purpose, commands, important paths, non-obvious constraints, and verification. Omit empty sections and generic coding advice.

```markdown
# AGENTS.md

## Project
## Commands
## App structure
## Architecture rules
## Styling and design system
## Accessibility
## Testing and validation
## Git workflow
## Agent guardrails
```

Example: “Tokens live in app/globals.css. Docs styles consume them in app/docs-theme.css. Run pnpm build to validate MDX routes.” This is more useful than “write clean code.”

Check every referenced local command and path; label external or future dependencies. The file guides authorized work, not permission to publish or expand a task.

## Worked example

# AGENTS.md

## Project
Next.js 16 App Router dashboard for a construction scheduling client. pnpm.

## Commands
- `pnpm dev` — local dev server
- `pnpm check` — Biome lint + format
- `pnpm test` — Vitest

## App structure
- `src/app/` routes; `src/components/ui/` primitives; `src/components/features/` feature components

## Architecture rules
- Server components by default; `use client` only at leaves
- Data fetching via TanStack Query hooks in `src/lib/data/`

## Styling and design system
- Tokens only from `src/styles/globals.css`; no inline hex or arbitrary values
- Components from `src/components/ui/`; no new primitives without review

## Accessibility
- WCAG 2.2 AA; visible focus ring on all interactive elements; 44px touch targets

## Testing and validation
- Component tests for primitives; Playwright smoke for critical flows; `pnpm check` before PRs

## Git workflow
- `feat/*` branches from `dev`; squash merge after human review

## Agent guardrails
- Ask before refactoring; never edit `pnpm-lock.yaml`; state assumptions in the PR description

## Gotchas

- Verify every command and path in the workspace; do not invent commands or components.
- Keep one authoritative home per rule; do not duplicate guidance across files.
- Record durable conventions only; do not embed task plans or full manuals.
- Mark unknowns as assumptions; do not present unverified tooling as fact.
- Match the client and file format in use; do not claim every client loads every filename.

## Boundaries

- Do not use when repository conventions do not exist yet — use `$setup` first to establish structure, commands, and env strategy.
- Do not invent validation commands or paths; mark unknowns as assumptions to confirm.

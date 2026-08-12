---
name: agent-context-file-planner
description: Use this skill when creating or improving AGENTS.md, CLAUDE.md, .cursorrules, or other project context files for AI coding agents. Captures project purpose, commands, stack, architecture rules, server/client boundaries, styling and design-token rules, accessibility, testing, git workflow, validation commands, and agent guardrails.
---

# Agent Context File Planner

Use this skill to create context that improves every future agent task. Include only instructions an agent would otherwise guess incorrectly.

## Process

1. Inspect or ask for project purpose, stack, folder structure, package manager, styling system, testing tools, and deployment target.
2. Capture commands the agent should run for development, checks, tests, and builds.
3. Capture architecture rules: server/client boundaries, data fetching, routing, state, file ownership.
4. Capture design-system rules: token usage, component library, variants, and no hardcoded visual values.
5. Capture accessibility, quality, and testing expectations.
6. Capture git workflow and PR expectations.
7. Add agent-specific guardrails: scope control, when to ask, no broad refactors, and validation before completion.

## Output format

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
- Server components by default; "use client" only at leaves
- Data fetching via TanStack Query hooks in `src/lib/data/`

## Styling and design system
- Tokens only from `src/styles/globals.css`; no inline hex or arbitrary values
- Components from `src/components/ui/`; no new primitives without review

## Accessibility
- WCAG 2.2 AA; visible focus ring on all interactive elements; 44px touch targets

## Testing and validation
- Component tests for primitives; Playwright smoke for critical flows; `pnpm check` before PRs

## Git workflow
- feat/* branches from dev; squash merge after human review

## Agent guardrails
- Ask before refactoring; never edit pnpm-lock.yaml; state assumptions in PR description

## Common mistakes to prevent

- Do not fill the file with generic advice.
- Do not omit design token rules; agents often hardcode colors, spacing, and shadows.
- Do not list validation commands unless they are known or explicitly assumed.
- Do not let the context file authorize broad edits by default.

## Boundaries

- Do not use when repo conventions do not exist yet — run `$project-foundation-planner` first.
- Do not invent validation commands; mark unknown commands as assumptions.

## Validate before final

- The output is ready to paste into a root context file.
- It names concrete commands, folders, and constraints when available.
- Unknowns are marked as assumptions or questions.

## See also

- [Design Engineering guide: Project Context Files](https://frontendguide.dev/docs/project-context-files)

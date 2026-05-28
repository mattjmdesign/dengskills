---
name: agent-context-file-planner
description: Plan or draft project context files for AI coding agents, including AGENTS.md, CLAUDE.md, .cursorrules, or similar repo instructions. Use when making a codebase agent-friendly by documenting stack, architecture rules, design-system constraints, accessibility requirements, testing standards, git workflow, and agent do-not-do rules.
---

# Agent Context File Planner

Use this skill to create context that improves every future agent task in a repository. The file should tell agents what they would otherwise guess incorrectly.

## Process

1. Inspect or ask for the project stack, app purpose, folder structure, package manager, styling system, testing tools, and deployment target.
2. Capture architecture rules: server/client boundaries, data fetching, routing, state management, and file ownership.
3. Capture design-system rules: token usage, component library, variant patterns, and no hardcoded visual values.
4. Capture accessibility and quality requirements.
5. Capture git workflow and PR expectations.
6. Add agent-specific guardrails: files to avoid, when to ask, validation commands, and no broad refactors unless requested.
7. Output a ready-to-save context file.

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

## Guardrails

- Keep instructions concrete and project-specific.
- Do not include generic advice the agent already knows.
- Include validation commands only if they are known or provided.
- Prefer constraints that prevent common agent failures: hardcoded tokens, unnecessary client components, broad edits, skipped states, and untested changes.

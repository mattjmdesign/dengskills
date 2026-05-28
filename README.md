# Design Engineering Agent Skills

Installable Agent Skills for product designers, design engineers, and AI-assisted teams moving from vibe-coded ideas to product-grade prototypes.

These skills are intentionally narrow. Each one guides an agent through one design-engineering process moment: clarifying intent, choosing fidelity, planning a repo, mapping IA, writing requirements, specifying components, or inventorying gap states.

The skill structure follows the official Agent Skills guidance copied in `agentskillsofficial/`: concise `SKILL.md` files, specific trigger descriptions, procedural instructions, output templates, common mistakes, validation checks, `agents/openai.yaml` metadata, and lightweight eval cases.

## Skill Pack

| Skill | Use when... |
|---|---|
| `product-intent-clarifier` | A product/client idea is still vague. |
| `prototype-fidelity-selector` | You need to decide how much fidelity to build. |
| `framework-fit-advisor` | You need to choose Next.js, Nuxt, Vite, or another path. |
| `project-foundation-planner` | You are setting up repo structure and tooling. |
| `git-workflow-planner` | Humans and agents need a safe branch/PR workflow. |
| `agent-context-file-planner` | You need AGENTS.md, CLAUDE.md, or .cursorrules. |
| `requirements-from-brief` | A brief needs testable functional/non-functional requirements. |
| `sitemap-planner` | You need IA, routes, navigation, and page hierarchy. |
| `user-flow-mapper` | You need happy paths and edge-case branches. |
| `content-hierarchy-planner` | You need to prioritize content and actions on a page. |
| `component-spec-writer` | You need component variants, props, states, and a11y before code. |
| `gap-state-inventory` | You need missing loading, empty, error, permission, and edge states. |

## Repository Layout

```txt
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    evals/evals.json
agentskillsofficial/
  Official Agent Skills reference docs copied for local authoring.
```

## Installation

Copy any folder under `skills/` into your agent's skill directory, such as `.agents/skills/` in a project or `~/.codex/skills/` for local Codex use.

```bash
cp -R skills/gap-state-inventory ~/.codex/skills/
```

## Philosophy

These skills make an AI coding agent pause at the right product-to-production step instead of jumping straight to implementation. They encode the Design Engineering workflow: clarify intent, choose fidelity, map the system, plan the implementation, then build and review with product-grade quality gates.

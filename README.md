# Design Engineering Skills

Give your AI assistant product-to-production judgement for building product-grade prototypes — not just vibe-coded screens.

Design Engineering Skills help coding agents pause at the right moment in the workflow: clarify product intent, choose the right prototype fidelity, plan the repo, map IA and flows, write requirements, specify components, and inventory missing states before code is generated.

## Install

Install the full skill pack with the skills CLI:

```bash
npx skills add mattjmdesign/dengskills
```

Once installed, your AI assistant can automatically load the relevant skill when a task matches one of the design-engineering moments below.

You can also browse the repository on skills.sh after the repo has been indexed by the telemetry service:

```text
https://skills.sh/mattjmdesign/dengskills
```

## What this is for

This skill pack is for product designers, design engineers, and AI-assisted teams who want to move from a rough idea or client request to a product-grade prototype with a professional workflow.

Use it when you want an agent to help with:

- clarifying a product or feature before implementation
- choosing the right framework or prototype fidelity
- setting up a repo that will not collapse under vibe-coded changes
- mapping sitemap, routes, user flows, and page hierarchy
- writing frontend requirements and acceptance-ready specs
- preparing components and gap states before UI code is generated
- initializing design systems, layout skeletons, and UI governance before feature work expands

## Skills

### Product Definition

Skills for turning vague product ideas into buildable direction.

| Skill | Use when... |
|---|---|
| `product-intent-clarifier` | A product/client idea is still vague. |
| `prototype-fidelity-selector` | You need to decide whether to sketch, wireframe, mock up, code prototype, or build near-production. |
| `requirements-from-brief` | A brief needs testable functional and non-functional frontend requirements. |

### Project Setup

Skills for choosing the technical path and collaboration model.

| Skill | Use when... |
|---|---|
| `framework-fit-advisor` | You need to choose Next.js, Nuxt, React + Vite, or another frontend path from product constraints. |
| `project-foundation-planner` | You are setting up repo structure, tooling, TypeScript, env, tokens, and tests. |
| `git-workflow-planner` | Humans and agents need a safe branch, PR, worktree, and review workflow. |
| `agent-context-file-planner` | You need `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar agent instructions. |


### UI Composition

Skills for setting up the visual system and page skeleton before agents build features.

| Skill | Use when... |
|---|---|
| `ui-system-initializer` | A new codebase or Figma file needs tokens, typography, spacing, radius, shadows, and light/dark mode before UI work starts. |
| `ui-layout-architect` | You need to plan layout shells, max widths, section rhythm, dashboard/sidebar dimensions, auth layouts, or whether to use shadcn/ui, Radix, Base UI, or custom primitives. |
| `ui-system-governance` | An existing project needs DESIGN.md, token/component/layout inventories, drift audits, or guardrails before more UI is added. |

### IA & Flows

Skills for mapping the product before visual design or implementation.

| Skill | Use when... |
|---|---|
| `sitemap-planner` | You need pages, routes, navigation, auth boundaries, and URL conventions. |
| `user-flow-mapper` | You need happy paths, failure branches, permission paths, and data touchpoints. |
| `content-hierarchy-planner` | You need to prioritize page content, actions, headings, and responsive order. |

### Build Readiness

Skills for preparing implementation so the agent does not guess the product shape.

| Skill | Use when... |
|---|---|
| `component-spec-writer` | You need component purpose, variants, states, props, accessibility, and acceptance criteria before code. |
| `gap-state-inventory` | You need missing loading, empty, error, offline, permission, expired-session, validation, and mutation states. |

## Example prompts

```text
Use $product-intent-clarifier to turn this rough app idea into a buildable product intent brief.
```

```text
Use $framework-fit-advisor to choose the right frontend framework for this client dashboard.
```

```text
Use $user-flow-mapper to map onboarding, including validation errors, API failures, and cancellation paths.
```

```text
Use $gap-state-inventory to identify missing states before we let an agent build this screen.
```

## Repository layout

```txt
skills.sh.json
LICENSE
README.md
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    evals/evals.json
```

`skills.sh.json` groups the skills on the skills.sh repository page. It does not change how the CLI installs skills or change the contents of any `SKILL.md` file.

## Local authoring notes

The official Agent Skills docs may be kept locally in `agentskillsofficial/` for reference while authoring, but that folder is intentionally ignored and not published in this repository.

## License

MIT © 2026 Matt J.M. Design

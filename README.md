# Design Engineering Skills

Give your AI assistant product-to-production judgement for building product-grade prototypes — not just vibe-coded screens.

Design Engineering Skills help coding agents pause at the right moment: clarify intent, choose fidelity, plan the repo, map flows, specify components, inventory missing states — and review a running slice when the first idea may have drifted.

The pack pairs with the [Design Engineering guide](https://frontendguide.dev/docs) — every skill is the executable form of a guide page, and the guide links back to its skill.

## Scope

This pack covers Product Definition through Build Readiness, plus `$production-readiness-review` after a preview exists. Testing strategy, deployment pipelines, and observability remain guide-only. Skills are for starting work *and* for revisiting work that already exists.

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

## Agent Plugins packaging

This repository is also a valid [Agent Plugins](https://agent-plugins.org/) package (v1.0.0 format). The root `plugin.json` is the portable manifest and `skills/` is the standard fixed location for Agent Skills — so any client that supports Agent Plugins can load this repo as a plugin directly, no skills CLI required.

The two formats share one source of truth: every `SKILL.md` conforms to the [Agent Skills specification](https://agentskills.io/specification). The skills.sh-specific files (`skills.sh.json` groupings, `agents/openai.yaml` client config, `evals/evals.json` test cases) live alongside the portable core and are ignored by Agent Plugins clients.

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

### QA & Delivery

Skills for interrogating a running slice.

| Skill | Use when... |
|---|---|
| `production-readiness-review` | A preview might be treated as a product. Score demo vs pilot vs production and list UI-owned risks. |

## Choosing the right skill

Several skills trigger on overlapping moments. Use this routing table when the right skill is unclear:

| If you need... | Use | Before/after... |
|---|---|---|
| The product is still vague — users, promise, workflow unknown | `product-intent-clarifier` | Always first. Do not start IA, design, or code while this is unresolved. |
| A clear idea, but you are unsure how polished to make it | `prototype-fidelity-selector` | After intent is clarified. Do not pick fidelity before knowing the validation question. |
| Agreed direction that needs testable requirements | `requirements-from-brief` | After intent + fidelity. Requirements say *what*, not which component. |
| A framework/stack decision | `framework-fit-advisor` | After requirements or alongside them, before repo setup. |
| Repo conventions before many files exist | `project-foundation-planner` | After the framework decision. |
| A safe human + agent git collaboration model | `git-workflow-planner` | With or after project foundation. |
| AGENTS.md / CLAUDE.md / cursor rules | `agent-context-file-planner` | After the repo conventions are known. |
| Pages, routes, navigation | `sitemap-planner` | After requirements; before visual design. |
| How a user completes one task, with failure branches | `user-flow-mapper` | With or after the sitemap. |
| What belongs on one page, ranked | `content-hierarchy-planner` | After the sitemap, before layout design. |
| Tokens/typography/light-dark for a new codebase | `ui-system-initializer` | Before components exist. Audit first if a system already exists. |
| Layout shells and page skeleton for an existing project | `ui-layout-architect` | After the UI system exists or the library decision is made. |
| Design-system documentation, drift audits, guardrails | `ui-system-governance` | Recurring — before larger PRs or after new UI additions. |
| A component definition before code | `component-spec-writer` | After tokens and primitives are established. |
| Missing loading/empty/error/edge states | `gap-state-inventory` | After component specs, before code generation, or on a live preview. |
| A slice that “looks done” | `production-readiness-review` | After a preview exists. Do not raise honesty level because the UI is pretty. |

The only fixed rule: skills whose output depends on another skill's output run after it. Within a phase there is no linear chain — but human review should gate every handoff between phases.

## Guide pairing

Each skill is the executable form of a page in the [Design Engineering guide](https://frontendguide.dev/docs):

| Skill | Guide page |
|---|---|
| `product-intent-clarifier` | Product Designer First |
| `prototype-fidelity-selector` | Prototyping & Validation |
| `requirements-from-brief` | Requirements Analysis |
| `framework-fit-advisor` | Tech Decisions |
| `project-foundation-planner` | Project Setup |
| `git-workflow-planner` | Collaborative Repository Workflow |
| `agent-context-file-planner` | Project Context Files |
| `ui-system-initializer` | Design System |
| `ui-layout-architect` | Layout Patterns & Scale |
| `ui-system-governance` | Design System Governance |
| `sitemap-planner` / `user-flow-mapper` | Information Architecture |
| `content-hierarchy-planner` | Layout Patterns & Scale |
| `component-spec-writer` | Component Architecture |
| `gap-state-inventory` | Error Handling |
| `production-readiness-review` | Production Risks the UI Owns |

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
plugin.json
LICENSE
README.md
CHANGELOG.md
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    evals/evals.json
```

`skills.sh.json` groups the skills on the skills.sh repository page. It does not change how the CLI installs skills or change the contents of any `SKILL.md` file. `plugin.json` is the Agent Plugins manifest — the portable package layer that any Agent Plugins-compatible client can load. `CHANGELOG.md` records pack versions; bump it whenever a skill's behaviour, triggers, or examples change.

## Local authoring notes

The official Agent Skills docs may be kept locally in `agentskillsofficial/` for reference while authoring, but that folder is intentionally ignored and not published in this repository.

## License

MIT © 2026 Matt J.M. Design

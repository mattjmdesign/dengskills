# Design Engineering Skills

Give your AI assistant product-to-production judgement for building product-grade prototypes — not just vibe-coded screens.

Design Engineering Skills help coding agents pause at the right moment: clarify intent, choose fidelity, plan the repo, map flows, specify components, inventory missing states — and review a running slice when the first idea may have drifted.

The pack pairs with the [Design Engineering guide](https://frontendguide.dev/docs) — every skill is the executable form of a guide page, and the guide links back to its skill.

## Scope

This pack covers Product Definition through Build Readiness, plus `$production-readiness-review` after a preview exists. Testing strategy, deployment pipelines, and observability remain guide-only. Skills are for starting work *and* for revisiting work that already exists.

## Install

The skills themselves are client-agnostic — every `SKILL.md` conforms to the [Agent Skills specification](https://agentskills.io/specification), and `skills/` is the standard fixed location. Only the packaging differs per client.

### Any agent (skills CLI)

```bash
npx skills add mattjmdesign/dengskills
```

Installs into whichever agent directories the CLI detects. Once installed, your assistant can load the relevant skill when a task matches one of the design-engineering moments below.

You can also browse the repository on skills.sh after the repo has been indexed by the telemetry service:

```text
https://skills.sh/mattjmdesign/dengskills
```

### Agent Plugins clients

The root `plugin.json` is an [Agent Plugins](https://agent-plugins.org/) v1.0.0 manifest, so any compatible client can load this repo as a plugin directly — point it at the repository, no CLI required.

### Claude Code

Claude Code uses its own manifest location, so it installs through this repository's own plugin marketplace:

```bash
claude plugin marketplace add mattjmdesign/dengskills
```

```bash
claude plugin install dengskills@dengskills
```

Or from inside Claude Code, `/plugin marketplace add mattjmdesign/dengskills` followed by `/plugin install dengskills@dengskills`.

Installed this way the skills are namespaced (`dengskills:sitemap-planner`) and load automatically when a task matches. Verify with `claude plugin details dengskills`.

Pick one method, not both. If you previously ran `npx skills add`, remove those copies before installing the plugin — otherwise every skill loads twice and the always-on description cost doubles. `npx skills remove` opens an interactive picker; deselect the dengskills entries there, or delete the installed symlinks directly.

## Packaging

One portable core, plus a thin packaging layer per client. No `SKILL.md` changes between clients; adding a client means adding a manifest, never forking the skills.

| Layer | Files | Read by |
|---|---|---|
| Agent Skills | `skills/<name>/SKILL.md` | Every client — the portable core |
| Agent Plugins v1.0.0 | `plugin.json` | Any [Agent Plugins](https://agent-plugins.org/) client |
| skills.sh | `skills.sh.json`, `agents/openai.yaml`, `evals/evals.json` | skills CLI and skills.sh |
| Claude Code | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | Claude Code |

Claude Code needs its own manifest because it reads `.claude-plugin/plugin.json` specifically and ignores a root `plugin.json` — hence two manifests carrying the same metadata. `scripts/check-sync.sh` fails if they disagree on version, homepage, repository, or license, so the duplication cannot drift. Clients that ignore a layer ignore it harmlessly.

Adding support for another client should follow the same rule: a new manifest beside the others, the portable `skills/` tree untouched.

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
skills/                         the portable core — client-agnostic
  <skill-name>/
    SKILL.md                    Agent Skills specification
    agents/openai.yaml          skills.sh client config
    evals/evals.json            skills.sh test cases
plugin.json                     Agent Plugins v1.0.0 manifest
skills.sh.json                  skills.sh page groupings
.claude-plugin/
  plugin.json                   Claude Code plugin manifest
  marketplace.json              Claude Code marketplace (this repo, one plugin)
scripts/
  check-sync.sh                 metadata + manifest sync check
  bump-version.sh               set the version across all manifests
LICENSE
README.md
CHANGELOG.md
```

`skills/` is the only directory that matters to an agent at runtime; everything at the root is packaging for one client or another. `skills.sh.json` groups the skills on the skills.sh repository page and changes neither installs nor any `SKILL.md`. `plugin.json` is the portable Agent Plugins manifest. `.claude-plugin/` holds the Claude Code equivalents, which Claude Code reads exclusively from that directory. `CHANGELOG.md` records pack versions; bump it whenever a skill's behaviour, triggers, or examples change.

Run `./scripts/check-sync.sh` before releasing. It checks that frontmatter names, README tables, skills.sh groupings, evals, and both plugin manifests all agree, and runs `claude plugin validate --strict` on the Claude Code manifests when the `claude` CLI is available.

## Releasing a change

Most clients cache an installed copy rather than reading the repository live, so a change only reaches installs once the version changes. Bump the version for every published change, including adding a skill.

1. Edit `skills/` — change a `SKILL.md`, or add `skills/<new-skill>/SKILL.md` with `name` matching the directory.
2. For a **new** skill, also add it to a `skills.sh.json` grouping and to the README Skills, routing, and guide-pairing tables. `check-sync.sh` fails until you do.
3. `./scripts/bump-version.sh patch` — or `minor` / `major` / an explicit `1.4.0`. Sets the version in every manifest at once; run it with no argument to print the current version.
4. Add the release to `CHANGELOG.md`.
5. `./scripts/check-sync.sh`
6. `git commit -am "Release v1.4.0" && git tag v1.4.0 && git push --follow-tags`

Semver for this pack: **patch** for wording and eval fixes, **minor** for a new skill or changed triggers, **major** for removing or renaming a skill, which breaks any reference to the old name.

### Refreshing an install

| Client | Command |
|---|---|
| skills CLI | `npx skills update` |
| Claude Code | `claude plugin marketplace update dengskills && claude plugin update dengskills`, then restart the session |

Claude Code installs are snapshot copies in a version-keyed directory, so `claude plugin update` reports "already at the latest version" and picks up nothing — new skills included — unless the manifest version changed. Step 3 is what makes it work.

`claude plugin tag . --push` is an optional extra for Claude Code consumers: it creates a `dengskills--v<version>` tag and refuses to run if the two manifests or the marketplace entry disagree on the version. Use it alongside the plain `v<version>` tag, not instead of it.

## Local authoring notes

The official Agent Skills docs may be kept locally in `agentskillsofficial/` for reference while authoring, but that folder is intentionally ignored and not published in this repository.

## License

MIT © 2026 Matt J.M. Design

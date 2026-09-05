# Design Engineering Skills

A practical AI partner for product designers working in code: turn client intent into a runnable prototype, refine the experience, and build something people can actually use.

The pack pairs with the [Design Engineering guide](https://frontendguide.dev/docs). Use a skill before work or to revisit what already exists. There is no required sequence and no need to load the entire pack for one task.

## Start with your work

```text
Use $prototype to build a client scheduling demo in this existing app.
Use $craft to improve this screen, then inspect the rendered result.
Use $slice to connect this workflow to real data and server permissions.
Use $readiness to assess whether this preview can support a real pilot.
```

`$intent` helps when the goal is unclear. Planning and system skills support the work when a specific uncertainty needs them. An authorized build request should produce working artifacts, not end with another plan.

## Install

```bash
npx skills add mattjmdesign/dengskills
```

For a local checkout before a release is published:

```bash
npx skills add /path/to/dengskills
```

Choose the relevant agents and project/global scope in the installer. Invocation syntax depends on the client; the examples use `$skill`. Ask by name when the client does not expose that syntax.

Claude Code plugin installation is also supported by the existing marketplace manifests:

```bash
claude plugin marketplace add mattjmdesign/dengskills
claude plugin install dengskills@dengskills
```

Codex installation uses the native plugin manifest:

```bash
codex plugin marketplace add mattjmdesign/dengskills
codex plugin add dengskills
```

Or install skills into Codex via the skills CLI:

```bash
npx skills add mattjmdesign/dengskills --agent codex
```

Use one installation method to avoid duplicate discovery. Claude plugin skill names are namespaced by the pack.

## Skills

| Skill | Use it to |
| --- | --- |
| `$intent` | Clarify the client goal or revisit the original promise. |
| `$prototype` | Build and refine a runnable prototype with honest simulations. |
| `$craft` | Compose, build, improve, or audit the visible interface. |
| `$slice` | Implement one real workflow through UI, data, permissions, and recovery. |
| `$states` | Find and resolve missing or misleading states. |
| `$readiness` | Assess intended real use with evidence, blockers, and unknowns. |
| `$requirements` | Turn a brief or feature into testable behavior. |
| `$flow` | Trace a task through decisions, interruptions, and recovery. |
| `$sitemap` | Organize routes, navigation, URL state, and access boundaries. |
| `$hierarchy` | Rank one page’s content and actions. |
| `$layout` | Define or revisit regions, widths, scroll, and responsive structure. |
| `$tokens` | Create or extend the smallest useful visual vocabulary. |
| `$component` | Define or revise a component’s API and behavior. |
| `$system` | Maintain shared UI decisions and plan consumer migrations. |
| `$stack` | Compare technical paths when the existing choice is unresolved. |
| `$setup` | Establish or improve a runnable repository foundation. |
| `$git` | Coordinate reviewable changes and shared-file ownership. |
| `$context` | Keep verified agent instructions concise and current. |

## Craft is included

`$craft` covers the whole visible experience — composition, type, responsive structure, interaction, and rendered critique — with references and deterministic helpers loaded as needed. Focused skills such as `$layout` or `$component` suit narrower decisions.

## Upgrading from 1.x

Version 2 uses shorter canonical names. This is a naming migration: old names are not aliases. Update saved prompts and installed copies; use the installer’s removal workflow to remove obsolete skills from the intended scope. Do not manually delete unrelated skills.

| Previous name | New name |
| --- | --- |
| `product-intent-clarifier` | `intent` |
| `prototype-fidelity-selector` | `prototype` |
| `requirements-from-brief` | `requirements` |
| `framework-fit-advisor` | `stack` |
| `project-foundation-planner` | `setup` |
| `git-workflow-planner` | `git` |
| `agent-context-file-planner` | `context` |
| `ui-system-initializer` | `tokens` |
| `ui-layout-architect` | `layout` |
| `ui-system-governance` | `system` |
| `sitemap-planner` | `sitemap` |
| `user-flow-mapper` | `flow` |
| `content-hierarchy-planner` | `hierarchy` |
| `component-spec-writer` | `component` |
| `gap-state-inventory` | `states` |
| `production-readiness-review` | `readiness` |

`craft` and `slice` are new to this pack. `prototype` replaces a fidelity recommendation with an executable prototyping workflow. [migration.json](migration.json) is the machine-readable mapping.

## Quality and maintenance

Instructions distinguish evidence from assumptions, preserve user scope, and scale planning and verification to the task. A mock is not a real integration, an automated check is not complete accessibility evaluation, and a readiness review does not authorize deployment or client messages.

- `bash scripts/check-sync.sh` checks names, groupings, eval metadata, references, invocation prompts, and package manifests.
- `bash scripts/bump-version.sh major|minor|patch` updates all version manifests together.

Each skill includes realistic evaluation cases in `evals/evals.json`. Metadata validation does not prove behavioral quality; exercise cases against actual task artifacts and record observed outcomes when evaluating releases.

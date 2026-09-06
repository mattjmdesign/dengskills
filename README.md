# Design Engineering Skills

[![skills.sh](https://skills.sh/b/mattjmdesign/dengskills)](https://skills.sh/mattjmdesign/dengskills)

An AI partner for product designers working in code: turn client intent into a runnable prototype, refine the experience, and build something people can actually use.

Pairs with the [Design Engineering guide](https://frontendguide.dev/docs). Use a skill before work or to revisit what already exists — no required sequence, no need to load the whole pack for one task.

## Start with your work

```text
Use $prototype to build a client scheduling demo in this existing app.
Use $craft to improve this screen, then inspect the rendered result.
Use $slice to connect this workflow to real data and server permissions.
Use $readiness to assess whether this preview can support a real pilot.
```

`$intent` helps when the goal itself is unclear. An authorized build request should produce working artifacts, not end with another plan.

## Skills

**Product definition** — frame the goal, build the prototype, pin the behavior:

| Skill | Use it to |
| --- | --- |
| `$intent` | Clarify the client goal or revisit the original promise. |
| `$prototype` | Build and refine a runnable prototype with honest simulations. |
| `$requirements` | Turn a brief or feature into testable behavior. |

**Project setup** — foundation, stack, collaboration, and agent instructions:

| Skill | Use it to |
| --- | --- |
| `$stack` | Compare technical paths when the existing choice is unresolved. |
| `$setup` | Establish or improve a runnable repository foundation. |
| `$git` | Coordinate reviewable changes and shared-file ownership. |
| `$context` | Keep verified agent instructions concise and current. |

**UI composition** — tokens, structure, system health, and overall craft:

| Skill | Use it to |
| --- | --- |
| `$tokens` | Create or extend the smallest useful visual vocabulary. |
| `$layout` | Define or revisit regions, widths, scroll, and responsive structure. |
| `$system` | Maintain shared UI decisions and plan consumer migrations. |
| `$craft` | Compose, build, improve, or audit the visible interface. |

**IA and flows** — where things live and how tasks run:

| Skill | Use it to |
| --- | --- |
| `$sitemap` | Organize routes, navigation, URL state, and access boundaries. |
| `$flow` | Trace a task through decisions, interruptions, and recovery. |
| `$hierarchy` | Rank one page's content and actions. |

**Build and iterate** — components, states, and one real workflow:

| Skill | Use it to |
| --- | --- |
| `$component` | Define or revise a component's API and behavior. |
| `$states` | Find and resolve missing or misleading states. |
| `$slice` | Implement one real workflow through UI, data, permissions, and recovery. |

**QA and delivery** — the go/no-go question:

| Skill | Use it to |
| --- | --- |
| `$readiness` | Assess intended real use with evidence, blockers, and unknowns. |

`$craft` covers the whole visible experience; `$layout`, `$tokens`, and `$component` suit narrower decisions. Each skill's `Boundaries` section says what it does not own.

## Install

```bash
npx skills add mattjmdesign/dengskills
```

For a local checkout:

```bash
npx skills add /path/to/dengskills
```

One skill only: `npx skills add mattjmdesign/dengskills --skill craft`. Choose agents and project/global scope in the installer; use one installation method to avoid duplicate discovery. Invocation syntax depends on the client — the examples use `$skill`; otherwise ask for the skill by name.

Claude Code and Codex plugin installs:

```bash
claude plugin marketplace add mattjmdesign/dengskills
claude plugin install dengskills@dengskills
codex plugin marketplace add mattjmdesign/dengskills
codex plugin add dengskills
```

The portable `plugin.json` ([Agent Plugins 1.0](https://agent-plugins.org)) also loads directly in ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code — no repackaging. Claude plugin skill names are namespaced by the pack.

OpenCode (including the desktop app) uses skills rather than plugin manifests — install the skills for it:

```bash
npx skills add mattjmdesign/dengskills --agent opencode
```

## Maintain

- `bash scripts/check-sync.sh` — metadata, groupings, evals, manifests.
- `python3 scripts/audit-security.py` — static security scan.
- `bash scripts/bump-version.sh major|minor|patch` — version all manifests together.
- `docs/SKILL-AUTHORING.md` — rules for changing skills.
- `CHANGELOG.md` — release history.

A mock is not a real integration, an automated check is not complete accessibility evaluation, and a readiness review does not authorize deployment or client messages.

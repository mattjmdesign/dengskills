# Changelog

## v1.3.0 — Claude Code packaging + release tooling

Packaging only. No `SKILL.md` changed, and no client's view of the skills changed except Claude Code's, which previously had none.

### Claude Code support
- Added `.claude-plugin/plugin.json`. Claude Code reads its plugin manifest from that path exclusively and ignores a root `plugin.json`, so the Agent Plugins manifest alone left the repo invisible to Claude Code even though every `SKILL.md` was already compatible. Verified: `claude plugin details dengskills` reports all 16 skills.
- Added `.claude-plugin/marketplace.json` listing this repo as a one-plugin marketplace with `source: "./"`, so `claude plugin marketplace add mattjmdesign/dengskills` + `claude plugin install dengskills@dengskills` works without a separate marketplace repository.
- The Claude Code manifest omits the Agent Plugins `$schema` and carries only fields Claude Code reads. Both manifests hold the same metadata; `check-sync.sh` fails if they disagree.

### Packaging model
- README now states the rule the repo follows: `skills/` is the portable core, every root file is packaging for one client, and supporting another client means adding a manifest beside the others — never forking a skill. The packaging table lists Agent Skills, Agent Plugins, skills.sh, and Claude Code as peer layers.

### Release tooling
- Added `scripts/bump-version.sh`: sets the version across every manifest at once, accepts `major` / `minor` / `patch` or an explicit version, and prints the remaining release steps. Version duplication across client manifests is now a one-command edit rather than three hand-edits that can drift.
- `scripts/check-sync.sh` gained manifest checks: the manifests must agree on version, homepage, repository, and license; the marketplace entry must point at the repo root; and both Claude Code manifests are run through `claude plugin validate --strict` when the CLI is present.
- README gained a "Releasing a change" section with a per-client refresh table. Documents the non-obvious part: most clients cache a version-keyed copy rather than reading the repo live, so `claude plugin update` picks up nothing — new skills included — unless the version changed. Verified both ways: adding a skill without a bump was ignored, with a bump it appeared.
- Ignored eval output, local agent-tool state, and `node_modules/`.

## v1.2.0 — Production readiness + revisit

- Added `$production-readiness-review` (QA & Delivery). Scores a running slice as demo / pilot / production and lists UI-owned risks.
- Skills now explicitly revisit existing work: `$product-intent-clarifier` and `$gap-state-inventory` include after-preview guidance.
- Pack scope is no longer “pre-code only.” Testing, deploy, and observability remain guide-only.

## v1.1.0 — Guide pairing, trigger discipline, worked examples

The pack is now explicitly paired with the [Design Engineering guide](https://frontendguide.dev/docs): every skill names its corresponding guide page, and the guide links back to its skills.

### Trigger discipline
- Added "Do not use when / use instead" guardrails to skills with overlapping triggers (`product-intent-clarifier`, `prototype-fidelity-selector`, `requirements-from-brief`, `content-hierarchy-planner`, `ui-layout-architect`, `ui-system-initializer`).
- Added a routing table to README.md: "If you need X, use Y before/after Z".
- `sitemap-planner` now covers filters-in-search-params and the route-vs-state distinction (grounds the existing `filters-url` eval).

### Worked examples
- Every SKILL.md now includes one filled example output following its own output format, so agents anchor on a concrete exemplar instead of an empty template.

### Evals
- Added negative evals to key skills (e.g. "does not recommend code prototype", "does not invent commands", "does not replace an existing token system").
- Existing evals unchanged and still passing in intent; `filters-url` is now grounded in the skill body.

### Scope
- README and docs now state the pack covers Product Definition through Build Readiness. QA/Delivery phases remain guide-only; post-build skills (testing strategy, pre-launch readiness) are on the roadmap.

### Agent Plugins packaging
- Added a root `plugin.json` manifest (Agent Plugins v1.0.0). The repo is now dual-packaged: installable via `npx skills add mattjmdesign/dengskills` *and* loadable directly as an Agent Plugin by any compatible client. `skills/` is the standard fixed location and every `SKILL.md` conforms to the Agent Skills specification; skills.sh-specific files (`skills.sh.json`, `agents/openai.yaml`, `evals/evals.json`) live alongside the portable core.
- Reviewed against the published Agent Plugins 1.0.0 spec: closed manifest fields only, canonical `$schema`, name constraints, and skills discovered as immediate children of `skills/`. `homepage` and all "See also" links now use `https://frontendguide.dev`.

### Sync tooling
- Added `scripts/check-sync.sh`: validates that frontmatter names/descriptions, README tables, `skills.sh.json` groupings, and each skill's evals all reference the same set of 15 skill names.

## v1.0.0 — Initial pack

15 skills across Product Definition, Project Setup, UI Composition, IA & Flows, and Build Readiness. Published on skills.sh and GitHub.

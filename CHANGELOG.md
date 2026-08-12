# Changelog

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

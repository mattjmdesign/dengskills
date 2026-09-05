# AGENTS.md — dengskills

Skills for design engineering: product designers building client prototypes and real products with AI. 18 skills in `skills/<name>/`, each a `SKILL.md` (instruction) plus `agents/openai.yaml` (client metadata) and `evals/` (eval cases + routing suite).

No required sequence. Load one skill per task, not the pack.

## Repo map

- `skills/<name>/SKILL.md` — the skill. Sections: Work, Deliver, Worked example, Gotchas, Boundaries.
- `skills/<name>/evals/evals.json` — behavioral eval cases. `evals/triggers.json` — routing suite (10 queries each; data only, no runner yet).
- `skills/<name>/agents/openai.yaml` — display name, default prompt, invocation policy.
- `skills/<name>/references/`, `scripts/` — loaded only when the skill points at them (`$craft` has both).
- `scripts/validate-repo.py` — source of truth for checks. `scripts/audit-security.py` — static scan.
- `docs/SKILL-AUTHORING.md` — rules for editing skills. Read it before changing any skill.
- `plugin.json`, `.claude-plugin/`, `.codex-plugin/` — install manifests (must agree on version; bump together).

## Which skill and why

**Product definition:** `$intent` when the goal is unclear (user, outcome, scope); `$prototype` to make it runnable and learn by trying; `$requirements` when behavior is agreed and needs testable acceptance. Do not build before `$intent` settles an unclear goal.

**Project setup:** `$stack` advises on the technical path (never scaffolds); `$setup` makes the repo runnable; `$git` plans parallel human/agent work (planning only — never pushes/merges); `$context` writes verified repo instructions (every command and path checked, never invented).

**UI composition:** `$tokens` for the visual vocabulary (roles before values, every pair contrast-checked); `$layout` for page structure from real content; `$system` for drift audits with migration paths; `$craft` for the whole visible experience with rendered verification.

**IA and flows:** `$sitemap` for where tasks live and who may enter; `$flow` for the task path including interruptions and recovery; `$hierarchy` for what one page prioritizes.

**Build and iterate:** `$component` for one component's contract; `$states` for everything outside the happy path; `$slice` for one real end-to-end workflow (server permission checks, durable save, recovery evidence — a mock is never a real integration).

**QA and delivery:** `$readiness` answers whether the preview supports its intended use with blockers named. It never authorizes launch or client messages.

**Known near-misses — pick carefully:** mediocre UI is `$craft`, shifting shells are `$layout`; messy component API is `$component`, missing loading/error coverage is `$states`; mock-to-real is `$slice`, click-to-learn is `$prototype`; pilot safety is `$readiness`, hardening work is `$slice`; vague goal is `$intent`, agreed behavior needing tests is `$requirements`. Each skill's `Boundaries` section is authoritative on overlaps.

## Rules for changing this repo

1. Read `docs/SKILL-AUTHORING.md` first.
2. Keep `SKILL.md` portable: no client-specific instructions, no new trust boundaries, no shared runtime imports. Reference new files from `SKILL.md` (one level deep).
3. Use new short `$names` only — never the pre-2.0 long names (mapping lives in `migration.json` for tooling).
4. Worked examples must be evidence-bound (detect → preserve → justify); no stack, branch, pixel, or font defaults.
5. Run `bash scripts/check-sync.sh --metadata-only` and `python3 scripts/audit-security.py` (zero FAIL findings) before finishing. Do not commit `__pycache__/`, eval output, or local agent-tool state.

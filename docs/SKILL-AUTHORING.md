# Skill authoring guide

Rules for changing skills in this repo. Short version: keep `SKILL.md`
portable and human-readable; put determinism, evaluation, and
client-specific behavior around the skills, not in them.

## Canonical model

Not every skill needs every section, but every skill follows the same
mental model:

- **Work** — the smallest reliable procedure: what evidence to inspect
  before deciding, then the steps. Procedures over declarations.
- **Deliver** — the output shape: an explicit template or format the
  agent must follow.
- **Worked example** — one filled example following the Deliver shape.
  Demonstrate evidence and reasoning; never establish a technology,
  architecture, sizing, branch, typography, framework, or product
  default unless it is intrinsic to the skill. Prefer detect →
  preserve → justify: show detected values, keep them, change only
  what the task justifies.
- **Gotchas** — 3–8 non-obvious mistakes agents repeatedly make on
  this work. Highest-value section per current authoring guidance;
  feed real observed corrections back here.
- **Boundaries** — adjacent skills and cases this skill must not own,
  as "do not use when … use `$other` instead" routing rules.

## Sentence test

Every sentence must pass: **would a competent agent likely get this
wrong without us saying it?** If not, remove it. Over-comprehensive
skills degrade performance by competing for model attention.

## Descriptions are a routing interface

Frontmatter `description` is all the agent sees when deciding whether
to load a skill. Style: "Use when …" imperative, focused on user
intent, with concrete trigger phrases. Keep under 500 characters.
Every description is covered by `evals/triggers.json` (10 cases:
5 positive, 5 negative with `expected_skill`, at least 3 near-miss).

## Progressive disclosure

Keep `SKILL.md` lean (under ~700 words; hard ceiling 5,000).
Move variant-specific detail into `references/` and link it from a
"Load when needed" table. Scripts in `scripts/` must be executable
helpers with clear run-vs-read intent, never required imports: someone
installing one skill receives everything it needs.

## No shared runtime

Repository-level `scripts/` may run test infrastructure, but production
skill dependencies stay inside each skill. No cross-skill imports.

## No MCP server

Skills plus local deterministic helpers are the architecture. A new
privileged trust boundary needs a specific external capability to
justify it — not a desire to seem "more agentic."

## Client adapters

Keep portable `SKILL.md` free of per-client behavior. Per-client
metadata lives in `agents/openai.yaml` (`display_name`,
`short_description`, `default_prompt`, explicit
`allow_implicit_invocation`). `allowed-tools` stays experimental:
usable where beneficial, never the primary security boundary.

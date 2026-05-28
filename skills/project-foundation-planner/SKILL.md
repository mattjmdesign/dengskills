---
name: project-foundation-planner
description: Plan the initial project foundation for a product-grade prototype or app repository. Use when setting up repo structure, tooling, TypeScript strictness, linting, formatting, environment variables, design token location, testing baseline, and documentation expectations before coding begins.
---

# Project Foundation Planner

Use this skill before creating many files. The goal is a foundation that lets designers, engineers, and agents work without inventing conventions on every task.

## Process

1. Identify selected framework and expected project type.
2. Recommend a feature-proximity folder structure rather than a technical-layer-only structure.
3. Define tooling defaults: package manager, TypeScript strictness, linting, formatting, test tools, and CI baseline.
4. Define environment variable strategy, including `.env.example` and runtime validation expectations.
5. Define where design tokens, primitives, feature components, shared utilities, and docs should live.
6. Identify project context files needed for agents.
7. Produce a setup checklist that can be implemented in order.

## Output format

```markdown
## Project foundation plan

**Framework/stack assumption:**

**Repository structure:**

**Tooling defaults:**

**TypeScript expectations:**

**Environment strategy:**

**Design system locations:**

**Testing baseline:**

**Agent context files:**

**Setup checklist:**

**Risks / decisions to confirm:**
```

## Guardrails

- Prefer predictable defaults over novel architecture.
- Do not create folders for hypothetical complexity unless the product needs them.
- Make environment and token decisions explicit early; agents otherwise hardcode values.

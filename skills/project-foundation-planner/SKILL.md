---
name: project-foundation-planner
description: Use this skill when setting up a new product-grade prototype or app repository before coding. Plans feature-oriented folder structure, package/tooling choices, TypeScript strictness, linting/formatting, environment variables, design token locations, primitive vs feature components, testing baseline, documentation, and agent context files.
---

# Project Foundation Planner

Use this skill before creating many files. The goal is a foundation that lets designers, engineers, and agents work without inventing conventions on every task.

## Process

1. Confirm framework, project type, package manager, styling approach, and deployment target when known.
2. Recommend a feature-proximity structure, not a root full of unrelated technical buckets.
3. Separate primitive UI components from composed feature components.
4. Define tooling defaults: TypeScript strictness, linting, formatting, testing, and CI baseline.
5. Define environment variable strategy, including `.env.example` and validation expectations.
6. Define where tokens, global styles, utilities, validation schemas, and docs live.
7. Identify required agent context files.
8. Produce an ordered setup checklist.

## Output format

````markdown
## Project foundation plan

**Stack assumption:**
**Package manager:**
**Deployment target:**

### Repository structure
```text
src/
  ...
```

### Tooling defaults
- [item]

### TypeScript expectations
- [item]

### Environment strategy
- [item]

### Design system locations
- [item]

### Testing baseline
- [item]

### Agent context files
- [item]

### Ordered setup checklist
- [ ] [criterion]

### Decisions to confirm
- [item]
````

## Worked example

## Project foundation plan

**Stack assumption:** Next.js App Router, TypeScript, Tailwind v4
**Package manager:** pnpm
**Deployment target:** Vercel

### Repository structure
```text
src/
  app/            — routes and layouts
  components/
    ui/           — primitives only
    features/     — one folder per feature
  lib/            — data access, validation schemas, utils
  styles/         — tokens and global css
```

### Tooling defaults
- Biome for lint + format; TypeScript strict: true
- Vitest + Testing Library; Playwright for critical flows

### TypeScript expectations
- strict mode; no `any` outside escape-hatch helpers

### Environment strategy
- `.env.example` checked in; zod-validated `env.ts` at startup

### Design system locations
- Tokens in `src/styles/globals.css` (@theme inline); primitives in `src/components/ui/`

### Testing baseline
- Smoke test per route; component tests for primitives with a11y checks

### Agent context files
- AGENTS.md with commands, structure, token rules, guardrails

### Ordered setup checklist
- [ ] Scaffold app + src layout
- [ ] Add Biome + strict TS
- [ ] Add .env.example + env validation
- [ ] Create token globals.css
- [ ] First primitive (Button) + test
- [ ] AGENTS.md

### Decisions to confirm
- Whether the client wants preview deploys per PR

## Common mistakes to prevent

- Do not create abstractions for hypothetical scale.
- Do not let feature components live in primitive UI folders.
- Do not leave env vars undocumented or unvalidated.
- Do not let agents infer design token locations later.

## Boundaries

- Do not use before the framework decision is made — run `$framework-fit-advisor` first.
- Do not use on an existing repo — audit it first; this skill plans greenfield foundations.

## Validate before final

- The plan identifies where primitives, feature components, tokens, env config, tests, and agent docs belong.
- The setup checklist can be executed in order.

## See also

- [Design Engineering guide: Project Setup](https://frontendguide.dev/docs/project-setup)

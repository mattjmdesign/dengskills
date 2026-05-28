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

## Common mistakes to prevent

- Do not create abstractions for hypothetical scale.
- Do not let feature components live in primitive UI folders.
- Do not leave env vars undocumented or unvalidated.
- Do not let agents infer design token locations later.

## Validate before final

- The plan identifies where primitives, feature components, tokens, env config, tests, and agent docs belong.
- The setup checklist can be executed in order.

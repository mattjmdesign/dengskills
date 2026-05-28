---
name: framework-fit-advisor
description: Recommend a frontend framework or stack based on product constraints, not preference. Use when choosing between Next.js, Nuxt, React with Vite, or similar paths for a website, SaaS app, dashboard, docs site, embedded tool, prototype, or client product, including routing, rendering, data, deployment, and handoff implications.
---

# Framework Fit Advisor

Use this skill to make stack decisions from the product operating model. The useful question is not "which framework is best"; it is which framework makes the product constraints easiest to express, preview, maintain, and hand off.

## Process

1. Identify product type: marketing/content, SaaS/dashboard, docs, e-commerce, canvas/tool, embedded widget, internal app, or experimental prototype.
2. Identify routing needs, auth needs, data ownership, SEO/metadata needs, interactivity level, deployment target, team familiarity, and design-system constraints.
3. Recommend one primary path and one acceptable fallback.
4. Explain implications for routing, rendering, data fetching, styling/tokens, testing, deployment, and AI-agent collaboration.
5. Produce a short decision record the team can keep in docs.

## Defaults

- Prefer **Next.js** for product sites, dashboards, docs, SaaS, Vercel deployment, metadata, server rendering, and mature app conventions.
- Prefer **Nuxt** for Vue-first teams, Vue design systems, content-heavy Vue products, and teams that prefer templates/composables.
- Prefer **React + Vite** for highly interactive tools, embedded apps, SPAs, custom runtimes, or fast exploratory prototypes where SSR conventions are not needed.

## Output format

```markdown
## Framework decision

**Recommended path:**

**Why this fits:**

**Fallback path:**

**Routing implications:**

**Data/rendering implications:**

**Design-system implications:**

**Testing/deployment implications:**

**Watch-outs:**

**Decision record:**
```

## Guardrails

- Do not recommend a stack based only on popularity.
- If the user lacks product constraints, ask for or infer the minimum needed constraints and mark assumptions.
- Include how the choice affects design-to-production workflow, not only developer experience.

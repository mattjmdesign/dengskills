---
name: framework-fit-advisor
description: Use this skill when choosing a frontend framework or stack for a product-grade prototype or app, especially Next.js vs Nuxt vs React + Vite. Bases the recommendation on product type, routing, rendering, SEO/metadata, auth, data ownership, interactivity, deployment, team familiarity, design-system needs, and handoff—not popularity.
---

# Framework Fit Advisor

Use this skill to make stack decisions from the product operating model. Recommend the framework that makes product constraints easiest to express, preview, maintain, and hand off.

## Process

1. Identify product type: marketing/content, SaaS/dashboard, docs, commerce, canvas/tool, embedded widget, internal app, or experimental prototype.
2. Identify routing, auth, data ownership, SEO/metadata, interactivity, deployment target, team familiarity, and design-system constraints.
3. Recommend one primary path and one acceptable fallback.
4. Explain implications for routing, rendering, data fetching, styling/tokens, testing, deployment, and AI-agent collaboration.
5. Produce a decision record.

## Decision defaults

- Prefer **Next.js** for product sites, SaaS, dashboards, docs, Vercel deployment, metadata, image handling, server rendering, and mature routing conventions.
- Prefer **Nuxt** for Vue-first teams, Vue design systems, template-centric workflows, and content-heavy Vue products.
- Prefer **React + Vite** for highly interactive tools, embedded apps, SPAs, custom runtimes, and fast exploratory prototypes that do not need full meta-framework conventions.

## Output format

```markdown
## Framework decision

**Recommended path:**
**Fallback path:**
**Decision confidence:** High / Medium / Low

### Why this fits
- [item]

### Product implications
- Routing:
- Data/rendering:
- Styling/design system:
- Testing:
- Deployment:
- Agent collaboration:

### Watch-outs
- [item]

### Decision record
We choose [framework] because [product constraints]. Revisit if [condition].
```

## Common mistakes to prevent

- Do not choose based only on what is trendy or familiar.
- Do not ignore routing/data/deployment when the user asks only about UI.
- Do not recommend Vite for product surfaces that clearly need SEO, metadata, server rendering, or app-router conventions unless those needs are intentionally out of scope.

## Validate before final

- The recommendation ties back to concrete product constraints.
- It includes at least one watch-out for the chosen stack.

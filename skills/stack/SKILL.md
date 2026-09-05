---
name: stack
description: "Choose or revisit a product stack using rendering, data, deployment, and maintenance constraints."
---

# Stack fit

Recommend a stack from the product's operating needs. Inspect an existing repository before proposing replacement; continuity, migration cost, and maintainer knowledge are part of fitness.

## Work

- Establish public discovery needs, interactive workload, offline needs, data ownership, authentication, integrations, hosting constraints, and who maintains it.
- Separate browser UI, server/API, database, and deployment decisions. A frontend framework does not provide the whole product architecture.
- Compare a primary option and a credible alternative against those constraints. Include keeping the existing stack when applicable.
- Check current official documentation for version-sensitive APIs, support, deployment adapters, licensing, or pricing that affect the recommendation.
- Explain the hardest tradeoff and the condition that would change the decision. Avoid claims about training-data popularity or universal performance advantages.

## Deliver

A short decision record: **choice, constraints served, cost accepted, deployment/data implications, uncertainty, revisit trigger**. Recommend a small feasibility check when integration uncertainty dominates.

Examples: a content-heavy site may benefit from prerendering or server rendering; a browser editor may favor a client-heavy runtime; an established Vue team may choose a Vue ecosystem solution. Vite is a build tool with SSR capabilities, not proof that SEO is impossible. Next.js is an option, not the default for every dashboard.

Do not scaffold or migrate a project when the request only asks for advice. Use `$setup` for an authorized foundation change.

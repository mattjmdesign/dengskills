---
name: stack
description: "Choose or revisit a product stack using rendering, data, deployment, and maintenance constraints. Use when comparing frameworks, when SEO, auth, or deploy targets constrain the choice, or when revisiting an existing stack."
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

Follow this shape:

**Recommended:** ...
**Fallback:** ...
**Confidence:** High / Medium / Low
**Constraints served:** ...
**Cost accepted:** ...
**Deployment/data:** ...
**Uncertainty:** ...
**Revisit if:** ...

Examples: a content-heavy site may benefit from prerendering or server rendering; a browser editor may favor a client-heavy runtime; an established Vue team may choose a Vue ecosystem solution. Vite is a build tool with SSR capabilities, not proof that SEO is impossible. Next.js is an option, not the default for every dashboard.

Do not scaffold or migrate a project when the request only asks for advice. Use `$setup` for an authorized foundation change.

## Worked example

**Recommended:** Next.js (App Router)
**Fallback:** React + Vite SPA with a thin API
**Confidence:** High
**Constraints served:** Marketing SEO and shared metadata plus an authenticated dashboard in one product; team deploys on Vercel and wants per-PR previews.
**Cost accepted:** Server/client boundary discipline; avoid `use client` creep on the marketing surface.
**Deployment/data:** `app/(marketing)` and `app/(dashboard)` groups; server components for initial data, TanStack Query for client freshness; Tailwind v4 tokens.
**Uncertainty:** Dashboard interactivity may outgrow server rendering; run a small client-island spike if canvas editing appears.
**Revisit if:** The dashboard becomes a canvas-heavy tool where instant HMR and a custom runtime matter more than SEO.

## Boundaries

- Do not use when product intent or requirements are unresolved — clarify with `$intent` or `$requirements` first; a stack choice without them is speculative.
- Do not use for a throwaway prototype — use `$prototype` instead.

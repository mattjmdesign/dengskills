---
name: product-intent-clarifier
description: Clarify a rough product idea, client request, or vibe-coding prompt into a buildable product intent brief. Use when the user wants to build an app, prototype, SaaS, website, dashboard, feature, or client product but has not yet defined target users, product promise, core job-to-be-done, constraints, risks, or what should be intentionally deferred.
---

# Product Intent Clarifier

Use this skill before recommending screens, components, frameworks, or implementation. The goal is to stop vibe coding from turning a vague idea into arbitrary UI.

## Process

1. Restate the product idea in one sentence.
2. Identify the primary user, secondary users, and client/business stakeholder.
3. Define the product promise: what gets easier, faster, safer, or more valuable.
4. Identify the core job-to-be-done and the first critical workflow.
5. Separate must-have v1 outcomes from nice-to-have features.
6. Surface constraints: timeline, audience, devices, data, integrations, budget, brand, compliance, accessibility, and deployment.
7. List assumptions and open questions. Do not silently invent product strategy.
8. Recommend the next design-engineering artifact: requirements, sitemap, user flow, prototype fidelity, or first slice.

## Output format

```markdown
## Product intent brief

**One-line concept:**

**Primary users:**

**Product promise:**

**Core job-to-be-done:**

**Primary workflow:**

**V1 must include:**

**Explicitly defer:**

**Constraints and risks:**

**Open questions:**

**Recommended next artifact:**
```

## Guardrails

- Prefer clear scope over impressive feature lists.
- Do not recommend implementation until the product promise and primary workflow are explicit.
- For client work, include the client-facing outcome, not only the end-user experience.
- Mark assumptions clearly when the user has not provided enough context.

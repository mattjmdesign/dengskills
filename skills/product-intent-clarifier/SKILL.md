---
name: product-intent-clarifier
description: Use this skill when a user has a rough product idea, client request, app concept, SaaS/dashboard/site idea, or vibe-coding prompt and needs to clarify product intent before design or code. Produces a product intent brief with users, product promise, job-to-be-done, first workflow, v1 scope, constraints, risks, assumptions, open questions, and the next design-engineering artifact.
---

# Product Intent Clarifier

Use this skill before recommending screens, components, frameworks, or implementation. Its job is to stop vague product ideas from becoming arbitrary UI.

## Process

1. Restate the idea in one sentence using the user's language.
2. Identify the primary user, secondary users, and client/business stakeholder.
3. Define the product promise: what becomes easier, faster, safer, clearer, or more valuable.
4. Name the core job-to-be-done and the first critical workflow.
5. Split v1 must-haves from later features.
6. Surface constraints: timeline, audience, devices, data, integrations, budget, brand, compliance, accessibility, deployment.
7. Mark assumptions and open questions. Do not silently invent product strategy.
8. Recommend the next artifact: requirements, sitemap, user flow, prototype fidelity, or first slice.

## Output format

```markdown
## Product intent brief

**One-line concept:**
**Primary users:**
**Client/business goal:**
**Product promise:**
**Core job-to-be-done:**
**First critical workflow:**

### V1 must include
- [item]

### Explicitly defer
- [item]

### Constraints and risks
- [item]

### Assumptions
- [item]

### Open questions
- [item]

**Recommended next artifact:**
```

## Worked example

## Product intent brief

**One-line concept:** A shared calendar for small construction crews so everyone knows which site they are on this week.
**Primary users:** Foremen (assign crews); crew members (check assignments).
**Client/business goal:** Replace the WhatsApp group that currently handles scheduling.
**Product promise:** Everyone knows where they work tomorrow without asking anyone.
**Core job-to-be-done:** Check tomorrow's assignment in under 10 seconds from a phone.
**First critical workflow:** Foreman creates the week's assignments; crew member opens today's view.

### V1 must include
- Weekly assignment view, per-user and per-site
- Foreman-only editing and assignment
- Notification when an assignment changes

### Explicitly defer
- Time tracking, payroll, GPS check-in

### Constraints and risks
- Worksite audience on low-end Android phones; no always-on connectivity

### Assumptions
- One foreman per crew; crews are under 15 people

### Open questions
- Should assignments support recurring weekly patterns?
- Must this integrate with an existing scheduling tool?

**Recommended next artifact:** Requirements for the assignment workflow.

## Common mistakes to prevent

- Do not turn a feature list into a product strategy.
- Do not start IA, visual design, or code while the primary user and workflow are unclear.
- Do not optimize for a client demo while ignoring what would make the prototype product-grade later.

## Boundaries

- Do not use when intent is clear and the open question is *how polished* to build — use `$prototype-fidelity-selector`.
- Do not use when an agreed brief already exists and needs testable requirements — use `$requirements-from-brief`.
- Do use again after a preview exists: compare the live slice to the original brief and list keep / fix / defer. Do not invent a new product.

## Validate before final

- The brief names a user, promise, workflow, scope boundary, and at least one risk or assumption.
- Any missing product facts are listed as open questions, not treated as known.

## See also

- [Design Engineering guide: Product Designer First](https://frontendguide.dev/docs/product-designer-first)

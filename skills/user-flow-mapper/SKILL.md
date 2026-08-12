---
name: user-flow-mapper
description: Use this skill when mapping how a user completes a task in a product, prototype, dashboard, onboarding, checkout, creation, editing, approval, or account flow. Produces happy path plus validation errors, API failures, permission branches, cancellation paths, success destinations, required UI states, and data/API/auth touchpoints.
---

# User Flow Mapper

Use this skill to make the path through a product explicit before designing screens or writing code. Include meaningful branches, not only the happy path.

## Process

1. Name the user goal, user role, entry point, and success outcome.
2. Map the happy path step by step.
3. Add branches for validation errors, empty states, API errors, permission failures, cancellation, back navigation, duplicate actions, and success.
4. Identify required UI states and messages at each branch.
5. Identify data/API/auth touchpoints.
6. Identify which steps are required for v1 and which can be deferred.

## Output format

````markdown
## User flow: [goal]

**User:**
**Entry point:**
**Success outcome:**

```text
[Start]
  → ...
```

### Branches and edge cases

### Required UI states

### Data/API/auth touchpoints

### V1 scope / deferred paths

### Open questions
````

## Worked example

## User flow: Create project

**User:** Project manager (authenticated)
**Entry point:** Dashboard "New project" button
**Success outcome:** Project created; user lands on its detail page

```text
[Dashboard] → [Create form] → validation pass → POST /api/projects → [Project detail]
```

### Branches and edge cases
- Validation error → inline field errors; keep all input
- API failure (network/500) → toast + retry; form state preserved
- Name already exists → 409 with field error
- Cancel/back → discard draft, confirm if fields are non-empty
- Expired session → redirect to login with return URL; restore draft from localStorage

### Required UI states
- Create form: idle, submitting (spinner + disabled), error banner; button copy "Create project" → "Creating…"

### Data/API/auth touchpoints
- POST /api/projects (auth required, Zod schema: name, teamId from session)

### V1 scope / deferred paths
- Deferred: project templates, bulk import

### Open questions
- Should create auto-invite team members?

## Common mistakes to prevent

- Do not show only the happy path.
- Do not label failures without a recovery path.
- Do not ignore what persists if the user cancels, navigates back, or retries.
- Do not forget permission and expired-session branches for authenticated products.

## Boundaries

- Do not use when page/route structure is the question — use `$sitemap-planner`.
- Do not use when the flow needs component-level behaviour — use `$component-spec-writer`.

## Validate before final

- The flow has an entry point, success destination, at least one failure branch, and required UI states.
- Any data mutation includes pending, success, and failure behavior.

## See also

- [Design Engineering guide: Information Architecture](https://frontendguide.dev/docs/information-architecture)

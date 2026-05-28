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

## Common mistakes to prevent

- Do not show only the happy path.
- Do not label failures without a recovery path.
- Do not ignore what persists if the user cancels, navigates back, or retries.
- Do not forget permission and expired-session branches for authenticated products.

## Validate before final

- The flow has an entry point, success destination, at least one failure branch, and required UI states.
- Any data mutation includes pending, success, and failure behavior.

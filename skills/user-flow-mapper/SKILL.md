---
name: user-flow-mapper
description: Map a user goal into a step-by-step product flow with happy path, variants, validation errors, API failures, permission differences, cancellation paths, success destinations, required UI states, and data touchpoints. Use when planning onboarding, checkout, creation, editing, account, dashboard, or client-demo flows.
---

# User Flow Mapper

Use this skill to make the path through a product explicit before designing screens or writing code. Include meaningful branches, not only the happy path.

## Process

1. Name the user goal and entry point.
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

## Guardrails

- Include recovery paths, not just failure labels.
- If a flow mutates data, include optimistic, pending, success, and failure behavior.
- If the user can abandon the flow, specify what persists and what is discarded.

---
name: gap-state-inventory
description: Inventory missing gap states for a screen, flow, component, or product prototype. Use when checking loading, empty, error, offline, permission denied, expired session, validation, disabled, partial data, slow network, localization, responsive, or other edge states that must be designed before a product-grade prototype or build.
---

# Gap State Inventory

Use this skill to find the undesigned interface. Gap states are often where real users spend time: loading, empty, failed, blocked, offline, unauthorized, and partially complete.

## Process

1. Identify the screen, component, or flow being reviewed.
2. List data dependencies, user permissions, network dependencies, and mutation points.
3. Inventory states across loading, empty, populated, partial, error, retry, offline, permission, expired session, validation, disabled, success, and destructive confirmation.
4. For each state, define user-visible behavior, copy needs, recovery path, and implementation owner.
5. Prioritize states as must-have for v1, should-have, or later.
6. Recommend tests or acceptance criteria for critical states.

## Output format

```markdown
## Gap state inventory

| State | Scenario | User-visible behavior | Recovery/action | Priority |
|---|---|---|---|---|

### Critical missing states

### Copy requirements

### Implementation notes

### Test/acceptance criteria
```

## Guardrails

- Do not say "handle errors" generically; name the error and recovery path.
- Include both first-load failures and refresh/mutation failures.
- Include permission and expired-session states for authenticated products.

---
name: gap-state-inventory
description: Use this skill when checking a screen, flow, component, or product-grade prototype for missing gap states: loading, empty, partial data, errors, retry, offline, permission denied, expired session, validation, disabled, success, destructive confirmation, slow network, localization, and responsive edge cases.
---

# Gap State Inventory

Use this skill to find the undesigned interface. Real users often experience products while loading, empty, failed, blocked, offline, unauthorized, or partially complete.

## Process

1. Identify the screen, component, or flow being reviewed.
2. List data dependencies, user permissions, network dependencies, and mutation points.
3. Inventory states: loading, empty, populated, partial, error, retry, offline, permission denied, expired session, validation, disabled, success, destructive confirmation, localization, and responsive edge cases.
4. For each state, define user-visible behavior, copy needs, recovery path, and implementation owner if known.
5. Prioritize states as must-have for v1, should-have, or later.
6. Recommend tests or acceptance criteria for critical states.

## Output format

```markdown
## Gap state inventory

| State | Scenario | User-visible behavior | Recovery/action | Priority |
|---|---|---|---|---|
| Loading |  |  |  |  |

### Critical missing states
- [item]

### Copy requirements
- [item]

### Implementation notes
- [item]

### Test / acceptance criteria
- [ ] [criterion]
```

## Common mistakes to prevent

- Do not say "handle errors" generically; name the error and recovery path.
- Do not include first-load failure only; include refresh and mutation failures.
- Do not forget permission and expired-session states for authenticated products.
- Do not design empty states without next-best action.

## Validate before final

- The inventory includes loading, empty, error, permission/session, and mutation states when relevant.
- Critical states have recovery actions and test criteria.

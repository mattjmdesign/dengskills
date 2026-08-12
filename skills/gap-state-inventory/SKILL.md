---
name: gap-state-inventory
description: Use this skill when checking a screen, flow, component, or product-grade prototype for missing gap states including loading, empty, partial data, errors, retry, offline, permission denied, expired session, validation, disabled, success, destructive confirmation, slow network, localization, and responsive edge cases.
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

## Worked example

## Gap state inventory

| State | Scenario | User-visible behavior | Recovery/action | Priority |
|---|---|---|---|---|
| Loading | Project list first load | Skeleton rows, not a spinner | — | Must |
| Empty | No projects yet | Illustration + "Create project" button | Create project | Must |
| Error | API 500 on refresh | Inline error with retry; stale data stays with "data from [time]" label | Retry button | Must |
| Permission denied | Viewer opens admin settings | Settings hidden; direct URL shows explanation | Back to dashboard | Must |
| Expired session | Token expiry mid-edit | Redirect to login with return URL; draft restored | Re-login | Must |
| Mutation pending | Create project submitted | Button disabled, spinner, "Creating…" | — | Must |
| Mutation failure | Create fails (network) | Toast with retry; form data preserved | Retry | Must |
| Destructive confirmation | Delete project | Confirm dialog naming the project | Cancel / Delete | Must |
| Offline | Board opened with no connectivity | Cached last-known board + offline badge | Reconnect banner | Should |
| Slow network | Filters on 3G | 300ms debounce + pending state | — | Should |

### Critical missing states
- Empty state for the team page (currently blank)
- No destructive confirmation on delete project

### Copy requirements
- Error: "We couldn't load your projects. Retry?" — button label "Try again"
- Empty: "No projects yet — create your first one."

### Implementation notes
- Skeleton components exist; reuse for team page
- Confirm dialog uses existing shadcn AlertDialog

### Test / acceptance criteria
- [ ] Empty-state test for 0 projects
- [ ] Retry re-fetches and clears the error state
- [ ] Delete requires confirmation before the mutation fires

## Common mistakes to prevent

- Do not say "handle errors" generically; name the error and recovery path.
- Do not include first-load failure only; include refresh and mutation failures.
- Do not forget permission and expired-session states for authenticated products.
- Do not design empty states without next-best action.

## Boundaries

- Do not use when the component has no spec — run `$component-spec-writer` first.
- Do not use when the flow structure is unknown — use `$user-flow-mapper`.

## Validate before final

- The inventory includes loading, empty, error, permission/session, and mutation states when relevant.
- Critical states have recovery actions and test criteria.

## See also

- [Design Engineering guide: Error Handling](https://frontendguide.dev/docs/error-handling)

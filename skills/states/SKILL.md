---
name: states
description: "Find and resolve missing states in an existing screen, flow, component, or specification. Use when checking loading, empty, error, permission, offline, or mutation recovery before a review or pilot."
---

# State coverage

Find the interface people encounter outside the ideal screenshot. A complete specification is not a prerequisite: inspecting incomplete work is the purpose of this skill.

## Work

- Identify actual data dependencies, roles, network calls, writes, and navigation paths.
- Separate initial loading from refresh; never-created data from filtered no-results; missing optional data from failed data; rejected writes from unknown outcomes.
- Inspect reachable permission, session, offline, conflict, partial-success, cancellation, and retry states. Mark irrelevant states rather than generating UI for them.
- For each gap, name the trigger, visible explanation, next action, retained input/data, and the layer responsible.
- Prioritize data loss, blocked primary tasks, misleading success, and access failures before minor polish.
- On live work, reproduce with safe test data. Do not fabricate that a state was observed or exercise consequential production actions just to complete coverage.

## Deliver

Report a compact table: **scenario → observed/planned behavior → recovery → priority → verification**. Include copy when ambiguity causes the failure. If fixes were requested, implement the reachable states and replay them.

```markdown
## State coverage

| Scenario | Observed / planned behavior | Recovery | Priority | Verification |
|---|---|---|---|---|
|  |  |  | Must / Should / Later |  |

### Critical missing
- [item]

### Copy
- [item]
```

Check that errors stay visible where action is needed, pending work is distinguishable from completion, and input survives safely. Avoid mandatory skeletons, illustrations, toasts, or confirmation dialogs without a task reason. Use `$readiness` when these findings inform a release decision.

## Worked example

## State coverage

| Scenario | Observed / planned behavior | Recovery | Priority | Verification |
|---|---|---|---|---|
| Project list first load | Skeleton rows hold layout; no full-screen spinner | — | Must | Render with throttled network; confirm no layout shift |
| No projects yet | Empty panel with "Create project" action | Create project | Must | Render with zero fixtures; confirm action routes correctly |
| Refresh fails after data loaded | Keep stale list with "data from [time]" notice plus inline retry | Retry | Must | Fail refresh; confirm stale rows persist and retry clears the error |
| Viewer opens admin settings | Settings hidden; direct URL shows explanation and a back action | Back to dashboard | Must | Request as viewer; confirm no admin mutation fires |
| Create fails on network | Preserve form input; show inline error with retry | Retry | Must | Drop network mid-submit; confirm no duplicate on retry |
| Delete project | Confirm dialog naming the project before the mutation fires | Cancel / Delete | Must | Confirm dialog blocks mutation until confirmed |

### Critical missing
- Team page has no empty state; currently renders blank
- Delete project has no confirmation; mutation fires immediately

### Copy
- Refresh error: "We couldn't refresh your projects. Data from 09:41." — action "Try again"
- Empty: "No projects yet — create your first one."

## Gotchas

- Give never-created empty and filtered no-results different copy and recovery; one explains how to start, the other how to adjust the filter.
- Give rejected writes and unknown outcomes different recovery; retry only when the contract makes it safe.
- Separate initial loading from refresh; keep stale data visible with a retry instead of replacing it with a spinner.
- Distinguish missing optional data from failed data; do not show an error where there is simply nothing.
- Preserve user input across failure and retry; do not clear a form to display an error.
- Reproduce states with safe test data; do not claim a state was observed without rendering it.

## Boundaries

- Do not use when the component contract is undefined — use `$component` first.
- Do not use when the entry-to-outcome flow is unknown — use `$flow` first.
- Do not use to judge whether a build supports demo, pilot, or production use — use `$readiness` instead.
- Do use on a runnable preview or live screen, not only on a spec; missing states in production are the point.

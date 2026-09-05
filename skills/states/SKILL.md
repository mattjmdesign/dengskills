---
name: states
description: "Find and resolve missing states in an existing screen, flow, component, or specification."
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

A compact table: **scenario → observed/planned behavior → recovery → priority → verification**. Include copy when ambiguity causes the failure. If fixes were requested, implement the reachable states and replay them.

Example: refresh failure keeps a previously loaded list with a stale-data notice; initial failure shows a recovery panel. A mutation timeout needs result reconciliation, not a generic retry that may duplicate work.

Check that errors stay visible where action is needed, pending work is distinguishable from completion, and input survives safely. Avoid mandatory skeletons, illustrations, toasts, or confirmation dialogs without a task reason. Use `$readiness` when these findings inform a release decision.

---
name: flow
description: "Map or review a task from entry to outcome, including mutations, interruptions, and recovery."
---

# User flow

Make the path executable, including what happens when the system does not give a clean answer. Use the existing workflow and permissions as evidence.

## Work

- Name the actor, entry point, goal, required information, and success destination.
- Trace the shortest complete path. At each transition, name the user action, system response, data owner, and visible feedback.
- Add relevant validation, authorization, timeout, conflict, cancellation, session expiry, and back-navigation branches. Avoid an exhaustive list of unreachable states.
- For writes, distinguish pending, committed, rejected, and outcome-unknown. A lost response may follow a successful write; define reconciliation or server-enforced idempotency before retrying.
- Decide what input survives interruption and for how long. Do not automatically store sensitive drafts in localStorage; match persistence to the data and shared-device risk.
- On a running feature, reproduce the path where possible and mark untested branches. Preserve product intent while correcting friction.

## Deliver

A compact flow diagram or ordered path with a branch table: **trigger → visible state → recovery → data/permission contract**. Include acceptance examples for consequential branches.

Example: a timed-out project creation first checks the operation's result before offering another create. A disabled button helps prevent repeat clicks but does not guarantee one server write.

Verify entry, success, interruption, and return behavior with the applicable input methods. Use `$states` for cross-screen coverage and `$component` for the interaction contract of a particular control.

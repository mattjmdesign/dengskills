---
name: flow
description: "Map or review a task from entry to outcome, including mutations, interruptions, and recovery. Use when mapping onboarding, checkout, creation, editing, approval, or account flows including failure and recovery branches."
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

Follow this shape:

## User flow: [goal]
**User:** ... **Entry:** ... **Success:** ...
Path: [Start] → ... → [Success]
Branches: trigger → visible state → recovery → data/permission contract
UI states: ...
Open questions: ...

Example: a timed-out project creation first checks the operation's result before offering another create. A disabled button helps prevent repeat clicks but does not guarantee one server write.

Verify entry, success, interruption, and return behavior with the applicable input methods. Use `$states` for cross-screen coverage and `$component` for the interaction contract of a particular control.

## Worked example

## User flow: Create project

**User:** Project manager (authenticated) **Entry:** Dashboard "New project" button **Success:** Project created; user lands on its detail page.
Path: [Dashboard] → [Create form] → validation pass → POST /api/projects → [Project detail]
Branches:
- Validation error → inline field errors; keep all input → correct and resubmit → no write yet.
- API failure (network/500) → toast plus retry; preserve form → retry the same operation → check result before re-creating.
- Name exists (409) → field error → rename and resubmit.
- Cancel/back with non-empty fields → confirm discard → discard draft.
- Expired session → login with return URL; restore draft → resume.
UI states: idle; submitting with spinner and disabled button ("Create project" → "Creating…"); error banner.
Data/permission contract: POST /api/projects requires auth; validate name and teamId from session; define idempotency before retry.
V1 scope: defer templates and bulk import.
Open questions: auto-invite team members on create?

## Boundaries

- Do not use when page or route structure is the question — use `$sitemap` instead.
- Do not use when a single control needs an interaction contract — use `$component` instead.

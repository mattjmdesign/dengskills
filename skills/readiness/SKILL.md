---
name: readiness
description: "Assess whether a build can support its intended demo, pilot, or production use using evidence and blocking risks. Use when a preview looks done, a client asks to launch, or a prototype path now faces real data and users."
---

# Release readiness

Judge the proposed use and consequence, not the polish of the preview. This is a scoped readiness review, not a security certification or authorization to launch.

## Work

- Identify the artifact, intended audience, data sensitivity, exposure, and claimed readiness. Recover intent from the brief, code, or user context; missing documentation does not prevent inspecting obvious risks.
- Verify the primary task and its critical failure paths. Distinguish real behavior, mocks, and unverified integration.
- Assess data persistence and recovery, server authorization and tenant isolation, input validation, secrets, async writes, accessibility, deployment, observability, and rollback as applicable.
- Use pass, fail, unverified, or not applicable with reasons and evidence. Do not average away a blocker or mark authentication as proof of authorization.
- Name must-fix items for the intended use. A real-data pilot still requires access enforcement and a data recovery decision.
- Record accepted risk only when an actual authorized person accepted it. Otherwise label it a proposed deferral with owner and revisit condition to resolve.

## Deliver

Lead with the supported use or blocking conclusion. Follow with **area → evidence/status → impact → required action**, then checks performed and unknowns. Keep the review focused on the existing product promise.

```markdown
## Readiness review

**Artifact:**
**Stated use:** demo | pilot | production
**Supported use:**
**Promise still true?** yes / no — [one line]

### Score
| Area | Demo | Pilot | Production | Notes |
|---|---|---|---|---|
| Data & persistence |  |  |  |  |
| Auth & permissions |  |  |  |  |
| Gap states |  |  |  |  |
| Security (UI-owned) |  |  |  |  |
| Tests & preview |  |  |  |  |
| Observability & rollback |  |  |  |  |

### Must fix before treating this as [level]
- [item]

### Accept explicitly
- [risk] — accepted by [who] — revisit when [signal]

### Next artifact
```

Do not publish, message stakeholders, alter permissions, or claim compliance as a side effect of review. Use `$states` for targeted recovery work and `$craft` when visible quality also needs evaluation.

## Worked example

## Readiness review

**Artifact:** `https://preview.example.com/dashboard`
**Stated use:** production (client asked to "just launch")
**Supported use:** pilot
**Promise still true?** Partially — primary job works; billing and invites are stubs

### Score
| Area | Demo | Pilot | Production | Notes |
|---|---|---|---|---|
| Data & persistence | Pass | Pass | Fail | Real DB; no backup or recovery decision |
| Auth & permissions | Pass | Fail | Fail | Login works; admin delete has no server check |
| Gap states | Pass | Fail | Fail | Empty dashboard renders blank |
| Security (UI-owned) | Pass | Fail | Fail | Delete fires from hidden UI without server enforcement |
| Tests & preview | Pass | Fail | Fail | Preview exists; no CI checks on the delete path |
| Observability & rollback | Unverified | Unverified | Unverified | No error tracking; rollback leaves stored deletes in place |

### Must fix before treating this as pilot
- Enforce server-side permission on delete and admin routes; hidden UI is not enforcement
- Add empty and error states to the project list with retry that preserves input
- Name the use to the client: pilot, not launch

### Accept explicitly
- EN-only — accepted by PM — revisit at first EU customer
- No backups — proposed deferral, owner eng lead — revisit before paying customers

### Next artifact
`$states` on dashboard and project list; then a written client note on pilot limits.

## Gotchas

- Let one blocker decide the level; do not average a fail away across passing areas.
- Treat login as identity only; it proves nothing about authorization — verify server enforcement on every consequential action.
- Treat hidden UI as no enforcement; probe the endpoint directly as an unauthorized identity.
- Record accepted risk only with a named authorized person and revisit signal; otherwise log a proposed deferral with owner.
- Remember rollback leaves stored changes and external effects in place; name the recovery decision explicitly.
- Stay inside the review scope; do not publish, message stakeholders, or claim compliance as a side effect.

## Boundaries

- Do not use when nothing is runnable — use `$slice` to build one real path first.
- Do not use when the question is only visual drift or token/component divergence — use `$system` instead.
- Do not use when the question is only missing states — use `$states` instead.

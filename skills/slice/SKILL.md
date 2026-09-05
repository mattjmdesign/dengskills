---
name: slice
description: "Implement or harden one real product workflow end to end in an existing or new codebase, connecting interface, data, permissions, recovery, and verification. Use when hardening a prototype path, implementing a client feature, or proving auth, recovery, and persistence."
---

# Build a real slice

Follow one user task through the system to a lasting result. Use this for a real feature, an inherited client project, or a prototype path that now needs actual persistence and access control.

## Locate the contract

Inspect the brief, repository instructions, existing UI/data patterns, API, schema, tests, and environment. Identify actor, entry, action, result, and the boundary of the requested work. Keep the product model, stack, routes, and integrations unless changing them is necessary and authorized.

Separate verified capabilities from unknown dependencies. Resolve routine details from the workspace. Ask only when a missing decision materially changes the outcome or consequence; continue independent work while it is unresolved.

## Implement through the layers

- Compose the interface from real product vocabulary and existing primitives. Preserve useful hierarchy, accessibility, and responsive behavior.
- Define the input/output and error contract. Validate untrusted data at runtime and expose only the fields the browser needs.
- Enforce authentication, authorization, and organization/resource scope on the server. Do not trust a submitted organization ID as membership evidence.
- Implement persistence and integrity constraints. For concurrent edits, define conflict behavior. For repeated or interrupted writes, use the service's idempotency/reconciliation mechanism; a disabled button is not duplicate protection.
- Update the correct cache or view after a confirmed result. Distinguish accepted background work from eventual completion.
- Include reachable loading, empty, rejected, denied, and unknown-outcome states. Preserve drafts only according to their sensitivity and lifetime.
- Keep migration and deployment compatibility explicit. An application rollback does not reverse stored changes or external effects.

## Verify the result people will use

Use isolated test identities/data. Replay the critical path, reload to verify persistence, check an unauthorized direct request, and exercise the highest-consequence recovery path. Add focused tests for meaningful invariants; do not pad coverage with implementation-mirroring assertions.

Run applicable repository checks and inspect the rendered narrow/wide result. Confirm where failures can be diagnosed without logging secrets or raw sensitive payloads.

## Deliver

State the working change, evidence, contract/migration notes, and any operational dependency that remains unverified. Do not label a mock as a completed real integration. If a service is unavailable, complete the safe local boundary and state exactly what blocks end-to-end proof.

```markdown
## Slice

**Change:**
**Evidence:**
**Contract / migration:**
**Unverified dependency:**
```

## Worked example

## Slice

**Change:** Editor renames a project; viewer requests are rejected server-side; rename persists across reload and respects organization scope
**Evidence:** Replay as editor and viewer with isolated test orgs; reload shows the stored name; direct viewer POST returns 403 and leaves the name unchanged; narrow/wide render checked; repo checks pass
**Contract / migration:** `PATCH /projects/:id` accepts `{name}` only, validates length server-side, enforces membership plus editor role, returns 403/404 without disclosing membership; no migration — existing rows unchanged; 409 on stale revision with client reload
**Unverified dependency:** Audit export to the client's SIEM remains unproven — endpoint unavailable in this environment; local audit row writes and is shown as pending export

## Boundaries

- Do not use to explore options without persistence or enforcement — use `$prototype` instead.
- Do not use for missing-state coverage alone — use `$states` instead.
- Do not use for visual refinement alone — use `$craft` instead.
- Do not use to judge whether the result supports demo, pilot, or production use — use `$readiness` instead.

Use `$readiness` when the result needs a release assessment. Do not publish, merge, message clients, or change account permissions solely to demonstrate completion.

---
name: slice
description: "Implement or harden one real product workflow end to end in an existing or new codebase, connecting interface, data, permissions, recovery, and verification."
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

Deliver the working change, evidence, contract/migration notes, and any operational dependency that remains unverified. Do not label a mock as a completed real integration. If a service is unavailable, complete the safe local boundary and state exactly what blocks end-to-end proof.

Use `$readiness` when the result needs a release assessment. Do not publish, merge, message clients, or change account permissions solely to demonstrate completion.

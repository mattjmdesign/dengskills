---
name: readiness
description: "Assess whether a build can support its intended demo, pilot, or production use using evidence and blocking risks."
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

Example: a hidden admin button with an unprotected delete endpoint blocks any pilot using real records. A working preview and successful login do not change that conclusion.

Do not publish, message stakeholders, alter permissions, or claim compliance as a side effect of review. Use `$states` for targeted recovery work and `$craft` when visible quality also needs evaluation.

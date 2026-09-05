---
name: prototype
description: "Build or revise a runnable prototype for a client goal, using realistic content and explicit real/mock boundaries to learn through interaction. Use when matching fidelity to the validation question, testing a task flow, or judging layout, motion, or latency in code."
---

# Prototype in code

Make the idea experienceable. For an authorized build request, produce a runnable artifact and inspect it; do not stop at a fidelity recommendation or another plan.

## Frame just enough to make

Read the brief and existing project. Identify the user, one complete task, the review question, and actual constraints. Preserve the chosen stack and useful components unless the user asks otherwise or a concrete incompatibility needs resolving.

Use code when real layout, content, keyboard input, motion, or latency behavior is the thing to judge. A sketch or clickable design may be sufficient for another question; explain that choice briefly when appropriate rather than imposing a mandatory progression.

## Build a convincing, honest slice

- State what must work, what is simulated, and what is deferred. Different parts may have different fidelity.
- Use realistic isolated fixture data; do not invent production customers, metrics, or capabilities. Keep fixtures clearly separate from live data.
- Complete one task through its outcome, with relevant pending and failure states. Avoid a collection of disconnected screens.
- Establish content hierarchy, responsive behavior, and interaction before fine decoration. Use `$craft` for substantial visible design when available; do not require another skill to begin.
- Keep simulations at replaceable boundaries. A mocked role switch shows an experience, not authorization. A local save may support a demo but is not durable multi-user persistence.

## Judge and revise

Open the result, replay the task, and inspect narrow and wide sizes plus the relevant content or state stress. Compare it to the client's goal. Revise a high-value issue revealed by the rendered result or task replay; do not invent user research.

## Deliver

State the artifact, how to try it, what is real/simulated/deferred, what the iteration taught, and the next decision. Mark unverified behavior honestly.

```markdown
## Prototype

**Artifact:**
**Try it:**
**Real:**
**Simulated:**
**Deferred:**
**What the iteration taught:**
**Next decision:**
```

## Worked example

## Prototype

**Artifact:** `/prototype/crew-assign` — crew lead finds tomorrow's site assignment on a phone
**Try it:** Open the preview, select the Crew role, search "Rivera," open the 06:00 assignment, acknowledge the shift change
**Real:** Layout, keyboard search, acknowledge interaction, narrow/wide responsive behavior, stale-assignment banner from fixture timestamps
**Simulated:** Roster from isolated fixtures; role switch changes the view only; acknowledge writes to local state
**Deferred:** Auth, push notifications, offline cache, supervisor approval chain
**What the iteration taught:** The change banner was missed below the map; moving it above the assignment card made the task recognizable in replay
**Next decision:** Confirm the change-acknowledgement rule with operations; use `$slice` if this path now needs real persistence and enforcement

## Gotchas

- Treat a role switch or local save as a demo of experience, not proof of authorization or persistence.
- Keep fixtures isolated from live data; do not invent customers, metrics, or capabilities.
- Complete one task through its outcome; do not present disconnected screens as a validated flow.
- Label real, simulated, and deferred behavior explicitly; do not let a working surface imply backend readiness.
- Replay the rendered result at narrow and wide sizes; do not judge the iteration from source alone.

## Boundaries

- Do not use when the user, outcome, or scope is vague — use `$intent` first.
- Do not use when the open question is testable behavior or acceptance rules — use `$requirements` instead.
- Do not use when the path needs real persistence, authorization, or recovery — use `$slice` instead.
- Do not use to judge whether a build supports demo, pilot, or production use — use `$readiness` instead.

When real people or data will use the result, do not treat the prototype label as a safety exemption. A deployment or client message requires the user's actual authorization, not merely completion of the prototype.

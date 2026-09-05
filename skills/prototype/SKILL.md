---
name: prototype
description: "Build or revise a runnable prototype for a client goal, using realistic content and explicit real/mock boundaries to learn through interaction."
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

Deliver the artifact or preview, how to try it, what is real/simulated, what the iteration taught you, and the next decision. Mark unverified behavior honestly.

When real people or data will use the result, do not treat the prototype label as a safety exemption. Use `$slice` to implement a real path and `$readiness` to assess the intended use. A deployment or client message requires the user's actual authorization, not merely completion of the prototype.

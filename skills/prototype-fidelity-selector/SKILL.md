---
name: prototype-fidelity-selector
description: Use this skill when deciding how much fidelity to build for a product idea, feature, or client demo: sketch, wireframe, clickable Figma prototype, high-fidelity mockup, code prototype, pilot-ready build, or near-production implementation. Helps avoid overbuilding or underbuilding by matching fidelity to the validation question and defining exit criteria.
---

# Prototype Fidelity Selector

Use this skill to match fidelity to the question being tested. Pick the cheapest artifact that can answer the question without hiding important product risk.

## Process

1. Identify the validation question: desirability, IA, task flow, visual direction, technical feasibility, performance feel, or client/demo readiness.
2. Choose the lowest sufficient fidelity.
3. Define what must be real and what can be mocked.
4. Define what not to build yet.
5. Set exit criteria for moving to the next fidelity.
6. Name risks of overbuilding and underbuilding.

## Fidelity defaults

- **Sketch / whiteboard:** rough layout and stakeholder alignment.
- **Low-fidelity wireframe:** navigation, content hierarchy, flow coverage.
- **Clickable prototype:** task flow validation and usability testing.
- **High-fidelity mockup:** visual review, token mapping, implementation handoff.
- **Code prototype:** real interaction, responsive behavior, performance feel, API/data assumptions.
- **Pilot-ready build:** client/user trial with real data paths and known limitations.
- **Near-production build:** hardened auth, errors, observability, deployment, and ownership.

## Output format

```markdown
## Fidelity recommendation

**Recommended fidelity:**
**Question being tested:**
**Why this is enough:**

### Must be real
- [item]

### Can be mocked
- [item]

### Do not build yet
- [item]

### Exit criteria
- [item]

### Risks
- Overbuilding:
- Underbuilding:

**Next step:**
```

## Common mistakes to prevent

- Do not recommend code when IA or workflow is still unknown.
- Do not recommend static mockups when real latency, responsiveness, or interaction is the central risk.
- Do not label a demo as production-grade unless data, auth, errors, deployment, and ownership are addressed.

## Validate before final

- The recommendation names the validation question and exit criteria.
- The plan clearly separates real behavior from mocked behavior.

---
name: prototype-fidelity-selector
description: Use this skill when deciding how much fidelity to build for a product idea, feature, or client demo. Covers sketch, wireframe, clickable Figma prototype, high-fidelity mockup, code prototype, pilot-ready build, and near-production implementation. Helps avoid overbuilding or underbuilding by matching fidelity to the validation question and defining exit criteria.
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

## Worked example

## Fidelity recommendation

**Recommended fidelity:** Clickable Figma prototype
**Question being tested:** Does the approval flow match how managers actually sign off?
**Why this is enough:** IA is settled; the open risk is task-flow comprehension, testable with a clickable prototype.

### Must be real
- The full 6-step approval sequence and its status labels
- Real role separation (requester vs approver)

### Can be mocked
- Backend data — prototype shows sample requests
- Notifications and email digests

### Do not build yet
- Auth integration, permission enforcement, audit log

### Exit criteria
- 4 of 5 test users complete the flow without help
- No test user asks "where do I approve?"

### Risks
- Overbuilding: coding the flow before validation would waste ~2 weeks
- Underbuilding: static mockups would not reveal step-ordering confusion

**Next step:** User flow mapping for the approval branches.

## Common mistakes to prevent

- Do not recommend code when IA or workflow is still unknown.
- Do not recommend static mockups when real latency, responsiveness, or interaction is the central risk.
- Do not label a demo as production-grade unless data, auth, errors, deployment, and ownership are addressed.

## Boundaries

- Do not use when the product and users are still vague — run `$product-intent-clarifier` first.
- Do not use when the question is one specific task flow — use `$user-flow-mapper`.

## Validate before final

- The recommendation names the validation question and exit criteria.
- The plan clearly separates real behavior from mocked behavior.

## See also

- [Design Engineering guide: Prototyping Validation](https://frontendguide.dev/docs/prototyping-validation)

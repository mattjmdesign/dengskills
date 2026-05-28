---
name: requirements-from-brief
description: Use this skill when turning a product brief, stakeholder notes, feature idea, client request, or vibe-coded concept into frontend requirements before design or implementation. Produces FR-XX functional requirements, NFR-XX quality constraints, explicit out-of-scope items, dependencies, assumptions, open questions, and a recommended next step.
---

# Requirements From Brief

Use this skill to translate product intent into requirements before interface solutions are chosen. Requirements describe what the user and system need, not which component to use.

## Process

1. Extract user goals, business goals, constraints, and data/API/auth dependencies.
2. Write functional requirements as `FR-XX: The system shall [action] when [condition] so that [outcome].`
3. Write non-functional requirements for performance, accessibility, responsiveness, browser support, security/privacy, reliability, and internationalization when relevant.
4. Identify explicit out-of-scope items for v1.
5. Identify assumptions and open questions.
6. Recommend acceptance criteria, sitemap, or user-flow mapping as the next step.

## Output format

```markdown
## Requirements

### Functional requirements
FR-01: The system shall ... when ... so that ...

### Non-functional requirements
NFR-01: ...

### Dependencies
- Data/API:
- Auth/permissions:
- Design system:

### Out of scope for v1
- [item]

### Assumptions
- [item]

### Open questions
- [item]

**Recommended next step:**
```

## Common mistakes to prevent

- Do not write requirements as UI solutions. "Compare 20 items" is a requirement; "show a table" is a possible solution.
- Do not skip NFRs because the user only described features.
- Do not hide auth, permission, or API dependencies inside vague wording.

## Validate before final

- Every FR is testable.
- At least accessibility and responsiveness are considered as NFRs unless clearly irrelevant.
- Unknowns are visible as assumptions or open questions.

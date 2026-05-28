---
name: requirements-from-brief
description: Convert a product brief, stakeholder notes, feature idea, or client request into precise frontend requirements. Use when defining functional requirements, non-functional requirements, constraints, explicit out-of-scope items, open questions, and testable product expectations before design or implementation.
---

# Requirements From Brief

Use this skill to translate product intent into requirements before interface solutions are chosen. Requirements describe what the user and system need, not the component or layout solution.

## Process

1. Extract user goals, business goals, constraints, and known data dependencies.
2. Write functional requirements as `FR-XX: The system shall [action] when [condition] so that [outcome].`
3. Write non-functional requirements for performance, accessibility, responsiveness, browser support, security/privacy, reliability, and internationalization when relevant.
4. Identify explicit out-of-scope items for v1.
5. Identify assumptions and open questions with owners if known.
6. Recommend acceptance criteria or user-flow mapping as the next step.

## Output format

```markdown
## Requirements

### Functional requirements

FR-01: The system shall ...

### Non-functional requirements

NFR-01: ...

### Out of scope for v1

### Constraints

### Assumptions

### Open questions

### Recommended next step
```

## Guardrails

- Do not write requirements as UI solutions. "The user needs to compare 20 items" is a requirement; "show a table" is a possible solution.
- Make every requirement testable.
- If a requirement depends on data, auth, permissions, or API behavior, call that out explicitly.

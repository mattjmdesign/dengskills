---
name: content-hierarchy-planner
description: Use this skill when planning what belongs on a page or screen before visual design or implementation. Defines page purpose, primary user decision/action, H1 and heading structure, primary/secondary/tertiary content, primary/secondary/destructive actions, responsive priority, and what to move, defer, collapse, or remove.
---

# Content Hierarchy Planner

Use this skill before layout design. A page that cannot rank its content is usually trying to do too many things.

## Process

1. Identify the page purpose in one sentence.
2. Define the user's primary decision or action on the page.
3. Rank content into primary, secondary, and tertiary groups.
4. Identify primary, secondary, and destructive actions.
5. Define heading structure and semantic landmarks.
6. Decide what should be hidden, deferred, collapsed, moved to another page, or shown conditionally.
7. Call out responsive priority: what appears first on mobile and what can move lower.

## Output format

```markdown
## Content hierarchy

**Page purpose:**
**Primary user decision/action:**
**H1:**

### Primary content
- [item]

### Secondary content
- [item]

### Tertiary metadata
- [item]

### Actions
- Primary:
- Secondary:
- Destructive:

### Responsive priority
- [item]

### Move / defer / remove
- [item]

### Accessibility notes
- [item]
```

## Common mistakes to prevent

- Do not give every card, metric, and CTA equal weight.
- Do not create multiple competing primary actions in one section.
- Do not break heading order to match visual size.
- Do not hide essential actions on mobile.

## Validate before final

- The plan names one primary decision/action.
- Content is ranked, not merely listed.
- Responsive and accessibility implications are included.

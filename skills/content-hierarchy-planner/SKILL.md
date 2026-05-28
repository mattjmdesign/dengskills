---
name: content-hierarchy-planner
description: Plan the content hierarchy of a page or screen before visual design or implementation. Use when deciding what belongs on a page, the primary action, secondary content, metadata, destructive actions, heading structure, layout priority, dashboard sections, or how to reduce clutter and improve user decision-making.
---

# Content Hierarchy Planner

Use this skill before layout design. A page that cannot rank its content is usually trying to do too many things.

## Process

1. Identify the page purpose in one sentence.
2. Define the user's primary decision or action on the page.
3. Rank content into primary, secondary, and tertiary groups.
4. Identify primary, secondary, and destructive actions.
5. Define recommended heading structure and semantic landmarks.
6. Note what should be hidden, deferred, collapsed, moved to another page, or shown only conditionally.
7. Call out responsive priority: what appears first on mobile and what can move lower.

## Output format

```markdown
## Content hierarchy

**Page purpose:**

**Primary user decision/action:**

**H1:**

**Primary content:**

**Secondary content:**

**Tertiary metadata:**

**Actions:**
- Primary:
- Secondary:
- Destructive:

**Responsive priority:**

**Move/defer/remove:**

**Accessibility notes:**
```

## Guardrails

- Do not treat every element as equally important.
- Prefer one primary action per page or section.
- Preserve semantic heading order even if visual styling differs.

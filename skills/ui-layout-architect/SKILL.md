---
name: ui-layout-architect
description: Use this skill when a project needs its UI skeleton planned before feature work begins. Produces layout shell decisions for landing pages, dashboards, auth flows, documentation, or app sections; audits existing component libraries such as shadcn/ui, Radix, Base UI, or custom primitives; defines responsive dimensions, max widths, global header/footer/sidebar behavior, and the page block structure agents should build within.
---

# UI Layout Architect

Use this skill before building page features. Its job is to decide where UI will live: the shells, dimensions, global regions, reusable blocks, and component primitives that keep a product from becoming a collection of unrelated screens.

## Process

1. Clarify the product surface: landing page, dashboard, auth flow, documentation, settings area, or mixed application.
2. Audit the codebase before generating anything. Look for `components/ui`, shadcn/ui files, Radix imports, Base UI imports, Tailwind config, global CSS tokens, existing layout components, and route-level layouts.
3. If a design system or component library already exists, use it. Do not generate duplicate Button, Input, Dialog, Card, Select, Tooltip, or layout primitives.
4. If no system exists, recommend the smallest appropriate starting point: external library, headless primitives, shadcn-style copy-owned components, or custom responsive primitives.
5. Define the layout shells needed for the project: `LandingLayout`, `DashboardLayout`, `AuthLayout`, `DocsLayout`, `SettingsLayout`, or another named shell.
6. Define dimensions as variables where possible: content max width, sidebar width, collapsed sidebar width, header height, section padding, card width, page gutters, and responsive breakpoints.
7. For landing pages, define the section skeleton: nav, hero, proof/social proof, feature blocks, product walkthrough, pricing or conversion block, FAQ if needed, footer, and whether header/footer are global.
8. For dashboards, define sidebar, header, main content, responsive drawer behavior, scroll regions, and empty/loading/error page states.
9. For auth pages, define centered card width, background, logo/heading placement, form width, recovery states, and no-navigation chrome.
10. Output the skeleton plan plus implementation-ready Tailwind examples using existing tokens and components.

## Output format

````markdown
## UI layout architecture plan

**Surface type:**
**Existing UI system found:**
**Design system/library decision:**
**Primary layout shells:**

### Existing primitives to reuse
- [component/library]: [how to use]

### Missing primitives or composites
- [component]: [why needed and how to add]

### Layout dimensions
| Dimension | Value | Variable / Tailwind | Used by |
| --- | --- | --- | --- |

### Page skeleton
- [global region / section / block]

### Responsive behavior
- [breakpoint behavior]

### Implementation sketch
```tsx
// layout shell or page skeleton
```

### Decisions to confirm
- [item]
````

## Common mistakes to prevent

- Do not start with a full page when the shell, max width, and section structure are undecided.
- Do not generate new primitives when shadcn/ui, Radix wrappers, Base UI wrappers, or custom primitives already exist.
- Do not hardcode dimensions in multiple places; prefer CSS custom properties or Tailwind theme variables.
- Do not let every page define its own header, footer, sidebar, gutters, or section spacing.
- Do not design only the happy path; include loading, empty, error, and responsive states in the skeleton.

## Validate before final

- The plan states what already exists and what should be reused.
- Layout shells and global regions are named clearly enough to map to files or Figma frames.
- Core dimensions are centralized as variables or theme values.
- The skeleton reduces future agent decisions instead of adding vague options.
- The plan explains how page content should sit inside the shell at mobile, tablet, and desktop sizes.

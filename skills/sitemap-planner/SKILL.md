---
name: sitemap-planner
description: Create an information architecture sitemap and route plan from product requirements or a feature brief. Use when mapping pages, screens, navigation, public/auth/admin areas, URL structure, route groups, nested routes, future routes, and page hierarchy before visual design or implementation.
---

# Sitemap Planner

Use this skill to turn product requirements into an information architecture. Treat routes as product contracts: URLs are shared, bookmarked, logged, and hard to change later.

## Process

1. Identify product areas: public marketing, auth, app shell, resource collections, settings, admin, support, and error routes.
2. Group pages by user mental model, not only database entities.
3. Define route hierarchy with stable lowercase kebab-case URLs.
4. Identify auth/permission boundaries.
5. Recommend navigation pattern: top nav, sidebar, breadcrumbs, tabs, nested settings nav, command palette, or a combination.
6. Include likely v2/v3 routes if they affect current URL choices.
7. Flag IA risks and naming ambiguity.

## Output format

````markdown
## Sitemap and routing plan

### Sitemap

```text
/
├── ...
```

### Navigation model

### Route conventions

### Auth and permission boundaries

### Future routes to preserve space for

### IA risks / questions
````

## Guardrails

- Use plural nouns for collections.
- Use search params for shareable filters and UI state.
- Do not encode session or auth state in the URL.
- If a page has too many unrelated jobs, recommend splitting it.

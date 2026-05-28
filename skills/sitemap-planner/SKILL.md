---
name: sitemap-planner
description: Use this skill when creating information architecture for a product, app, website, dashboard, or prototype. Maps pages/screens, route hierarchy, public vs authenticated vs admin areas, navigation model, URL conventions, route groups, nested routes, future routes, and IA risks before visual design or implementation.
---

# Sitemap Planner

Use this skill to turn product requirements into information architecture. Treat routes as product contracts: URLs are shared, bookmarked, logged, and hard to change later.

## Process

1. Identify product areas: public marketing, auth, app shell, resource collections, settings, admin, support, and error routes.
2. Group pages by user mental model, not only database entities.
3. Define route hierarchy with stable lowercase kebab-case URLs.
4. Identify auth and permission boundaries.
5. Recommend navigation pattern: top nav, sidebar, breadcrumbs, tabs, nested settings nav, command palette, or combination.
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

## Common mistakes to prevent

- Do not flatten everything into one dashboard route.
- Do not encode session or auth state in URLs.
- Do not use vague navigation labels that users cannot predict.
- Do not ignore v2 routes when they would force a URL redesign later.

## Validate before final

- The sitemap includes public/authenticated boundaries when relevant.
- The navigation recommendation matches depth and task frequency.
- The URL conventions are explicit.

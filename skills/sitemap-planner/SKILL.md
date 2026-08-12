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
4. Split route state from client state: shareable view state (filters, sort, pagination, selected tab) belongs in URL search parameters; private transient state (unsaved form steps) stays in component state. Never encode auth or session state in URLs.
5. Identify auth and permission boundaries.
6. Recommend navigation pattern: top nav, sidebar, breadcrumbs, tabs, nested settings nav, command palette, or combination.
7. Include likely v2/v3 routes if they affect current URL choices.
8. Flag IA risks and naming ambiguity.

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

## Worked example

## Sitemap and routing plan

### Sitemap
```text
/
├── pricing
├── docs
├── login
├── (dashboard)
│   ├── projects            → /projects
│   │   └── [id]            → /projects/:id
│   ├── team
│   └── settings
│       └── billing
└── (admin)
    └── users
```

### Navigation model
Top nav for marketing; sidebar inside (dashboard); nested settings nav; breadcrumbs in admin.

### Route conventions
- lowercase kebab-case; collection = route; shareable view state (filters, sort, pagination) = URL search params, e.g. `/projects?status=active&sort=updated`
- Private transient state (unsaved form steps) stays in component state, not the URL
- Never encode auth or session state in URLs

### Auth and permission boundaries
- (dashboard) requires login; (admin) requires admin role — server-side checks, not just redirects.

### Future routes to preserve space for
- `/reports`, `/api-keys` — do not squat these names today.

### IA risks / questions
- "Projects" vs "Jobs" naming — confirm client vocabulary before locking URLs.

## Common mistakes to prevent

- Do not flatten everything into one dashboard route.
- Do not encode session or auth state in URLs.
- Do not use vague navigation labels that users cannot predict.
- Do not ignore v2 routes when they would force a URL redesign later.

## Boundaries

- Do not use when the question is one task flow — use `$user-flow-mapper`.
- Do not use when requirements are unknown — run `$requirements-from-brief` first.

## Validate before final

- The sitemap includes public/authenticated boundaries when relevant.
- The navigation recommendation matches depth and task frequency.
- The URL conventions are explicit.

## See also

- [Design Engineering guide: Information Architecture](https://frontendguide.dev/docs/information-architecture)

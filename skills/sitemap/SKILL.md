---
name: sitemap
description: "Plan or revise product navigation, route hierarchy, URL state, and access boundaries. Use when creating IA for an app, site, dashboard, or prototype before visual design or implementation."
---

# Sitemap

Map where users expect tasks and information to live. Start from vocabulary, frequency, and relationships rather than mirroring database tables.

## Work

- Inspect the existing routes and requirements. List actual URLs separately from framework folders; route groups are organizational, not authorization boundaries.
- Identify public, authenticated, organization-scoped, and privileged areas. Name where server checks enforce access, including direct requests.
- Choose navigation based on depth and task frequency. Keep labels predictable; do not invent future routes without a current reason.
- Put non-sensitive shareable view state in URL parameters. Keep credentials, personal input, and private drafts out of URLs, which can enter history, logs, and referrers.
- Define deep-link, reload, back/forward, not-found, and expired-session behavior. Validate return destinations before redirecting.
- For a revision, preserve existing URLs where possible; otherwise map redirects and check incoming links, bookmarks, metadata, and search indexing.

## Deliver

A concise route tree plus **user job, access rule, navigation location, URL state, migration/unknown** where needed. Distinguish proposed endpoints from existing ones.

Follow this shape:

Route tree: / → ... (mark proposed vs existing)
Navigation: ...
Conventions: ...
Access: ...
Migration/unknowns: ...

Example: `/projects?status=active` can preserve a list view; `/projects/:id` still checks that the signed-in user may read that project. Hiding the sidebar link does not protect the record.

Check that the primary task can be found and reopened through a direct URL. Use `$flow` for the sequence inside a task and `$hierarchy` for one page's content priority.

## Worked example

Route tree:
/ (existing)
├── pricing (existing)
├── docs (existing)
├── login (existing)
├── (dashboard) → /projects, /projects/:id, /team, /settings/billing (proposed)
└── (admin) → /users (proposed)
Navigation: top nav for marketing; sidebar inside dashboard; nested settings nav; breadcrumbs in admin.
Conventions: lowercase kebab-case; collections as routes; shareable view state in search params, e.g. `/projects?status=active&sort=updated`; keep unsaved steps in component state; never encode auth in URLs.
Access: dashboard requires login; admin requires admin role; enforce with server checks on `/projects/:id`, not hidden links.
Migration/unknowns: preserve existing marketing URLs; confirm "Projects" vs "Jobs" vocabulary before locking URLs; reserve `/reports` and `/api-keys` without building them.

## Gotchas

- Do not treat route groups or hidden links as authorization boundaries; require server checks on direct requests.
- Do not place credentials, personal input, or private drafts in URL parameters.
- Do not mirror database tables as navigation; start from vocabulary, frequency, and task relationships.
- Do not invent future routes without a current reason; reserve names without building them.
- Do not redirect to unvalidated return URLs; validate destinations before redirecting after login.

## Boundaries

- Do not use when the question is one task sequence — use `$flow` instead.
- Do not use when requirements are unknown — run `$requirements` first.

---
name: sitemap
description: "Plan or revise product navigation, route hierarchy, URL state, and access boundaries."
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

Example: `/projects?status=active` can preserve a list view; `/projects/:id` still checks that the signed-in user may read that project. Hiding the sidebar link does not protect the record.

Check that the primary task can be found and reopened through a direct URL. Use `$flow` for the sequence inside a task and `$hierarchy` for one page's content priority.

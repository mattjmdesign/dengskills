---
name: production-readiness-review
description: Use this skill when a running preview, prototype, or vibe-coded slice might be treated as a real product. Scores demo vs pilot vs production, lists UI-owned risks (secrets, permissions, XSS, SEO posture, i18n, flags), and names what must be fixed or explicitly accepted before launch.
---

# Production Readiness Review

Use this skill after something exists — a preview URL, a client demo, a PR that “looks done.” Its job is to stop a plausible UI from being silently treated as production.

## Process

1. Name the artifact (URL or PR) and the honesty level the client thinks they are getting.
2. Restate the product promise from the brief. If there is no brief, stop and run `$product-intent-clarifier`.
3. Score demo / pilot / production against data, auth, gap states, tests, and ops.
4. Inventory UI-owned risks: secrets in the client, hidden-UI-as-security, raw error rendering, uploads, public vs app SEO, locale/RTL, feature flags.
5. List keep / fix / defer. Every defer needs an owner and a trigger to revisit.
6. Recommend the next artifact: fix list, `$gap-state-inventory`, `$ui-system-governance`, or a ship decision.

## Output format

```markdown
## Production readiness review

**Artifact:**
**Stated honesty level:** demo | pilot | production
**Recommended honesty level:**
**Promise still true?** yes / no — [one line]

### Score
| Area | Demo | Pilot | Production | Notes |
|---|---|---|---|---|
| Data & persistence |  |  |  |  |
| Auth & permissions |  |  |  |  |
| Gap states |  |  |  |  |
| Security (UI-owned) |  |  |  |  |
| SEO / public surface |  |  |  |  |
| i18n |  |  |  |  |
| Tests & preview |  |  |  |  |
| Observability & rollback |  |  |  |  |

### Must fix before treating this as [level]
- [item]

### Accept explicitly
- [risk] — accepted by [who] — revisit when [signal]

### Next artifact
```

## Worked example

## Production readiness review

**Artifact:** https://preview.example.com/dashboard
**Stated honesty level:** production (client asked to “just launch”)
**Recommended honesty level:** pilot
**Promise still true?** Partially — primary job works; billing and invites are stubs.

### Score
| Area | Demo | Pilot | Production | Notes |
|---|---|---|---|---|
| Data & persistence | ✓ | ✓ | — | Real DB; no backups discussed |
| Auth & permissions | ✓ | ✓ | — | Auth works; admin is hidden UI only |
| Gap states | ✓ | — | — | Empty dashboard is blank |
| Security (UI-owned) | ✓ | — | — | `NEXT_PUBLIC` analytics key only; delete has no server check |
| SEO / public surface | ✓ | ✓ | — | App routes should be noindex; not set |
| i18n | ✓ | ✓ | ✓ | EN-only accepted |
| Tests & preview | ✓ | — | — | No CI tests; preview exists |
| Observability & rollback | — | — | — | No error tracking |

### Must fix before treating this as pilot
- Server-side permission on delete and admin routes
- Empty and error states on the project list
- Name the honesty level to the client: pilot, not launch

### Accept explicitly
- EN-only — accepted by PM — revisit at first EU customer
- No backups — accepted by eng lead — revisit before paying customers

### Next artifact
`$gap-state-inventory` on dashboard + project list; then a written client note on pilot vs production.

## Common mistakes to prevent

- Do not turn this into an OWASP or Lighthouse dump. Score the product.
- Do not invent a new roadmap. Keep / fix / defer against the existing promise.
- Do not call hidden buttons “secure.”
- Do not raise honesty level because the UI is pretty.

## Boundaries

- Do not use when nothing is runnable — specify and build a slice first.
- Do not use when the question is only visual drift — use `$ui-system-governance`.
- Do not use when the question is only missing states — use `$gap-state-inventory`.

## Validate before final

- Honesty level is named, and recommended level is not higher than the weakest row.
- Every deferred risk has an owner and a revisit signal.

## See also

- [Design Engineering guide: Production Risks the UI Owns](https://frontendguide.dev/docs/production-risks)

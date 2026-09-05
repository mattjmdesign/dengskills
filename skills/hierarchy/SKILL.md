---
name: hierarchy
description: "Rank a screen\u2019s information and actions; improve headings, decision support, and narrow-screen priority. Use when planning what belongs on a page before layout, visual design, or implementation."
---

# Content hierarchy

Help the user make the page's primary decision. Inventory real content before deciding which blocks the page should contain.

## Work

- Name the user, page purpose, and next useful action. For a reading page, comprehension may be the main job rather than conversion.
- Rank essential decision information, supporting explanation, and incidental metadata. Keep consequences near consequential actions.
- Establish a descriptive title, meaningful section headings, and reading order. Do not use visual size to choose semantic heading levels.
- Reduce competing emphasis through grouping, position, and copy before adding borders or cards.
- State what moves or collapses on narrow screens and how users retrieve it. Essential content must remain available.
- For existing pages, identify keep, rewrite, move, and remove decisions with reasons. Do not fabricate proof, customer quotes, or product capabilities to make a layout convincing.

## Deliver

A ranked content outline with sample copy where useful, action labels, responsive order, and one observable acceptance condition. Keep the response proportional to the page.

Follow this shape:

**Page purpose:** ...
**Primary decision:** ... **H1:** ...
Primary: ...
Secondary: ...
Tertiary: ...
Actions: Primary / Secondary / Destructive
Responsive priority: ...
Move / defer / remove: ...
Accessibility notes: ...

Example: an invitation screen needs recipient, organization, role, and access consequence before “Send invitation.” A decorative illustration is secondary; the role explanation is not.

Check that the first visible information answers the user's immediate question, that heading/keyboard order matches the visual sequence, and that text expansion does not bury the action. Use `$layout` for region sizing; `$craft` for a rendered composition and visual refinement.

## Worked example

**Page purpose:** Convince a visiting foreman to start a free trial.
**Primary decision:** Start free trial. **H1:** Know where your crew is this week.
Primary: 3-step explanation (schedule → assign → notify); screenshot of the weekly board.
Secondary: feature bullets (offline mode, SMS notifications); customer quote.
Tertiary: pricing link, FAQ link, legal links.
Actions: Primary — Start free trial; Secondary — See pricing; Destructive — none.
Responsive priority: H1 → CTA → screenshot → steps → features.
Move / defer / remove: Move deep-dives to a features page; remove the second hero CTA.
Accessibility notes: single h1; h2 per section; CTA is a real link.

## Gotchas

- Do not choose heading levels by visual size; keep semantic order aligned with visual and keyboard sequence.
- Do not add cards, borders, or emphasis to fix competition; regroup, reposition, and rewrite copy first.
- Do not fabricate quotes, metrics, or capabilities to fill a thin page.
- Do not hide essential content on narrow screens without a retrieval path.
- Do not separate consequential actions from their consequence explanation.

## Boundaries

- Do not use when region sizing or page shell is the question — use `$layout` instead.
- Do not use when whole-site navigation is undecided — use `$sitemap` instead.

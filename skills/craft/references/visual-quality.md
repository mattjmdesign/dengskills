# Visual quality and anti-generic design

Use this reference to create a coherent visual voice and remove accidental AI-generated aesthetics without replacing them with another formula.

## Contents

1. Coherence before novelty
2. Product UI and narrative UI
3. Common AI failure patterns
4. Repair strategies
5. Fine craft pass

## 1. Coherence before novelty

Professional design feels decided.

- Use a small visual grammar: type relationships, spacing rhythm, shape language, surface treatment, color strategy, icon style, imagery, and motion behavior.
- Tie each choice to product character or user context.
- Repeat the grammar consistently enough to form recognition.
- Allow contrast where hierarchy or meaning requires it.
- Remove effects that cannot explain their role.
- Prefer one product-native signature or consistently executed deliberate restraint over many unrelated gestures.

Distinctiveness is not a universal requirement. Familiarity, trust, speed, and low cognitive load may be the more professional choice. The goal is specific and appropriate, not merely unusual.

Before polishing, describe why this interface could belong only to this product. If the answer is only its logo and accent color, the visual direction is underdeveloped.

## 2. Product UI and narrative UI

Product and task surfaces:

- Optimize recognition, stable placement, comparison, feedback, and recovery.
- Use familiar controls unless a new interaction creates a clear task advantage.
- Keep expressive elements subordinate to ongoing work.
- Let density match frequency and expertise.
- Make system state and consequences obvious.

Narrative, campaign, portfolio, and brand surfaces:

- Use pacing, typography, imagery, composition, and motion to create a memorable sequence.
- Keep the story anchored to real product value and content.
- Preserve readable copy, obvious navigation, and meaningful calls to action.
- Avoid repeating the same section scaffold down the page.

Mixed surfaces, such as onboarding or pricing inside a product, should bridge the two deliberately rather than switching visual languages accidentally.

## 3. Common AI failure patterns

Treat these as diagnostic signals, not universal bans.

### Card soup

Signal: every heading, statistic, feature, control group, and note sits in an equally elevated rounded rectangle.

Cost: weak hierarchy, excessive containment, visual noise, and poor responsive behavior.

Ask whether the content represents a distinct object or interactive unit. Replace unnecessary cards with spacing, alignment, separators, lists, tables, or one shared surface.

### Pill soup

Signal: tabs, filters, metadata, buttons, statuses, and labels all use the same fully rounded capsule.

Cost: actions and information become hard to distinguish.

Reserve pills for compact choices, tags, or statuses whose shape carries meaning. Use other control and text treatments elsewhere.

### Generic hero formula

Signal: oversized centered headline, vague gradient word, two buttons, decorative glow, floating product mockup, and an unearned logo row.

Cost: interchangeable brand, poor information density, weak evidence.

Start from the buyer question, product proof, and desired action. Choose a composition that makes that content specific.

### Feature-icon grid

Signal: repeated colored icon square, heading, and two lines of copy in equal cards.

Cost: every benefit has equal weight and no narrative.

Group by user job, show one real workflow, use annotated product evidence, or vary composition according to importance.

### Dashboard template

Signal: sidebar, top search bar, four stat cards, line chart, and recent-activity table regardless of task.

Cost: navigation and metrics are invented before the workflow is understood.

Start with the recurring user decision. Add navigation and metrics only when they support it.

### Decorative depth

Signal: borders, large soft shadows, gradients, translucent surfaces, blur, glows, and oversized radius all appear together.

Cost: muddy hierarchy and expensive visual noise.

Choose one depth model. Use border, tonal surface, or elevation according to layer ownership.

### Centered everything

Signal: headings, body copy, lists, cards, controls, and data all align to center.

Cost: poor scanning, weak relationships, unstable long content.

Center a short focal message when appropriate. Left-align reading, forms, lists, and structured data.

### Giant type with fragile wrapping

Signal: display text dominates the viewport, breaks at arbitrary words, or overflows on intermediate widths.

Cost: reduced comprehension and brittle layout.

Cap display size from content and available width, balance short headings, and test exact copy at every topology.

### Random micro-styling

Signal: nearby components use slightly different radii, grays, padding, icon weight, or border styles.

Cost: the interface feels generated one element at a time.

Map each value to a semantic role and normalize shared primitives.

### Decoration as content substitute

Signal: abstract blobs, stock metrics, fake testimonials, or generic illustrations fill a content gap.

Cost: false product claims and weak communication.

Keep the surface honest. Use a restrained structure and flag missing content.

### State blindness

Signal: only the ideal loaded state is designed.

Cost: the interface collapses under actual use.

Design loading, empty, error, partial, disabled, success, permissions, and recovery before fine polish.

## 4. Repair strategies

When a result feels generic:

1. Remove decoration temporarily.
2. Re-rank content and actions.
3. Strengthen one layout idea: scale contrast, directional flow, density, or spatial grouping.
4. Choose a product-native signature or a deliberate-restraint strategy.
5. Reintroduce only the materials that support that idea.
6. Test real content and interaction before judging the still image.

When a result feels loud:

- Reduce the number of emphasized elements.
- Collapse the color palette into clearer roles.
- Remove redundant containers and effects.
- Restore readable text sizes and measures.
- Use one focal contrast instead of many.

When a result feels bland:

- Clarify the product thesis rather than adding random color.
- Strengthen type contrast and composition.
- Use a signature grounded in content or interaction, or strengthen the proportion, rhythm, type, and detail that make restraint feel intentional.
- Introduce meaningful imagery, data treatment, material, or motion.
- Vary narrative pacing without breaking component coherence.

When a result feels cramped:

- Fix hierarchy and remove low-value content.
- Increase group and section separation before enlarging every component.
- Let the primary region own more width.
- Change topology instead of shrinking type.

When a result feels sparse:

- Confirm that content is actually missing.
- Increase useful evidence, examples, comparisons, or next actions.
- Tune measure and composition; do not inflate type or add empty cards merely to occupy space.

## 5. Fine craft pass

Inspect at actual rendered size:

- Text baselines and icon optical alignment.
- Consistent edge alignment across regions.
- Heading line breaks and orphan words.
- Border intersections and doubled separators.
- Radius consistency and nested-radius relationships.
- Focus, hover, active, selected, disabled, loading, and error states.
- Icon family, weight, size, and stroke alignment.
- Numeric alignment and changing-value stability.
- Button label width during loading.
- Tooltip, menu, dialog, and toast placement near viewport edges.
- Sticky and fixed layers at scroll boundaries.
- Scrollbar appearance and scroll ownership.
- Image crop, focal point, resolution, and alternative text.
- Skeleton-to-content layout shift.
- Empty, one-item, many-item, and long-content rhythm.
- Dark theme, forced colors, and reduced motion when supported.

Polish should improve comprehension, confidence, and feel. Do not spend the final pass adding effects that create new hierarchy or resilience problems.

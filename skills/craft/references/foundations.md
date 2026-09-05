# Design foundations

Use this reference to convert product intent and real content into a coherent visual system.

## Contents

1. Product and audience
2. Attention and hierarchy
3. Composition and grouping
4. Typography
5. Spacing and density
6. Color and depth
7. Tokens and consistency
8. Visual direction

## 1. Product and audience

Design for a concrete situation:

- Who is using the interface?
- What are they trying to finish?
- How often do they use it?
- What is their likely level of expertise?
- What information is sensitive, urgent, uncertain, or irreversible?
- Are they scanning, comparing, reading, creating, monitoring, or transacting?
- What environment and input method are likely?

Translate the answers into interface behavior. A frequently used operations tool should optimize recognition, density, keyboard flow, and stable placement. A first-use consumer flow should optimize orientation, reassurance, and progressive disclosure. A brand-led page may prioritize narrative pacing and memorable expression, but it must still preserve comprehension and action clarity.

Do not invent product metrics, testimonials, categories, or features to fill a layout. Missing content is a product question, not a decoration opportunity.

## 2. Attention and hierarchy

Treat attention as a limited budget.

- Establish one dominant entry point per view or coherent region.
- Make the primary action the most prominent actionable element, not necessarily the largest object.
- Reduce emphasis on supporting actions through position, weight, contrast, or treatment.
- Use size, weight, contrast, color, and whitespace together. Avoid maxing out all five.
- Place related explanation near the decision it supports.
- Keep reading order aligned with DOM order and keyboard order.
- Make headings describe the content below them rather than decorate the page.
- Use progressive disclosure for advanced or infrequent decisions, never for information required to make the current decision.

Run a blur test mentally or with a screenshot: the major regions and the intended first action should remain legible when detail is ignored.

Avoid competing peaks. If the logo, heading, metric, illustration, banner, and button all demand first attention, none of them has priority.

## 3. Composition and grouping

Build the page from regions and relationships before choosing card styles.

- Start with a page frame: navigation, context, primary content, supporting content, and system feedback.
- Align meaningful edges. A small number of strong alignment lines feels calmer than many slightly different insets.
- Use proximity before borders. Use a border, background, or elevation only when it clarifies containment, separation, or interaction.
- Keep nested containers rare. A card inside a card usually means the grouping model is unresolved.
- Let important content own enough width. Do not squeeze the primary task beside a decorative or low-value rail.
- Use asymmetry when it reinforces priority, not merely to appear creative.
- Keep repeated items structurally consistent while allowing content-driven variation.
- Preserve negative space around important decisions, headings, and transitions.

Choose a container strategy deliberately:

- Reading surfaces: constrain measure and allow generous outer space.
- Work surfaces: use available width but keep controls and text in readable regions.
- Dense data surfaces: prioritize column meaning, scanning, and stable alignment.
- Immersive or canvas surfaces: minimize chrome while keeping navigation and recovery accessible.

## 4. Typography

Define roles before sizes:

- Display or page title.
- Section heading.
- Body or primary UI text.
- Label or supporting metadata.
- Data or code where a specialized face is useful.

Use the fewest roles that express the hierarchy.

- Start body text around 1rem for reading-heavy content. Dense product UI may use a carefully tested 0.875rem base, but do not use tiny text to solve crowding.
- Keep explanatory prose near 45–75 characters per line.
- Use line height roughly 1.4–1.65 for prose and tighter values for large headings or compact controls.
- Keep hierarchy visible through size and weight, not only color.
- Limit routine text weights. Too many nearby weights create noise.
- Use responsive type only where the composition benefits; product controls usually need stable sizes.
- Balance short display headings and prevent single-word orphan lines when supported.
- Preserve user text scaling. Do not freeze text inside fixed-height containers.
- Use tabular numerals for columns and changing numeric values when alignment matters.
- Use uppercase only for short, deliberate labels, not sentences.

Choose fonts from product needs. System fonts can be excellent for familiar, high-performance product UI. Expressive fonts can strengthen narrative or brand surfaces. Do not reject or add a font merely to seem designed.

## 5. Spacing and density

Use a small spacing ladder rather than unrelated numbers. A practical starting set may be 4, 8, 12, 16, 24, 32, 48, 64, adjusted to the product.

Apply nested spacing logic:

    control internals < related item gap < group gap < section gap < major transition

- Repeat spacing relationships, not necessarily identical whitespace everywhere.
- Use denser spacing for high-frequency comparison and looser spacing for orientation or high-consequence decisions.
- Add space around changes in topic, ownership, or task stage.
- Align text optically with icons and controls; mathematical centering can still look off.
- Avoid solving every issue by adding more whitespace. Density should match the job.
- Do not compress touch targets when visual density is needed. The visible glyph can be small while its hit area remains generous.

Check both sparse and dense content. A layout that only looks good with exactly three short rows is not a system.

## 6. Color and depth

Assign roles before values:

- Canvas and surface.
- Primary and secondary text.
- Border or separator.
- Brand or accent.
- Focus.
- Success, warning, danger, and informational feedback.

Keep the palette explainable.

- Use accent color primarily for action, selection, focus, or meaningful emphasis.
- Keep status colors semantically stable and pair them with text or iconography.
- Verify text and non-text contrast in actual rendered combinations.
- Avoid weak gray text on tinted surfaces.
- Use neutral surfaces to clarify layer ownership, not to create alternating decoration.
- Use elevation when one element must appear above another. Do not combine heavy borders, large shadows, blur, and glow by default.
- Keep corner radius proportional to component size and brand character. Random radius changes break family resemblance.
- Avoid gradients, glass effects, and colored blobs unless they support the chosen visual direction and survive contrast and performance checks.

Dark and light themes are environmental decisions, not genre defaults. Verify both when both are supported; do not invert colors mechanically.

## 7. Tokens and consistency

Create or reuse semantic roles:

- Color by purpose rather than hue name.
- Spacing by relationship rather than component name.
- Type by role rather than isolated pixel value.
- Radius, border, elevation, and motion as small scales.
- Component variants only when the semantic or behavioral difference is real.

Prefer semantic tokens such as surface-raised, text-muted, action-primary, and status-danger over raw color names in component code. Keep the token set small enough to understand.

When an existing system is present:

1. Inventory tokens and representative components.
2. Identify drift and missing roles.
3. Reuse sound primitives.
4. Change a shared primitive only after checking its consumers.
5. Add a new token or variant only when existing roles cannot express the need.

## 8. Visual direction

Write a direction from evidence:

    For [user in situation], the interface should feel [three qualities]
    so they can [task], expressed through [specific compositional or material choices].

Choose one product-native signature or explicitly choose deliberate restraint, not a collection of effects. A signature might be a distinctive type relationship, strong color field, unusually clear data treatment, editorial pacing, tactile control behavior, illustration system, or spatial model. Deliberate restraint still needs resolved proportion, rhythm, typography, interaction, and detail.

Then name two category defaults to resist. Examples:

- A tool does not need dark mode, neon accents, and terminal typography.
- A startup does not need a gradient hero, floating dashboard mockup, and three feature cards.
- A premium service does not need beige backgrounds, serif headlines, and excessive whitespace.
- A finance product does not need navy, gold, and generic market charts.

Do not invert a cliché into another automatic style. Derive the visual grammar from audience, content, brand, and use context.

Check coherence:

- Do typography, shape, spacing, imagery, motion, and copy sound like the same product?
- Does the signature repeat enough to feel intentional without becoming a gimmick, or does the restraint feel consistently authored rather than merely sparse?
- Can decoration be removed without harming structure? If structure collapses, hierarchy is under-designed.
- Is the result familiar enough to operate and distinct enough to belong to this product?

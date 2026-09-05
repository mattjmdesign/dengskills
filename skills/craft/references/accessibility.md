# Accessibility and inclusive interaction

Use this reference as a practical implementation and verification guide. For web work, use WCAG 2.2 Level AA as the default baseline unless the project specifies another standard. For native software, map the same user outcomes to platform semantics, text scaling, accessibility APIs, input methods, and applicable platform or legal requirements; use WCAG2ICT as supporting guidance where relevant. This reference supports, but does not replace, complete conformance evaluation, assistive-technology testing, or expert review.

Distinguish the source of a rule:

- Baseline: applicable WCAG 2.2 Level A and AA success criteria.
- Safety margin: stronger defaults such as 44 by 44 CSS pixel touch areas and robust focus appearance.
- Craft heuristic: evidence-informed guidance that improves usability but is not itself a conformance requirement.

Only WCAG success criteria are normative for WCAG conformance. W3C Understanding pages, techniques, ARIA Authoring Practices, and design-system guidance are informative. Never infer conformance from a short checklist or automated scan.

Choose the semantic track first:

- Web: apply HTML semantics, DOM order, ARIA only where needed, CSS-pixel reflow, browser zoom, and WCAG 2.2 checks.
- Native: use the platform's semantic controls, accessibility tree and APIs, traversal model, user text scaling, appearance settings, and supported assistive technologies. Use platform-adaptation.md for the completion matrix.

## Contents

1. Semantics and structure
2. Keyboard and focus
3. Names, instructions, and errors
4. Visual access
5. Pointer and touch
6. Motion and media
7. Dynamic content
8. Test sequence
9. Standards anchors

## 1. Semantics and structure

Start with native HTML or platform controls.

- On the web, use landmarks for header, navigation, main content, complementary content, and footer.
- Keep one descriptive page or screen title and a logical heading or semantic grouping hierarchy. Do not choose semantic levels for visual size.
- On the web, use buttons for actions, links for navigation, lists for lists, and tables for tabular relationships. On native platforms, use the equivalent platform-native roles and controls.
- Preserve a logical semantic and accessibility traversal order even when visual layout changes. For web work, keep DOM order aligned with that sequence.
- Support portrait and landscape unless a specific orientation is essential to the task.
- Give repeated landmarks and navigation regions distinguishable names.
- Associate table headers with the data they describe.
- Identify language changes when they affect pronunciation.
- Keep decorative images out of the accessibility tree and give informative images a useful text alternative.

On the web, use ARIA only when native HTML semantics cannot express the pattern. On native platforms, add custom accessibility metadata only when the platform control does not already expose the correct role, name, value, and state. Do not implement only part of a composite pattern.

## 2. Keyboard and focus

Every supported input method needs a complete path. On keyboard-capable surfaces, every pointer action needs a keyboard path unless the task is inherently path-based and an equivalent exists. On touch-first native surfaces, verify the platform's focus or traversal model and relevant assistive inputs rather than inventing web keyboard behavior.

- Keep interactive elements in a logical focus order.
- Avoid positive tabindex values.
- Make focus visible against every background and component state.
- Do not remove outlines without an equally visible replacement.
- Ensure sticky headers, dialogs, and overlays do not obscure the focused element.
- Support expected keys for tabs, menus, listboxes, trees, dialogs, and other composite widgets.
- Move focus only when context changes enough to require it, such as opening a modal or presenting a submission error summary.
- Return focus after dismissing a temporary surface.
- Provide a skip path around repeated navigation on content-heavy pages.
- Avoid keyboard traps, including nested scroll regions and hidden offscreen controls.

Test the entire primary task from a fresh page load using only the keyboard. A component-by-component spot check is not enough.

## 3. Names, instructions, and errors

Every control needs a name that describes its purpose.

- Prefer a visible label associated programmatically with the control.
- Make icon-only controls understandable to assistive technology and sighted users.
- Keep accessible names aligned with visible labels so voice-control users can target them.
- Put format requirements and constraints before or near the field.
- Identify invalid fields in text and associate the error with the field.
- Suggest a correction when known.
- Preserve entered values after errors.
- Announce an error summary or focus it when a failed submission affects multiple fields.
- Do not require users to re-enter information already supplied in the same process unless essential.
- Keep authentication possible without puzzles dependent on memory, transcription, or a single sensory ability.
- For legal, financial, destructive, or stored-data changes, provide review and correction, reversibility, or a clear confirmation step as appropriate.
- Do not block password managers or paste without an essential security reason and an accessible alternative.

Do not rely on placeholder text, tooltip-only instructions, color, position, or icon shape as the sole label.

## 4. Visual access

Verify rendered combinations rather than token names.

- Maintain at least 4.5:1 contrast for normal text and 3:1 for large text under WCAG AA definitions.
- Maintain at least 3:1 contrast for meaningful non-text boundaries and states such as focus indicators and control outlines where required.
- Do not use color as the only cue for status, selection, validation, or chart meaning.
- Support text resizing to 200 percent without loss of content or function.
- For web content, support reflow without loss of content or function at 320 CSS pixels wide for vertically scrolling content, the common equivalent of 400 percent zoom on a 1280 CSS pixel viewport.
- For web content designed to scroll horizontally, verify the corresponding 256 CSS pixel height requirement. Treat genuinely two-dimensional content such as maps, diagrams, video, games, presentations, and data tables as scoped exceptions, not a reason to exempt the whole page.
- For native content, verify the platform's supported user text-scaling range at the smallest supported window or device surface, including split or multi-window conditions where applicable.
- Survive user text-spacing overrides of 1.5 line height, 2 times paragraph spacing, 0.12em letter spacing, and 0.16em word spacing without losing content or function. These are resilience test values, not mandatory authored defaults.
- Avoid fixed-height text containers that clip after scaling.
- Keep important text in real text rather than images.
- Preserve usability in forced-colors or high-contrast modes when the platform supports them.
- Do not disable browser zoom.

Muted text is still text. If it communicates useful information, it must remain readable.

## 5. Pointer and touch

- On the web, provide comfortable hit areas. Aim for at least 44 by 44 CSS pixels for primary touch controls when the platform permits.
- On the web, at minimum make pointer targets 24 by 24 CSS pixels or satisfy a documented WCAG spacing or equivalent-control exception.
- On native platforms, follow the target platform's current target-size guidance in its own units and verify the actual hit area, not only the visible glyph.
- Keep the visible target and hit target spatially aligned.
- Avoid interactions that require precise dragging. Provide buttons, menus, or fields as alternatives.
- Provide a single-pointer alternative to multipoint or path-based gestures unless the gesture is essential.
- Provide a click or tap alternative to dragging unless dragging is essential.
- Prefer activation on pointer-up, or provide cancellation or undo for accidental activation.
- Let users cancel an accidental pointer action before completion when possible.
- Do not place unrelated destructive and primary targets tightly together.
- Support hover information on focus and make it dismissible and persistent long enough to use.
- Make content that appears on hover or focus dismissible, hoverable, and persistent until the trigger loses hover or focus, the content becomes invalid, or the user dismisses it.

Test with touch emulation only as a supplement. Real mobile browser and on-screen keyboard behavior can differ.

## 6. Motion and media

- Respect prefers-reduced-motion and remove or simplify nonessential animation.
- Avoid flashing that can trigger seizures.
- Provide pause, stop, hide, or update-frequency controls for automatically moving or updating content when WCAG requires them.
- Do not require motion gestures without a conventional control alternative.
- Let users pause moving, blinking, scrolling, or auto-updating content when it competes with reading.
- Keep essential content available without animation completing.
- Provide captions for prerecorded spoken video and transcripts or equivalent alternatives where required.
- Do not autoplay audio unexpectedly.
- Keep animation purposeful, brief, and free of layout instability.

Reduced motion is not always zero motion. Preserve necessary state change through an immediate transition, crossfade, or other low-motion alternative.

## 7. Dynamic content

Dynamic updates need the right notification, not the loudest notification.

- Move focus for a new context that requires immediate interaction, such as a modal.
- Use a status message or polite live region for nonblocking results.
- Use assertive announcements sparingly for urgent conditions.
- Avoid announcing rapid intermediate updates.
- Keep loading state, disabled state, and progress semantics synchronized with the visual UI.
- Announce sortable table state, expanded state, selected state, validation state, and current navigation state programmatically.
- Preserve focus when lists refresh or items are removed. Move it to the nearest logical target when the focused item disappears.
- Make timeouts discoverable and extendable when the user can lose work.

Screen readers do not need every visual detail, but they do need equivalent purpose, structure, state, and outcome.

## 8. Test sequence

Run the smallest trustworthy sequence:

1. Inspect semantic structure and accessible names in the accessibility tree.
2. Complete the primary task with keyboard only on keyboard-capable targets. On touch-first native targets without a supported keyboard path, complete it with touch and the platform's primary accessibility traversal or control method.
3. Check focus visibility, traversal order, traps, and overlay behavior wherever the platform exposes focus or accessibility traversal.
4. Run automated accessibility checks for detectable issues.
5. Verify contrast in actual rendered states.
6. On the web, test 200 percent text resize and reflow at 320 CSS pixels wide; test 256 CSS pixels high for horizontally scrolling content when applicable. On native platforms, test supported user text scaling at the smallest supported surface.
7. Test reduced motion and forced colors when relevant.
8. Test at least one representative screen-reader flow for high-impact or custom interaction.
9. Recheck after fixes; automation cannot prove the absence of barriers.

Document the browser or platform, viewport, window or device surface, input method, state, and tool used. Mark untested areas unverified.

## 9. Standards anchors

Use current official guidance when a conformance claim matters:

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI tutorials: https://www.w3.org/WAI/tutorials/
- ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Understanding WCAG 2.2: https://www.w3.org/WAI/WCAG22/Understanding/
- WAI evaluation guidance: https://www.w3.org/WAI/test-evaluate/
- WCAG2ICT for non-web software: https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/

For web products, treat platform guidelines as additional context, not substitutes for web accessibility requirements. For native products, use the target platform's current accessibility guidance and APIs alongside applicable standards and requirements.

# Components, states, and interaction

Use this reference to turn a screen into predictable, reusable behavior rather than a static arrangement.

## Contents

1. Component contract
2. Action hierarchy
3. Forms
4. Navigation and disclosure
5. Dialogs, menus, and overlays
6. Data and collections
7. Async feedback and recovery
8. UX copy
9. State inventory

## 1. Component contract

Define a component by responsibility, anatomy, semantics, variants, states, content limits, and responsive behavior.

For each meaningful component, answer:

- What user or system job does it own?
- What is its semantic element or interaction pattern?
- Which parts are required and optional?
- Which variants represent a real semantic difference?
- What are its default, hover, focus, active, selected, disabled, loading, error, and success behaviors?
- What happens with long, missing, or translated content?
- What changes when its container becomes narrow?
- Which events or state changes does it expose?
- How is it named and operated without a pointer?

Keep primitive components flexible and product components opinionated. Do not build a universal component with dozens of booleans when composition would express the structure more clearly.

Preserve one source of truth for behavior. A visual button variant should not silently change business logic.

Organize implementation by ownership:

- Primitives own semantics, interaction mechanics, tokens, and low-level variants.
- Product components own a recognizable domain job and its content contract.
- Screens or feature compositions own data orchestration, task order, and layout topology.
- Keep state near the smallest owner that can coordinate it without duplicating truth.
- Extract repetition only when behavior and meaning repeat, not merely because two fragments look similar once.
- Keep a component's styles, tests, examples, and accessibility notes discoverable according to the host project's conventions.

## 2. Action hierarchy

Give actions stable semantic levels:

- Primary: advances the main task.
- Secondary: supports the task without being the default.
- Tertiary or quiet: low-emphasis local action.
- Destructive: causes meaningful loss or irreversible change.

Use one primary action per decision region. A page can contain multiple regions, but competing primary buttons should not appear without clear scoping.

Button rules:

- On the web, use a button for an action and a link for navigation. On native platforms, use the platform control and role that distinguishes action from navigation.
- Label with a specific verb and object: Save changes, Invite member, Download report.
- Keep visible text for important actions. Use icon-only controls only when the symbol is conventional and an accessible name and tooltip are present.
- Keep loading labels stable when width changes would cause layout shift. Preserve enough context to explain the pending action.
- Prevent duplicate submission while preserving focus and status feedback.
- Explain why an action is unavailable when the reason is not obvious.
- Keep destructive styling proportional. Do not make every cancel or remove action visually alarming.
- Place destructive actions away from routine primary actions and provide undo or confirmation based on consequence.

Do not use disabled controls to hide product rules. Provide the condition or next step when users can resolve it.

## 3. Forms

Design forms around decisions and recovery.

- Use a persistent visible label. Placeholder text may show an example, never the only label.
- Keep helper text close to the field and validation text closer still.
- Mark optional or required fields consistently; avoid asterisks without explanation.
- Match input type, input mode, autocomplete, and keyboard to the data.
- Preserve user input after a validation or network error.
- Validate at a humane time. Do not show an error before the user has had a reasonable chance to respond.
- Identify errors in text, associate them with fields, and provide a correction path.
- On failed submission, focus or announce an error summary when multiple fields need attention.
- Group related controls semantically. On the web, use fieldset and legend where that relationship matters; on native platforms, use the equivalent accessibility grouping and label.
- Use radio buttons for a small visible set of mutually exclusive choices, checkboxes for independent choices, and a select or combobox only when the list justifies it.
- Do not replace familiar inputs with custom controls unless the interaction gain outweighs keyboard, mobile, and accessibility cost.
- Keep labels and fields in a stable order across responsive topologies.
- Reserve space or use careful layout for inline messages so validation does not cause destructive shifting.

For high-consequence actions, show what will happen before submission. For sensitive data, explain storage and visibility near the field.

## 4. Navigation and disclosure

Navigation should answer where am I, what is here, and where can I go next.

- Mark the current location visually and semantically.
- Keep the navigation label stable across surfaces.
- Use breadcrumbs when they explain real hierarchy, not as decoration.
- Use tabs for peer views of the same context, not for sequential steps or unrelated destinations.
- Keep tabs reachable and operable with the expected keyboard model.
- Use accordions for optional detail, not to hide the primary task or split a short page into needless clicks.
- Use steppers only when order, progress, or validation across stages is meaningful.
- Preserve back, cancel, and exit behavior in multi-step flows.
- Avoid dead ends. Every empty, permission-limited, or error surface should provide an appropriate next action.

If a disclosure trigger changes content, update its accessible expanded state and preserve a logical focus position.

## 5. Dialogs, menus, and overlays

Use overlays for temporary, focused work.

- Prefer inline or dedicated-page content when the task is complex, deep-linkable, or frequently compared with background content.
- Give dialogs a clear title, initial focus, contained keyboard focus when modal, Escape behavior where safe, and focus return to the trigger.
- Keep the close action discoverable and avoid multiple competing dismissal patterns.
- Do not make destructive confirmation dialogs vague. Name the object, consequence, and action.
- Position menus and popovers within the usable viewport and escape clipping or stacking contexts.
- Close transient surfaces on an intentional outside interaction without discarding in-progress work silently.
- Keep tooltips supplemental. Never place required instructions or actions only in a tooltip.
- Avoid hover-only popovers. Support focus and touch.
- Prevent background scroll only while a modal truly owns interaction, and restore it cleanly.

Use platform-native dialog, popover, and disclosure semantics when they meet the interaction. On the web, add ARIA only to complete a pattern, not to imitate semantics on arbitrary containers.

## 6. Data and collections

Choose the representation from the user task:

- Lists for scanning and selecting items.
- Tables for comparing values across a shared column model.
- Cards for distinct objects with meaningful boundaries and mixed content.
- Description lists for label-value relationships.
- Charts for patterns, with accessible numeric alternatives for essential data.

Do not default to equal cards for every collection.

For collections:

- Keep selection, hover, and focus visually distinct.
- Keep row-level actions available without hover.
- Make bulk-selection scope and effect explicit.
- Preserve filters and sort when returning from detail when users expect continuity.
- Show the active filter state and a clear reset path.
- Distinguish no results from no data and from unavailable data.
- Keep pagination or infinite loading status understandable and keyboard reachable.
- Use skeletons only when they resemble the stable final structure and the delay warrants them.

For drag and drop, provide a non-drag alternative, clear drop targets, and confirmation of the new order or location.

## 7. Async feedback and recovery

Every asynchronous action needs:

1. An immediate acknowledgment.
2. A stable pending state.
3. A clear success or error outcome.
4. A retry, correction, undo, or support path when failure is recoverable.

Choose the feedback surface by scope:

- Inline feedback for a local field or component.
- Region status for a section or data view.
- Toast for nonblocking confirmation that does not require a decision.
- Banner for persistent page-level conditions.
- Dialog for an interruptive decision requiring immediate attention.

Do not use a toast for a failure whose recovery controls disappear with it. Do not announce the same event in multiple competing surfaces.

Differentiate:

- Initial loading from background refresh.
- Empty data from no search results.
- Partial data from complete success.
- Permission denial from generic failure.
- Offline or timeout from validation errors.

Keep stale content visible during safe background refresh when it helps continuity. Indicate freshness when decisions depend on it.

## 8. UX copy

Write specific, operational language.

- Prefer user vocabulary over internal system names.
- State what happened, why it matters, and what the user can do next.
- Keep headings and button labels distinct; do not repeat the same sentence three times.
- Use sentence case unless the brand system establishes another readable convention.
- Avoid generic labels such as Submit, Continue, Learn more, OK, and Yes when a specific action fits.
- Keep link text meaningful out of context.
- Put important qualifications before commitment, not in tiny copy afterward.
- Use calm, direct language for errors. Do not blame the user.
- Preserve important nouns when shortening copy for narrow layouts.
- Format dates, numbers, currency, names, and addresses for the target locale.

Do not generate empty marketing superlatives to make a sparse screen feel complete.

## 9. State inventory

Create a compact matrix for each critical surface:

| State | Trigger | Visible UI | Available actions | Focus or announcement | Recovery |
| --- | --- | --- | --- | --- | --- |
| Ready | Data available | Primary content | Main and secondary actions | Natural reading order | Not needed |
| Loading | Initial request | Stable progress treatment | Cancel if applicable | Announce meaningful delay | Retry after failure |
| Empty | Valid zero data | Explanation and next step | Create, import, or clear filter | Heading receives context | User action |
| Error | Failed operation | Specific error near scope | Retry, correct, undo, support | Focus or live announcement | Preserve work |
| Success | Completed action | Confirmation and new state | Logical next action | Polite status | Undo if appropriate |
| Disabled | Rule prevents action | Control plus reason | Resolve prerequisite | Remains understandable | Clear requirement |
| Permission | Access restricted | Scope and owner | Request access or return | Heading and explanation | Escalation path |

Add domain states such as partial, stale, offline, conflict, destructive confirmation, or expired session when the workflow can reach them.

Do not declare a surface complete when only its ideal state exists.

# Platform adaptation

Use this reference when the target is native mobile, tablet, desktop, cross-platform, or a product that spans web and native clients. Preserve the shared product logic, but express it through the target platform's layout, navigation, control, input, and accessibility conventions.

## Contents

1. Choose a platform track
2. Shared product contract
3. Web track
4. Native mobile and tablet track
5. Native desktop track
6. Cross-platform track
7. Adaptive verification matrix

## 1. Choose a platform track

Before designing, name:

- Target operating systems, device classes, and framework.
- Minimum supported OS or browser versions when known.
- Smallest and largest supported window or surface.
- Portrait, landscape, split-view, multi-window, foldable, or external-display conditions that matter.
- Expected inputs: touch, keyboard, pointer, stylus, gamepad, spatial input, voice, switch, or screen reader.
- Platform navigation and lifecycle behavior that must remain familiar.

Do not apply HTML, CSS pixels, hover, DOM order, or browser zoom rules literally to native software. Translate the user outcome to native layout primitives, semantic controls, accessibility APIs, text scaling, window behavior, and platform tests.

## 2. Shared product contract

Keep these outcomes consistent across platforms:

- The same primary user, task, success condition, content priority, terminology, and consequence model.
- Clear orientation, action hierarchy, feedback, recovery, and non-happy states.
- Resilience to long content, localization, user text scaling, sparse and dense data, and interrupted work.
- Semantic controls, accessible names, logical traversal, perceivable state, comfortable targets, and reduced-motion behavior.
- One coherent brand system adapted to platform materials and conventions rather than copied pixel for pixel.

Allow platform differences when they improve familiarity or capability. Navigation placement, menus, selection, disclosure, back behavior, window chrome, and command surfaces may differ while preserving the same product model.

## 3. Web track

Use semantic HTML, native browser behavior, intrinsic CSS layout, DOM reading order, keyboard focus, pointer and touch paths, browser zoom, text resize, reflow, reduced motion, forced colors, and supported responsive widths.

Apply the exact web checks in responsive-layout.md and accessibility.md, including WCAG reflow conditions where applicable. Verify route identity, browser behavior, console output, and page-level overflow.

## 4. Native mobile and tablet track

Prefer the target platform's native controls, navigation model, typography system, safe-area handling, and accessibility semantics.

- Support user font scaling or dynamic type without clipping, overlap, lost actions, or fixed-height text containers.
- Adapt from compact phone surfaces through landscape, tablet, split view, resizable windows, and relevant fold or hinge conditions.
- Respect system bars, cutouts, safe areas, on-screen keyboards, and edge gestures.
- Preserve expected back, dismissal, tab, stack, sheet, and deep-link behavior.
- Keep touch as a complete path; add keyboard, pointer, stylus, switch, voice, and screen-reader paths when supported by the target device and task.
- Verify focus restoration, announcements, rotor or traversal order, custom gestures, and alternatives to drag or multipoint interaction.
- Test background, resume, interruption, permission denial, offline, and stale-session behavior when the workflow can encounter them.

Use platform units and current platform guidance for minimum targets and spacing. A 44 by 44 CSS-pixel web safety margin is not a literal native measurement.

## 5. Native desktop track

Design for resizing, precision input, keyboard efficiency, multiple windows, and persistent work.

- Define a usable minimum window size and a deliberate wide-window strategy.
- Keep content readable without stretching every region across the available window.
- Support complete keyboard traversal, visible focus, shortcuts that do not conflict with the platform, pointer context, and screen-reader operation.
- Use familiar menus, toolbars, sidebars, inspectors, dialogs, selection models, drag behavior, and window controls for the target OS.
- Preserve user work across window changes, cancellation, failed saves, conflicts, and app relaunch where the product contract requires it.
- Verify text scaling, high-contrast or forced-color modes, reduced motion, and system appearance settings supported by the platform.

Do not make a desktop app feel like a fixed phone canvas or a browser page with native chrome attached.

## 6. Cross-platform track

Share product decisions, semantic tokens, content models, and domain components where useful. Keep platform adapters for navigation, commands, system surfaces, accessibility semantics, input, and lifecycle behavior.

- Avoid a lowest-common-denominator component library that erases native expectations.
- Do not fork behavior invisibly: the same label and appearance should not produce different consequences without a platform reason.
- Keep platform-specific code at explicit ownership boundaries.
- Test each target independently; success on one renderer does not prove another.
- Record intentional differences so future agents do not “normalize” them away.

## 7. Adaptive verification matrix

For every supported platform, record:

| Condition | Evidence to collect |
| --- | --- |
| Surface | Smallest, transition, and largest supported window or device size |
| Content | Long localized labels, large user text, sparse data, dense data, and unbroken values |
| Orientation and windowing | Relevant portrait, landscape, split, resize, fold, or multi-window cases |
| Inputs | Every primary platform input plus relevant assistive technology |
| Appearance | Supported light, dark, high-contrast, forced-color, and reduced-motion settings |
| System UI | Safe areas, system bars, keyboard, menus, sheets, overlays, and window edges |
| Lifecycle | Loading, empty, error, offline, permission, interruption, resume, and recovery as applicable |
| Critical task | A safe replay through confirmation, feedback, and recovery without unauthorized external mutation |

Use the platform's inspector, accessibility tools, test framework, screenshots or recordings, and direct interaction. Mark any unsupported or untested condition explicitly; do not substitute a web-only automated score for native verification.

# Review, evidence, and verification

Use this reference to audit an interface or verify a build or improvement. For ordinary work, keep evidence as concise notes and captures. The structured records, gates, and schema below apply when producing a formal scorecard; they are not required paperwork for every UI edit. Preserve the same distinction between observed, failed, and unverified checks in either format.

## Contents

1. Evidence sources
2. Evaluation gates
3. Finding model
4. Severity and confidence
5. Scorecard
6. Audit procedure
7. Verification procedure
8. Output contracts

## 1. Evidence sources

Use the strongest available evidence:

1. Reproduced behavior in the live interface.
2. Rendered screenshot or video at a named viewport, window or device size, and state.
3. Accessibility tree or inspector, computed layout or styles, browser or app console, or automated test output.
4. Source file and line with a direct, explainable consequence.
5. Inference from surrounding implementation.

Do not present an inference as a reproduced defect. Static code can confirm some semantic or token issues but cannot prove visual quality, reading order, keyboard behavior, or responsive success.

For each check, record the route, screen, or component; viewport, window, or device size; state; input method; theme; and relevant content stress.

Use production content as evidence without mutating it. Exercise future volume, missing media, and empty states with isolated fixtures or test data. A polished fallback that invents plausible people, publications, testimonials, activity, metrics, or other factual claims is a content-integrity defect, not successful design completion.

For multi-surface work, also maintain a target inventory. Name every primary surface and explicitly highlighted control, then include at least one representative surface from each remaining page family. When the user names the whole site, app, or product, inventory every discoverable user-facing route family and shared global region and state exclusions before work. Record each target's Preserve, Repair, Refine, Recompose, Create, or Evaluate disposition; rationale; intended outcome; status; and evidence. A sample can support discovery, but cannot silently narrow the stated scope.

Represent each scorecard evidence item as a structured record with all of:

- evidence_type: one enumerated type from the generated template, such as screenshot, interaction_replay, test_output, accessibility_tree, source_reference, or measurement.
- artifact: screenshot, recording, test output, accessibility-tree capture, or source reference.
- location: route, screen, component, or file and line.
- viewport_or_state: viewport, theme, content case, and state; use “not applicable” only when genuinely irrelevant.
- input_methods: one or more enumerated methods such as keyboard, pointer, touch, screen_reader, voice_control, automation, or static_inspection.
- method: browser, tool, test, or reproduction procedure.
- result: the observable outcome, not “checked,” “pass,” or another conclusion-only placeholder.

Use a stable artifact locator: a file, capture, report, tool export, URL, or source line. “Manual review,” “all screens,” and “everything passed” are not evidence.

## 2. Evaluation gates

Use pass, fail, unverified, or not-applicable. In the JSON scorecard, encode not-applicable as `na`.

### G0 Intent

Know the primary user, critical task, success condition, named scope targets, constraints, and material assumptions.

### G1 Structure

Define content priority, reading order, main layout regions, responsive intent, required states, design opportunities, and the chosen direction.

### G2 Functional

Make the critical task executable with clear controls, feedback, consequences, and recovery.

### G3 Resilience

Render narrow, intermediate, and wide layouts plus at least one content-stress case. Replay a materially different route or state at one unchanged size and inspect unexpected movement. Prove client-routed transitions remained in the same document and that the interactive runtime was attached; full reloads do not count. Leave no unintended page overflow, overlap, clipping, destructive wrapping, or dynamic instability.

### G4 Inclusive interaction

Check semantics, accessible names, keyboard traversal, visible focus, contrast, zoom or text scaling, target sizing, and motion behavior as applicable.

### G5 Craft

Meet the non-substitutable authorship ceiling. Realize the design thesis through coherent hierarchy, composition, typography, rhythm, color, materials, iconography, component treatment, product specificity, and context-appropriate expression. A clean and consistent result is not sufficient by itself.

### G6 Regression

Replay the critical task after changes, prove coverage of every named target, discovered in-scope route family, and shared global region, compare the baseline or stated intent with the final result, check affected siblings after systemic fixes, and document exceptions.

A professional-grade Build or Improve claim requires G0–G6 to pass. A professional Audit claim requires G0–G5; G6 may be `na` with the explicit reason that the audit made no changes. Unverified is not pass. Give a specific reason for every not-applicable gate; if no gate applies, the evidence is incomplete. Say “no issues found in the tested scope,” not “WCAG compliant,” unless a complete conformance evaluation was actually performed.

For each gate, populate its `coverage` array with these exact check identifiers:

| Gate | Required coverage for pass |
| --- | --- |
| G0 | `primary_user`, `critical_task`, `success_condition`, `scope_targets`, `constraints_assumptions` |
| G1 | `content_priority`, `reading_order`, `layout_regions`, `adaptive_behavior`, `required_states`, `design_opportunity`, `design_direction` |
| G2 | `critical_task_replay`, `control_feedback`, `error_recovery` |
| G3 | `narrow_size`, `intermediate_size`, `wide_size`, `content_stress`, `overflow_overlap_clipping`, `dynamic_layout_stability` |
| G4 | `semantics_names`, `keyboard_or_platform_input`, `visible_focus`, `contrast`, `zoom_or_text_scaling`, `target_size`, `reduced_motion` |
| G5 | `design_thesis_realized`, `hierarchy`, `typography`, `composition_rhythm`, `color_material_iconography`, `component_coherence`, `product_specificity_brand_fit`, `signature_or_restraint_execution`, `rendered_critique` |
| G6 | `critical_task_regression`, `in_scope_surface_coverage`, `named_target_coverage`, `baseline_or_intent_comparison`, `affected_siblings`, `exceptions_recorded` |

A passing G3 needs distinct evidence at three exact sizes, a named content-stress case, and a same-size route or state transition with an observable stability result. A passed short-to-long route case must identify a same-document client-side transition. A passing G4 needs at least two observed or runtime accessibility/interaction records across at least two direct input or assistive-technology methods; source declarations do not count. A passing G5 needs rendered evidence from at least two observations; completed Create or Recompose work and completed primary Refine work also need a rendered critique iteration and final render. Required baseline, iteration, and final phases use distinct artifact locators. A passing G6 needs runtime interaction-replay, video, or test evidence that the critical task was replayed after the change and that every in-scope target was covered. Mark a gate unverified when this coverage was not actually performed.

The priority sequence is not a completion shortcut. Functional, accessibility, resilience, semantic, test, and infrastructure work cannot stand in for a requested visual or compositional improvement.

## 3. Finding model

Use one record per distinct root cause:

| Field | Meaning |
| --- | --- |
| ID | Stable identifier |
| Location | Screen, route, component, or file and line |
| Viewport or state | Conditions needed to observe it |
| Observation | What directly happens |
| Evidence | Screenshot, reproduction, tool output, or source location |
| User impact | Task, comprehension, access, trust, or efficiency cost |
| Root cause | Underlying design or implementation reason |
| Severity | P0, P1, P2, or P3 |
| Confidence | Confirmed, likely, or hypothesis |
| Scope | Systemic or local |
| Affects primary flow | True when the finding touches the critical task; false otherwise |
| Remediation | Smallest durable fix |
| Verification | Exact check that proves the fix |
| Status | Open, resolved, or accepted |

Do not create several findings for the same token or component defect. Record one systemic finding and name affected surfaces.

`accepted` means the risk was consciously accepted, not fixed; it remains unresolved for score caps and release judgment.

## 4. Severity and confidence

### Severity

- P0 Blocker: the critical task cannot be completed; behavior is destructive or unsafe; or a required input method cannot operate the flow.
- P1 Major: materially impairs a primary task, creates a major accessibility barrier, repeatedly breaks responsive use, or causes serious ambiguity or loss of work.
- P2 Moderate: localized friction, readability, feedback, state, consistency, or recovery issue with a viable workaround.
- P3 Polish: low-impact visual or interaction refinement.

Prioritize user harm and task impact, not how visually obvious a defect appears. A systemic P2 may outrank several local P2 findings.

### Confidence

- Confirmed: directly reproduced or observed.
- Likely: strong evidence supports the finding but the complete behavior was not reproduced.
- Hypothesis: plausible and worth checking, but evidence is incomplete.

Do not lower severity because confidence is low. Keep the dimensions separate and verify high-impact hypotheses first.

## 5. Scorecard

Use scoring to summarize evidence, not replace findings.

Rate each dimension from 0 to 4:

- 0: missing or fundamentally broken.
- 1: severe shortcomings.
- 2: functional but generic, inconsistent, fragile, or incompletely verified.
- 3: professional, coherent, resilient, and evidenced.
- 4: exceptionally refined, highly adaptive, and low-friction.

| Dimension | Weight |
| --- | ---: |
| Product intent, hierarchy, and content priority | 10 |
| Layout, spacing, alignment, and density | 15 |
| Typography and readability | 10 |
| Responsive and content resilience | 15 |
| Interaction, states, feedback, and recovery | 10 |
| Accessibility and input methods | 10 |
| Component and system coherence | 10 |
| Design authorship and product specificity | 10 |
| Visual craft and brand fit | 10 |

Apply caps:

- Any unresolved P0: overall score cannot exceed 49 and the result is not viable.
- Any unresolved P1 affecting the primary flow: overall score cannot exceed 69.
- Any other unresolved P1: overall score cannot exceed 79 and cannot receive a ready or exceptional judgment.
- Any failed applicable gate: overall score cannot exceed 69.
- Any unverified applicable gate: overall score cannot exceed 79.
- No applicable gates: overall score cannot exceed 79 and the judgment is evidence incomplete.
- A dimension without evidence cannot exceed 2.
- A professional-grade result requires every dimension to reach at least 3; a high total cannot hide weak layout, authorship, craft, or accessibility.

Interpretation:

- 90–100: exceptional.
- 80–89: strong and ready for its intended release bar.
- 70–79: usable but meaningful work or evidence remains.
- Below 70: not ready.

The release judgment must follow gate status and findings, even when the weighted total is high.

## 6. Audit procedure

1. Confirm Audit mode and the no-edit boundary.
2. Identify the critical task and supported environments.
3. Inspect design-system, component, and content context.
4. Inventory primary, representative, supporting, and explicitly named surfaces; record Preserve, Repair, Refine, Recompose, or Evaluate decisions.
5. Render representative narrow, intermediate, and wide views when possible.
6. Confirm the target is local or a designated test environment with disposable or isolated data.
7. Replay only the non-consequential portion of the critical task and inspect non-happy states. Do not send, charge, order, delete, publish, or mutate external state without explicit authorization.
8. Test keyboard, focus, zoom, content expansion, reduced motion, dynamic stability, and touch or pointer behavior as applicable.
9. Run automation and the conservative source scan as supporting evidence.
10. Group observations by root cause.
11. Assign severity and confidence from user impact.
12. Return findings first, followed by gate status, scorecard if useful, strengths, and unverified areas.

Avoid rewriting the product from personal taste. Tie aesthetic findings to hierarchy, brand fit, comprehension, coherence, or task behavior.

## 7. Verification procedure

For a build or improvement:

1. Start the actual target application and confirm the route or screen identity.
2. Confirm it is local or a designated test environment and that data is disposable or safely isolated. If not, stop before consequential actions and mark those checks unverified.
3. Inventory every named target and every discovered in-scope route family and shared global region; list exclusions. Use a representative page to prove each family implementation and capture matching baselines for Improve work.
4. Render and critique the first implementation at thumbnail and actual size, revise the highest-leverage issue, and capture the result when the mandate includes visible work.
5. Test the narrowest supported width, one intermediate transition width, and a comfortable wide width.
6. Test immediately on both sides of layout transitions.
7. Apply long-label, dense, sparse, and relevant error or loading cases.
8. At one unchanged size, replay short-to-long route or state changes, overlay scroll locking, and applicable font, media, skeleton, or async transitions. Prove the runtime is attached and client routes remain same-document. Compare named persistent-anchor x, y, width, and height geometry plus scroll behavior; use client width and gutter as diagnostics when compensated scroll locking preserves the anchor.
9. Complete the safely testable task with pointer or touch.
10. Complete it with keyboard when the platform supports keyboard interaction.
11. Check focus, announcements, contrast, zoom or scaling, target size, and reduced motion as applicable.
12. Inspect overlays, scrolling, sticky layers, viewport edges, and layout-shift evidence.
13. Inspect console and test output.
14. Re-run the safely testable critical path after the final change.
15. Compare baseline or stated intent with final captures and record residual risks and exact unverified areas.

Do not stop at a clean screenshot. A polished static state can conceal broken workflow, focus, or recovery.

## 8. Output contracts

### Audit

Lead with findings:

    P1 — Checkout summary actions overflow at 390px
    Evidence: route, viewport, screenshot or reproduction, and source location
    Impact: the primary purchase action is partly obscured
    Root cause: fixed minimum width in the shared action group
    Fix: allow the content column to shrink and stack the group below its stress width
    Verify: replay checkout at 320px, 390px, 200% zoom, and with the longest label

Then include:

- Gate table.
- Scorecard when it helps comparison.
- Strong choices worth preserving.
- Unverified areas and their risk.

### Build or Improve

Report:

- The product and design thesis used.
- A surface coverage matrix with Preserve, Repair, Refine, Recompose, or Create decisions and status.
- Material structural and visible design decisions, separate from accessibility, resilience, semantic, and infrastructure work.
- Components and states added or changed.
- Evidence: matching baseline or intent and final captures, critique iteration, routes, widths, dynamic transitions, state cases, input methods, checks, and test commands.
- Remaining risks or blockers.

Keep the handoff concise. Link to artifacts or files instead of narrating every edit.

### Audit JSON for the scorer

Generate a starter template with:

    python3 /path/to/dengskills/skills/craft/scripts/score_ui_audit.py --example

Replace the starter scope, fill it from actual evidence, then validate:

    python3 /path/to/dengskills/skills/craft/scripts/score_ui_audit.py audit.json --format markdown

For a professional completion claim, require the gate and local-artifact check explicitly:

    python3 /path/to/dengskills/skills/craft/scripts/score_ui_audit.py audit.json --format markdown --require-professional

The default command also withholds professional status when a claimed local artifact is missing; the strict flag additionally exits nonzero.

Do not manufacture evidence to satisfy the schema. Use unverified status where checks were not performed.

Schema version 2 requires:

- `platform` and a compact `design_thesis` with classical and expressive targets plus `signature_or_restraint`.
- `scope_targets` whose ids exactly match the surface inventory, plus an explicit `scope_exclusions` list even when it is empty.
- `surfaces` covering every named target, discovered in-scope route family, and shared global region; a representative page supplies family evidence without removing siblings from scope.
- A disposition, rationale, opportunity list, success delta, status, and evidence for each surface.
- `iterations` for completed Create or Recompose work and completed primary Refine work.
- `stability_cases` for relevant route, state, loading, media, font, overlay, and viewport transitions. Passed interactive cases declare `runtime_attached: true`; passed short-to-long route cases also declare `same_document: true`, name at least two page surfaces, and cover both with runtime measurement or test output.
- Evidence records with `phase` and `surface_ids` so baselines, iterations, final renders, and runtime measurements remain traceable.

For primary Improve targets classified Refine or Recompose, include matching rendered baseline and final evidence. Completed Create or Recompose work and completed primary Refine work need an iteration and final render. Preserve is valid when evidence shows the surface is already strong; Repair is valid for a bounded defect on an otherwise sound surface and does not force an authorship iteration.

The generated record intentionally fails validation until its `REPLACE` scope is changed. It includes a complete _finding_template. Copy that object into findings, replace its values with observed evidence, and remove the template before handoff. Every surface, iteration, stability case, gate, dimension, and finding evidence array uses this exact object shape:

    {
      "evidence_type": "screenshot",
      "phase": "observed",
      "surface_ids": ["checkout"],
      "artifact": "artifacts/checkout-390.png",
      "location": "/checkout, PurchaseActions",
      "viewport_or_state": "390 by 844 CSS px, ready state",
      "input_methods": ["keyboard", "pointer"],
      "method": "Playwright reproduction and rendered screenshot",
      "result": "The purchase action extends 96 CSS px beyond the viewport."
    }

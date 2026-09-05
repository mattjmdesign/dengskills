#!/usr/bin/env python3
"""Validate an evidence-based UI audit and render a gated scorecard."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


DIMENSIONS = (
    ("intent", "Product intent, hierarchy, and content priority", 10),
    ("layout", "Layout, spacing, alignment, and density", 15),
    ("typography", "Typography and readability", 10),
    ("responsive", "Responsive and content resilience", 15),
    ("interaction", "Interaction, states, feedback, and recovery", 10),
    ("accessibility", "Accessibility and input methods", 10),
    ("coherence", "Component and system coherence", 10),
    ("authorship", "Design authorship and product specificity", 10),
    ("craft", "Visual craft and brand fit", 10),
)

GATES = (
    ("G0", "Intent"),
    ("G1", "Structure"),
    ("G2", "Functional"),
    ("G3", "Resilience"),
    ("G4", "Inclusive interaction"),
    ("G5", "Craft"),
    ("G6", "Regression"),
)

GATE_CHECKS = {
    "G0": (
        "primary_user",
        "critical_task",
        "success_condition",
        "scope_targets",
        "constraints_assumptions",
    ),
    "G1": (
        "content_priority",
        "reading_order",
        "layout_regions",
        "adaptive_behavior",
        "required_states",
        "design_opportunity",
        "design_direction",
    ),
    "G2": (
        "critical_task_replay",
        "control_feedback",
        "error_recovery",
    ),
    "G3": (
        "narrow_size",
        "intermediate_size",
        "wide_size",
        "content_stress",
        "overflow_overlap_clipping",
        "dynamic_layout_stability",
    ),
    "G4": (
        "semantics_names",
        "keyboard_or_platform_input",
        "visible_focus",
        "contrast",
        "zoom_or_text_scaling",
        "target_size",
        "reduced_motion",
    ),
    "G5": (
        "design_thesis_realized",
        "hierarchy",
        "typography",
        "composition_rhythm",
        "color_material_iconography",
        "component_coherence",
        "product_specificity_brand_fit",
        "signature_or_restraint_execution",
        "rendered_critique",
    ),
    "G6": (
        "critical_task_regression",
        "in_scope_surface_coverage",
        "named_target_coverage",
        "baseline_or_intent_comparison",
        "affected_siblings",
        "exceptions_recorded",
    ),
}

GATE_MINIMUM_EVIDENCE = {
    "G0": 1,
    "G1": 1,
    "G2": 1,
    "G3": 4,
    "G4": 2,
    "G5": 2,
    "G6": 2,
}

REQUIRED_GATES_BY_MODE = {
    "build": frozenset(gate_id for gate_id, _ in GATES),
    "improve": frozenset(gate_id for gate_id, _ in GATES),
    "audit": frozenset({"G0", "G1", "G2", "G3", "G4", "G5"}),
}

EVIDENCE_STRING_FIELDS = (
    "artifact",
    "location",
    "viewport_or_state",
    "method",
    "result",
)

EVIDENCE_FIELDS = (
    "evidence_type",
    "phase",
    "surface_ids",
    *EVIDENCE_STRING_FIELDS,
    "input_methods",
)

VALID_EVIDENCE_TYPES = {
    "accessibility_tree",
    "assistive_technology_session",
    "console_output",
    "design_artifact",
    "interaction_replay",
    "manual_observation",
    "measurement",
    "screenshot",
    "source_reference",
    "test_output",
    "video",
}

RENDERED_EVIDENCE_TYPES = {"design_artifact", "screenshot", "video"}

VALID_EVIDENCE_PHASES = {
    "baseline",
    "candidate",
    "iteration",
    "final",
    "observed",
    "runtime",
    "source",
}

VALID_INPUT_METHODS = {
    "automation",
    "gamepad",
    "keyboard",
    "not_applicable",
    "pointer",
    "screen_reader",
    "spatial_input",
    "static_inspection",
    "stylus",
    "switch_control",
    "touch",
    "voice_control",
}

PLACEHOLDER_VALUES = {
    "check",
    "checked",
    "example",
    "fill me",
    "n/a",
    "ok",
    "pass",
    "passed",
    "placeholder",
    "replace me",
    "tbd",
    "todo",
}

GENERIC_ARTIFACTS = {
    "accessibility check",
    "audit",
    "browser",
    "checklist",
    "inspection",
    "manual check",
    "manual review",
    "notes",
    "review",
    "screenshot",
    "source",
    "test",
    "test results",
    "tool output",
}

GENERIC_LOCATIONS = {
    "all pages",
    "all routes",
    "all screens",
    "all screens and states",
    "application",
    "app",
    "component",
    "entire app",
    "everywhere",
    "page",
    "route",
    "screen",
    "site",
    "website",
    "whole app",
}

CONCLUSION_ONLY = re.compile(
    r"^(?:everything|all(?: checks?| screens?| states?)?|the interface|the ui|it)?\s*"
    r"(?:is |are |was |were )?"
    r"(?:fine|good|great|okay|ok|passed|successful|verified|working|works|"
    r"compliant|professional|responsive|accessible|ready)"
    r"(?: successfully| as expected| with no issues?)?[.!]?$",
    re.I,
)

ARTIFACT_LOCATOR = re.compile(
    r"(?:[/\\.#:]|\bline\s+\d+\b|\b\d{2,}\b|"
    r"\b(?:accessibility (?:tree|inspector)|console (?:capture|output)|"
    r"playwright|lighthouse|axe|xcuitest|xctest|espresso|maestro)\b)",
    re.I,
)

OBSERVABLE_RESULT = re.compile(
    r"(?:\b\d+(?:\.\d+)?\b|\b(?:aligned?|announced?|balanced?|changed?|"
    r"clipped?|composed?|contained?|displayed?|extended?|failed?|focused?|"
    r"improved?|measured?|moved?|opened?|overflow(?:ed|ing)?|preserved?|"
    r"prevented?|read|received?|remained?|rendered?|returned?|selected?|"
    r"shifted?|showed|shows?|visible|wrapped?)\b)",
    re.I,
)

VALID_MODES = {"build", "improve", "audit"}
VALID_PLATFORMS = {
    "web",
    "ios",
    "android",
    "macos",
    "windows",
    "cross_platform",
    "other",
}
VALID_GATE_STATUSES = {"pass", "fail", "unverified", "na"}
VALID_SEVERITIES = {"P0", "P1", "P2", "P3"}
VALID_FINDING_STATUSES = {"open", "resolved", "accepted"}
VALID_CONFIDENCE = {"confirmed", "likely", "hypothesis"}
VALID_SCOPES = {"systemic", "local"}
VALID_SURFACE_KINDS = {"page", "section", "component", "flow", "overlay", "state"}
VALID_SURFACE_SALIENCE = {"primary", "representative", "supporting"}
VALID_SURFACE_DISPOSITIONS = {
    "create",
    "evaluate",
    "preserve",
    "refine",
    "repair",
    "recompose",
}
VALID_SURFACE_STATUSES = {
    "created",
    "changed",
    "preserved",
    "evaluated",
    "blocked",
    "unverified",
}
VALID_OPPORTUNITIES = {
    "preserve_strength",
    "composition",
    "layout_rhythm",
    "typography",
    "controls",
    "content_hierarchy",
    "brand_expression",
    "responsive_topology",
    "dynamic_stability",
    "interaction_states",
    "accessibility",
}
VALID_STABILITY_CASES = {
    "short_long_transition",
    "state_transition",
    "async_content_settle",
    "font_load",
    "media_load",
    "scroll_lock",
    "sticky_fixed_boundary",
    "viewport_change",
}
RUNTIME_REQUIRED_STABILITY_CASES = {
    "async_content_settle",
    "scroll_lock",
    "short_long_transition",
    "state_transition",
}


@dataclass(frozen=True)
class DimensionResult:
    dimension_id: str
    label: str
    weight: int
    rating: float
    effective_rating: float
    evidence: tuple[dict[str, Any], ...]
    notes: str


def example_evidence() -> dict[str, Any]:
    return {
        "evidence_type": "screenshot",
        "phase": "observed",
        "surface_ids": ["checkout"],
        "artifact": "artifacts/checkout-390.png",
        "location": "/checkout, PurchaseActions",
        "viewport_or_state": "390 by 844 CSS px, ready state",
        "input_methods": ["keyboard", "pointer"],
        "method": "Playwright reproduction and rendered screenshot",
        "result": "The purchase action extends 96 CSS px beyond the viewport.",
    }


def example_document() -> dict[str, Any]:
    return {
        "schema_version": 2,
        "title": "Interface review",
        "mode": "audit",
        "platform": "web",
        "scope": "REPLACE with exact routes, screens, sizes, states, input methods, and the critical task.",
        "scope_targets": ["checkout"],
        "scope_exclusions": [],
        "design_thesis": {
            "experience": "A calm checkout that keeps the purchase decision obvious.",
            "qualities": ["trustworthy", "direct", "considered"],
            "primary_action": "Complete purchase",
            "first_attention": "Order total and purchase action",
            "classical_quality_target": "High clarity, stable alignment, and restrained complexity.",
            "expressive_quality_target": "A quiet editorial confidence appropriate to the brand.",
            "signature_or_restraint": "A strong order-summary rail with precise typographic contrast.",
            "reflexes_to_avoid": ["equal card treatment", "gratuitous gradients"],
            "change_boundary": "Preserve checkout behavior, data, and payment-provider contracts.",
        },
        "surfaces": [
            {
                "id": "checkout",
                "location": "/checkout, PurchaseActions",
                "kind": "page",
                "family": "commerce checkout",
                "salience": "primary",
                "disposition": "evaluate",
                "rationale": "This page owns the critical purchase decision.",
                "opportunities": ["composition", "dynamic_stability"],
                "success_delta": "The audit establishes whether hierarchy and layout remain stable.",
                "status": "evaluated",
                "evidence": [example_evidence()],
            }
        ],
        "iterations": [],
        "stability_cases": [
            {
                "id": "checkout-load",
                "case_type": "async_content_settle",
                "surface_ids": ["checkout"],
                "status": "unverified",
                "evidence": [],
                "notes": "Replace with measured loading-state evidence.",
            }
        ],
        "gates": [
            {
                "id": gate_id,
                "status": "unverified",
                "coverage": [],
                "evidence": [],
                "notes": "Not yet evaluated.",
            }
            for gate_id, _ in GATES
        ],
        "dimensions": [
            {
                "id": dimension_id,
                "rating": 0,
                "evidence": [],
                "notes": "Not yet rated.",
            }
            for dimension_id, _, _ in DIMENSIONS
        ],
        "findings": [],
        "_finding_template": {
            "id": "F-001",
            "location": "/checkout, PurchaseActions",
            "viewport_or_state": "390 by 844 CSS px, ready state",
            "observation": "The purchase action extends beyond the viewport.",
            "evidence": [example_evidence()],
            "impact": "The primary purchase task is partly obscured.",
            "root_cause": "The shared action group has a fixed minimum width.",
            "severity": "P1",
            "confidence": "confirmed",
            "scope": "systemic",
            "affects_primary_flow": True,
            "remediation": "Allow the action group to shrink and stack at its content stress point.",
            "verification": "Replay checkout at 320 and 390 CSS px and at 200 percent zoom.",
            "status": "open",
        },
    }


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_placeholder(value: str) -> bool:
    normalized = " ".join(value.strip().lower().split()).rstrip(".:")
    return (
        normalized in PLACEHOLDER_VALUES
        or normalized.startswith("replace ")
        or normalized.startswith("describe ")
        or normalized.startswith("name the ")
    )


def normalized_phrase(value: str) -> str:
    return " ".join(value.strip().lower().split()).rstrip(".:")


def validate_scope(value: Any, errors: list[str]) -> None:
    if not non_empty_string(value):
        errors.append("scope must name the tested interface and conditions")
        return
    cleaned = value.strip()
    if is_placeholder(cleaned) or normalized_phrase(cleaned) in GENERIC_LOCATIONS:
        errors.append(
            "scope must replace starter text with exact routes or screens, sizes, "
            "states, input methods, and the critical task"
        )
    elif len(cleaned) < 30:
        errors.append(
            "scope is too vague to define the tested interface and conditions"
        )


def validate_scope_targets(
    value: Any,
    surfaces: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[str]:
    if not isinstance(value, list) or not value:
        errors.append("scope_targets must be a non-empty list of surface ids")
        return []
    targets: list[str] = []
    seen: set[str] = set()
    for position, target in enumerate(value):
        if not non_empty_string(target):
            errors.append(f"scope_targets[{position}] must be a non-empty surface id")
        elif target in seen:
            errors.append(f"scope_targets contains duplicate surface id {target}")
        else:
            seen.add(target)
            targets.append(target)

    surface_ids = set(surfaces)
    target_ids = set(targets)
    missing_surfaces = target_ids - surface_ids
    undeclared_surfaces = surface_ids - target_ids
    if missing_surfaces:
        errors.append(
            "scope_targets missing surface records for: "
            + ", ".join(sorted(missing_surfaces))
        )
    if undeclared_surfaces:
        errors.append(
            "surfaces contain targets not declared in scope_targets: "
            + ", ".join(sorted(undeclared_surfaces))
        )
    return targets


def validate_scope_exclusions(value: Any, errors: list[str]) -> list[str]:
    if not isinstance(value, list):
        errors.append("scope_exclusions must be a list")
        return []
    exclusions: list[str] = []
    seen: set[str] = set()
    for position, exclusion in enumerate(value):
        if not non_empty_string(exclusion) or is_placeholder(exclusion):
            errors.append(
                f"scope_exclusions[{position}] must be a specific non-empty string"
            )
            continue
        cleaned = " ".join(exclusion.strip().split())
        normalized = normalized_phrase(cleaned)
        if normalized in seen:
            errors.append(f"scope_exclusions contains duplicate {cleaned}")
            continue
        seen.add(normalized)
        exclusions.append(cleaned)
    return exclusions


def validate_evidence(
    value: Any,
    label: str,
    errors: list[str],
    require_one: bool = False,
    known_surface_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list of structured evidence objects")
        return []
    if require_one and not value:
        errors.append(f"{label} must contain at least one evidence object")
        return []

    validated: list[dict[str, Any]] = []
    fingerprints: set[str] = set()
    for position, record in enumerate(value):
        record_label = f"{label}[{position}]"
        if not isinstance(record, dict):
            errors.append(f"{record_label} must be an object")
            continue

        normalized: dict[str, Any] = {}
        evidence_type = record.get("evidence_type")
        if evidence_type not in VALID_EVIDENCE_TYPES:
            allowed = ", ".join(sorted(VALID_EVIDENCE_TYPES))
            errors.append(f"{record_label}.evidence_type must be one of: {allowed}")
        else:
            normalized["evidence_type"] = evidence_type

        phase = record.get("phase")
        if phase not in VALID_EVIDENCE_PHASES:
            allowed = ", ".join(sorted(VALID_EVIDENCE_PHASES))
            errors.append(f"{record_label}.phase must be one of: {allowed}")
        else:
            normalized["phase"] = phase

        raw_surface_ids = record.get("surface_ids")
        if not isinstance(raw_surface_ids, list) or not raw_surface_ids:
            errors.append(
                f"{record_label}.surface_ids must be a non-empty list of surface ids"
            )
        else:
            surface_ids: list[str] = []
            seen_surface_ids: set[str] = set()
            for surface_position, surface_id in enumerate(raw_surface_ids):
                if not non_empty_string(surface_id):
                    errors.append(
                        f"{record_label}.surface_ids[{surface_position}] must be a non-empty string"
                    )
                elif surface_id in seen_surface_ids:
                    errors.append(
                        f"{record_label}.surface_ids contains duplicate {surface_id}"
                    )
                elif (
                    known_surface_ids is not None
                    and surface_id not in known_surface_ids
                ):
                    errors.append(
                        f"{record_label}.surface_ids references unknown surface {surface_id}"
                    )
                else:
                    seen_surface_ids.add(surface_id)
                    surface_ids.append(surface_id)
            if surface_ids and len(surface_ids) == len(raw_surface_ids):
                normalized["surface_ids"] = surface_ids

        for field in EVIDENCE_STRING_FIELDS:
            field_value = record.get(field)
            if not non_empty_string(field_value):
                errors.append(f"{record_label}.{field} must be a non-empty string")
                continue
            cleaned = " ".join(field_value.strip().split())
            if is_placeholder(cleaned):
                errors.append(f"{record_label}.{field} cannot be placeholder evidence")
                continue
            phrase = normalized_phrase(cleaned)
            if field in {"artifact", "location", "method", "result"} and (
                phrase == "not applicable" or phrase.startswith("not applicable;")
            ):
                errors.append(f"{record_label}.{field} must identify concrete evidence")
                continue

            if field == "artifact":
                if phrase in GENERIC_ARTIFACTS or not ARTIFACT_LOCATOR.search(cleaned):
                    errors.append(
                        f"{record_label}.artifact must be a stable file, capture, "
                        "tool report, or other specific locator"
                    )
                    continue
                if evidence_type in RENDERED_EVIDENCE_TYPES:
                    artifact_path = cleaned.split("#", 1)[0]
                    is_url = bool(re.match(r"^[a-z][a-z0-9+.-]*://", cleaned, re.I))
                    is_path = (
                        "/" in artifact_path
                        or "\\" in artifact_path
                        or bool(Path(artifact_path).suffix)
                    )
                    if not (is_url or is_path):
                        errors.append(
                            f"{record_label}.artifact for rendered evidence must "
                            "be a file path or URL"
                        )
                        continue
            elif field == "location" and phrase in GENERIC_LOCATIONS:
                errors.append(
                    f"{record_label}.location must name a specific route, screen, "
                    "component, artifact section, or source line"
                )
                continue
            elif field == "viewport_or_state" and (
                phrase
                in {
                    "all sizes",
                    "all states",
                    "all viewports",
                    "all screens and states",
                    "default",
                    "multiple sizes",
                    "responsive",
                    "various states",
                    "various viewports",
                }
            ):
                errors.append(
                    f"{record_label}.viewport_or_state must name exact sizes, "
                    "platform conditions, content cases, or states"
                )
                continue
            elif field == "method":
                if phrase in GENERIC_ARTIFACTS or len(cleaned) < 16:
                    errors.append(
                        f"{record_label}.method must name the tool and reproduction, "
                        "inspection, comparison, or measurement procedure"
                    )
                    continue
            elif field == "result":
                if len(cleaned) < 24 or CONCLUSION_ONLY.fullmatch(cleaned):
                    errors.append(
                        f"{record_label}.result must describe a concrete observable "
                        "outcome, not a conclusion-only pass claim"
                    )
                    continue
                if not OBSERVABLE_RESULT.search(cleaned):
                    errors.append(
                        f"{record_label}.result must name an observed behavior, "
                        "measurement, state change, or visible outcome"
                    )
                    continue
            normalized[field] = cleaned

        input_methods = record.get("input_methods")
        if not isinstance(input_methods, list) or not input_methods:
            errors.append(
                f"{record_label}.input_methods must be a non-empty list of "
                "enumerated input methods"
            )
        else:
            valid_inputs: list[str] = []
            seen_inputs: set[str] = set()
            for input_position, input_method in enumerate(input_methods):
                if input_method not in VALID_INPUT_METHODS:
                    allowed = ", ".join(sorted(VALID_INPUT_METHODS))
                    errors.append(
                        f"{record_label}.input_methods[{input_position}] must be one "
                        f"of: {allowed}"
                    )
                elif input_method in seen_inputs:
                    errors.append(
                        f"{record_label}.input_methods contains duplicate "
                        f"{input_method}"
                    )
                else:
                    seen_inputs.add(input_method)
                    valid_inputs.append(input_method)
            if valid_inputs and len(valid_inputs) == len(input_methods):
                normalized["input_methods"] = valid_inputs

        extra_fields = set(record) - set(EVIDENCE_FIELDS)
        if extra_fields:
            extras = ", ".join(sorted(extra_fields))
            errors.append(f"{record_label} has unknown field(s): {extras}")
        if len(normalized) == len(EVIDENCE_FIELDS) and not extra_fields:
            fingerprint = json.dumps(normalized, sort_keys=True)
            if fingerprint in fingerprints:
                errors.append(f"{record_label} duplicates another evidence record")
            else:
                fingerprints.add(fingerprint)
                validated.append(normalized)
    return validated


def has_rendered_evidence(
    evidence: list[dict[str, Any]], phases: set[str] | None = None
) -> bool:
    return any(
        record["evidence_type"] in RENDERED_EVIDENCE_TYPES
        and (phases is None or record["phase"] in phases)
        for record in evidence
    )


def rendered_artifacts(
    evidence: list[dict[str, Any]], phases: set[str] | None = None
) -> set[str]:
    return {
        record["artifact"]
        for record in evidence
        if record["evidence_type"] in RENDERED_EVIDENCE_TYPES
        and (phases is None or record["phase"] in phases)
    }


def surface_requires_iteration(surface: dict[str, Any]) -> bool:
    return (
        surface.get("status") in {"created", "changed"}
        and surface.get("disposition") in {"create", "refine", "recompose"}
        and (
            surface.get("salience") == "primary"
            or surface.get("disposition") in {"create", "recompose"}
        )
    )


def indexed(
    items: Any,
    key: str,
    errors: list[str],
    label: str,
) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list):
        errors.append(f"{label} must be a list")
        return {}

    result: dict[str, dict[str, Any]] = {}
    for position, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{label}[{position}] must be an object")
            continue
        item_id = item.get(key)
        if not non_empty_string(item_id):
            errors.append(f"{label}[{position}].{key} must be a non-empty string")
            continue
        if item_id in result:
            errors.append(f"{label} contains duplicate {key} {item_id}")
            continue
        result[item_id] = item
    return result


def validate_exact_string_list(
    value: Any,
    label: str,
    exact_length: int,
    errors: list[str],
) -> list[str]:
    if not isinstance(value, list) or len(value) != exact_length:
        errors.append(f"{label} must contain exactly {exact_length} non-empty strings")
        return []
    result: list[str] = []
    seen: set[str] = set()
    for position, item in enumerate(value):
        if not non_empty_string(item) or is_placeholder(item):
            errors.append(f"{label}[{position}] must be a specific non-empty string")
            continue
        cleaned = " ".join(item.strip().split())
        normalized = normalized_phrase(cleaned)
        if normalized in seen:
            errors.append(f"{label} contains duplicate value {cleaned}")
            continue
        seen.add(normalized)
        result.append(cleaned)
    return result


def validate_design_thesis(value: Any, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append("design_thesis must be an object")
        return {}

    required_text = (
        "experience",
        "primary_action",
        "first_attention",
        "classical_quality_target",
        "expressive_quality_target",
        "signature_or_restraint",
        "change_boundary",
    )
    result: dict[str, Any] = {}
    for field in required_text:
        item = value.get(field)
        if not non_empty_string(item) or is_placeholder(item):
            errors.append(f"design_thesis.{field} must be a specific non-empty string")
        else:
            result[field] = " ".join(item.strip().split())

    result["qualities"] = validate_exact_string_list(
        value.get("qualities"), "design_thesis.qualities", 3, errors
    )
    result["reflexes_to_avoid"] = validate_exact_string_list(
        value.get("reflexes_to_avoid"),
        "design_thesis.reflexes_to_avoid",
        2,
        errors,
    )

    expected_fields = set(required_text) | {"qualities", "reflexes_to_avoid"}
    extras = set(value) - expected_fields
    if extras:
        errors.append(
            "design_thesis has unknown field(s): " + ", ".join(sorted(extras))
        )
    return result


def validate_surfaces(
    value: Any,
    mode: str | None,
    errors: list[str],
) -> dict[str, dict[str, Any]]:
    surfaces = indexed(value, "id", errors, "surfaces")
    if not surfaces:
        errors.append("surfaces must inventory at least one target")
        return surfaces
    known_surface_ids = set(surfaces)
    if not any(item.get("salience") == "primary" for item in surfaces.values()):
        errors.append("surfaces must include at least one primary target")

    allowed_dispositions = {
        "build": {"create"},
        "improve": {"preserve", "refine", "repair", "recompose"},
        "audit": {"evaluate"},
    }.get(mode, VALID_SURFACE_DISPOSITIONS)
    expected_status = {
        "create": "created",
        "preserve": "preserved",
        "refine": "changed",
        "repair": "changed",
        "recompose": "changed",
        "evaluate": "evaluated",
    }

    family_evidence: dict[str, bool] = {}
    for surface_id, surface in surfaces.items():
        label = f"surface {surface_id}"
        for field in ("location", "family", "rationale", "success_delta"):
            item = surface.get(field)
            if not non_empty_string(item) or is_placeholder(item):
                errors.append(f"{label}.{field} must be a specific non-empty string")
        if normalized_phrase(str(surface.get("location", ""))) in GENERIC_LOCATIONS:
            errors.append(f"{label}.location must identify a specific target")

        kind = surface.get("kind")
        if kind not in VALID_SURFACE_KINDS:
            errors.append(
                f"{label}.kind must be one of: "
                + ", ".join(sorted(VALID_SURFACE_KINDS))
            )
        salience = surface.get("salience")
        if salience not in VALID_SURFACE_SALIENCE:
            errors.append(
                f"{label}.salience must be one of: "
                + ", ".join(sorted(VALID_SURFACE_SALIENCE))
            )
        disposition = surface.get("disposition")
        if disposition not in VALID_SURFACE_DISPOSITIONS:
            errors.append(
                f"{label}.disposition must be one of: "
                + ", ".join(sorted(VALID_SURFACE_DISPOSITIONS))
            )
        elif disposition not in allowed_dispositions:
            errors.append(
                f"{label}.disposition {disposition} is incompatible with mode {mode}"
            )

        status = surface.get("status")
        if status not in VALID_SURFACE_STATUSES:
            errors.append(
                f"{label}.status must be one of: "
                + ", ".join(sorted(VALID_SURFACE_STATUSES))
            )
        elif disposition in expected_status and status not in {
            expected_status[disposition],
            "blocked",
            "unverified",
        }:
            errors.append(
                f"{label}.status {status} does not match disposition {disposition}"
            )

        opportunities = surface.get("opportunities")
        if not isinstance(opportunities, list) or not opportunities:
            errors.append(f"{label}.opportunities must be a non-empty list")
        else:
            seen_opportunities: set[str] = set()
            for position, opportunity in enumerate(opportunities):
                if opportunity not in VALID_OPPORTUNITIES:
                    errors.append(
                        f"{label}.opportunities[{position}] must be one of: "
                        + ", ".join(sorted(VALID_OPPORTUNITIES))
                    )
                elif opportunity in seen_opportunities:
                    errors.append(
                        f"{label}.opportunities contains duplicate {opportunity}"
                    )
                else:
                    seen_opportunities.add(opportunity)

        completed = status in {"created", "changed", "preserved", "evaluated"}
        evidence = validate_evidence(
            surface.get("evidence"),
            f"{label}.evidence",
            errors,
            require_one=completed,
            known_surface_ids=known_surface_ids,
        )
        surface["_validated_evidence"] = evidence
        for record in evidence:
            if surface_id not in record["surface_ids"]:
                errors.append(
                    f"{label}.evidence must reference its own surface id {surface_id}"
                )

        if completed and disposition in {
            "create",
            "preserve",
            "refine",
            "repair",
            "recompose",
        }:
            if not has_rendered_evidence(evidence, {"final"}):
                errors.append(
                    f"{label} needs final rendered screenshot, video, or "
                    "design-artifact evidence"
                )
        if (
            completed
            and mode == "improve"
            and salience == "primary"
            and disposition in {"refine", "recompose"}
            and not (
                has_rendered_evidence(evidence, {"baseline"})
                and has_rendered_evidence(evidence, {"final"})
            )
        ):
            errors.append(
                f"{label} needs rendered baseline and final evidence for primary "
                "Improve work"
            )
        elif (
            completed
            and mode == "improve"
            and disposition
            in {
                "refine",
                "recompose",
            }
        ):
            if rendered_artifacts(evidence, {"baseline"}) & rendered_artifacts(
                evidence, {"final"}
            ):
                errors.append(
                    f"{label} baseline and final renders must use distinct artifacts"
                )
        if (
            completed
            and mode == "audit"
            and not has_rendered_evidence(evidence, {"observed", "runtime", "final"})
        ):
            errors.append(f"{label} needs observed rendered evidence for Audit work")

        family = surface.get("family")
        if kind == "page" and non_empty_string(family):
            family_evidence.setdefault(family, False)
            if (
                salience in {"primary", "representative"}
                and completed
                and has_rendered_evidence(evidence, {"final", "observed", "runtime"})
            ):
                family_evidence[family] = True

        expected_fields = {
            "id",
            "location",
            "kind",
            "family",
            "salience",
            "disposition",
            "rationale",
            "opportunities",
            "success_delta",
            "status",
            "evidence",
            "_validated_evidence",
        }
        extras = set(surface) - expected_fields
        if extras:
            errors.append(f"{label} has unknown field(s): " + ", ".join(sorted(extras)))

    for family, has_evidence in family_evidence.items():
        if not has_evidence:
            errors.append(
                f"page family {family} needs final or observed representative evidence"
            )
    return surfaces


def validate_iterations(
    value: Any,
    mode: str | None,
    surfaces: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append("iterations must be a list")
        return []
    known_surface_ids = set(surfaces)
    result: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    iterated_surfaces: set[str] = set()
    for position, item in enumerate(value):
        label = f"iterations[{position}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue
        iteration_id = item.get("id")
        if not non_empty_string(iteration_id):
            errors.append(f"{label}.id must be a non-empty string")
        elif iteration_id in seen_ids:
            errors.append(f"iterations contains duplicate id {iteration_id}")
        else:
            seen_ids.add(iteration_id)
        surface_id = item.get("surface_id")
        if surface_id not in known_surface_ids:
            errors.append(f"{label}.surface_id references an unknown surface")
        else:
            iterated_surfaces.add(surface_id)
        for field in ("critique", "response"):
            text_value = item.get(field)
            if not non_empty_string(text_value) or is_placeholder(text_value):
                errors.append(f"{label}.{field} must be a specific non-empty string")
        evidence = validate_evidence(
            item.get("evidence"),
            f"{label}.evidence",
            errors,
            require_one=True,
            known_surface_ids=known_surface_ids,
        )
        if surface_id in known_surface_ids and any(
            surface_id not in record["surface_ids"] for record in evidence
        ):
            errors.append(f"{label}.evidence must reference surface {surface_id}")
        if evidence and not has_rendered_evidence(evidence, {"iteration"}):
            errors.append(
                f"{label}.evidence must include a rendered iteration-phase artifact"
            )
        item["_validated_evidence"] = evidence
        extras = set(item) - {
            "id",
            "surface_id",
            "critique",
            "response",
            "evidence",
            "_validated_evidence",
        }
        if extras:
            errors.append(f"{label} has unknown field(s): " + ", ".join(sorted(extras)))
        result.append(item)

    if mode in {"build", "improve"}:
        required_iterations = {
            surface_id
            for surface_id, surface in surfaces.items()
            if surface_requires_iteration(surface)
        }
        for surface_id in sorted(required_iterations - iterated_surfaces):
            errors.append(
                f"surface {surface_id} requires a rendered critique iteration"
            )
    return result


def validate_stability_cases(
    value: Any,
    surfaces: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append("stability_cases must be a list")
        return []
    known_surface_ids = set(surfaces)
    result: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for position, item in enumerate(value):
        label = f"stability_cases[{position}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue
        case_id = item.get("id")
        if not non_empty_string(case_id):
            errors.append(f"{label}.id must be a non-empty string")
        elif case_id in seen_ids:
            errors.append(f"stability_cases contains duplicate id {case_id}")
        else:
            seen_ids.add(case_id)
        case_type = item.get("case_type")
        if case_type not in VALID_STABILITY_CASES:
            errors.append(
                f"{label}.case_type must be one of: "
                + ", ".join(sorted(VALID_STABILITY_CASES))
            )
        raw_surface_ids = item.get("surface_ids")
        case_surface_ids: set[str] = set()
        if not isinstance(raw_surface_ids, list) or not raw_surface_ids:
            errors.append(f"{label}.surface_ids must be a non-empty list")
        else:
            for surface_id in raw_surface_ids:
                if surface_id in case_surface_ids:
                    errors.append(
                        f"{label}.surface_ids contains duplicate {surface_id}"
                    )
                elif surface_id not in known_surface_ids:
                    errors.append(
                        f"{label}.surface_ids references unknown surface {surface_id}"
                    )
                else:
                    case_surface_ids.add(surface_id)
        status = item.get("status")
        if status not in VALID_GATE_STATUSES:
            errors.append(f"{label}.status must be pass, fail, unverified, or na")
        notes = item.get("notes")
        if not isinstance(notes, str):
            errors.append(f"{label}.notes must be a string")
        elif status == "na" and (len(notes.strip()) < 12 or is_placeholder(notes)):
            errors.append(f"{label} with status na requires a specific reason")
        same_document = item.get("same_document")
        if same_document is not None and not isinstance(same_document, bool):
            errors.append(f"{label}.same_document must be true or false")
        runtime_attached = item.get("runtime_attached")
        if runtime_attached is not None and not isinstance(runtime_attached, bool):
            errors.append(f"{label}.runtime_attached must be true or false")
        evidence = validate_evidence(
            item.get("evidence"),
            f"{label}.evidence",
            errors,
            require_one=status in {"pass", "fail"},
            known_surface_ids=known_surface_ids,
        )
        if status == "pass" and not any(
            record["phase"] == "runtime" for record in evidence
        ):
            errors.append(f"{label} pass requires runtime-phase evidence")
        if status == "pass" and not any(
            record["phase"] == "runtime"
            and record["evidence_type"] in {"measurement", "test_output"}
            for record in evidence
        ):
            errors.append(
                f"{label} pass requires runtime measurement or test-output evidence"
            )
        evidenced_surface_ids = {
            surface_id for record in evidence for surface_id in record["surface_ids"]
        }
        if evidence and not evidenced_surface_ids.issubset(case_surface_ids):
            errors.append(f"{label}.evidence references surfaces outside the case")
        if status in {"pass", "fail"} and not case_surface_ids.issubset(
            evidenced_surface_ids
        ):
            errors.append(
                f"{label}.evidence must cover every surface named by the case"
            )
        if (
            status == "pass"
            and case_type in RUNTIME_REQUIRED_STABILITY_CASES
            and runtime_attached is not True
        ):
            errors.append(
                f"{label} pass requires runtime_attached: true for {case_type}"
            )
        if status == "pass" and case_type == "short_long_transition":
            page_surface_ids = {
                surface_id
                for surface_id in case_surface_ids
                if surfaces[surface_id].get("kind") == "page"
            }
            if len(case_surface_ids) < 2 or page_surface_ids != case_surface_ids:
                errors.append(
                    f"{label} short_long_transition requires at least two page surfaces"
                )
            if same_document is not True:
                errors.append(
                    f"{label} pass requires same_document: true for the client-side route transition"
                )
        item["_validated_evidence"] = evidence
        extras = set(item) - {
            "id",
            "case_type",
            "surface_ids",
            "status",
            "same_document",
            "runtime_attached",
            "evidence",
            "notes",
            "_validated_evidence",
        }
        if extras:
            errors.append(f"{label} has unknown field(s): " + ", ".join(sorted(extras)))
        result.append(item)
    return result


def validate_gate_coverage(
    gate_id: str,
    gate: dict[str, Any],
    status: Any,
    evidence: list[dict[str, Any]],
    errors: list[str],
    mode: str | None,
    requires_authorship_iteration: bool,
) -> list[str]:
    raw_coverage = gate.get("coverage")
    expected = set(GATE_CHECKS[gate_id])
    if not isinstance(raw_coverage, list):
        errors.append(f"gate {gate_id}.coverage must be a list of check identifiers")
        return []

    coverage: list[str] = []
    seen: set[str] = set()
    for position, check in enumerate(raw_coverage):
        if not isinstance(check, str) or not check.strip():
            errors.append(
                f"gate {gate_id}.coverage[{position}] must be a check identifier"
            )
            continue
        normalized = check.strip()
        if normalized not in expected:
            allowed = ", ".join(GATE_CHECKS[gate_id])
            errors.append(
                f"gate {gate_id}.coverage[{position}] must be one of: {allowed}"
            )
        elif normalized in seen:
            errors.append(f"gate {gate_id}.coverage contains duplicate {normalized}")
        else:
            seen.add(normalized)
            coverage.append(normalized)

    if status == "pass":
        missing = [check for check in GATE_CHECKS[gate_id] if check not in seen]
        if missing:
            errors.append(
                f"gate {gate_id} cannot pass without coverage for: "
                + ", ".join(missing)
            )
        minimum = GATE_MINIMUM_EVIDENCE[gate_id]
        if len(evidence) < minimum:
            errors.append(
                f"gate {gate_id} pass requires at least {minimum} distinct evidence "
                f"record{'s' if minimum != 1 else ''}"
            )
    elif status == "fail" and not coverage:
        errors.append(f"gate {gate_id} fail must name at least one covered check")

    combined = " ".join(
        " ".join(
            str(record[field]) for field in ("viewport_or_state", "method", "result")
        )
        for record in evidence
    )

    if status == "pass" and gate_id == "G3":
        widths: set[int] = set()
        for record in evidence:
            size_text = record["viewport_or_state"]
            size_match = re.search(
                r"\b(\d{2,4})\s*(?:x|by|×)\s*\d{2,4}", size_text, re.I
            )
            if size_match is None:
                size_match = re.search(
                    r"\b(?:width\s*)?(\d{2,4})\s*(?:css\s*)?(?:px|pt|dp)\b",
                    size_text,
                    re.I,
                )
            if size_match is not None:
                widths.add(int(size_match.group(1)))
        if len(widths) < 3:
            errors.append(
                "gate G3 pass requires evidence at three distinct exact widths or "
                "window sizes"
            )
        if not re.search(
            r"(?:content stress|long (?:label|text|value)|text expansion|"
            r"expanded text|dense data|sparse data|unbroken value|locali[sz]|"
            r"dynamic type|font scaling|zoom)",
            combined,
            re.I,
        ):
            errors.append(
                "gate G3 pass requires evidence of a named content-stress or "
                "text-scaling case"
            )
        if not re.search(
            r"(?:overflow|overlap|clip|wrap|within (?:the )?(?:viewport|window|"
            r"bounds)|horizontal scroll|out of bounds)",
            combined,
            re.I,
        ):
            errors.append(
                "gate G3 pass requires an observable overflow, overlap, clipping, "
                "wrapping, or bounds result"
            )
        if not re.search(
            r"(?:short.{0,12}long|route (?:change|transition)|state transition|"
            r"scrollbar|scroll lock|font load|media load|skeleton|layout shift|"
            r"anchor (?:geometry|position)|client width|modal)",
            combined,
            re.I,
        ):
            errors.append(
                "gate G3 pass requires an observable same-size dynamic layout-stability result"
            )

    if status == "pass" and gate_id == "G4":
        runtime_accessibility_evidence = [
            record
            for record in evidence
            if record["phase"] in {"observed", "runtime"}
            and record["evidence_type"]
            in {
                "accessibility_tree",
                "assistive_technology_session",
                "interaction_replay",
                "manual_observation",
                "measurement",
                "screenshot",
                "test_output",
                "video",
            }
        ]
        if len(runtime_accessibility_evidence) < 2:
            errors.append(
                "gate G4 pass requires at least two observed or runtime "
                "accessibility or interaction evidence records"
            )
        direct_inputs = {
            input_method
            for record in evidence
            for input_method in record["input_methods"]
            if input_method not in {"automation", "not_applicable", "static_inspection"}
        }
        if len(direct_inputs) < 2:
            errors.append(
                "gate G4 pass requires evidence from at least two direct input or "
                "assistive-technology methods"
            )
        required_signals = {
            "semantics_names": r"(?:semantic|accessible name|accessibility tree|role|label)",
            "visible_focus": r"focus",
            "contrast": r"(?:contrast|forced colors?|high contrast)",
            "zoom_or_text_scaling": r"(?:zoom|text scal|font scal|dynamic type|magnification)",
            "target_size": r"(?:target size|hit area|touch area|pointer target)",
            "reduced_motion": r"(?:reduced motion|motion|animation)",
        }
        for check, pattern in required_signals.items():
            if check in seen and not re.search(pattern, combined, re.I):
                errors.append(
                    f"gate G4 coverage {check} needs a matching observable result"
                )

    if status == "pass" and gate_id == "G2":
        if not any(
            record["phase"] == "runtime"
            and record["evidence_type"]
            in {"interaction_replay", "test_output", "video"}
            for record in evidence
        ):
            errors.append(
                "gate G2 pass requires runtime interaction-replay, video, or test evidence"
            )
        if not re.search(
            r"(?:feedback|announc|confirm|selected|opened|closed|success|error|"
            r"state changed|became visible)",
            combined,
            re.I,
        ):
            errors.append("gate G2 pass requires an observable control-feedback result")
        if not re.search(
            r"(?:recover|recovery|retry|cancel|undo|dismiss|escape|return focus|"
            r"corrected|cleared)",
            combined,
            re.I,
        ):
            errors.append("gate G2 pass requires an observable recovery result")

    if status == "pass" and gate_id == "G5":
        rendered_evidence_count = sum(
            record["evidence_type"] in RENDERED_EVIDENCE_TYPES for record in evidence
        )
        if rendered_evidence_count < 2:
            errors.append(
                "gate G5 pass requires at least two distinct rendered screenshot, "
                "video, or design-artifact evidence records"
            )
        if mode in {"build", "improve"} and requires_authorship_iteration:
            if not (
                has_rendered_evidence(evidence, {"iteration"})
                and has_rendered_evidence(evidence, {"final"})
            ):
                errors.append(
                    "gate G5 pass requires rendered iteration and final evidence "
                    "for authored Build or Improve work"
                )
            elif rendered_artifacts(evidence, {"iteration"}) & rendered_artifacts(
                evidence, {"final"}
            ):
                errors.append(
                    "gate G5 iteration and final renders must use distinct artifacts"
                )

    if (
        status == "pass"
        and gate_id == "G6"
        and not re.search(
            r"(?:replay|re-ran|reran|regression|after (?:the )?(?:change|fix))",
            combined,
            re.I,
        )
    ):
        errors.append(
            "gate G6 pass requires evidence that the critical task was replayed "
            "after the change"
        )
    if (
        status == "pass"
        and gate_id == "G6"
        and not any(
            record["phase"] == "runtime"
            and record["evidence_type"]
            in {"interaction_replay", "test_output", "video"}
            for record in evidence
        )
    ):
        errors.append(
            "gate G6 pass requires runtime interaction-replay, video, or test evidence"
        )
    if status == "pass" and gate_id == "G6":
        paired_comparison = any(
            re.search(first, combined, re.I) and re.search(second, combined, re.I)
            for first, second in (
                (r"\bbaseline\b", r"\bfinal\b"),
                (r"\bbefore\b", r"\bafter\b"),
                (r"\boriginal\b", r"\bcurrent\b"),
            )
        )
        intent_comparison = bool(
            re.search(r"\bstated intent\b", combined, re.I)
            and re.search(r"\b(?:comparison|compared|against)\b", combined, re.I)
        )
        if not (paired_comparison or intent_comparison):
            errors.append(
                "gate G6 pass requires an observable paired baseline/final, "
                "before/after, or stated-intent comparison"
            )

    return coverage


def validate_document(
    document: Any,
) -> tuple[list[str], list[str], list[DimensionResult], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    warnings: list[str] = []
    dimensions: list[DimensionResult] = []

    if not isinstance(document, dict):
        return ["audit root must be a JSON object"], warnings, dimensions, {}

    if document.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    if not non_empty_string(document.get("title")):
        errors.append("title must be a non-empty string")
    mode = document.get("mode")
    if mode not in VALID_MODES:
        errors.append("mode must be build, improve, or audit")
    platform = document.get("platform")
    if platform not in VALID_PLATFORMS:
        errors.append("platform must be one of: " + ", ".join(sorted(VALID_PLATFORMS)))
    validate_scope(document.get("scope"), errors)

    document["_validated_design_thesis"] = validate_design_thesis(
        document.get("design_thesis"), errors
    )
    surfaces = validate_surfaces(document.get("surfaces"), mode, errors)
    document["_validated_scope_targets"] = validate_scope_targets(
        document.get("scope_targets"), surfaces, errors
    )
    document["_validated_scope_exclusions"] = validate_scope_exclusions(
        document.get("scope_exclusions"), errors
    )
    known_surface_ids = set(surfaces)
    requires_authorship_iteration = any(
        surface_requires_iteration(surface) for surface in surfaces.values()
    )
    document["_validated_iterations"] = validate_iterations(
        document.get("iterations"), mode, surfaces, errors
    )
    for iteration in document["_validated_iterations"]:
        surface_id = iteration.get("surface_id")
        if surface_id not in surfaces:
            continue
        iteration_artifacts = rendered_artifacts(
            iteration.get("_validated_evidence", []), {"iteration"}
        )
        final_artifacts = rendered_artifacts(
            surfaces[surface_id].get("_validated_evidence", []), {"final"}
        )
        if iteration_artifacts & final_artifacts:
            errors.append(
                f"iteration {iteration.get('id', '?')} and surface {surface_id} "
                "final render must use distinct artifacts"
            )
    stability_cases = validate_stability_cases(
        document.get("stability_cases"), surfaces, errors
    )
    document["_validated_stability_cases"] = stability_cases

    gates = indexed(document.get("gates"), "id", errors, "gates")
    expected_gate_ids = {gate_id for gate_id, _ in GATES}
    for gate_id, _ in GATES:
        gate = gates.get(gate_id)
        if gate is None:
            errors.append(f"missing gate {gate_id}")
            continue
        status = gate.get("status")
        if status not in VALID_GATE_STATUSES:
            errors.append(
                f"gate {gate_id}.status must be pass, fail, unverified, or na"
            )
        evidence = validate_evidence(
            gate.get("evidence"),
            f"gate {gate_id}.evidence",
            errors,
            require_one=status in {"pass", "fail"},
            known_surface_ids=known_surface_ids,
        )
        coverage = validate_gate_coverage(
            gate_id,
            gate,
            status,
            evidence,
            errors,
            mode,
            requires_authorship_iteration,
        )
        notes = gate.get("notes", "")
        if not isinstance(notes, str):
            errors.append(f"gate {gate_id}.notes must be a string")
        elif status == "na" and (
            len(notes.strip()) < 12
            or is_placeholder(notes)
            or notes.strip().lower().rstrip(".") == "not applicable"
        ):
            errors.append(f"gate {gate_id} with status na requires a specific reason")
        gate["_validated_evidence"] = evidence
        gate["_validated_coverage"] = coverage
    for extra in sorted(set(gates) - expected_gate_ids):
        warnings.append(f"unknown gate {extra} is ignored")

    g3_status = gates.get("G3", {}).get("status")
    passed_stability = [
        item for item in stability_cases if item.get("status") == "pass"
    ]
    if g3_status == "pass" and not passed_stability:
        errors.append("gate G3 cannot pass without a passed stability case")
    page_count = sum(
        1 for surface in surfaces.values() if surface.get("kind") == "page"
    )
    if (
        g3_status == "pass"
        and platform == "web"
        and page_count > 1
        and not any(
            item.get("status") == "pass"
            and item.get("case_type") == "short_long_transition"
            for item in stability_cases
        )
    ):
        errors.append(
            "multi-page web scope needs a passed short_long_transition stability case"
        )

    if gates.get("G6", {}).get("status") == "pass":
        incomplete_surfaces = [
            surface_id
            for surface_id, surface in surfaces.items()
            if surface.get("status") in {"blocked", "unverified"}
        ]
        if incomplete_surfaces:
            errors.append(
                "gate G6 cannot pass with incomplete in-scope surfaces: "
                + ", ".join(sorted(incomplete_surfaces))
            )
        g6_evidence = gates["G6"].get("_validated_evidence", [])
        evidenced_surface_ids = {
            surface_id for record in g6_evidence for surface_id in record["surface_ids"]
        }
        missing_g6_surfaces = known_surface_ids - evidenced_surface_ids
        if missing_g6_surfaces:
            errors.append(
                "gate G6 evidence does not cover in-scope surfaces: "
                + ", ".join(sorted(missing_g6_surfaces))
            )

    raw_dimensions = indexed(document.get("dimensions"), "id", errors, "dimensions")
    expected_dimension_ids = {dimension_id for dimension_id, _, _ in DIMENSIONS}
    for dimension_id, label, weight in DIMENSIONS:
        item = raw_dimensions.get(dimension_id)
        if item is None:
            errors.append(f"missing dimension {dimension_id}")
            continue
        rating = item.get("rating")
        if isinstance(rating, bool) or not isinstance(rating, (int, float)):
            errors.append(
                f"dimension {dimension_id}.rating must be a number from 0 to 4"
            )
            continue
        if not math.isfinite(float(rating)) or rating < 0 or rating > 4:
            errors.append(f"dimension {dimension_id}.rating must be between 0 and 4")
            continue
        evidence = validate_evidence(
            item.get("evidence"),
            f"dimension {dimension_id}.evidence",
            errors,
            known_surface_ids=known_surface_ids,
        )
        if (
            dimension_id in {"layout", "authorship", "craft"}
            and float(rating) >= 3
            and not has_rendered_evidence(evidence, {"final", "observed"})
        ):
            errors.append(
                f"dimension {dimension_id} rated 3 or above requires final or "
                "observed rendered evidence"
            )
        notes = item.get("notes", "")
        if not isinstance(notes, str):
            errors.append(f"dimension {dimension_id}.notes must be a string")
            continue
        effective = float(rating)
        if not evidence and effective > 2:
            effective = 2.0
            warnings.append(
                f"dimension {dimension_id} was capped at 2 because it has no evidence"
            )
        dimensions.append(
            DimensionResult(
                dimension_id=dimension_id,
                label=label,
                weight=weight,
                rating=float(rating),
                effective_rating=effective,
                evidence=tuple(evidence),
                notes=notes.strip(),
            )
        )
    for extra in sorted(set(raw_dimensions) - expected_dimension_ids):
        warnings.append(f"unknown dimension {extra} is ignored")

    findings = indexed(document.get("findings"), "id", errors, "findings")
    required_text_fields = (
        "location",
        "viewport_or_state",
        "observation",
        "impact",
        "root_cause",
        "remediation",
        "verification",
    )
    for finding_id, finding in findings.items():
        for field in required_text_fields:
            if not non_empty_string(finding.get(field)):
                errors.append(
                    f"finding {finding_id}.{field} must be a non-empty string"
                )
        evidence = validate_evidence(
            finding.get("evidence"),
            f"finding {finding_id}.evidence",
            errors,
            require_one=True,
            known_surface_ids=known_surface_ids,
        )
        finding["_validated_evidence"] = evidence
        if finding.get("severity") not in VALID_SEVERITIES:
            errors.append(f"finding {finding_id}.severity must be P0, P1, P2, or P3")
        if finding.get("status") not in VALID_FINDING_STATUSES:
            errors.append(
                f"finding {finding_id}.status must be open, resolved, or accepted"
            )
        if finding.get("confidence") not in VALID_CONFIDENCE:
            errors.append(
                f"finding {finding_id}.confidence must be confirmed, likely, or hypothesis"
            )
        if finding.get("scope") not in VALID_SCOPES:
            errors.append(f"finding {finding_id}.scope must be systemic or local")
        if not isinstance(finding.get("affects_primary_flow"), bool):
            errors.append(
                f"finding {finding_id}.affects_primary_flow must be true or false"
            )

    return errors, warnings, dimensions, findings


def score_document(
    document: dict[str, Any],
    dimensions: list[DimensionResult],
    findings: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    raw_score = sum(item.weight * item.effective_rating / 4.0 for item in dimensions)
    cap = 100.0
    cap_reasons: list[str] = []

    unresolved_findings = [
        item for item in findings.values() if item.get("status") != "resolved"
    ]
    has_p0 = any(item.get("severity") == "P0" for item in unresolved_findings)
    has_primary_p1 = any(
        item.get("severity") == "P1" and item.get("affects_primary_flow") is True
        for item in unresolved_findings
    )
    has_any_p1 = any(item.get("severity") == "P1" for item in unresolved_findings)

    if has_p0:
        cap = min(cap, 49.0)
        cap_reasons.append("unresolved P0 finding")
    if has_primary_p1:
        cap = min(cap, 69.0)
        cap_reasons.append("unresolved P1 affecting the primary flow")
    elif has_any_p1:
        cap = min(cap, 79.0)
        cap_reasons.append("unresolved P1 finding")

    gate_statuses = {
        item["id"]: item["status"]
        for item in document["gates"]
        if isinstance(item, dict)
        and item.get("id") in {gate_id for gate_id, _ in GATES}
    }
    failed_gates = [
        gate_id for gate_id, status in gate_statuses.items() if status == "fail"
    ]
    unverified_gates = [
        gate_id for gate_id, status in gate_statuses.items() if status == "unverified"
    ]
    na_gates = [gate_id for gate_id, status in gate_statuses.items() if status == "na"]
    required_gate_ids = REQUIRED_GATES_BY_MODE.get(
        document.get("mode"), frozenset(gate_id for gate_id, _ in GATES)
    )
    optional_gate_ids = {gate_id for gate_id, _ in GATES} - set(required_gate_ids)
    required_unverified_gates = [
        gate_id
        for gate_id in sorted(required_gate_ids)
        if gate_statuses.get(gate_id) == "unverified"
    ]
    required_na_gates = [
        gate_id
        for gate_id in sorted(required_gate_ids)
        if gate_statuses.get(gate_id) == "na"
    ]
    applicable_gate_statuses = [
        status for status in gate_statuses.values() if status != "na"
    ]
    no_applicable_gates = not applicable_gate_statuses

    if failed_gates:
        cap = min(cap, 69.0)
        cap_reasons.append("failed applicable gate")
    if unverified_gates:
        cap = min(cap, 79.0)
        cap_reasons.append("unverified gate")
    if required_na_gates:
        cap = min(cap, 79.0)
        cap_reasons.append("not-applicable required gate")
    if no_applicable_gates:
        cap = min(cap, 79.0)
        cap_reasons.append("no applicable evidence gates")

    final_score = min(raw_score, cap)
    has_unresolved_p0_or_p1 = has_p0 or has_any_p1
    all_required_gates_pass = all(
        gate_statuses.get(gate_id) == "pass" for gate_id in required_gate_ids
    )
    optional_gates_resolved = all(
        gate_statuses.get(gate_id) in {"pass", "na"} for gate_id in optional_gate_ids
    )
    dimension_floor_failures = [
        item.dimension_id for item in dimensions if item.effective_rating < 3
    ]
    dimension_floor_pass = not dimension_floor_failures and len(dimensions) == len(
        DIMENSIONS
    )
    g5_pass = gate_statuses.get("G5") == "pass"
    professional_grade = (
        final_score >= 80
        and all_required_gates_pass
        and optional_gates_resolved
        and not has_unresolved_p0_or_p1
        and dimension_floor_pass
        and g5_pass
    )

    if has_p0:
        judgment = "Not viable"
    elif failed_gates or has_primary_p1:
        judgment = "Not ready"
    elif unverified_gates or required_na_gates or no_applicable_gates:
        judgment = "Evidence incomplete"
    elif has_any_p1:
        judgment = "Needs meaningful refinement"
    elif (
        professional_grade
        and final_score >= 90
        and not unresolved_findings
        and dimension_floor_pass
        and all(
            next(
                item.effective_rating
                for item in dimensions
                if item.dimension_id == dimension_id
            )
            >= 3.5
            for dimension_id in ("layout", "authorship", "craft")
        )
    ):
        judgment = "Exceptional"
    elif professional_grade:
        judgment = "Strong"
    elif final_score >= 70:
        judgment = "Needs meaningful refinement"
    else:
        judgment = "Not ready"

    finding_counts = {
        severity: sum(
            1 for item in unresolved_findings if item.get("severity") == severity
        )
        for severity in ("P0", "P1", "P2", "P3")
    }

    return {
        "raw_score": round(raw_score, 1),
        "cap": round(cap, 1),
        "score": round(final_score, 1),
        "cap_reasons": cap_reasons,
        "judgment": judgment,
        "professional_grade": professional_grade,
        "dimension_floor_pass": dimension_floor_pass,
        "dimension_floor_failures": dimension_floor_failures,
        "failed_gates": failed_gates,
        "unverified_gates": unverified_gates,
        "na_gates": na_gates,
        "required_unverified_gates": required_unverified_gates,
        "required_na_gates": required_na_gates,
        "optional_gates_resolved": optional_gates_resolved,
        "artifact_existence_checked": False,
        "missing_local_artifacts": [],
        "no_applicable_gates": no_applicable_gates,
        "unresolved_finding_counts": finding_counts,
    }


def apply_artifact_availability(
    result: dict[str, Any], missing_artifacts: list[str]
) -> dict[str, Any]:
    result["artifact_existence_checked"] = True
    result["missing_local_artifacts"] = list(missing_artifacts)
    if not missing_artifacts:
        return result

    result["cap"] = min(float(result["cap"]), 79.0)
    result["score"] = min(float(result["score"]), 79.0)
    if "missing local evidence artifacts" not in result["cap_reasons"]:
        result["cap_reasons"].append("missing local evidence artifacts")
    result["professional_grade"] = False
    if result["judgment"] in {"Exceptional", "Strong"}:
        result["judgment"] = "Evidence incomplete"
    return result


def evidence_summary(record: dict[str, Any]) -> str:
    return (
        f"[{record['evidence_type']}; {record['phase']}; surfaces "
        f"{', '.join(record['surface_ids'])}] {record['artifact']} at "
        f"{record['location']}; {record['viewport_or_state']}; inputs: "
        f"{', '.join(record['input_methods'])}; "
        f"method: {record['method']}; result: {record['result']}"
    )


def unresolved_findings(
    findings: dict[str, dict[str, Any]],
) -> list[tuple[str, dict[str, Any]]]:
    result = [
        (finding_id, item)
        for finding_id, item in findings.items()
        if item.get("status") != "resolved"
    ]
    result.sort(
        key=lambda pair: (
            int(pair[1]["severity"][1]),
            0 if pair[1]["scope"] == "systemic" else 1,
            pair[0],
        )
    )
    return result


def markdown_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def markdown_report(
    document: dict[str, Any],
    warnings: list[str],
    dimensions: list[DimensionResult],
    findings: dict[str, dict[str, Any]],
    result: dict[str, Any],
) -> str:
    gate_labels = dict(GATES)
    lines = [
        f"# {document['title']}",
        "",
        f"- Schema: {document['schema_version']}",
        f"- Mode: {document['mode']}",
        f"- Platform: {document['platform']}",
        f"- Scope: {document['scope']}",
        f"- Scope targets: {', '.join(document['scope_targets'])}",
        (
            f"- Scope exclusions: {', '.join(document['scope_exclusions'])}"
            if document["scope_exclusions"]
            else "- Scope exclusions: none"
        ),
        "",
        "## Design thesis",
        "",
        f"- Experience: {document['design_thesis']['experience']}",
        f"- Qualities: {', '.join(document['design_thesis']['qualities'])}",
        f"- Primary action: {document['design_thesis']['primary_action']}",
        f"- First attention: {document['design_thesis']['first_attention']}",
        f"- Classical target: {document['design_thesis']['classical_quality_target']}",
        f"- Expressive target: {document['design_thesis']['expressive_quality_target']}",
        f"- Signature or restraint: {document['design_thesis']['signature_or_restraint']}",
        f"- Reflexes to avoid: {', '.join(document['design_thesis']['reflexes_to_avoid'])}",
        f"- Change boundary: {document['design_thesis']['change_boundary']}",
        "",
        "## Surface coverage",
        "",
        "| Target | Location | Family | Salience | Disposition | Status | Evidence | Success delta |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- |",
    ]

    for surface in document["surfaces"]:
        lines.append(
            f"| {markdown_cell(surface['id'])} | {markdown_cell(surface['location'])} | "
            f"{markdown_cell(surface['family'])} | {surface['salience']} | "
            f"{surface['disposition']} | {surface['status']} | "
            f"{len(surface['_validated_evidence'])} | "
            f"{markdown_cell(surface['success_delta'])} |"
        )

    lines.extend(["", "## Authorship iterations", ""])
    if document["_validated_iterations"]:
        for iteration in document["_validated_iterations"]:
            lines.extend(
                [
                    f"### {iteration['id']} — {iteration['surface_id']}",
                    "",
                    f"- Critique: {iteration['critique']}",
                    f"- Response: {iteration['response']}",
                    "- Evidence:",
                ]
            )
            for evidence in iteration["_validated_evidence"]:
                lines.append(f"  - {evidence_summary(evidence)}")
            lines.append("")
    else:
        lines.extend(["No implementation iteration supplied.", ""])

    lines.extend(
        [
            "## Dynamic stability cases",
            "",
            "| Case | Type | Surfaces | Status | Evidence | Notes |",
            "| --- | --- | --- | --- | ---: | --- |",
        ]
    )
    if document["_validated_stability_cases"]:
        for item in document["_validated_stability_cases"]:
            lines.append(
                f"| {markdown_cell(item['id'])} | {item['case_type']} | "
                f"{markdown_cell(', '.join(item['surface_ids']))} | {item['status']} | "
                f"{len(item['_validated_evidence'])} | {markdown_cell(item['notes'])} |"
            )
    else:
        lines.append("| None supplied | — | — | unverified | 0 | — |")

    lines.extend(["", "## Unresolved findings", ""])

    active_findings = unresolved_findings(findings)
    if not active_findings:
        lines.append("No unresolved findings in the supplied record.")
        lines.append("")
    else:
        for finding_id, item in active_findings:
            lines.extend(
                [
                    f"### {item['severity']} {finding_id}: {item['observation']}",
                    "",
                    f"- Location: {item['location']} ({item['viewport_or_state']})",
                    f"- Impact: {item['impact']}",
                    f"- Confidence: {item['confidence']}; scope: {item['scope']}",
                    f"- Affects primary flow: {str(item['affects_primary_flow']).lower()}",
                    f"- Status: {item['status']}",
                    f"- Root cause: {item['root_cause']}",
                    f"- Remediation: {item['remediation']}",
                    f"- Verification: {item['verification']}",
                    "- Evidence:",
                ]
            )
            for evidence in item["_validated_evidence"]:
                lines.append(f"  - {evidence_summary(evidence)}")
            lines.append("")

    lines.extend(
        [
            "## Scorecard",
            "",
            f"- Score: {result['score']:.1f}/100 (raw {result['raw_score']:.1f})",
            f"- Judgment: {result['judgment']}",
            "- Professional-grade evidence gate: "
            + ("pass" if result["professional_grade"] else "not passed"),
        ]
    )
    if result["dimension_floor_failures"]:
        lines.append(
            "- Dimensions below the professional floor: "
            + ", ".join(result["dimension_floor_failures"])
        )
    if result["cap_reasons"]:
        lines.append(
            f"- Score cap: {result['cap']:.1f} due to "
            + ", ".join(result["cap_reasons"])
        )

    lines.extend(
        [
            "",
            "## Gates",
            "",
            "| Gate | Status | Coverage | Evidence | Notes |",
            "| --- | --- | ---: | ---: | --- |",
        ]
    )
    for gate in document["gates"]:
        gate_id = gate["id"]
        if gate_id not in gate_labels:
            continue
        notes = gate.get("notes", "").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {gate_id} {gate_labels[gate_id]} | {gate['status']} | "
            f"{len(gate['_validated_coverage'])}/{len(GATE_CHECKS[gate_id])} | "
            f"{len(gate['_validated_evidence'])} | {notes} |"
        )

    lines.extend(["", "## Gate evidence", ""])
    for gate in document["gates"]:
        gate_id = gate["id"]
        if gate_id not in gate_labels:
            continue
        lines.append(f"### {gate_id} {gate_labels[gate_id]}")
        lines.append("")
        coverage = gate["_validated_coverage"]
        lines.append(
            "- Coverage: " + (", ".join(coverage) if coverage else "none supplied")
        )
        if gate["_validated_evidence"]:
            lines.append("- Evidence:")
            for evidence in gate["_validated_evidence"]:
                lines.append(f"  - {evidence_summary(evidence)}")
        else:
            lines.append("- Evidence: none supplied")
        lines.append("")

    lines.extend(
        [
            "",
            "## Dimensions",
            "",
            "| Dimension | Weight | Rating | Effective | Evidence |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in dimensions:
        lines.append(
            f"| {item.label} | {item.weight} | {item.rating:g}/4 | "
            f"{item.effective_rating:g}/4 | {len(item.evidence)} |"
        )

    lines.extend(["", "## Dimension evidence", ""])
    for item in dimensions:
        lines.append(f"### {item.label}")
        lines.append("")
        if item.evidence:
            for evidence in item.evidence:
                lines.append(f"- {evidence_summary(evidence)}")
        else:
            lines.append("- No evidence supplied.")
        lines.append("")

    if warnings:
        lines.extend(["", "## Validation adjustments", ""])
        lines.extend(f"- {warning}" for warning in warnings)

    lines.extend(
        [
            "",
            "## Reminder",
            "",
            "This score summarizes the supplied structured evidence. It is not an "
            "accessibility conformance claim and cannot replace rendered, interaction, "
            "or assistive-technology testing.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def public_record(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def json_report(
    document: dict[str, Any],
    warnings: list[str],
    dimensions: list[DimensionResult],
    findings: dict[str, dict[str, Any]],
    result: dict[str, Any],
) -> str:
    payload = {
        "schema_version": document["schema_version"],
        "title": document["title"],
        "mode": document["mode"],
        "platform": document["platform"],
        "scope": document["scope"],
        "scope_targets": document["scope_targets"],
        "scope_exclusions": document["scope_exclusions"],
        "design_thesis": document["design_thesis"],
        "surfaces": [public_record(item) for item in document["surfaces"]],
        "iterations": [
            public_record(item) for item in document["_validated_iterations"]
        ],
        "stability_cases": [
            public_record(item) for item in document["_validated_stability_cases"]
        ],
        "findings": [public_record(item) for _, item in sorted(findings.items())],
        "result": result,
        "gates": [
            public_record(item)
            for item in document["gates"]
            if item.get("id") in {gate_id for gate_id, _ in GATES}
        ],
        "dimensions": [
            {
                "id": item.dimension_id,
                "label": item.label,
                "weight": item.weight,
                "rating": item.rating,
                "effective_rating": item.effective_rating,
                "evidence": list(item.evidence),
                "notes": item.notes,
            }
            for item in dimensions
        ],
        "warnings": warnings,
        "disclaimer": (
            "The result summarizes supplied structured evidence. It is not an "
            "accessibility conformance claim."
        ),
    }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and score an evidence-based UI audit JSON record."
    )
    parser.add_argument("input", nargs="?", help="Path to the audit JSON record")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument("--output", help="Write the report to this file")
    parser.add_argument(
        "--example",
        action="store_true",
        help="Print a starter audit JSON template that requires real scope and evidence",
    )
    parser.add_argument(
        "--require-professional",
        action="store_true",
        help="Exit with status 1 unless the professional-grade gate passes",
    )
    return parser.parse_args()


def emit_output(output: str, destination: str | None) -> bool:
    if not destination:
        sys.stdout.write(output)
        return True
    try:
        Path(destination).write_text(output, encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"could not write report: {error}", file=sys.stderr)
        return False
    return True


def iter_document_evidence(document: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for collection_name in (
        "surfaces",
        "iterations",
        "stability_cases",
        "gates",
        "dimensions",
        "findings",
    ):
        collection = document.get(collection_name, [])
        if not isinstance(collection, list):
            continue
        for item in collection:
            if not isinstance(item, dict):
                continue
            evidence = item.get("evidence", [])
            if isinstance(evidence, list):
                records.extend(
                    record for record in evidence if isinstance(record, dict)
                )
    return records


def missing_local_artifacts(
    document: dict[str, Any],
    input_path: Path,
) -> list[str]:
    missing: set[str] = set()
    path_suffixes = {
        ".css",
        ".gif",
        ".html",
        ".jpeg",
        ".jpg",
        ".json",
        ".log",
        ".md",
        ".mp4",
        ".pdf",
        ".png",
        ".svg",
        ".txt",
        ".webm",
        ".webp",
    }
    for record in iter_document_evidence(document):
        artifact = record.get("artifact")
        if not non_empty_string(artifact):
            continue
        parsed = urlparse(artifact)
        if parsed.scheme and parsed.scheme.lower() != "file":
            continue
        if parsed.scheme.lower() == "file":
            candidate_text = unquote(parsed.path)
        else:
            candidate_text = artifact.split("#", 1)[0]
            candidate_text = re.sub(
                r":(?:line\s*)?\d+(?::\d+)?$", "", candidate_text, flags=re.I
            )
        candidate = Path(candidate_text)
        looks_path_like = (
            candidate.suffix.lower() in path_suffixes
            or "/" in candidate_text
            or "\\" in candidate_text
            or candidate.is_absolute()
        )
        if not looks_path_like:
            continue
        resolved = (
            candidate if candidate.is_absolute() else input_path.parent / candidate
        )
        if not resolved.is_file():
            missing.add(artifact)
    return sorted(missing)


def main() -> int:
    args = parse_args()
    if args.example:
        if args.input:
            print("--example cannot be combined with an input path", file=sys.stderr)
            return 2
        output = json.dumps(example_document(), indent=2) + "\n"
        return 0 if emit_output(output, args.output) else 2

    if not args.input:
        print("an input path is required unless --example is used", file=sys.stderr)
        return 2

    input_path = Path(args.input)
    try:
        document = json.loads(input_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"audit file not found: {args.input}", file=sys.stderr)
        return 2
    except (OSError, UnicodeError) as error:
        print(f"could not read audit file: {error}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as error:
        print(
            f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}",
            file=sys.stderr,
        )
        return 2

    errors, warnings, dimensions, findings = validate_document(document)
    if errors:
        print("audit validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 2

    missing_artifacts = missing_local_artifacts(document, input_path)
    if args.require_professional:
        if missing_artifacts:
            print("audit validation failed:", file=sys.stderr)
            for artifact in missing_artifacts:
                print(
                    f"- local evidence artifact not found: {artifact}", file=sys.stderr
                )
            return 2

    result = apply_artifact_availability(
        score_document(document, dimensions, findings), missing_artifacts
    )
    if missing_artifacts:
        warnings.append(
            f"professional grade was withheld because {len(missing_artifacts)} "
            "local evidence artifact(s) were not found"
        )
    if args.format == "json":
        output = json_report(document, warnings, dimensions, findings, result)
    else:
        output = markdown_report(document, warnings, dimensions, findings, result)

    if not emit_output(output, args.output):
        return 2
    if args.require_professional and not result["professional_grade"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

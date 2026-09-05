#!/usr/bin/env python3
"""Compare before/after browser geometry for visible layout stability.

The analyzer deliberately treats CLS as supplementary evidence. A case passes only
when its explicit before/after geometry is valid and remains within the configured
CSS-pixel tolerance.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


DEFAULT_THRESHOLD_CSS_PX = 1.0
EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_INVALID = 2

ANCHOR_METRICS = ("x", "y", "width", "height")
CASE_TYPE_CONTRACTS = {
    "async-content": (True, False, True),
    "async-content-settle": (True, False, True),
    "banner-insert": (True, False, True),
    "data-transition": (True, False, True),
    "dialog-open": (True, False, True),
    "drawer-open": (True, False, True),
    "font-load": (True, False, False),
    "font-loading": (True, False, False),
    "history-navigation": (True, True, True),
    "image-load": (True, False, False),
    "media-load": (True, False, False),
    "menu-open": (True, False, True),
    "modal-open": (True, False, True),
    "navigation": (True, True, True),
    "overlay-open": (True, False, True),
    "route-transition": (True, True, True),
    "scroll-lock": (True, False, True),
    "scrollbar": (False, False, False),
    "scrollbar-gutter": (False, False, False),
    "scrollbar-navigation": (True, True, True),
    "short-long-transition": (True, True, True),
    "skeleton-settle": (True, False, True),
    "state-transition": (True, False, True),
    "sticky-fixed-boundary": (True, False, False),
    "validation-insert": (True, False, True),
    "video-load": (True, False, False),
}

_MISSING = object()


@dataclass(frozen=True)
class Snapshot:
    viewport_width: float
    client_width: float
    anchor: dict[str, float] | None
    anchor_identity: str | None
    state: Any


@dataclass(frozen=True)
class StabilityCase:
    case_id: str
    platform: str
    case_type: str
    before: Snapshot
    after: Snapshot
    cls: float | None
    state: Any
    same_document: bool | None
    runtime_attached: bool | None


class SchemaError(ValueError):
    """Raised when the input document cannot describe a valid comparison."""


def _is_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _number(
    value: Any,
    location: str,
    errors: list[str],
    *,
    positive: bool = False,
    nonnegative: bool = False,
) -> float | None:
    if not _is_number(value):
        errors.append(f"{location} must be a finite number")
        return None
    result = float(value)
    if positive and result <= 0:
        errors.append(f"{location} must be greater than 0")
        return None
    if nonnegative and result < 0:
        errors.append(f"{location} must be 0 or greater")
        return None
    return result


def _aliased_value(
    data: Mapping[str, Any],
    aliases: Sequence[str],
    location: str,
    errors: list[str],
    *,
    required: bool = True,
) -> Any:
    present = [name for name in aliases if name in data]
    if not present:
        if required:
            errors.append(f"{location} is required")
        return _MISSING
    if len(present) > 1:
        first = data[present[0]]
        if any(data[name] != first for name in present[1:]):
            errors.append(f"{location} has conflicting aliases: {', '.join(present)}")
        else:
            errors.append(
                f"{location} is duplicated through aliases: {', '.join(present)}"
            )
    return data[present[0]]


def _validate_metadata(value: Any, location: str, errors: list[str]) -> Any:
    if value is _MISSING:
        return _MISSING
    if value is None or isinstance(value, bool):
        errors.append(f"{location} must be non-empty state metadata")
        return value
    if isinstance(value, str):
        if not value.strip():
            errors.append(f"{location} must not be empty")
        return value
    if isinstance(value, Mapping):
        if not value:
            errors.append(f"{location} must not be empty")
        return dict(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        if not value:
            errors.append(f"{location} must not be empty")
        return list(value)
    if _is_number(value):
        return value
    errors.append(f"{location} must be a string, number, object, or array")
    return value


def _boolean_field(
    data: Mapping[str, Any],
    field: str,
    location: str,
    errors: list[str],
) -> bool | None:
    if field not in data:
        return None
    value = data[field]
    if not isinstance(value, bool):
        errors.append(f"{location}.{field} must be true or false")
        return None
    return value


def _parse_anchor(
    data: Mapping[str, Any], location: str, errors: list[str]
) -> tuple[dict[str, float] | None, str | None]:
    nested = data.get("anchor", _MISSING)
    flat_keys = {
        metric: f"anchor_{metric}"
        for metric in ANCHOR_METRICS
        if f"anchor_{metric}" in data
    }
    flat_identity_keys = {
        name: f"anchor_{name}"
        for name in ("id", "selector", "name")
        if f"anchor_{name}" in data
    }
    if nested is not _MISSING and (flat_keys or flat_identity_keys):
        errors.append(
            f"{location}.anchor cannot be combined with flat anchor geometry or identity fields"
        )
        return None, None
    if nested is _MISSING and not flat_keys and not flat_identity_keys:
        return None, None

    if nested is not _MISSING:
        if not isinstance(nested, Mapping):
            errors.append(f"{location}.anchor must be an object")
            return None, None
        anchor_data = nested
    else:
        anchor_data = {
            metric: data[field_name] for metric, field_name in flat_keys.items()
        }
        anchor_data.update(
            {name: data[field_name] for name, field_name in flat_identity_keys.items()}
        )

    metrics: dict[str, float] = {}
    for metric in ANCHOR_METRICS:
        if metric not in anchor_data:
            continue
        value = _number(
            anchor_data[metric],
            f"{location}.anchor.{metric}",
            errors,
            positive=metric in {"width", "height"},
        )
        if value is not None:
            metrics[metric] = value
    if not any(metric in anchor_data for metric in ANCHOR_METRICS):
        errors.append(
            f"{location}.anchor must include at least one of x, y, width, or height"
        )

    identity: str | None = None
    identity_fields = [
        name for name in ("id", "selector", "name") if name in anchor_data
    ]
    if len(identity_fields) > 1:
        errors.append(
            f"{location}.anchor must use only one identity field: id, selector, or name"
        )
    if identity_fields:
        raw_identity = anchor_data[identity_fields[0]]
        if not isinstance(raw_identity, str) or not raw_identity.strip():
            errors.append(f"{location}.anchor identity must be a non-empty string")
        else:
            identity = raw_identity.strip()

    return metrics or None, identity


def _parse_snapshot(
    raw: Any,
    location: str,
    errors: list[str],
) -> Snapshot | None:
    if not isinstance(raw, Mapping):
        errors.append(f"{location} must be an object")
        return None

    viewport_raw = _aliased_value(
        raw,
        ("viewport_width", "viewportWidth"),
        f"{location}.viewport_width",
        errors,
    )
    client_raw = _aliased_value(
        raw,
        ("client_width", "clientWidth"),
        f"{location}.client_width",
        errors,
    )
    viewport_width = (
        _number(viewport_raw, f"{location}.viewport_width", errors, positive=True)
        if viewport_raw is not _MISSING
        else None
    )
    client_width = (
        _number(client_raw, f"{location}.client_width", errors, positive=True)
        if client_raw is not _MISSING
        else None
    )
    anchor, identity = _parse_anchor(raw, location, errors)
    state = _validate_metadata(raw.get("state", _MISSING), f"{location}.state", errors)

    if viewport_width is None or client_width is None:
        return None
    if client_width > viewport_width:
        errors.append(
            f"{location}.client_width cannot exceed {location}.viewport_width"
        )
    return Snapshot(
        viewport_width=viewport_width,
        client_width=client_width,
        anchor=anchor,
        anchor_identity=identity,
        state=state,
    )


def _state_metadata(
    raw: Mapping[str, Any],
    before: Snapshot,
    after: Snapshot,
    location: str,
    errors: list[str],
) -> Any:
    top_state_fields = [name for name in ("state", "states") if name in raw]
    if len(top_state_fields) > 1:
        errors.append(f"{location} cannot define both state and states")
    top_state = (
        _validate_metadata(
            raw[top_state_fields[0]], f"{location}.{top_state_fields[0]}", errors
        )
        if top_state_fields
        else _MISSING
    )
    if isinstance(top_state, Mapping):
        has_top_before = "before" in top_state
        has_top_after = "after" in top_state
        if has_top_before != has_top_after:
            errors.append(
                f"{location}.{top_state_fields[0]} must include both before and "
                "after when either is provided"
            )
        elif has_top_before and has_top_after:
            normalized_top_state = dict(top_state)
            normalized_top_state["before"] = _validate_metadata(
                top_state["before"],
                f"{location}.{top_state_fields[0]}.before",
                errors,
            )
            normalized_top_state["after"] = _validate_metadata(
                top_state["after"],
                f"{location}.{top_state_fields[0]}.after",
                errors,
            )
            top_state = normalized_top_state

    has_before_state = before.state is not _MISSING
    has_after_state = after.state is not _MISSING
    if has_before_state != has_after_state:
        errors.append(
            f"{location} must provide state metadata for both before and after snapshots"
        )

    if has_before_state and has_after_state:
        snapshot_states: Any = {"before": before.state, "after": after.state}
        if top_state is not _MISSING:
            return {"snapshots": snapshot_states, "case": top_state}
        return snapshot_states

    if top_state is _MISSING:
        errors.append(
            f"{location} requires state metadata, either at case level or in both snapshots"
        )
        return None
    return top_state


def _parse_case(raw: Any, index: int) -> tuple[StabilityCase | None, list[str]]:
    location = f"cases[{index}]"
    errors: list[str] = []
    if not isinstance(raw, Mapping):
        return None, [f"{location} must be an object"]

    raw_id = raw.get("id", raw.get("name", f"case-{index + 1}"))
    if not isinstance(raw_id, str) or not raw_id.strip():
        errors.append(f"{location}.id must be a non-empty string when provided")
        case_id = f"case-{index + 1}"
    else:
        case_id = raw_id.strip()

    raw_platform = raw.get("platform", _MISSING)
    if not isinstance(raw_platform, str) or not raw_platform.strip():
        errors.append(f"{location}.platform must be a non-empty string")
        platform = "unknown"
    else:
        platform = raw_platform.strip()

    raw_type = raw.get("type", _MISSING)
    if not isinstance(raw_type, str) or not raw_type.strip():
        errors.append(f"{location}.type must be a non-empty string")
        case_type = "unknown"
    else:
        case_type = raw_type.strip()

    before = _parse_snapshot(raw.get("before", _MISSING), f"{location}.before", errors)
    after = _parse_snapshot(raw.get("after", _MISSING), f"{location}.after", errors)

    cls_value: float | None = None
    if "cls" in raw:
        cls_value = _number(raw["cls"], f"{location}.cls", errors, nonnegative=True)

    if before is None or after is None:
        return None, errors

    state = _state_metadata(raw, before, after, location, errors)

    if (before.anchor is None) != (after.anchor is None):
        errors.append(
            f"{location} must provide anchor geometry in both before and after snapshots"
        )
    elif before.anchor is not None and after.anchor is not None:
        before_metrics = set(before.anchor)
        after_metrics = set(after.anchor)
        if before_metrics != after_metrics:
            errors.append(
                f"{location} anchor metrics must match before and after "
                f"(before: {', '.join(sorted(before_metrics)) or 'none'}; "
                f"after: {', '.join(sorted(after_metrics)) or 'none'})"
            )
        if bool(before.anchor_identity) != bool(after.anchor_identity):
            errors.append(
                f"{location} must identify the compared anchor in both snapshots or neither"
            )
        elif (
            before.anchor_identity
            and after.anchor_identity
            and before.anchor_identity != after.anchor_identity
        ):
            errors.append(
                f"{location} anchors identify different elements "
                f"({before.anchor_identity!r} and {after.anchor_identity!r})"
            )

    normalized_type = case_type.strip().lower().replace("_", "-")
    contract = CASE_TYPE_CONTRACTS.get(normalized_type)
    if contract is None:
        errors.append(
            f"{location}.type must be one of: " + ", ".join(sorted(CASE_TYPE_CONTRACTS))
        )
        needs_anchor = False
        needs_same_document = False
        needs_runtime = False
    else:
        needs_anchor, needs_same_document, needs_runtime = contract

    if needs_anchor and (before.anchor is None or after.anchor is None):
        errors.append(
            f"{location} type {case_type!r} requires comparable anchor geometry; "
            "client widths and CLS alone cannot verify content stability"
        )
    elif needs_anchor and before.anchor is not None and after.anchor is not None:
        missing_metrics = set(ANCHOR_METRICS) - set(before.anchor)
        if missing_metrics:
            errors.append(
                f"{location} type {case_type!r} requires complete anchor x, y, "
                "width, and height geometry; missing "
                + ", ".join(sorted(missing_metrics))
            )
        if not before.anchor_identity or not after.anchor_identity:
            errors.append(
                f"{location} type {case_type!r} requires the same named anchor "
                "selector, id, or name in both snapshots"
            )

    state_pair: tuple[Any, Any] | None = None
    if isinstance(state, Mapping):
        if "before" in state and "after" in state:
            state_pair = (state["before"], state["after"])
        elif isinstance(state.get("snapshots"), Mapping):
            snapshots = state["snapshots"]
            if "before" in snapshots and "after" in snapshots:
                state_pair = (snapshots["before"], snapshots["after"])
    if state_pair is None:
        errors.append(
            f"{location} must identify distinct before and after state metadata"
        )
    elif state_pair[0] == state_pair[1]:
        errors.append(f"{location} before and after states must be different")

    same_document = _boolean_field(raw, "same_document", location, errors)
    if needs_same_document and same_document is not True:
        errors.append(
            f"{location} type {case_type!r} requires same_document: true; a full "
            "document load does not verify client-side route stability"
        )

    runtime_attached = _boolean_field(raw, "runtime_attached", location, errors)
    if needs_runtime and runtime_attached is not True:
        errors.append(
            f"{location} type {case_type!r} requires runtime_attached: true; "
            "static output or a detached client runtime cannot verify this transition"
        )

    if errors:
        return None, errors
    return (
        StabilityCase(
            case_id=case_id,
            platform=platform,
            case_type=case_type,
            before=before,
            after=after,
            cls=cls_value,
            state=state,
            same_document=same_document,
            runtime_attached=runtime_attached,
        ),
        [],
    )


def _root_cases(document: Any) -> list[Any]:
    if isinstance(document, list):
        cases = document
    elif isinstance(document, Mapping) and "cases" in document:
        cases = document["cases"]
        if not isinstance(cases, list):
            raise SchemaError("cases must be an array")
    elif isinstance(document, Mapping) and {
        "platform",
        "type",
        "before",
        "after",
    }.issubset(document):
        cases = [document]
    else:
        raise SchemaError(
            "input must be a case object, an array of cases, or an object with a cases array"
        )
    if not cases:
        raise SchemaError("at least one stability case is required")
    return list(cases)


def _check(
    check_id: str,
    label: str,
    before: float,
    after: float,
    threshold: float,
    *,
    authoritative: bool = True,
) -> dict[str, Any]:
    delta = after - before
    passed = abs(delta) <= threshold
    return {
        "id": check_id,
        "label": label,
        "before": before,
        "after": after,
        "delta_css_px": delta,
        "absolute_delta_css_px": abs(delta),
        "status": "pass" if passed else "fail",
        "role": "authoritative" if authoritative else "diagnostic",
        "message": (
            f"{label} changed by {_format_number(delta)} CSS px "
            f"(allowed absolute change: {_format_number(threshold)} CSS px)."
        ),
    }


def analyze_case(case: StabilityCase, threshold: float) -> dict[str, Any]:
    has_complete_anchor = (
        case.before.anchor is not None
        and case.after.anchor is not None
        and set(ANCHOR_METRICS).issubset(case.before.anchor)
        and set(ANCHOR_METRICS).issubset(case.after.anchor)
    )
    checks = [
        _check(
            "viewport-width",
            "Viewport width",
            case.before.viewport_width,
            case.after.viewport_width,
            threshold,
        ),
        _check(
            "client-width",
            "Document client width",
            case.before.client_width,
            case.after.client_width,
            threshold,
            authoritative=not has_complete_anchor,
        ),
        _check(
            "scrollbar-gutter",
            "Reserved scrollbar gutter",
            case.before.viewport_width - case.before.client_width,
            case.after.viewport_width - case.after.client_width,
            threshold,
            authoritative=not has_complete_anchor,
        ),
    ]

    if case.before.anchor is not None and case.after.anchor is not None:
        for metric in ANCHOR_METRICS:
            if metric not in case.before.anchor or metric not in case.after.anchor:
                continue
            checks.append(
                _check(
                    f"anchor-{metric}",
                    f"Anchor {metric}",
                    case.before.anchor[metric],
                    case.after.anchor[metric],
                    threshold,
                )
            )

    issues = [
        check["message"]
        for check in checks
        if check["status"] == "fail" and check["role"] == "authoritative"
    ]
    diagnostics = [
        check["message"]
        for check in checks
        if check["status"] == "fail" and check["role"] == "diagnostic"
    ]
    max_delta = max(check["absolute_delta_css_px"] for check in checks)
    return {
        "id": case.case_id,
        "platform": case.platform,
        "type": case.case_type,
        "status": "fail" if issues else "pass",
        "threshold_css_px": threshold,
        "state": case.state,
        "same_document": case.same_document,
        "runtime_attached": case.runtime_attached,
        "cls": case.cls,
        "cls_role": "supplementary; not used as the sole pass condition",
        "max_absolute_delta_css_px": max_delta,
        "checks": checks,
        "issues": issues,
        "diagnostics": diagnostics,
    }


def analyze_document(
    document: Any, threshold: float = DEFAULT_THRESHOLD_CSS_PX
) -> dict[str, Any]:
    if not _is_number(threshold) or float(threshold) < 0:
        raise SchemaError("threshold must be a finite number 0 or greater")
    normalized_threshold = float(threshold)
    raw_cases = _root_cases(document)

    results: list[dict[str, Any]] = []
    input_errors: list[str] = []
    for index, raw_case in enumerate(raw_cases):
        case, errors = _parse_case(raw_case, index)
        if errors:
            raw_cls = raw_case.get("cls") if isinstance(raw_case, Mapping) else None
            safe_cls = (
                float(raw_cls) if _is_number(raw_cls) and float(raw_cls) >= 0 else None
            )
            case_id = (
                raw_case.get("id", raw_case.get("name", f"case-{index + 1}"))
                if isinstance(raw_case, Mapping)
                else f"case-{index + 1}"
            )
            results.append(
                {
                    "id": case_id if isinstance(case_id, str) else f"case-{index + 1}",
                    "platform": (
                        raw_case.get("platform")
                        if isinstance(raw_case, Mapping)
                        else None
                    ),
                    "type": raw_case.get("type")
                    if isinstance(raw_case, Mapping)
                    else None,
                    "status": "invalid",
                    "threshold_css_px": normalized_threshold,
                    "state": None,
                    "same_document": None,
                    "runtime_attached": None,
                    "cls": safe_cls,
                    "cls_role": "supplementary; not used as the sole pass condition",
                    "max_absolute_delta_css_px": None,
                    "checks": [],
                    "issues": errors,
                    "diagnostics": [],
                }
            )
            input_errors.extend(errors)
            continue
        assert case is not None
        results.append(analyze_case(case, normalized_threshold))

    counts = {
        "total": len(results),
        "passed": sum(result["status"] == "pass" for result in results),
        "failed": sum(result["status"] == "fail" for result in results),
        "invalid": sum(result["status"] == "invalid" for result in results),
    }
    status = "invalid" if counts["invalid"] else "fail" if counts["failed"] else "pass"
    return {
        "status": status,
        "threshold_css_px": normalized_threshold,
        "summary": counts,
        "cases": results,
        "errors": input_errors,
    }


def exit_code(report: Mapping[str, Any]) -> int:
    status = report.get("status")
    if status == "invalid":
        return EXIT_INVALID
    if status == "fail":
        return EXIT_FAIL
    return EXIT_PASS


def _format_number(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    number = float(value)
    if number == 0:
        number = 0.0
    return f"{number:.3f}".rstrip("0").rstrip(".")


def _markdown_cell(value: Any) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report: Mapping[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Layout stability analysis",
        "",
        f"**Status:** {str(report['status']).upper()}",
        "",
        (
            f"Geometry tolerance: {_format_number(report['threshold_css_px'])} CSS px. "
            "Complete persistent-anchor geometry is authoritative when supplied; "
            "client width and gutter become diagnostic. CLS is supplementary evidence "
            "and never substitutes for before/after geometry."
        ),
        "",
        (
            f"Cases: {summary['total']} total; {summary['passed']} passed; "
            f"{summary['failed']} failed; {summary['invalid']} invalid."
        ),
        "",
        "| Case | Platform | Type | Same document | Runtime | Status | Max change | CLS |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: |",
    ]
    for result in report["cases"]:
        max_delta = result["max_absolute_delta_css_px"]
        max_text = f"{_format_number(max_delta)} px" if max_delta is not None else "—"
        cls_text = _format_number(result["cls"]) if result["cls"] is not None else "—"
        lines.append(
            "| "
            + " | ".join(
                _markdown_cell(value)
                for value in (
                    result["id"],
                    result["platform"],
                    result["type"],
                    (
                        "yes"
                        if result["same_document"] is True
                        else "no"
                        if result["same_document"] is False
                        else "—"
                    ),
                    (
                        "attached"
                        if result["runtime_attached"] is True
                        else "detached"
                        if result["runtime_attached"] is False
                        else "—"
                    ),
                    str(result["status"]).upper(),
                    max_text,
                    cls_text,
                )
            )
            + " |"
        )

    for result in report["cases"]:
        lines.extend(["", f"## {_markdown_cell(result['id'])}", ""])
        lines.append(f"Status: **{str(result['status']).upper()}**")
        if result["state"] is not None:
            lines.extend(
                [
                    "",
                    "State metadata:",
                    "",
                    "```json",
                    json.dumps(result["state"], indent=2, sort_keys=True),
                    "```",
                ]
            )
        if result["checks"]:
            lines.extend(
                [
                    "",
                    "| Measurement | Before | After | Change | Role | Status |",
                    "| --- | ---: | ---: | ---: | --- | --- |",
                ]
            )
            for check in result["checks"]:
                lines.append(
                    "| "
                    + " | ".join(
                        (
                            _markdown_cell(check["label"]),
                            _format_number(check["before"]),
                            _format_number(check["after"]),
                            _format_number(check["delta_css_px"]),
                            str(check["role"]),
                            str(check["status"]).upper(),
                        )
                    )
                    + " |"
                )
        if result["issues"]:
            lines.extend(["", "Issues:", ""])
            lines.extend(f"- {issue}" for issue in result["issues"])
        if result["diagnostics"]:
            lines.extend(["", "Diagnostic changes:", ""])
            lines.extend(f"- {item}" for item in result["diagnostics"])

    return "\n".join(lines) + "\n"


def example_document() -> dict[str, Any]:
    return {
        "cases": [
            {
                "id": "short-to-long-route",
                "platform": "web-desktop-chromium",
                "type": "scrollbar-navigation",
                "same_document": True,
                "runtime_attached": True,
                "before": {
                    "viewport_width": 1440,
                    "client_width": 1425,
                    "anchor": {
                        "selector": "main",
                        "x": 120,
                        "y": 96,
                        "width": 1200,
                        "height": 640,
                    },
                    "state": {"route": "/short", "scrollbar": "reserved"},
                },
                "after": {
                    "viewport_width": 1440,
                    "client_width": 1425,
                    "anchor": {
                        "selector": "main",
                        "x": 120,
                        "y": 96,
                        "width": 1200,
                        "height": 640,
                    },
                    "state": {"route": "/long", "scrollbar": "visible"},
                },
                "cls": 0,
            }
        ]
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare explicit before/after geometry for scrollbar, font, media, "
            "async-content, modal, and navigation layout stability."
        )
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="JSON file to analyze, or - for stdin",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD_CSS_PX,
        metavar="CSS_PX",
        help="Maximum allowed absolute geometry change (default: 1 CSS px)",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Print an example JSON document and exit",
    )
    args = parser.parse_args(argv)
    if not args.example and not args.input:
        parser.error("input is required unless --example is used")
    if not math.isfinite(args.threshold) or args.threshold < 0:
        parser.error("--threshold must be a finite number 0 or greater")
    return args


def _load_json(path: str) -> Any:
    def reject_nonstandard_number(value: str) -> None:
        raise SchemaError(f"non-standard JSON number {value!r} is not allowed")

    if path == "-":
        return json.load(sys.stdin, parse_constant=reject_nonstandard_number)
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle, parse_constant=reject_nonstandard_number)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.example:
        print(json.dumps(example_document(), indent=2, sort_keys=True))
        return EXIT_PASS

    try:
        document = _load_json(args.input)
        report = analyze_document(document, args.threshold)
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError) as error:
        report = {
            "status": "invalid",
            "threshold_css_px": args.threshold,
            "summary": {"total": 0, "passed": 0, "failed": 0, "invalid": 1},
            "cases": [],
            "errors": [str(error)],
        }

    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    else:
        print(render_markdown(report), end="")
        if report["errors"] and not report["cases"]:
            for error in report["errors"]:
                print(f"- {error}")
    return exit_code(report)


if __name__ == "__main__":
    raise SystemExit(main())

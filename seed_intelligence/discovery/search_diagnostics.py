"""Interpret optional recorded diagnostics without inventing absent measurements."""
from statistics import mean

from ..contracts import numeric
from ..core.seed_manifest import MANIFEST_HASH
from ..profiler.seed_semantics import recorded_columns
from ..profiler.structure_analyzer import structural_cohorts


def _hotspot(metrics):
    sections = metrics.get("recorded_section_seconds")
    if not isinstance(sections, dict):
        return
    durations = {name: value for name, value in list(sections.items())[:32]
                 if isinstance(name, str) and 0 < len(name) <= 100 and numeric(value) and value > 0}
    if not durations:
        return
    largest = max(durations, key=durations.get)
    share = durations[largest] / sum(durations.values())
    if share >= 0.5:
        return {"section": largest, "shareOfRecordedSeconds": share}


def _reproduced(metrics):
    failures = metrics.get("recorded_failure_counts")
    if isinstance(failures, dict):
        result = {name: count for name, count in list(failures.items())[:32]
                  if isinstance(name, str) and 0 < len(name) <= 100 and type(count) is int and count >= 2}
        return result or None


def _sensitivity(metrics):
    trials = metrics.get("recorded_parameter_trials")
    if not isinstance(trials, list):
        return
    values = {}
    for trial in trials[-32:]:
        if (isinstance(trial, dict) and trial.get("manifestHash") == MANIFEST_HASH
                and numeric(trial.get("value")) and numeric(trial.get("reportedMean"))):
            values[trial["value"]] = trial["reportedMean"]
    if len(values) >= 2 and len(set(values.values())) > 1:
        return {"distinctValues": len(values), "reportedMeanRange": max(values.values()) - min(values.values())}


def _binding(metrics, deltas):
    result = {}
    for name, flags in recorded_columns(metrics, "recorded_binding_constraints").items():
        if not all(type(flag) is bool for flag in flags):
            continue
        limited = [delta for delta, flag in zip(deltas, flags) if flag]
        free = [delta for delta, flag in zip(deltas, flags) if not flag]
        if len(limited) >= 3 and len(free) >= 3 and mean(limited) < mean(free):
            result[name] = {"bindingCases": len(limited), "meanDelta": mean(limited)}
    return result


def search_diagnostics(metrics, deltas):
    def groups(name):
        return structural_cohorts(recorded_columns(metrics, name), deltas)

    signals = {
        "commonHotspot": _hotspot(metrics),
        "algorithmInteraction": groups("recorded_algorithm_cohorts"),
        "reproducedFailure": _reproduced(metrics),
        "instanceRelations": groups("recorded_relationship_cohorts"),
        "parameterSensitivity": _sensitivity(metrics),
        "bindingConstraints": _binding(metrics, deltas),
    }
    return {key: value for key, value in signals.items() if value}

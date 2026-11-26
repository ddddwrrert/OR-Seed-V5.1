from ..profiler.profile_updater import add_recorded_features
from ..profiler.seed_profiler import compare
from ..storage.history import reference_ids
from ..storage.evaluation_cache import cached_evaluation
from ..storage.profile_store import evidence_profile
from .unknown_pattern_detector import unexplained_regression
from .recorded_evidence import analyze
from .search_diagnostics import search_diagnostics

def opportunities(rows, parent, evaluations, threshold):
    current = cached_evaluation(evaluations, parent["id"])
    references = []
    for reference in reference_ids(rows, parent):
        previous = cached_evaluation(evaluations, reference)
        profile = compare(previous, current)
        if profile and unexplained_regression(profile, threshold):
            profile = add_recorded_features(profile, current["metrics"])
            telemetry = analyze(previous, current, current["metrics"]["score_direction"])
            source = current.get("sourceEvidence")
            if isinstance(source, dict) and isinstance(source.get("sourceStructure"), dict):
                telemetry["sourceStructure"] = source["sourceStructure"]
            telemetry.update(profile.get("observedFeatures", {}))
            telemetry.update(search_diagnostics(current["metrics"], profile["deltas"]))
            references.append(evidence_profile(reference, profile, telemetry))
    return references

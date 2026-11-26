from ..contracts import hypothesis
from ..reliability.evidence_analyzer import plausible_gain
from ..reliability.evidence_registry import cited_evidence
from ..storage.evidence_store import find_reference
from ..profiler.feature_registry import register_feature

def review(report, references, threshold):
    if not hypothesis(report):
        return
    match = find_reference(references, report.get("reference"))
    gain, cost = report.get("expectedGain"), report.get("cost")
    if (not match or not plausible_gain(gain, threshold, match["profile"]["recoverableMean"])
            or not isinstance(cost, str) or not cost.strip() or len(cost) > 400):
        return
    cited = cited_evidence(report, match)
    if cited is None:
        return
    reviewed = {**report, "recoverableMean": match["profile"]["recoverableMean"],
                "recordedEvidence": cited}
    return register_feature(reviewed, match["profile"])

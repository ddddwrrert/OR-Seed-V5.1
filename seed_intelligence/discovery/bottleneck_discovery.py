from ..contracts import hypothesis, numeric
from ..profiler.seed_profiler import compare, observe_feature
from ..storage.history import reference_ids

def opportunities(rows, parent, evaluations, threshold):
    current = evaluations.get(parent["id"])
    references = []
    for reference in reference_ids(rows, parent):
        profile = compare(evaluations.get(reference), current)
        if profile and profile["improvements"] and profile["recoverableMean"] > threshold:
            references.append({"reference": reference, "profile": profile})
    return references

def review(report, references, threshold):
    if not hypothesis(report):
        return
    match = next((item for item in references if item["reference"] == report.get("reference")), None)
    gain, cost = report.get("expectedGain"), report.get("cost")
    if (not match or not numeric(gain) or not threshold < gain <= match["profile"]["recoverableMean"]
            or not isinstance(cost, str) or not cost.strip() or len(cost) > 400):
        return
    reviewed = {**report, "recoverableMean": match["profile"]["recoverableMean"]}
    if report.get("feature") is not None:
        feature = observe_feature(report["feature"], match["profile"])
        if not feature:
            return
        reviewed["feature"] = feature
    return reviewed

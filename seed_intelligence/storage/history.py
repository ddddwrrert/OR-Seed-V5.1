from .candidate_store import recent_challengers
from .hypothesis_store import hypotheses_for

def reference_ids(rows, parent):
    compared = recent_challengers(rows, parent["id"])
    existing = [report["reference"] for report in hypotheses_for(rows, parent["id"]) if report.get("reference")]
    ancestor = [parent["parent"]] if parent.get("parent") else []
    return list(dict.fromkeys(compared + existing + ancestor))

def discovered(rows, parent_id):
    return hypotheses_for(rows, parent_id)

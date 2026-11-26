from ..core.score_registry import scored_record
from ..discovery.source_code_analyzer import source_evidence

def score_evaluation(metrics, source):
    record = scored_record(metrics)
    if record["fitness"] is not None:
        record["sourceEvidence"] = source_evidence(source[:16000].decode("utf-8", errors="replace"))
    return record

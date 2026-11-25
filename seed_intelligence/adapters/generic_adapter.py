from ..core.evaluation_contract import panel

def evidence_capabilities(evaluation):
    metrics = (evaluation or {}).get("metrics", {})
    return {
        "pairedScores": panel(metrics) is not None,
        "runtime": isinstance(metrics.get("max_execution_time_sec"), (int, float)),
        "trace": isinstance(metrics.get("search_trace"), list) and bool(metrics["search_trace"]),
        "operatorGains": isinstance(metrics.get("operator_gains"), dict) and bool(metrics["operator_gains"]),
    }

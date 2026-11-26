def parent_metrics(evaluation):
    metrics = (evaluation or {}).get("metrics")
    return metrics if isinstance(metrics, dict) else {}

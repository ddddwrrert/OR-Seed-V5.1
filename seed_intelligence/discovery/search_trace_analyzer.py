from ..contracts import numeric

def trace_evidence(after, direction):
    observations = {}
    trace = after.get("search_trace")
    if isinstance(trace, list):
        recent = trace[-32:]
        scores = [event.get("score") for event in recent if isinstance(event, dict)]
        if len(scores) == len(recent) and len(scores) >= 3 and all(numeric(score) for score in scores):
            # Trace scores must use the same direction as the task for this summary.
            if after.get("search_trace_score") == "official":
                suffix = 1
                for score in reversed(scores[:-1]):
                    if score != scores[-1]:
                        break
                    suffix += 1
                observations["trace"] = {"samples": len(scores), "tailPlateauSamples": suffix,
                                         "observedGain": (scores[-1] - scores[0]) * direction}

    return observations

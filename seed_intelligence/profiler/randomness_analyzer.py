from statistics import mean
from ..contracts import numeric

def repeat_variation(metrics):
    repeats = metrics.get("recorded_repeat_means")
    if (not isinstance(repeats, list) or not 2 <= len(repeats) <= 32
            or not all(numeric(value) for value in repeats)):
        return None
    return {"recordedRuns": len(repeats), "spread": max(repeats) - min(repeats),
            "meanReported": mean(repeats)}

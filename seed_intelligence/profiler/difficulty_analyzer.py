from statistics import mean
from ..contracts import numeric

def timing_difficulty(metrics, deltas):
    rows = metrics.get("seed_scores", [])
    seconds = [row.get("seconds") for row in rows]
    if len(seconds) != len(deltas) or not all(numeric(value) and value >= 0 for value in seconds):
        return None
    ordered = sorted(range(len(seconds)), key=seconds.__getitem__)
    size = len(seconds) // 5
    fast, slow = ordered[:size], ordered[-size:]
    if seconds[fast[-1]] == seconds[slow[0]]:
        return None
    return {"fastMeanSeconds": mean(seconds[index] for index in fast),
            "slowMeanSeconds": mean(seconds[index] for index in slow),
            "slowMeanDelta": mean(deltas[index] for index in slow),
            "fastMeanDelta": mean(deltas[index] for index in fast)}

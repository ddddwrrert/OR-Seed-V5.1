from ..contracts import numeric

def outcome(parent, fitness):
    delta = fitness - parent if numeric(parent) and numeric(fitness) else None
    return {
        "delta": delta,
        "outcome": "invalid" if delta is None else "improved" if delta > 0 else "no-improvement",
        "candidateCost": 1,
    }

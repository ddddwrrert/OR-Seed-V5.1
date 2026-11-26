from ..feedback.per_seed_delta import paired_delta

def response(previous, current):
    deltas = paired_delta(previous, current)
    if deltas is None:
        return
    regressions = [(seed, delta) for seed, delta in enumerate(deltas) if delta < 0]
    return {"deltas": deltas, "regressions": regressions,
            "improvements": sum(delta > 0 for delta in deltas),
            "recoverableMean": sum(-delta for _, delta in regressions) / len(deltas)}

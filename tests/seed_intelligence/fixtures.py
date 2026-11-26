from test_controller import BUDGET, CHILD, PARENT, evaluation, hypothesis

def contrasted(**metrics):
    prior = evaluation([120] * 25 + [80] * 25)
    current = evaluation([100] * 50)
    current["metrics"].update(metrics)
    return {CHILD["id"]: prior, PARENT["id"]: current}

def report(**extra):
    return {**hypothesis("different-neighborhood"), "reference": CHILD["id"],
            "expectedGain": 2, "cost": "one candidate", **extra}

def trials(key, *deltas):
    return [{"guidance": {"id": key, "delta": delta,
                           "outcome": "improved" if delta > 0 else "no-improvement"}}
            for delta in deltas]

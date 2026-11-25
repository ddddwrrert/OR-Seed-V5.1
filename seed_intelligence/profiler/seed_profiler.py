from statistics import mean
from ..core.evaluation_contract import panel
from ..contracts import numeric

def compare(previous, current):
    if not all(isinstance(record, dict) and numeric(record.get("fitness")) for record in (previous, current)):
        return
    before, after = (panel(record.get("metrics")) for record in (previous, current))
    if not before or not after or before[0] != after[0]:
        return
    deltas = [(b - a) * after[0] for a, b in zip(before[1], after[1])]
    regressions = [(seed, delta) for seed, delta in enumerate(deltas) if delta < 0]
    return {
        "deltas": deltas,
        "regressions": regressions,
        "improvements": sum(delta > 0 for delta in deltas),
        "recoverableMean": sum(-delta for _, delta in regressions) / len(deltas),
        "scoreRange": max(after[1]) - min(after[1]),
    }

def observe_feature(feature, profile):
    if not isinstance(feature, dict):
        return
    name, observation, seeds = (feature.get(key) for key in ("name", "observation", "seeds"))
    if not isinstance(name, str) or not name.strip() or len(name) > 150:
        return
    if not isinstance(observation, str) or not observation.strip() or len(observation) > 1000:
        return
    deltas = profile["deltas"]
    if (not isinstance(seeds, list) or not 0 < len(seeds) < len(deltas)
            or any(type(seed) is not int or not 0 <= seed < len(deltas) for seed in seeds)
            or len(set(seeds)) != len(seeds)):
        return
    cohort = set(seeds)
    observed = mean(deltas[seed] for seed in seeds)
    outside = mean(delta for seed, delta in enumerate(deltas) if seed not in cohort)
    if observed < 0 and observed < outside:
        return {"name": name, "observation": observation, "seeds": seeds, "observedDelta": observed}

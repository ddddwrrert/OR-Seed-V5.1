from statistics import mean

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

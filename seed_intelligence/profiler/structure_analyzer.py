from collections import defaultdict
from statistics import mean

def structural_cohorts(columns, deltas):
    results = {}
    for name, values in columns.items():
        if not all(isinstance(value, str) and 0 < len(value) <= 100 for value in values):
            continue
        groups = defaultdict(list)
        for seed, label in enumerate(values):
            groups[label].append(deltas[seed])
        covered = {label: {"count": len(scores), "meanDelta": mean(scores)}
                   for label, scores in groups.items() if len(scores) >= 3}
        if len(covered) > 1:
            results[name] = covered
    return results

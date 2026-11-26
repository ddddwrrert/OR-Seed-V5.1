from statistics import mean
from ..contracts import numeric

def numeric_contrasts(columns, deltas):
    results = {}
    for name, values in columns.items():
        if not all(numeric(value) for value in values):
            continue
        cutoff = sorted(values)[len(values) // 2]
        low = [index for index, value in enumerate(values) if value < cutoff]
        high = [index for index, value in enumerate(values) if value >= cutoff]
        if min(len(low), len(high)) >= 5:
            results[name] = {"split": cutoff,
                             "lowerMeanDelta": mean(deltas[index] for index in low),
                             "upperMeanDelta": mean(deltas[index] for index in high)}
    return results

from statistics import median

def score_scale(scores):
    ordered = sorted(scores)
    midpoint = median(ordered)
    return {"scoreRange": ordered[-1] - ordered[0], "median": midpoint,
            "medianAbsoluteDeviation": median(abs(score - midpoint) for score in ordered)}

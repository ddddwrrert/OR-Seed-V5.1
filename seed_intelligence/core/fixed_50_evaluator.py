from .evaluation_guard import panel
from .seed_manifest import SEEDS

def mean_score(scores):
    return sum(scores) / len(SEEDS)

def panel_score(metrics):
    result = panel(metrics)
    if result is not None:
        direction, scores = result
        return direction * mean_score(scores)

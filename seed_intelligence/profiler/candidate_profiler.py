from ..core.evaluation_guard import panel
from ..core.fixed_50_evaluator import mean_score
from .score_scale_analyzer import score_scale

def candidate_profile(metrics):
    result = panel(metrics)
    if result is None:
        return None
    direction, scores = result
    return {"direction": direction, "mean": mean_score(scores), **score_scale(scores)}

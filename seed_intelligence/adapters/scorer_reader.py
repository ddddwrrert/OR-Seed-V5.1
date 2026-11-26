from ..core.evaluation_guard import panel

def scorer_capability(metrics):
    observed = panel(metrics)
    return {"pairedScores": observed is not None,
            "scoreDirection": observed[0] if observed else None}

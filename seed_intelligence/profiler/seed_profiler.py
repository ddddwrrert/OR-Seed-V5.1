from .candidate_profiler import candidate_profile
from .open_feature_discovery import observe_feature
from .response_analyzer import response

def compare(previous, current):
    observed = response(previous, current)
    if observed is not None:
        return {**observed, **candidate_profile(current["metrics"])}

from ..reliability.hypothesis_competition import active_hypotheses
from .strategy_value_estimator import priority

def choose(candidates, rows):
    return min(active_hypotheses(candidates, rows), key=priority, default=None)

from ..budget.cost_tracker import charge_candidate
from ..contracts import numeric

def experiment(parent, fitness):
    delta = fitness - parent if numeric(parent) and numeric(fitness) else None
    state = "invalid" if delta is None else "improved" if delta > 0 else "no-improvement"
    return charge_candidate({"delta": delta, "outcome": state})

from .necessity_gate import requires_evidence
from .strategy_composer import compose, explicit_workflows
from .strategy_scheduler import choose

def route(candidates, rows, references):
    applicable = [candidate for candidate in candidates if requires_evidence(candidate, references)]
    resolved = list(explicit_workflows(applicable, rows))
    return compose(choose(resolved, rows), resolved, rows)

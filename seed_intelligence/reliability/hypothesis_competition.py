from ..integration.survival_hook import survives_policy
from .guidance_controller import summarize

def active_hypotheses(candidates, rows):
    for candidate in candidates:
        status = summarize(rows, candidate["id"])
        if survives_policy(status):
            yield {**candidate, **status}

from ..contracts import numeric
from ..discovery.discovery_feedback import review_worker_report
from ..feedback.evolution_feedback import outcome

def assessed_trial(guidance, report, parent, fitness, config):
    record = outcome(parent.get("fitness"), fitness)
    threshold = (config or {}).get("minExpectedGain", 0)
    threshold = max(0, threshold) if numeric(threshold) else 0
    accepted = review_worker_report(guidance, report, parent, fitness, threshold)
    return {"observation": record, "discovery": accepted}

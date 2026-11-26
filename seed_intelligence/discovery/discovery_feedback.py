from ..evolution.candidate_analyzer import completed_trial
from .hypothesis_validator import review

def review_worker_report(guidance, report, parent, fitness, threshold):
    if guidance.get("inspect") and completed_trial(fitness):
        accepted = review(report, guidance["references"], threshold)
        if accepted:
            return {**accepted, "parent": parent["id"]}

from .execution_analyzer import execution_evidence
from .operator_gain_analyzer import operator_evidence
from .scoring_behavior_analyzer import scoring_evidence
from .search_trace_analyzer import trace_evidence

def analyze(previous, current, direction):
    before, after = previous["metrics"], current["metrics"]
    return {**execution_evidence(before, after), **trace_evidence(after, direction),
            **operator_evidence(after), **scoring_evidence(previous, current, before, after)}

from ..strategy_matcher import differing_cohorts

DIRECTION = 'Select a mechanism using a measured instance feature and compare to the current shared algorithm.'
EVIDENCE = 'algorithmInteraction'

def match(reference):
    return differing_cohorts(reference, EVIDENCE)

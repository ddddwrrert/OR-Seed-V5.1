from ..strategy_matcher import differing_cohorts

DIRECTION = 'Choose a local search operator using a verified structural attribute.'
EVIDENCE = 'structuralFeatures'

def match(reference):
    return differing_cohorts(reference, EVIDENCE)

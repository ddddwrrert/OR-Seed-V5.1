from ..strategy_matcher import differing_numeric_groups

DIRECTION = 'Use a threshold on the observed input distribution and verify transfer across the whole panel.'
EVIDENCE = 'numericFeatures'

def match(reference):
    return differing_numeric_groups(reference, EVIDENCE)

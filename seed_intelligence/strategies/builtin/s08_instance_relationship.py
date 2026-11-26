from ..strategy_matcher import differing_cohorts

DIRECTION = 'Reuse valid state across related instance components, checking independence assumptions.'
EVIDENCE = 'instanceRelations'

def match(reference):
    return differing_cohorts(reference, EVIDENCE)

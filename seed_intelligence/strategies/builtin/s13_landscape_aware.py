from ..strategy_matcher import plateau

DIRECTION = 'On a measured score plateau, reconsider neighborhoods or add a bounded restart.'
EVIDENCE = 'trace'

def match(reference):
    return plateau(reference, EVIDENCE)

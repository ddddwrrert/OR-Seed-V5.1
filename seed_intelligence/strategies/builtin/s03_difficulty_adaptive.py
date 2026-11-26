from ..strategy_matcher import difficulty_regresses

DIRECTION = 'Move effort from quick cases to slower cases, keeping the same total limit.'
EVIDENCE = 'timingDifficulty'

def match(reference):
    return difficulty_regresses(reference, EVIDENCE)

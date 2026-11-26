from ..strategy_matcher import runtime_increased

DIRECTION = 'Reallocate the existing candidate time limit away from measured slow work.'
EVIDENCE = 'pairedRuntime'

def match(reference):
    return runtime_increased(reference, EVIDENCE)

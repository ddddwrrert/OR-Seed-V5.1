from ..strategy_matcher import signal

DIRECTION = 'Repair the specific reproducible failure while preserving the accepted case behavior.'
EVIDENCE = 'reproducedFailure'

def match(reference):
    return signal(reference, EVIDENCE)

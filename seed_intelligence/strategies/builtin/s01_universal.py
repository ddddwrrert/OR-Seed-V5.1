from ..strategy_matcher import signal

DIRECTION = 'Improve a common hot loop or data structure without adding instance branches.'
EVIDENCE = 'commonHotspot'

def match(reference):
    return signal(reference, EVIDENCE)

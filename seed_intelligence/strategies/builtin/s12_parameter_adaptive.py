from ..strategy_matcher import signal

DIRECTION = 'Replace the sensitive constant with a bounded rule from measured parameter responses.'
EVIDENCE = 'parameterSensitivity'

def match(reference):
    return signal(reference, EVIDENCE)

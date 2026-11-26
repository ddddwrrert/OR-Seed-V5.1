from ..strategy_matcher import signal

DIRECTION = 'Use the recorded binding constraint to prune invalid moves or repair them cheaply.'
EVIDENCE = 'bindingConstraints'

def match(reference):
    return signal(reference, EVIDENCE)

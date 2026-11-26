from ..strategy_matcher import variable_runs

DIRECTION = 'Make internal random search reproducible or reduce variance without altering evaluation seeds.'
EVIDENCE = 'repeatVariation'

def match(reference):
    return variable_runs(reference, EVIDENCE)

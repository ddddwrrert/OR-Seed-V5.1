from ..strategy_matcher import rare_regression

DIRECTION = 'Handle the small regressing cohort without changing behavior on the rest of the panel.'
EVIDENCE = 'rareRegression'

def match(reference):
    return rare_regression(reference, EVIDENCE)

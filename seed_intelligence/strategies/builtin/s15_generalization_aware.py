from ..strategy_matcher import proxy_disagrees

DIRECTION = 'Repair a direction that improves a proxy while degrading the full official mean.'
EVIDENCE = 'proxy'

def match(reference):
    return proxy_disagrees(reference, EVIDENCE)

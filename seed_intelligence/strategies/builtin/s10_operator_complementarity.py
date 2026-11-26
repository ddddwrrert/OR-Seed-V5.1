from ..strategy_matcher import complementary_operators

DIRECTION = 'Give complementary search operators distinct roles rather than applying them indiscriminately.'
EVIDENCE = 'operators'

def match(reference):
    return complementary_operators(reference, EVIDENCE)

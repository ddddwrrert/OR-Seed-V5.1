import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, PARENT, hypothesis, trials

class WrongGuidance(unittest.TestCase):
    def test_a_rejected_hypothesis_yields_to_a_distinct_candidate(self):
        rows = trials("wrong", -10, -5)
        cfg = {"hypotheses": [hypothesis("wrong"), hypothesis("different")]}
        self.assertEqual(decide(rows, PARENT, BUDGET, 0, cfg, {})["id"], "different")

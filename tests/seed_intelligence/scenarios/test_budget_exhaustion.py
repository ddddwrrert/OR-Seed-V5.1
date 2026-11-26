import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, CHILD, PARENT, contrasted

class Exhaustion(unittest.TestCase):
    def test_discovery_obeys_same_budget_cap(self):
        self.assertIsNone(decide([CHILD], PARENT, BUDGET, 1, {"maxCandidates": 1}, contrasted()))

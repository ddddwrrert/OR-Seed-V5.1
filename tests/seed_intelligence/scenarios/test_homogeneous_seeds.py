import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, PARENT, CHILD, evaluation

class HomogeneousSeeds(unittest.TestCase):
    def test_flat_response_does_not_spend_a_discovery_slot(self):
        evaluations = {CHILD["id"]: evaluation([9] * 50), PARENT["id"]: evaluation([10] * 50)}
        self.assertIsNone(decide([CHILD], PARENT, BUDGET, 0, {}, evaluations))

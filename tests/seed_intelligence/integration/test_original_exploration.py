import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, PARENT, hypothesis

class OriginalExploration(unittest.TestCase):
    def test_reserved_slots_return_the_original_worker_signal(self):
        config = {"hypotheses": [hypothesis("approved")]}
        original_slot = {**BUDGET, "used": 4, "remaining": 8}
        self.assertIsNone(decide([], PARENT, original_slot, 0, config, {}))

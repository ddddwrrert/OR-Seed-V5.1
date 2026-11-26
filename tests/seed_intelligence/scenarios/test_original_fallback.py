import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, CHILD, PARENT, contrasted

class Fallback(unittest.TestCase):
    def test_inspected_parent_without_viable_report_returns_original(self):
        inspected = {**CHILD, "discoveryAttempt": True}
        self.assertIsNone(decide([inspected], PARENT, BUDGET, 1, {}, contrasted()))

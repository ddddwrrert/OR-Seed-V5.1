import unittest


from seed_intelligence.controller import assess, decide
from fixtures import BUDGET, CHILD, PARENT, contrasted, report

class UnknownBottleneck(unittest.TestCase):
    def test_unknown_direction_can_be_accepted_without_builtin_category(self):
        decision = decide([CHILD], PARENT, BUDGET, 0, {}, contrasted())
        result = assess(decision, report(id="new-operator-fusion"), PARENT, 101, {})
        self.assertEqual(result["discovery"]["id"], "new-operator-fusion")
        self.assertNotIn("builtin", result["discovery"])

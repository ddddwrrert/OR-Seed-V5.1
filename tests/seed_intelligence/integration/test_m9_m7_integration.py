import unittest


from seed_intelligence.controller import assess, decide
from fixtures import BUDGET, CHILD, PARENT, contrasted, report

class DiscoveryToReliability(unittest.TestCase):
    def test_validated_report_can_be_selected_for_trial(self):
        records = contrasted()
        decision = decide([CHILD], PARENT, BUDGET, 0, {}, records)
        result = assess(decision, report(), PARENT, 102, {})
        rows = [CHILD, {"id": "c000002", "parent": PARENT["id"], "discoveryAttempt": True,
                        "fitness": 102, "discovery": result["discovery"]}]
        guided = decide(rows, PARENT, BUDGET, 1, {}, records)
        self.assertEqual(guided["id"], "different-neighborhood")

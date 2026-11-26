import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, CHILD, PARENT, contrasted

class ProfileToDiscovery(unittest.TestCase):
    def test_observed_labels_are_visible_in_worker_evidence(self):
        evidence = contrasted(instance_features={"new topology": ["cluster"] * 25 + ["chain"] * 25})
        decision = decide([CHILD], PARENT, BUDGET, 0, {"automaticBuiltins": False}, evidence)
        self.assertIn("new topology", " ".join(decision["instructions"]))

import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, PARENT, hypothesis

class Mutation(unittest.TestCase):
    def test_worker_instructions_include_choice_and_counterevidence(self):
        decision = decide([], PARENT, BUDGET, 0, {"hypotheses": [hypothesis("candidate")]}, {})
        lines = " ".join(decision["instructions"])
        self.assertIn("may ignore", lines)
        self.assertIn("Counterevidence:", lines)

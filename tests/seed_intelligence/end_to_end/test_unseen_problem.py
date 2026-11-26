import unittest


from seed_intelligence.controller import decide
from fixtures import BUDGET, CHILD, PARENT, contrasted

class UnseenTask(unittest.TestCase):
    def test_unknown_task_uses_registered_capabilities_not_a_problem_id(self):
        evaluation = contrasted(recorded_reactive_events=["normal event"])
        decision = decide([CHILD], {**PARENT, "task": "previously unseen"}, BUDGET, 0, {}, evaluation)
        self.assertEqual(decision["capabilities"]["adapter"], "reactive")
        self.assertEqual(decision["capabilities"]["reactiveEventCount"], 1)

import unittest


from seed_intelligence.composer.workflow_executor import stages
from fixtures import hypothesis, trials

class Workflow(unittest.TestCase):
    def test_three_validated_steps_follow_declared_order(self):
        keys = ["first", "second", "third"]
        items = [{**hypothesis(key), "compatibleWith": [other for other in keys if key != other]} for key in keys]
        rows = [row for key in keys for row in trials(key, 2, 3)]
        self.assertEqual([item["id"] for item in stages(list(reversed(keys)), items, rows)], list(reversed(keys)))
        self.assertEqual(stages(["first", "second", "first"], items, rows), [])
        self.assertEqual(stages(keys, items, rows[:-1]), [])

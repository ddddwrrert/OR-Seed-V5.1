import unittest


from seed_intelligence.controller import assess
from seed_intelligence.reliability.guidance_controller import summarize
from fixtures import PARENT

class Feedback(unittest.TestCase):
    def test_only_valid_fitness_updates_probability(self):
        reports = [assess({}, None, PARENT, value, {})["observation"] for value in (105, None)]
        status = summarize([{"guidance": {"id": "x", **report}} for report in reports], "x")
        self.assertEqual(status["trials"], 2)
        self.assertEqual(status["reliability"], 2 / 3)

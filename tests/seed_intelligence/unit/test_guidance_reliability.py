import unittest


from seed_intelligence.reliability.guidance_controller import summarize
from fixtures import trials

class Reliability(unittest.TestCase):
    def test_win_probability_does_not_replace_measured_magnitude(self):
        status = summarize(trials("x", -100, 1, 2), "x")
        self.assertGreater(status["reliability"], 0.5)
        self.assertLess(status["meanGain"], 0)
        self.assertNotEqual(status["state"], "validated")

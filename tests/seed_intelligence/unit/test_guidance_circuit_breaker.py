import unittest


from seed_intelligence.reliability.guidance_controller import summarize
from fixtures import trials

class CircuitBreaker(unittest.TestCase):
    def test_two_failures_archive_even_after_historical_success(self):
        self.assertEqual(summarize(trials("x", 1, 2, 3, -1, 0), "x")["state"], "archived")

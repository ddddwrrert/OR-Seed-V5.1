import unittest


from seed_intelligence.profiler.seed_profiler import compare
from fixtures import evaluation

class Profile(unittest.TestCase):
    def test_minimize_direction_is_applied_per_seed(self):
        prior = evaluation([10] * 50, -1)
        current = evaluation([9] * 25 + [13] * 25, -1)
        profile = compare(prior, current)
        self.assertEqual(profile["improvements"], 25)
        self.assertEqual(profile["recoverableMean"], 1.5)

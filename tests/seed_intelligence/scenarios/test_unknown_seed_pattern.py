import unittest


from seed_intelligence.profiler.open_feature_discovery import observe_feature

class UnknownPattern(unittest.TestCase):
    def test_noncontiguous_seed_cohort_is_evaluated_as_reported(self):
        feature = {"name": "periodic leading digit", "observation": "repeated pattern", "seeds": [0, 11, 42]}
        deltas = [-2 if seed in feature["seeds"] else 1 for seed in range(50)]
        self.assertEqual(observe_feature(feature, {"deltas": deltas})["observedDelta"], -2)

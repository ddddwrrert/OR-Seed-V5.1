import unittest


from seed_intelligence.profiler.feature_registry import register_feature

class Cohort(unittest.TestCase):
    def test_open_feature_validates_name_and_real_distinct_seed_members(self):
        feature = {"name": "a mechanism invented during search", "observation": "observed twice", "seeds": [4]}
        self.assertEqual(register_feature({"feature": feature}, {"deltas": [3, 2, 1, 0, -2]})["feature"]["observedDelta"], -2)
        self.assertIsNone(register_feature({"feature": {**feature, "seeds": [4, 4]}}, {"deltas": [3, 2, 1, 0, -2]}))

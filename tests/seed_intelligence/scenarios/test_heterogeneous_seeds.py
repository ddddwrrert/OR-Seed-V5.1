import unittest


from seed_intelligence.profiler.problem_profiler import observed_features
from fixtures import evaluation

class Heterogeneity(unittest.TestCase):
    def test_metadata_requires_open_cohorts_with_sufficient_members(self):
        metrics = evaluation([100] * 50)["metrics"]
        metrics["instance_features"] = {"unknown_size": list(range(50)), "single_cohort": ["a"] * 50}
        observed = observed_features(metrics, [-1] * 25 + [1] * 25)
        self.assertIn("unknown_size", observed["numericFeatures"])
        self.assertNotIn("structuralFeatures", observed)

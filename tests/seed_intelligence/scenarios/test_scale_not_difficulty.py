import unittest


from seed_intelligence.profiler.difficulty_analyzer import timing_difficulty
from fixtures import evaluation

class Scale(unittest.TestCase):
    def test_wide_scores_with_equal_runtime_show_no_timing_difficulty(self):
        metrics = evaluation([100 * seed for seed in range(50)])["metrics"]
        for seed in metrics["seed_scores"]:
            seed["seconds"] = 1
        self.assertIsNone(timing_difficulty(metrics, [0] * 50))

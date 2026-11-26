import unittest


from seed_intelligence.core.evaluation_contract import panel_score
from seed_intelligence.core.score_registry import scored_record
from fixtures import evaluation

class FixedPanel(unittest.TestCase):
    def test_proxy_cannot_replace_formal_score(self):
        metrics = {**evaluation(range(50))["metrics"], "combined_score": 9000}
        record = scored_record(metrics)
        self.assertEqual(record["fitness"], 24.5)
        self.assertEqual(record["manifest"]["aggregation"], "arithmetic_mean")
        metrics["seed_scores"] += metrics["seed_scores"][:1]
        self.assertIsNone(panel_score(metrics))

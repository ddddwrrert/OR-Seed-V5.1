import unittest

from seed_intelligence.controller import assess, decide
from seed_intelligence.core.evaluation_contract import SEEDS, manifest, panel_score
from seed_intelligence.profiler.seed_profiler import compare
from seed_intelligence.strategies.strategy_registry import registry


def evaluation(scores, direction=1):
    return {
        "fitness": direction * sum(scores) / 50,
        "metrics": {
            "score_direction": direction,
            "seed_scores": [
                {"seed": seed, "score": score, "accepted": True}
                for seed, score in zip(SEEDS, scores)
            ],
        },
    }


PARENT = {"id": "c000000", "fitness": 100}
CHILD = {"id": "c000001", "parent": PARENT["id"], "fitness": 100}
BUDGET = {"used": 3, "remaining": 9, "max": 12}


def hypothesis(key):
    return {"id": key, "direction": f"Try {key}", "evidence": "Measured differences",
            "counterevidence": "Search variance is a competing explanation"}


class ContractTests(unittest.TestCase):
    def test_fixed_panel_and_direction(self):
        record = evaluation(range(50), -1)
        self.assertEqual(panel_score(record["metrics"]), -24.5)
        self.assertEqual(manifest()["seeds"], tuple(range(50)))
        for replacement in (51, 1, True):
            rows = [dict(row) for row in record["metrics"]["seed_scores"]]
            rows[0]["seed"] = replacement
            self.assertIsNone(panel_score({**record["metrics"], "seed_scores": rows}))

    def test_scale_is_not_difficulty_or_an_opportunity(self):
        scores = [1000 * seed for seed in SEEDS]
        parent_eval = evaluation(scores)
        child_eval = evaluation([score + 10 for score in scores])
        comparison = compare(parent_eval, child_eval)
        self.assertGreater(comparison["scoreRange"], 10000)
        self.assertEqual(comparison["recoverableMean"], 0)
        self.assertIsNone(decide([CHILD], PARENT, BUDGET, 0, {},
                                 {PARENT["id"]: parent_eval, CHILD["id"]: child_eval}))


class StrategyIntegrationTests(unittest.TestCase):
    def test_unknown_strategy_and_builtin_registration(self):
        builtin = {"builtin": "s05", "evidence": "Failure reproduced",
                   "counterevidence": "Candidate compile was flaky"}
        self.assertEqual({strategy["id"] for strategy in registry([builtin], [hypothesis("novel")])},
                         {"novel", "s05"})

    def test_only_validated_compatible_directions_can_compose(self):
        a = {**hypothesis("a"), "compatibleWith": ["b"]}
        b = {**hypothesis("b"), "compatibleWith": ["a"]}
        config = {"hypotheses": [a, b]}
        rows = [{"guidance": {"id": key, "outcome": "improved", "delta": 3}}
                for key in ("a", "a", "b", "b")]
        joint = decide(rows, PARENT, BUDGET, 0, config, {})
        self.assertEqual(joint["id"], "joint:a+b")
        self.assertEqual(joint["trials"], 0)
        for _ in range(2):
            result = assess(joint, None, PARENT, 98, {})
            rows.append({"guidance": {"id": joint["id"], **result["observation"]}})
        self.assertEqual(decide(rows, PARENT, BUDGET, 0, config, {})["id"], "a")
        self.assertIsNone(decide(rows, PARENT, BUDGET, 4, config, {}))
        self.assertIsNone(decide(rows, PARENT, {**BUDGET, "used": 4}, 0, config, {}))

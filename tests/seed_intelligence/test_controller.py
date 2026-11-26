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

class RecordedEvidenceTests(unittest.TestCase):
    def test_optional_telemetry_and_old_discovery_reach_m7(self):
        former, current = evaluation([110] * 25 + [90] * 25), evaluation([100] * 50)
        former["metrics"].update(max_execution_time_sec=2, proxy_score=10, proxy_score_direction=1)
        current["metrics"].update(
            max_execution_time_sec=3, proxy_score=5, proxy_score_direction=1,
            search_trace_score="official", search_trace=[{"score": 5}, {"score": 7}, {"score": 7}],
            operator_gains={"custom move": [1, 3]},
        )
        for record, seconds in ((former, 1), (current, 2)):
            for case in record["metrics"]["seed_scores"]:
                case["seconds"] = seconds
        panels = {PARENT["id"]: current, CHILD["id"]: former}
        initial = decide([CHILD], PARENT, BUDGET, 0, {}, panels)
        telemetry = initial["references"][0]["telemetry"]
        self.assertEqual(telemetry["trace"]["tailPlateauSamples"], 2)
        self.assertEqual(telemetry["operators"]["custom move"]["meanReportedGain"], 2)
        self.assertEqual(telemetry["pairedRuntime"]["slowerSeeds"], 50)
        report = {**hypothesis("unseen"), "reference": CHILD["id"], "expectedGain": 2,
                  "cost": "one candidate", "telemetryKeys": ["trace", "pairedRuntime"]}
        checked = assess(initial, report, PARENT, 101, {})["discovery"]
        self.assertEqual(checked["recordedEvidence"]["trace"]["observedGain"], 2)
        fabricated = {**report, "telemetryKeys": ["missing"]}
        self.assertIsNone(assess(initial, fabricated, PARENT, 101, {})["discovery"])
        later = [CHILD, {"id": "c000002", "parent": PARENT["id"], "fitness": 101,
                         "discoveryAttempt": True, "discovery": checked}]
        later.extend({"id": f"c{index:06}", "parent": "other", "fitness": 100}
                     for index in range(3, 20))
        selected = decide(later, PARENT, BUDGET, 1, {}, panels)
        self.assertEqual(selected["id"], "unseen")
        self.assertFalse(selected["inspect"])

    def test_renaming_same_direction_does_not_restart_archived_trials(self):
        prior = hypothesis("old")
        updated = {**hypothesis("new"), "direction": "  TRY   OLD "}
        rows = [{"guidance": {**prior, "outcome": "no-improvement", "delta": -1}}] * 2
        self.assertIsNone(decide(rows, PARENT, BUDGET, 0, {"hypotheses": [updated]}, {}))

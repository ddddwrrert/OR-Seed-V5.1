import unittest


from seed_intelligence.strategies.dynamic.strategy_loader import load_discovered
from seed_intelligence.strategies.strategy_registry import registry
from fixtures import report

class DynamicStrategies(unittest.TestCase):
    def test_loading_is_isolated_to_the_current_parent(self):
        rows = [{"fitness": 1, "discovery": report(parent="a")},
                {"fitness": None, "discovery": report(parent="b")}]
        self.assertEqual(len(registry([], list(load_discovered(rows, "a")))), 1)
        self.assertEqual(list(load_discovered(rows, "b")), [])

class EvidenceBackedBuiltins(unittest.TestCase):
    def test_registry_uses_all_fifteen_evidence_contracts(self):
        from seed_intelligence.strategies.strategy_generator import from_evidence
        telemetry = {
            "commonHotspot": {"section": "queue"}, "reproducedFailure": {"retry": 2},
            "parameterSensitivity": {"distinctValues": 2}, "bindingConstraints": {"space": 10},
            "pairedRuntime": {"meanDeltaSeconds": 1}, "trace": {"tailPlateauSamples": 4},
            "operators": {"fast": {}, "slow": {}}, "proxy": {"directionDisagrees": True},
            "repeatVariation": {"spread": 2}, "timingDifficulty": {"slowMeanDelta": 0, "fastMeanDelta": 1},
            "numericFeatures": {"size": {"lowerMeanDelta": 1, "upperMeanDelta": 2}},
        }
        for key in ("structuralFeatures", "algorithmInteraction", "instanceRelations"):
            telemetry[key] = {"shape": {"first": {"meanDelta": -1}, "second": {"meanDelta": 1}}}
        reference = {"reference": "past", "telemetry": telemetry,
                     "profile": {"regressions": [(3, -4)], "recoverableMean": 1}}
        offers = list(from_evidence([reference], "current"))
        self.assertEqual({item["builtin"] for item in offers}, {f"s{i:02}" for i in range(1, 16)})
        self.assertEqual(list(from_evidence([], "current")), [])

    def test_recorded_sections_trigger_a_real_controller_proposal(self):
        from seed_intelligence.controller import decide
        from fixtures import BUDGET, CHILD, PARENT, contrasted
        panels = contrasted(recorded_section_seconds={"heap rebuild": 10, "other": 2})
        decision = decide([CHILD], PARENT, BUDGET, 0, {}, panels)
        self.assertEqual(decision["builtin"], "s01")
        self.assertIn("heap rebuild", decision["evidence"])

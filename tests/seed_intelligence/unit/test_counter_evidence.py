import unittest


from seed_intelligence.reliability.evidence_registry import cited_evidence

class Evidence(unittest.TestCase):
    def test_forged_or_malformed_citations_are_rejected(self):
        ref = {"telemetry": {"trace": {"samples": 3}}}
        self.assertEqual(cited_evidence({"telemetryKeys": ["trace"]}, ref), ref["telemetry"])
        self.assertIsNone(cited_evidence({"telemetryKeys": ["unknown"]}, ref))
        self.assertIsNone(cited_evidence({"telemetryKeys": [{}]}, ref))

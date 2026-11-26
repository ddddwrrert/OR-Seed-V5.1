import unittest


from pathlib import Path
from subprocess import run
import json
import sys

class ControllerBridge(unittest.TestCase):
    def test_controller_stdin_stdout_matches_organon_bridge_contract(self):
        root = Path(__file__).resolve().parents[3]
        request = {"action": "plan", "rows": [], "parent": {"id": "c000000", "fitness": 5},
                   "budget": {"max": 4, "used": 1, "remaining": 3}, "spent": 0,
                   "config": {"hypotheses": [{"id": "x", "direction": "try x", "evidence": "score",
                                            "counterevidence": "noise"}]}, "evaluations": {}}
        result = run([sys.executable, "-B", str(root / "seed_intelligence/controller.py")],
                     input=json.dumps(request), text=True, capture_output=True, check=True)
        self.assertEqual(json.loads(result.stdout)["id"], "x")

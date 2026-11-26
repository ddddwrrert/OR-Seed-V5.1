import unittest


from pathlib import Path
from subprocess import run
import json
import os
import sys

class RealAHC001(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OR_SEED_AHC001_TASK"), "requires a real compatible AHC001 task and configured ALE-Bench")
    def test_real_ahc001_fixed_panel(self):
        root = Path(__file__).resolve().parents[3]
        task = Path(os.environ["OR_SEED_AHC001_TASK"]).resolve()
        settings = json.loads((task / "task.json").read_text(encoding="utf-8"))
        runner = root / "plugins/dsh-evolve-loop/src/providers/run_evaluator.py"
        process = run([sys.executable, "-B", str(runner), str(task), str(task / settings["program"])],
                      text=True, capture_output=True, check=True)
        result = json.loads(process.stdout)
        self.assertIsNotNone(result["fitness"])
        self.assertEqual([row["seed"] for row in result["metrics"]["seed_scores"]], list(range(50)))

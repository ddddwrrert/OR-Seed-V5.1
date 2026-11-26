import unittest


from pathlib import Path
from subprocess import run
import os
import shutil

class FullEvolution(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OR_SEED_RUN_NODE_E2E"), "enable with OR_SEED_RUN_NODE_E2E=1 or run verify.py")
    def test_actual_worker_bridge_and_fixed_panel_export(self):
        self.assertIsNotNone(shutil.which("node"))
        root = Path(__file__).resolve().parents[3]
        run(["node", "--test", "tests/or-seed.test.mjs"], cwd=root, check=True)

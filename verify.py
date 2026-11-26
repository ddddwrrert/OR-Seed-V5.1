"""Run local acceptance from a fresh checkout without ALE-Bench credentials."""
from pathlib import Path
from subprocess import run
import os
import sys

KIT = Path(__file__).resolve().parent
env = {**os.environ, "OR_SEED_PYTHON": sys.executable}
commands = [
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests/seed_intelligence", "-v"],
    [sys.executable, "-B", "tests/test_ahc_panel.py"],
    ["node", "--test", "tests/or-seed.test.mjs"],
]
for command in commands:
    run(command, cwd=KIT, env=env, check=True)

"""Build the plugin archive with the canonical Python controller included."""
from pathlib import Path
from shutil import copy2, copytree, ignore_patterns, which
from subprocess import run
from tempfile import TemporaryDirectory

KIT = Path(__file__).resolve().parents[2]

def main():
    npm = which("npm.cmd") or which("npm")
    if not npm:
        raise SystemExit("npm is required to package the evolve plugin.")
    with TemporaryDirectory(prefix="or-seed-package-") as temporary:
        staging = Path(temporary) / "dsh-evolve-loop"
        copytree(KIT / "plugins/dsh-evolve-loop", staging,
                 ignore=ignore_patterns("node_modules", "__pycache__", "*.pyc", "seed_intelligence"))
        package = staging / "src/seed_intelligence"
        copytree(KIT / "seed_intelligence", package,
                 ignore=ignore_patterns("__pycache__", "*.pyc"))
        copy2(KIT / "configs/seed_intelligence.yaml", package / "defaults.yaml")
        run([npm, "pack", "--pack-destination", str(KIT / "dist")], cwd=staging, check=True)

if __name__ == "__main__":
    main()

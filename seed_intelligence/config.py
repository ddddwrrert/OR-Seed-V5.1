from pathlib import Path
import json
from .contracts import numeric

def resolve(config, budget):
    package = Path(__file__).resolve().parent
    defaults = package / "defaults.yaml"
    if not defaults.is_file():
        defaults = package.parent / "configs/seed_intelligence.yaml"
    config = {**json.loads(defaults.read_text(encoding="utf-8")), **(config or {})}
    maximum = budget["max"]
    cap = config.get("maxCandidates", maximum // 3)
    threshold = config.get("minExpectedGain", 0)
    return {
        "cap": min(cap, maximum // 2) if type(cap) is int else 0,
        "threshold": max(0, threshold) if numeric(threshold) else 0,
        "discovery": config.get("discovery", True) is not False,
        "hypotheses": config.get("hypotheses", []),
    }

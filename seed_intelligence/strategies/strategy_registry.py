from ..contracts import hypothesis
from ..reliability.duplicate_hypothesis_detector import direction_key
from .builtin import CATALOG
from .strategy_validator import viable_strategies

BUILTINS = {key: strategy.DIRECTION for key, strategy in CATALOG.items()}

def registry(configured, discovered, rows=()):
    candidates = {}
    seen = set()
    history = {}
    for row in rows:
        prior = row.get("guidance")
        if hypothesis(prior):
            history.setdefault(direction_key(prior), prior["id"])
    for item in [*discovered, *(configured if isinstance(configured, list) else [])]:
        if not isinstance(item, dict):
            continue
        builtin = item.get("builtin")
        if builtin is not None:
            if not isinstance(builtin, str) or builtin not in BUILTINS:
                continue
            item = {"id": builtin, "direction": BUILTINS[builtin], **item}
        if not next(viable_strategies([item]), None):
            continue
        key = direction_key(item)
        if key in seen:
            continue
        seen.add(key)
        identifier = history.get(key, item["id"])
        candidates.setdefault(identifier, {**item, "id": identifier})
    return list(candidates.values())

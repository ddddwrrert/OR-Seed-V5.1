from ..contracts import hypothesis

# Initial catalog. Each entry requires explicit evidence for the current problem.
BUILTINS = {
    "s01": "Improve the shared search implementation",
    "s02": "Exploit instance structure",
    "s03": "Adapt effort to supported difficulty signals",
    "s04": "Match a mechanism to instance properties",
    "s05": "Repair a reproducible failure",
    "s06": "Control search randomness",
    "s07": "Adapt to an observed distribution",
    "s08": "Exploit verified instance relationships",
    "s09": "Handle a demonstrated rare case",
    "s10": "Combine complementary search operators",
    "s11": "Reallocate search effort",
    "s12": "Adapt sensitive parameters",
    "s13": "Use measured search landscape behavior",
    "s14": "Exploit problem constraints",
    "s15": "Improve robustness across the panel",
}

def registry(configured, discovered):
    candidates = {}
    for item in [*discovered, *(configured if isinstance(configured, list) else [])]:
        if not isinstance(item, dict):
            continue
        builtin = item.get("builtin")
        if builtin is not None:
            if not isinstance(builtin, str) or builtin not in BUILTINS:
                continue
            item = {"id": builtin, "direction": BUILTINS[builtin], **item}
        if not hypothesis(item):
            continue
        candidates[item["id"]] = item
    return list(candidates.values())

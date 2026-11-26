from statistics import mean
from ..contracts import numeric

def _maximum_runtime(metrics):
    value = metrics.get("max_execution_time_sec")
    return value if numeric(value) and value >= 0 else None


def execution_evidence(before, after):
    observations = {}

    previous_runtime, runtime = _maximum_runtime(before), _maximum_runtime(after)
    if previous_runtime is not None and runtime is not None and runtime != previous_runtime:
        observations["maxRuntimeDeltaSeconds"] = runtime - previous_runtime

    old_cases, new_cases = before.get("seed_scores", []), after.get("seed_scores", [])
    differences = []
    for old, new in zip(old_cases, new_cases):
        old_time, new_time = old.get("seconds"), new.get("seconds")
        if numeric(old_time) and numeric(new_time) and old_time >= 0 and new_time >= 0:
            differences.append(new_time - old_time)
    if len(differences) == 50 and any(differences):
        observations["pairedRuntime"] = {
            "meanDeltaSeconds": mean(differences),
            "slowerSeeds": sum(delta > 0 for delta in differences),
        }

    return observations

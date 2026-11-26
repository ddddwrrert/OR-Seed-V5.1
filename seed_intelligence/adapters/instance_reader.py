from ..profiler.seed_semantics import recorded_columns

def instance_properties(metrics):
    return sorted(recorded_columns(metrics, "instance_features"))

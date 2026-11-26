from ..profiler.seed_semantics import recorded_columns

def generator_properties(metrics):
    return sorted(recorded_columns(metrics, "generator_parameters"))

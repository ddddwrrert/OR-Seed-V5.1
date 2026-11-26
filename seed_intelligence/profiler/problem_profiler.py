from .difficulty_analyzer import timing_difficulty
from .distribution_analyzer import numeric_contrasts
from .randomness_analyzer import repeat_variation
from .seed_semantics import recorded_columns
from .structure_analyzer import structural_cohorts

def observed_features(metrics, deltas):
    columns = recorded_columns(metrics, "instance_features")
    return {key: value for key, value in {
        "numericFeatures": numeric_contrasts(columns, deltas),
        "structuralFeatures": structural_cohorts(columns, deltas),
        "timingDifficulty": timing_difficulty(metrics, deltas),
        "repeatVariation": repeat_variation(metrics),
    }.items() if value}

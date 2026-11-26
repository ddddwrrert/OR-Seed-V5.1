from .problem_profiler import observed_features

def add_recorded_features(profile, metrics):
    features = observed_features(metrics, profile["deltas"])
    return {**profile, "observedFeatures": features} if features else profile

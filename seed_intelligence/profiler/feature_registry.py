from .open_feature_discovery import observe_feature

def register_feature(report, profile):
    if report.get("feature") is None:
        return dict(report)
    feature = observe_feature(report["feature"], profile)
    if feature is not None:
        return {**report, "feature": feature}

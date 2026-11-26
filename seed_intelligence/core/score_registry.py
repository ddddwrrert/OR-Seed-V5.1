from .fixed_50_evaluator import panel_score
from .seed_manifest import manifest
from ..profiler.candidate_profiler import candidate_profile

def scored_record(metrics):
    return {"metrics": metrics, "fitness": panel_score(metrics), "manifest": manifest(),
            "profile": candidate_profile(metrics)}

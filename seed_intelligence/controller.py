"""Unified entry point for the Organon seed policy, via JSON on stdin/stdout."""
if not __package__:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    __package__ = "seed_intelligence"

from .adapters.problem_loader import task_record
from .budget.budget_controller import eligible
from .discovery.bottleneck_discovery import opportunities
from .integration.feedback_hook import assessed_trial as assess
from .integration.generation_hook import generation_plan
from .integration.initialization_hook import policy_for
from .integration.organon_adapter import serve

def decide(rows, parent, budget, spent, config, evaluations):
    policy = policy_for(rows, parent, budget, spent, config, evaluations)
    if not policy or not eligible(parent, budget, spent, policy["cap"]):
        return
    references = opportunities(rows, parent, evaluations, policy["threshold"]) if policy["discovery"] else []
    return generation_plan(policy, rows, parent, references, task_record(evaluations, parent))

if __name__ == "__main__":
    serve(decide, assess)

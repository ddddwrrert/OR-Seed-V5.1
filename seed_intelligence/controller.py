"""Unified entry point for the Organon seed policy, via JSON on stdin/stdout."""
if not __package__:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    __package__ = "seed_intelligence"

from .adapters.generic_adapter import evidence_capabilities
from .budget.budget_guard import eligible
from .composer.adaptive_composer import choose, companions
from .config import resolve
from .contracts import numeric
from .discovery.bottleneck_discovery import opportunities, review
from .evolution.mutation_plan import plan
from .feedback.evolution_feedback import outcome
from .integration.organon_adapter import serve
from .storage.history import discovered
from .strategies.strategy_registry import registry

def decide(rows, parent, budget, spent, config, evaluations):
    policy = resolve(config, budget)
    if not eligible(parent, budget, spent, policy["cap"]):
        return
    threshold = policy["threshold"]
    references = opportunities(rows, parent, evaluations, threshold) if policy["discovery"] else []
    proposals = [review(report, references, threshold) for report in discovered(rows, parent["id"])]
    candidates = registry(policy["hypotheses"], proposals)
    selected = choose(candidates, rows)
    companion = companions(selected, candidates, rows)
    composition = None
    if companion:
        other = next(item for item in candidates if item["id"] == companion[0])
        combined = {**selected, "id": "joint:" + "+".join(sorted([selected["id"], other["id"]]))}
        combined.update(direction=selected["direction"] + "\n" + other["direction"],
                        evidence=selected["evidence"] + "\n" + other["evidence"],
                        counterevidence=selected["counterevidence"] + "\n" + other["counterevidence"])
        jointly_selected = choose([combined], rows)
        if jointly_selected:
            composition = companion
            selected = jointly_selected
    inspect = bool(references) and not any(
        row.get("parent") == parent["id"] and row.get("discoveryAttempt") for row in rows
    )
    return plan(selected, inspect, references, evidence_capabilities(evaluations.get(parent["id"])), composition)

def assess(guidance, report, parent, fitness, config):
    record = outcome(parent.get("fitness"), fitness)
    accepted = None
    if guidance.get("inspect") and numeric(fitness):
        threshold = (config or {}).get("minExpectedGain", 0)
        threshold = max(0, threshold) if numeric(threshold) else 0
        accepted = review(report, guidance["references"], threshold)
        if accepted:
            accepted["parent"] = parent["id"]
    return {"observation": record, "discovery": accepted}

if __name__ == "__main__":
    serve(decide, assess)

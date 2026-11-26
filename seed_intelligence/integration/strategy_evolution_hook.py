from .selection_hook import select_guidance
from ..discovery.discovery_history import previously_discovered
from ..discovery.hypothesis_validator import review
from ..strategies.strategy_generator import from_evidence
from ..strategies.strategy_registry import registry

def next_direction(policy, rows, parent, references):
    discoveries = [review(report, references, policy["threshold"])
                   for report in previously_discovered(rows, parent["id"])]
    if policy["automaticBuiltins"]:
        discoveries.extend(from_evidence(references, parent["id"]))
    registered = registry(policy["hypotheses"], discoveries, rows)
    return select_guidance(registered, rows, references)

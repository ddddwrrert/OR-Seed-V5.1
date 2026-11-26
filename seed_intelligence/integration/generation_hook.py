from ..adapters.generic_adapter import evidence_capabilities
from ..discovery.discovery_trigger import should_inspect
from ..evolution.mutation_plan import plan
from .strategy_evolution_hook import next_direction

def generation_plan(policy, rows, parent, references, evaluation):
    selected, composition = next_direction(policy, rows, parent, references)
    inspect = should_inspect(references, rows, parent["id"])
    return plan(selected, inspect, references, evidence_capabilities(evaluation), composition)

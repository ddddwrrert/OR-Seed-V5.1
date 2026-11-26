from ..budget.fallback_controller import has_seed_work
from ..discovery.open_hypothesis_generator import research_lines
from .seed_conditioned_mutation import mutation_instructions

def dispatch(selected, inspect, references):
    if not has_seed_work(selected, inspect):
        return
    return mutation_instructions(selected) + (research_lines(references) if inspect else [])

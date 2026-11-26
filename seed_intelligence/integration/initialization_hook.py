from ..config import resolve
from .integration_guard import valid_context

def policy_for(rows, parent, budget, spent, config, evaluations):
    if valid_context(rows, parent, budget, spent, evaluations):
        return resolve(config, budget)

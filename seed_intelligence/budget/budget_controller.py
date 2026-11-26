from ..contracts import numeric
from ..reliability.original_exploration_guard import original_slot
from .search_budget_guard import within_budget

def eligible(parent, budget, spent, cap):
    return (numeric(parent.get("fitness")) and not original_slot(budget)
            and within_budget(spent, cap))

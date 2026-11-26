from .discovery_budget_guard import uninspected

def discovery_allowed(rows, parent_id, references):
    return bool(references) and uninspected(rows, parent_id)

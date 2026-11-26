from ..storage.budget_store import valid_budget

def valid_context(rows, parent, budget, spent, evaluations):
    return (isinstance(rows, list) and all(isinstance(row, dict) for row in rows)
            and isinstance(parent, dict) and isinstance(parent.get("id"), str)
            and valid_budget(budget) and type(spent) is int and spent >= 0
            and isinstance(evaluations, dict))

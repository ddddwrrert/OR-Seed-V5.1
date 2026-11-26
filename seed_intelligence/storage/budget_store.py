def valid_budget(budget):
    if not isinstance(budget, dict):
        return False
    maximum, used, remaining = (budget.get(key) for key in ("max", "used", "remaining"))
    return (all(type(value) is int for value in (maximum, used, remaining))
            and maximum > 0 and 0 <= used <= maximum and remaining == maximum - used)

from ..budget.marginal_value_estimator import measured_value

def priority(item):
    return (item["trials"] > 0, -item["reliability"], -measured_value(item))

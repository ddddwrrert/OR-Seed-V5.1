from ..budget.early_stopping import discovery_allowed

def should_inspect(references, rows, parent_id):
    return discovery_allowed(rows, parent_id, references)

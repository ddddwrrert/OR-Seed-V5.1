from .strategy_store import stored_strategies

def hypotheses_for(rows, parent_id):
    return [report for report in stored_strategies(rows, parent_id)]

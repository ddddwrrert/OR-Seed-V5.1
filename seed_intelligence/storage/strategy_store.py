from ..strategies.dynamic.strategy_loader import load_discovered

def stored_strategies(rows, parent_id):
    return load_discovered(rows, parent_id)

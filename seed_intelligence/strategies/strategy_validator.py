from .strategy_contract import valid_strategy

def viable_strategies(items):
    return (item for item in items if valid_strategy(item))

from ..strategy_contract import valid_strategy

def from_experiment(row):
    report = row.get("discovery")
    return dict(report) if valid_strategy(report) else None

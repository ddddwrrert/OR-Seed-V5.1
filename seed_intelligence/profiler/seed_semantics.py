from ..core.seed_manifest import SEEDS

def recorded_columns(metrics, field, limit=32):
    records = metrics.get(field)
    if not isinstance(records, dict):
        return {}
    columns = {}
    for name, values in list(records.items())[:limit]:
        if (isinstance(name, str) and 0 < len(name) <= 100 and isinstance(values, list)
                and len(values) == len(SEEDS)):
            columns[name] = values
    return columns

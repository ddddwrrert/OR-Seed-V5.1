def cached_evaluation(evaluations, identifier):
    record = evaluations.get(identifier)
    return record if isinstance(record, dict) else None

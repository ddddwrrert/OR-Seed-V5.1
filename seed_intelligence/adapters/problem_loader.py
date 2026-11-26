def task_record(evaluations, parent):
    record = evaluations.get(parent["id"])
    return record if isinstance(record, dict) else None

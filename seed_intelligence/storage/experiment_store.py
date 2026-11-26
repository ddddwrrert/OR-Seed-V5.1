def guidance_experiments(rows, identifier):
    for row in rows:
        record = row.get("guidance")
        if isinstance(record, dict) and record.get("id") == identifier:
            yield record

def previous_inspection(rows, parent_id):
    return any(row.get("parent") == parent_id and row.get("discoveryAttempt") for row in rows)

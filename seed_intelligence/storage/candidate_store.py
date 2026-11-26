from ..contracts import numeric

def recent_challengers(rows, parent_id, limit=10):
    return [row["id"] for row in reversed(rows)
            if row.get("id") and row.get("parent") == parent_id and numeric(row.get("fitness"))][:limit]

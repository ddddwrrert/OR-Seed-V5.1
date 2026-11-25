from ..contracts import numeric

def reference_ids(rows, parent):
    recent = [
        row["id"] for row in reversed(rows[-10:])
        if row.get("id") and row.get("parent") == parent["id"] and numeric(row.get("fitness"))
    ]
    return list(dict.fromkeys(recent + ([parent["parent"]] if parent.get("parent") else [])))

def discovered(rows, parent):
    for row in rows[-10:]:
        report = row.get("discovery")
        if numeric(row.get("fitness")) and isinstance(report, dict) and report.get("parent") == parent:
            yield report

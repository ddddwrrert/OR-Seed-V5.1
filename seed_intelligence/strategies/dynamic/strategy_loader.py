from ...contracts import numeric
from .strategy_serializer import from_experiment

def load_discovered(rows, parent_id):
    for row in rows:
        if numeric(row.get("fitness")):
            report = from_experiment(row)
            if report and report.get("parent") == parent_id:
                yield report

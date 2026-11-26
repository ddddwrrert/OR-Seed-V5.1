from statistics import mean
from ..contracts import numeric

def measured_rewards(records):
    deltas = [record["delta"] for record in records if numeric(record.get("delta"))]
    wins = sum(delta > 0 for delta in deltas)
    return len(deltas), wins, mean(deltas) if deltas else 0

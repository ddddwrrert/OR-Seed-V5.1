from ..contracts import numeric
from ..core.evaluation_guard import panel

def paired_delta(previous, current):
    if not all(isinstance(record, dict) and numeric(record.get("fitness")) for record in (previous, current)):
        return
    before, after = (panel(record.get("metrics")) for record in (previous, current))
    if before and after and before[0] == after[0]:
        return [(new - old) * after[0] for old, new in zip(before[1], after[1])]

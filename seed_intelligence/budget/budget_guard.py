from ..contracts import numeric

def eligible(parent, budget, spent, cap):
    return (numeric(parent.get("fitness")) and budget["used"] % 2 == 1
            and budget["remaining"] >= 2 and spent < cap)

from math import isfinite

def numeric(value):
    return type(value) in (int, float) and isfinite(value)

def hypothesis(item):
    fields = ("id", "direction", "evidence", "counterevidence")
    return isinstance(item, dict) and all(
        isinstance(item.get(key), str) and item[key].strip() and len(item[key]) <= 1500
        for key in fields
    )

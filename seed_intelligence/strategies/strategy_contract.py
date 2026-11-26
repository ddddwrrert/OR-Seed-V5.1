from ..contracts import hypothesis

def valid_strategy(item):
    if not hypothesis(item):
        return False
    for key in ("compatibleWith", "workflow"):
        if key in item and (not isinstance(item[key], list) or
                            not all(isinstance(value, str) for value in item[key])):
            return False
    return True

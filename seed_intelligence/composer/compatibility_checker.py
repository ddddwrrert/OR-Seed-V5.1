def compatible(left, right):
    return (left["id"] != right["id"]
            and isinstance(left.get("compatibleWith"), list)
            and right["id"] in left["compatibleWith"]
            and isinstance(right.get("compatibleWith"), list)
            and left["id"] in right["compatibleWith"])

def original_slot(budget):
    return budget["used"] % 2 == 0 or budget["remaining"] < 2

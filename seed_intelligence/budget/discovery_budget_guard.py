from ..evolution.mutation_history import previous_inspection

def uninspected(rows, parent_id):
    return not previous_inspection(rows, parent_id)

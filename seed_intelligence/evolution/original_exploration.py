def original_exploration(selected, inspection):
    # None is the Organon bridge's signal to invoke the original mutator normally.
    return selected is None and not inspection

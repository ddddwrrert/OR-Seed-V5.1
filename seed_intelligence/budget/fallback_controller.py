from ..evolution.original_exploration import original_exploration

def has_seed_work(selected, inspection):
    return not original_exploration(selected, inspection)

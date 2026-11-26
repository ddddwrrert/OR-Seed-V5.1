from ..storage.experiment_store import guidance_experiments

def trial_records(rows, key):
    return list(guidance_experiments(rows, key))

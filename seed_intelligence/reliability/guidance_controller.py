from .guidance_lifecycle import lifecycle
from .hypothesis_registry import hypothesis_trials
from .reliability_updater import update

def summarize(rows, key):
    trials = hypothesis_trials(rows, key)
    valid, wins, reliability, gain = update(trials)
    state = lifecycle(trials, valid, wins, reliability, gain)
    return {"id": key, "trials": len(trials), "wins": wins, "contrary": len(trials) - wins,
            "reliability": reliability, "meanGain": gain, "state": state}

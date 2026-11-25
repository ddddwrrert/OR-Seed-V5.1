from statistics import mean
from ..contracts import numeric

def summarize(rows, key):
    trials = [row["guidance"] for row in rows if (row.get("guidance") or {}).get("id") == key]
    observed = [trial["delta"] for trial in trials if numeric(trial.get("delta"))]
    wins = sum(delta > 0 for delta in observed)
    reliability = (1 + wins) / (2 + len(observed))
    net = mean(observed) if observed else 0
    misses = 0
    for trial in reversed(trials):
        if trial.get("outcome") == "improved":
            break
        misses += 1
    state = "uncertain"
    if not trials:
        state = "proposed"
    elif misses >= 2 or (len(observed) - wins >= 2 and reliability <= 0.4):
        state = "archived"
    elif wins >= 2 and reliability > 0.5 and net > 0:
        state = "validated"
    elif len(trials) == 1:
        state = "testing"
    return {"id": key, "trials": len(trials), "wins": wins, "contrary": len(trials) - wins,
            "reliability": reliability, "meanGain": net, "state": state}

from .guidance_circuit_breaker import exhausted

def lifecycle(trials, valid, wins, reliability, mean_gain):
    if not trials:
        return "proposed"
    if exhausted(trials, valid, wins, reliability):
        return "archived"
    if wins >= 2 and reliability > 0.5 and mean_gain > 0:
        return "validated"
    return "testing" if len(trials) == 1 else "uncertain"

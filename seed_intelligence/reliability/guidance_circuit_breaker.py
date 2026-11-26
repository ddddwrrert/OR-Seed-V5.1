from ..feedback.failure_memory import recent_misses

def exhausted(trials, valid, wins, reliability):
    return recent_misses(trials) >= 2 or (valid - wins >= 2 and reliability <= 0.4)

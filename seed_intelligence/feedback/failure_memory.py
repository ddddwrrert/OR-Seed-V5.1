def recent_misses(trials):
    count = 0
    for trial in reversed(trials):
        if trial.get("outcome") == "improved":
            break
        count += 1
    return count

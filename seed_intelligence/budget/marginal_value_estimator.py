def measured_value(item):
    return item["meanGain"] / max(1, item.get("candidateCost", 1))

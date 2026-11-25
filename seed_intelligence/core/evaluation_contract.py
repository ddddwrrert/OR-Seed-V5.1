from hashlib import sha256

SEEDS = tuple(range(50))
MANIFEST_HASH = sha256(",".join(map(str, SEEDS)).encode()).hexdigest()

def panel(metrics):
    if not isinstance(metrics, dict):
        return
    direction = metrics.get("score_direction")
    rows = metrics.get("seed_scores")
    if type(direction) is not int or direction not in (-1, 1):
        return
    if not isinstance(rows, list) or len(rows) != len(SEEDS):
        return
    scores = []
    for seed, row in zip(SEEDS, rows):
        if (not isinstance(row, dict) or type(row.get("seed")) is not int
                or row["seed"] != seed or row.get("accepted") is not True
                or type(row.get("score")) is not int):
            return
        scores.append(row["score"])
    return direction, scores

def panel_score(metrics):
    result = panel(metrics)
    if result:
        direction, scores = result
        return direction * (sum(scores) / len(SEEDS))


def manifest():
    return {"seeds": SEEDS, "hash": MANIFEST_HASH, "aggregation": "arithmetic_mean"}

def candidate_profile(metrics):
    result = panel(metrics)
    if result is None:
        return None
    direction, scores = result
    return {"direction": direction, "scoreRange": max(scores) - min(scores),
            "mean": sum(scores) / len(SEEDS)}

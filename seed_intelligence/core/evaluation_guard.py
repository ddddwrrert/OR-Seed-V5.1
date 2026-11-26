from .seed_manifest import SEEDS

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

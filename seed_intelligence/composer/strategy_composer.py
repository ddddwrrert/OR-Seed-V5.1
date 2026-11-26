from .compatibility_checker import compatible
from .strategy_scheduler import choose
from .workflow_executor import stages

def compose(selected, candidates, rows):
    if not selected or selected["state"] != "validated":
        return selected, None
    for candidate in candidates:
        if not compatible(selected, candidate):
            continue
        sequence = stages([selected["id"], candidate["id"]], candidates, rows)
        if not sequence:
            continue
        identifiers = [stage["id"] for stage in sequence]
        combined = {**selected, "id": "joint:" + "+".join(sorted(identifiers))}
        for key in ("direction", "evidence", "counterevidence"):
            combined[key] = "\n".join(stage[key] for stage in sequence)
        jointly_selected = choose([combined], rows)
        if jointly_selected:
            return jointly_selected, identifiers[1:]
    return selected, None

def explicit_workflows(candidates, rows):
    for candidate in candidates:
        if not candidate.get("workflow"):
            yield candidate
            continue
        sequence = stages(candidate["workflow"], candidates, rows)
        if sequence:
            steps = [f"{index}. {item['direction']}" for index, item in enumerate(sequence, 1)]
            yield {**candidate, "direction": candidate["direction"] + "\n" + "\n".join(steps)}

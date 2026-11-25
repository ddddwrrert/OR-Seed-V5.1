from ..reliability.guidance_controller import summarize

def choose(candidates, rows):
    options = [{**candidate, **summarize(rows, candidate["id"])} for candidate in candidates]
    active = [item for item in options if item["state"] != "archived"]
    if not active:
        return None
    return min(active, key=lambda item: (item["trials"] > 0, -item["reliability"], -item["meanGain"]))

def companions(selected, candidates, rows):
    # Composition is opt-in and requires two individually validated directions.
    if not selected or selected["state"] != "validated":
        return []
    allowed = selected.get("compatibleWith")
    if not isinstance(allowed, list):
        return []
    return [
        item["id"] for item in candidates
        if item["id"] != selected["id"] and item["id"] in allowed
        and isinstance(item.get("compatibleWith"), list) and selected["id"] in item["compatibleWith"]
        and summarize(rows, item["id"])["state"] == "validated"
    ][:1]

"""Build an ordered one-candidate workflow from validated compatible directions."""
from itertools import combinations
from ..reliability.guidance_controller import summarize
from .compatibility_checker import compatible

def stages(identifiers, candidates, rows):
    if not 2 <= len(identifiers) <= 6 or len(set(identifiers)) != len(identifiers):
        return []
    catalog = {candidate["id"]: candidate for candidate in candidates if not candidate.get("workflow")}
    if not all(identifier in catalog for identifier in identifiers):
        return []
    sequence = [catalog[identifier] for identifier in identifiers]
    if not all(summarize(rows, item["id"])["state"] == "validated" for item in sequence):
        return []
    return sequence if all(compatible(left, right) for left, right in combinations(sequence, 2)) else []

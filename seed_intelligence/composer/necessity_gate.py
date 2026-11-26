def requires_evidence(candidate, references):
    # A user can provide a fully stated hypothesis independently of M9.
    if not candidate.get("reference"):
        return True
    return any(item["reference"] == candidate["reference"] for item in references)

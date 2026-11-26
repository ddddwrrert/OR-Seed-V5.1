def survives_policy(status):
    # Candidate program survival remains the official score provider's decision.
    return status["state"] != "archived"

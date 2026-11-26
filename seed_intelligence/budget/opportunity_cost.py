def worthwhile(upper_bound, minimum, candidate_cost=1):
    return candidate_cost > 0 and upper_bound / candidate_cost > minimum

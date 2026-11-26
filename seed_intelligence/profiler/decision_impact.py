from ..budget.opportunity_cost import worthwhile

def actionable(profile, threshold):
    return bool(profile and profile["improvements"] and worthwhile(profile["recoverableMean"], threshold))

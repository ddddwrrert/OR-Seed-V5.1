def signal(reference, name):
    observed = reference.get("telemetry", {})
    features = reference["profile"].get("observedFeatures", {})
    return observed.get(name, features.get(name))


def rare_regression(reference, _):
    count = len(reference["profile"]["regressions"])
    return {"regressingSeeds": count} if 0 < count <= 4 else None


def proxy_disagrees(reference, name):
    value = signal(reference, name)
    return value if value and value.get("directionDisagrees") else None


def plateau(reference, name):
    value = signal(reference, name)
    return value if value and value["tailPlateauSamples"] >= 3 else None


def runtime_increased(reference, name):
    value = signal(reference, name)
    return value if value and value["meanDeltaSeconds"] > 0 else None


def complementary_operators(reference, name):
    value = signal(reference, name)
    return value if value and len(value) >= 2 else None


def differing_numeric_groups(reference, name):
    return {key: group for key, group in (signal(reference, name) or {}).items()
            if group["lowerMeanDelta"] != group["upperMeanDelta"]}


def differing_cohorts(reference, name):
    return {key: groups for key, groups in (signal(reference, name) or {}).items()
            if len({group["meanDelta"] for group in groups.values()}) > 1}


def variable_runs(reference, name):
    value = signal(reference, name)
    return value if value and value["spread"] > 0 else None


def difficulty_regresses(reference, name):
    value = signal(reference, name)
    return value if value and value["slowMeanDelta"] < value["fastMeanDelta"] else None

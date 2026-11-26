from statistics import mean
from ..contracts import numeric

def operator_evidence(after):
    observations = {}
    operators = after.get("operator_gains")
    if isinstance(operators, dict):
        summaries = {}
        for name, values in list(operators.items())[:32]:
            if not isinstance(name, str) or not 0 < len(name) <= 80 or not isinstance(values, list):
                continue
            sample = values[-32:]
            if sample and all(numeric(value) for value in sample):
                summaries[name] = {"samples": len(sample), "meanReportedGain": mean(sample)}
        if summaries:
            observations["operators"] = summaries

    return observations

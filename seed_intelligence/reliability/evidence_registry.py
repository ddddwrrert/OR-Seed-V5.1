from .counter_evidence import corroborates

def cited_evidence(report, reference):
    keys = report.get("telemetryKeys", [])
    telemetry = reference.get("telemetry", {})
    if corroborates(keys, telemetry):
        return {key: telemetry[key] for key in keys}

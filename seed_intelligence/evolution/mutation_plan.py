def plan(selected, inspect, references, capabilities, companion=None):
    if not selected and not inspect:
        return None
    result = {**(selected or {}), "inspect": inspect, "references": references if inspect else [],
              "capabilities": capabilities}
    if companion:
        result["composition"] = companion
    return result

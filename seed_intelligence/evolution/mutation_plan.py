from .exploration_dispatcher import dispatch

def plan(selected, inspect, references, capabilities, companion=None):
    instructions = dispatch(selected, inspect, references)
    if instructions is None:
        return
    result = {**(selected or {}), "inspect": inspect, "references": references if inspect else [],
              "capabilities": capabilities, "instructions": instructions}
    if companion:
        result["composition"] = companion
    return result

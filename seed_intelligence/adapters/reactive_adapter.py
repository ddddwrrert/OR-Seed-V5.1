from .base_adapter import Adapter

def reactive_adapter(capabilities, metrics):
    events = metrics.get("recorded_reactive_events")
    if isinstance(events, list) and events:
        return Adapter("reactive", {**capabilities, "reactiveEventCount": len(events)})
    return Adapter("generic", capabilities)

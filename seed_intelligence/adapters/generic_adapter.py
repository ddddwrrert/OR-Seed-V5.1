from .baseline_reader import parent_metrics
from .capability_discovery import capabilities
from .reactive_adapter import reactive_adapter

def evidence_capabilities(evaluation):
    metrics = parent_metrics(evaluation)
    adapter = reactive_adapter(capabilities(metrics), metrics)
    return {**adapter.capabilities, "adapter": adapter.name}

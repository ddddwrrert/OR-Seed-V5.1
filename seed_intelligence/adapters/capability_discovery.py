from ..contracts import numeric
from .generator_reader import generator_properties
from .instance_reader import instance_properties
from .scorer_reader import scorer_capability

def capabilities(metrics):
    return {**scorer_capability(metrics),
        "runtime": numeric(metrics.get("max_execution_time_sec")),
        "trace": isinstance(metrics.get("search_trace"), list) and bool(metrics["search_trace"]),
        "operatorGains": isinstance(metrics.get("operator_gains"), dict) and bool(metrics["operator_gains"]),
        "generatorProperties": generator_properties(metrics),
        "instanceProperties": instance_properties(metrics),
    }

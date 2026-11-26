from dataclasses import dataclass

@dataclass(frozen=True)
class Adapter:
    name: str
    capabilities: dict

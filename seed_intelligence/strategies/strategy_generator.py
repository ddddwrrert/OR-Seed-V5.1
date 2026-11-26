import json
from .builtin import CATALOG

def from_evidence(references, parent_id):
    for identifier, strategy in CATALOG.items():
        for reference in references:
            evidence = strategy.match(reference)
            if evidence:
                description = json.dumps(evidence, ensure_ascii=False)[:950]
                yield {
                    "id": f"{identifier}:{parent_id}", "builtin": identifier,
                    "direction": strategy.DIRECTION, "reference": reference["reference"],
                    "evidence": f"{strategy.EVIDENCE} in paired evaluation: {description}",
                    "counterevidence": "The recorded association can be incidental or specific to this parent. Check the official panel and existing time limit.",
                    "recoverableMean": reference["profile"]["recoverableMean"],
                }
                break

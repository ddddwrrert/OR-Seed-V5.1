import json

def research_lines(references):
    instructions = [
        "Optional bottleneck discovery during this candidate. Keep choosing and implementing one complete solution.",
        "Use existing source inspection and recorded contrasts. Do not run extra probes or edit extra files.",
        "If you see a promising one-candidate change, report one OR_SEED_HYPOTHESIS JSON line with id, direction, evidence, counterevidence, reference, expectedGain (whole-panel mean points), cost, and optional feature {name, observation, seeds} or telemetryKeys. Any mechanism can be proposed.",
    ]
    for item in references[:4]:
        profile = item["profile"]
        signals = {**profile.get("observedFeatures", {}), **item["telemetry"]}
        instructions.append(
            f"Reference {item['reference']}: recoverable mean at most {profile['recoverableMean']}; "
            f"seed regressions: {json.dumps(profile['regressions'])}; "
            f"recorded telemetry: {json.dumps(signals, ensure_ascii=False)[:2400]}."
        )
    return instructions

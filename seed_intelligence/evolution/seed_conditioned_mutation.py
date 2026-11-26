from .soft_guidance import guidance_lines

def mutation_instructions(selected):
    lines = guidance_lines(selected)
    feature = (selected or {}).get("feature")
    if feature:
        lines.append(f"Observed feature: {feature['name']} ({feature['observedDelta']} mean points). "
                     f"{feature['observation']}")
    return lines

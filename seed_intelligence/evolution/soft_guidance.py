def guidance_lines(selected):
    if not selected:
        return []
    return [
        "Optional hypothesis. You may ignore it and choose any better direction.",
        selected["direction"],
        f"Supporting evidence: {selected['evidence']}",
        f"Counterevidence: {selected['counterevidence']}",
        "The prediction is an improved complete 50-seed mean. Consider what would falsify it.",
    ]

from ..composer.adaptive_router import route

def select_guidance(strategies, rows, references):
    # Organon has selected the code parent already. Rank only its optional directions.
    return route(strategies, rows, references)

from ..storage.hypothesis_store import hypotheses_for

def previously_discovered(rows, parent_id):
    return hypotheses_for(rows, parent_id)

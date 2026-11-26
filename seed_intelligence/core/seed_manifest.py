from hashlib import sha256

SEEDS = tuple(range(50))
MANIFEST_HASH = sha256(",".join(map(str, SEEDS)).encode()).hexdigest()

def manifest():
    return {"seeds": SEEDS, "hash": MANIFEST_HASH, "aggregation": "arithmetic_mean"}

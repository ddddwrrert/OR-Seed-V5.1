from ..contracts import numeric

def scoring_evidence(previous, current, before, after):
    observations = {}
    proxy_before, proxy_after = before.get("proxy_score"), after.get("proxy_score")
    proxy_direction = after.get("proxy_score_direction")
    if (numeric(proxy_before) and numeric(proxy_after) and type(proxy_direction) is int
            and proxy_direction in (-1, 1) and before.get("proxy_score_direction") == proxy_direction):
        proxy_gain = (proxy_after - proxy_before) * proxy_direction
        actual_gain = current["fitness"] - previous["fitness"]
        if proxy_gain and numeric(actual_gain):
            observations["proxy"] = {"reportedProxyGain": proxy_gain, "formalGain": actual_gain,
                                     "directionDisagrees": proxy_gain * actual_gain < 0}
    return observations

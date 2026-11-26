def corroborates(keys, telemetry):
    return (isinstance(keys, list) and len(keys) <= 8
            and all(isinstance(key, str) and key in telemetry for key in keys))

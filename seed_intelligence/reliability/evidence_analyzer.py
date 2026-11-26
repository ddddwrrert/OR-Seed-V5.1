from ..contracts import numeric

def plausible_gain(gain, threshold, upper_bound):
    return numeric(gain) and threshold < gain <= upper_bound

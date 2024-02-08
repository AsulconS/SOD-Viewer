from math import modf


def map_range(value, from_, to):
    return to[0] + (to[1] - to[0]) * ((value - from_[0]) / (from_[1] - from_[0]))


def default_x_function(t):
    if t < 0.9:
        return 0.6
    elif t < 1.1:
        return map_range(t, from_=(0.9, 1.1), to=(0.6, 1.0))
    elif t < 2.4:
        return 1.0
    elif t < 2.5:
        return map_range(t, from_=(2.4, 2.5), to=(1.0, 0.25))
    elif t < 3.5:
        return 0.25
    elif t < 4.5:
        return map_range(t, from_=(3.5, 4.5), to=(0.25, 0.8))
    elif t < 5.0:
        return map_range(t, from_=(4.5, 5.0), to=(0.8, 0.6))
    else:
        return 0.6


def spiky_x_function(t):
    t_prime = modf(t)[0]
    if t_prime < 0.5:
        return map_range(t_prime, from_=(0.0, 0.5), to=(0.65, 0.75))
    else:
        return map_range(t_prime, from_=(0.5, 1.0), to=(0.75, 0.65))


def jitter_x_function(t):
    t_prime = modf(15.0 * t)[0]
    if t_prime < 0.5:
        return map_range(t_prime, from_=(0.0, 0.5), to=(0.68, 0.72))
    else:
        return map_range(t_prime, from_=(0.5, 1.0), to=(0.72, 0.68))

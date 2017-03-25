import random
from numpy.random import normal

def delay(duration, percentage_variation):
    stdev = percentage_variation / 100.0 * duration
    random_additive_noise = normal(0, stdev)
    return max(0, int(duration + random_additive_noise))

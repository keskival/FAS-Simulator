#!/usr/bin/python
import random

def delay(duration, percentage_variation):
    # TODO: Normal distribution would be more accurate.
    random_multiplier = random.randint(-percentage_variation * 100, percentage_variation * 100) / 10000 + 1;
    return duration * random_multiplier

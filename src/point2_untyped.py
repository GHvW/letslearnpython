# type: ignore

from functools import partial
import math

def distance_to(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 + 
        (p1[1] - p2[1]) ** 2)


# partial application
distance_to_origin = partial(distance_to, (0, 0))
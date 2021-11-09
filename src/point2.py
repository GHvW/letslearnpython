from typing import Callable, Tuple
from functools import partial
import math

# typealias
Coordinate = Tuple[float, float]

# with tuple instead of class
def distance_to(p1: Coordinate, p2: Coordinate) -> float:
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 + 
        (p1[1] - p2[1]) ** 2)


# partial application
distance_to_origin: Callable[[Tuple[float, float]], float] = partial(distance_to, (0, 0))
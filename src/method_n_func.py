# from typing import Tuple
import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def distance_to(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


distance_to(Point(0, 0), Point(1, 1))

Point(0, 0).distance_to(Point(1, 1))

Point.distance_to(Point(0, 0), Point(1, 1))

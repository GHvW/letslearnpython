import math

# class syntax
class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # equality
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Point):
            return (self.x == o.x) and (self.y == o.y)
        return False

    def distance_to(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + 
            (self.y - other.y) ** 2)


# type: ignore
import math

# class syntax
class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # equality
    def __eq__(self, o: object):
        if isinstance(o, Point):
            return (self.x == o.x) and (self.y == o.y)
        return False

    def distance_to(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 + 
            (self.y - other.y) ** 2)


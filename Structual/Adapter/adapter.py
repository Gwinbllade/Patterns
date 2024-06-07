import math
from typing import Tuple


class CartesianCoordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coord(self) -> Tuple:
        return (self.x, self.y)


class PolarCoordinate:
    def __init__(self, radius: int, angle: int):
        self.radius = radius
        self.angle = angle

    def get_coord(self) -> Tuple:
        return self.radius, self.angle


class CartesianToPolarAdapter(PolarCoordinate):
    def __init__(self, cartesianCoordinate: 'CartesianCoordinate'):
        self.radius = math.sqrt(cartesianCoordinate.x ** 2 + cartesianCoordinate.y ** 2)
        self.angle = math.atan2(cartesianCoordinate.y, cartesianCoordinate.x)


cartesian_coordinate = CartesianCoordinate(3, 4)
adapter = CartesianToPolarAdapter(cartesian_coordinate)

print(f"Cartesian coordinates: ({cartesian_coordinate.get_coord()})")
print(f"Polar coordinates: ({adapter.get_coord()})")

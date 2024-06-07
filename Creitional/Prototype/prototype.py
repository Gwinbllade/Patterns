import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def __copy__(self) -> 'Shape':
        pass

    @abstractmethod
    def __str__(self):
        pass


class Rectangle(Shape):
    def __init__(self, x: int, y: int, color: str, width: int, height: int):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def __copy__(self):
        new = self.__class__(self.x, self.y, self.color, self.width, self.height)
        return new
    def __str__(self):
        return f'Rectangle({self.x}, {self.y}, {self.color}, {self.width}, {self.height})'


class Circle(Shape):
    def __init__(self, x: int, y: int, color: str, radius: int):
        super().__init__(x, y, color)
        self.radius = radius

    def __copy__(self):
        new = self.__class__(self.x, self.y, self.color, self.radius)
        return new

    def __str__(self):
        return f'Circle({self.x}, {self.y}, {self.color}, {self.radius}'


class Application:
    def __init__(self):
        self.shapes = []

        circle = Circle(10, 10, 'red', 20)
        self.shapes.append(circle)

        another_circle = copy.copy(circle)
        self.shapes.append(another_circle)

        rectangle = Rectangle(0, 0, 'blue', 10, 20)
        self.shapes.append(rectangle)

    def business_logic(self):
        shapes_copy = []
        for shape in self.shapes:
            shapes_copy.append(copy.copy(shape))
        return shapes_copy


test = Application()
shapes = test.business_logic()

for shape in shapes:
    print(shape)
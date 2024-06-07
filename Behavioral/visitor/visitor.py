from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit(self, place: 'Place'):
        pass


class Place(ABC):
    def accept(self, visitor: Visitor):
        pass


class Zoo(Place):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Cinema(Place):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Park(Place):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Controller(Visitor):
    def __init__(self):
        self.__state = ""

    @property
    def state(self):
        return self.__state

    def visit(self, place: Place):
        if isinstance(place, Zoo):
            self.__state = "Visitor in zoo"
        elif isinstance(place, Cinema):
            self.__state = "Visitor in cinema"
        elif isinstance(place, Park):
            self.__state = "Visitor in park"


if __name__ == "__main__":
    places = [Cinema(), Zoo(), Park()]
    visitor = Controller()

    for place in places:
        visitor.visit(place)
        print(visitor.state)


from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.parts = []

    def add_part(self, part: str):
        self.parts.append(part)

    def list_parts(self):
        print(f"Car parts: {', '.join(self.parts)}")


class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def build_part_a(self):
        self.car.add_part("Колесо")

    def build_part_b(self):
        self.car.add_part("Двигун")

    def build_part_c(self):
        self.car.add_part("Кузов")

    def get_result(self) -> Car:
        return self.car


class Director:
    def __construct_car(self, builder: Builder):
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()

    def build_minimal_viable_product(self, builder: Builder):
        builder.build_part_a()
        builder.build_part_b()

    def build_full_featured_product(self, builder: Builder):
        self.__construct_car(builder)


director = Director()
builder = CarBuilder()

print("Standard car:")
director.build_full_featured_product(builder)
builder.get_result().list_parts()

print("\nMinimal Viable Car:")
builder = CarBuilder()
director.build_minimal_viable_product(builder)
builder.get_result().list_parts()

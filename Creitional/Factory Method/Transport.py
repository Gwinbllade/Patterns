class Transport:
    def __init__(self):
        print("Create transport")

    def run(self):
        print("Run")


class Car(Transport):
    def __init__(self):
        print("Create car")

    def run(self):
        print("Car run")


class Airplane(Transport):
    def __init__(self):
        print("Crate Airplane")

    def run(self):
        print("Airplane flying")


class Ship(Transport):
    def __init__(self):
        print("Create Ship")

    def run(self):
        print("Ship sailing ")


class CreatorTransport:
    def factory_method(self) -> Transport:
        return Transport()

    def run_transport(self):
        product = self.factory_method()
        product.run()


class CreateAirplane(CreatorTransport):
    def factory_method(self) -> Airplane:
        return Airplane()


class CreateShip(CreatorTransport):
    def factory_method(self) -> Ship:
        return Ship()


class CreateCar(CreatorTransport):
    def factory_method(self) -> Car:
        return Car()


def fabric_logic(create: CreatorTransport):
    create.run_transport()


fabric_logic(CreateCar())
fabric_logic(CreateAirplane())

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
    def factory_method(self) :
        return Airplane()
    
    def run_transport(self):
        product = self.factory_method()
        product.run()
        
    

class CreateAirplane(CreatorTransport):
    def factory_method(self) :
        return Airplane()

class CreateShip(CreatorTransport):
    def factory_method(self):
        return Ship()

class CreateCar(CreatorTransport):
    def factory_method(self):
        return Car()        
    

def fabric_logic(creater: CreatorTransport):
    creater.run_transport()


fabric_logic(CreateCar())
fabric_logic(CreateAirplane())

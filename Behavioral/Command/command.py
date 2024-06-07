from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass


class Conveyor:
    def on(self):
        print("Conveyor on")

    def off(self):
        print("Conveyor off")

    def speed_increase(self):
        print("Speed increase")

    def speed_decrease(self):
        print("Speed decrease")


class ConveyorWorkCommand(Command):
    def __init__(self, conveyor: Conveyor):
        self.conveyor = conveyor

    def positive(self):
        self.conveyor.on()

    def negative(self):
        self.conveyor.off()


class ConveyourSpeedCommand(Command):
    def __init__(self, conveyor: Conveyor):
        self.conveyor = conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decrease()


class Pult():
    def __init__(self):
        self.__commands: Dict[int, Command] = {}

    def set_commands(self, button: int, commands: Command):
        self.__commands[button] = commands

    def press_on(self, button: int):
        self.__commands[button].positive()

    def press_cancel(self, button: int):
        self.__commands[button].negative()


conveyor = Conveyor()
pult = Pult()
pult.set_commands(0, ConveyorWorkCommand(conveyor))
pult.set_commands(1, ConveyourSpeedCommand(conveyor))

pult.press_on(0)
pult.press_on(1)
pult.press_cancel(1)
pult.press_cancel(0)

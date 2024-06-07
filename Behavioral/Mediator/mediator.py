from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, emp: "Employee", msg: str):
        pass


class Employee(ABC):
    def __init__(self, med: Mediator):
        self._mediator = med

    def set_mediator(self, med: "Mediator"):
        self._mediator = med


class Builder(Employee):
    def __init__(self, med: Mediator = None):
        super().__init__(med)
        self.__is_built = False

    def set_work(self, state: bool):
        self.__is_built = state
        if state:
            print("Будівельник починає будувати")
            self.execute_work()
        else:
            print("Будівельник зупиняє роботу")

    def execute_work(self):
        print("Будівельик будує")
        self._mediator.notify(self, "Будівельний будує")


class Director(Employee):
    def __init__(self, med: Mediator = None):
        super().__init__(med)
        self.__text = None

    def give_command(self, txt: str):
        self.__text = txt
        if txt == "":
            print("Директор знає, що будівельник будує")
        else:
            print("Директор дав команду будувати")
            self._mediator.notify(self, txt)


class Controller(Mediator):
    def __init__(self, builder: Builder, director: Director):
        self.__builder = builder
        self.__director = director
        self.__builder.set_mediator(self)
        self.__director.set_mediator(self)

    def notify(self, emp: "Employee", msg: str):
        if isinstance(emp, Director):
            if msg == "":
                self.__builder.set_work(False)
            else:
                self.__builder.set_work(True)

        if isinstance(emp, Builder):
            if msg == "Будівельний будує":
                self.__director.give_command("")


builder = Builder()
director = Director()

mediator = Controller(builder, director)
director.give_command("Будувати")

print()

# builder.execute_work()

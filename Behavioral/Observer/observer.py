from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self, p: int):
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers = []

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, observer: IObserver) -> None:
        print(f"До спостерігачів доданий об'єкт {observer}")
        self.__observers.append(observer)

    def remove_observer(self, observer):
        print(f"З спостерігачів видалений об'єкт {observer}")
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.__price)


class Wholesale(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 100:
            print(f"Товар куплено об'єктом {self} по оптовій ціні")
            self.__product.remove_observer(self)


class SimpleBuyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 200:
            print(f"Товар куплено об'єктом {self} по зниженій ціні")
            self.__product.remove_observer(self)


product = Product(500)
wholeseller = Wholesale(product)
simplebuyer = SimpleBuyer(product)

while (True):
    new_price = int(input("Введінть нову ціну товану: "))
    product.change_price(new_price)

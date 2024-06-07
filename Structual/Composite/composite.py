from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Leaf(Component):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def get_price(self):
        total_price = 0
        for child in self.children:
            total_price += child.get_price()
        return total_price


class Product(Leaf):
    def __init__(self, name, price):
        super().__init__(price)
        self.name = name


class Box(Composite):
    def __init__(self, name):
        super().__init__()
        self.name = name


def calculate_total_price(order):
    return order.get_price()


# Example usage
product1 = Product("Product 1", 10)
product2 = Product("Product 2", 20)
box1 = Box("Box 1")
box1.add(Product("Product 3", 30))
box1.add(Product("Product 4", 40))
box2 = Box("Box 2")
box2.add(box1)
box2.add(Product("Product 5", 50))
order = Box("Order")
order.add(product1)
order.add(product2)
order.add(box2)
total_price = calculate_total_price(order)
print(f"Total price of the order: {total_price}")

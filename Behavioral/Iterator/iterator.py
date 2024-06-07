from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class DirectIterator(Iterator):
    def __init__(self, collection: 'Collection'):
        self.data = collection.data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def __str__(self):
        return "DirectIterator"


class ReverseIterator(Iterator):
    def __init__(self, collection: 'Collection'):
        self.data = collection.data
        self.index = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

    def __str__(self):
        return "ReverseIterator"


class Collection:
    def __init__(self):
        self.__data = []

    def add(self, value):
        self.data.append(value)

    @property
    def data(self):
        return self.__data


if __name__ == "__main__":
    collection = Collection()
    collection.add(1)
    collection.add(2)
    collection.add(3)

    iterators = [DirectIterator(collection), ReverseIterator(collection)]

    for iterator in iterators:
        print(iterator)
        for element in iterator:
            print(element)

from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader) -> None:
        self.__reader = reader

    def read(self, url: str):
        self.__reader.parse(url)


class NewsSiteReader(Reader):
    def parse(self, url: str):
        print("Parse news site " + url)


class SocialNetworkReader(Reader):
    def parse(self, url: str):
        print("Parse social network " + url)


if __name__ == "__main__":
    reader = ResourceReader(NewsSiteReader())

    url = "https://tsn.com"
    reader.read(url)

    url = "https://instagram.com"

    reader.set_strategy(SocialNetworkReader())
    reader.read(url)

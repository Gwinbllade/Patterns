from abc import ABC, abstractmethod
from typing import Dict, List


class IDatabase(ABC):
    def __init__(self):
        self.users_data: List[str] = []

    @abstractmethod
    def insert(self, user_data: str):
        pass

    @abstractmethod
    def get_user(self, user_id) -> str:
        pass


class LiteSQL(IDatabase):
    def insert(self, user_data: str):
        self.users_data.append(user_data)

    def get_user(self, user_id: int) -> str:
        for id in range(len(self.users_data)):
            if id == user_id:
                return self.users_data[id]


class DatabaseProxy(IDatabase):
    def __init__(self, DB: IDatabase):
        self.__database = DB
        self.__cache: Dict[int, str] = {}

    def get_user(self, user_id: int) -> str:
        user_data = None
        if self.__cache.get(user_id) is not None:
            print("Data from cache")
            user_data = self.__cache[user_id]
        else:
            print("Data from DB")
            user_data = self.__database.get_user(user_id)
            self.__cache[user_id] = user_data

        return user_data

    def insert(self, user_data: str):
        self.__database.insert(user_data)


my_database = DatabaseProxy(LiteSQL())
my_database.insert("Stepan")
my_database.insert("Ivan")
my_database.insert("Ihor")
my_database.insert("Oleg")

my_database.get_user(0)
my_database.get_user(0)

my_database.get_user(1)
my_database.get_user(0)

class Singleton(type):
    _instances = {}

    def __init__(cls, name: str, bases: str, namespace: str):
        print("Init Singleton")
        print(f"Creat new class {cls}")

    def __call__(cls, *args, **kwargs) -> object:
        print("__call__ in singleton")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DB(metaclass=Singleton):
    def __new__(cls, *args, **kwargs):
        print("__new__ in DB")

    pass


db = DB()

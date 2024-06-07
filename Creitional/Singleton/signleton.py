class DB:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


connect_1 = DB()
connect_2 = DB()

print(connect_2 == connect_1)
print(connect_1, connect_2)

### Мета класи
### Порядок виклики магічних методів
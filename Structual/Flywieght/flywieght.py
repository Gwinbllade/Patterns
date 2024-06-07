from abc import ABC, abstractmethod


class EnemyFlyweight(ABC):

    @abstractmethod
    def render(self, position):
        pass


class Enemy(EnemyFlyweight):
    def __init__(self, texture):
        self.__texture = texture

    def render(self, position):
        print(f"Rendering Enemy at position {position} with texture: {self.__texture}")


class EnemyFlyweightFactory:
    __flyweights = {}

    @staticmethod
    def get_flyweight(texture):
        if texture not in EnemyFlyweightFactory.__flyweights:
            EnemyFlyweightFactory.__flyweights[texture] = Enemy(texture)

        return EnemyFlyweightFactory.__flyweights[texture]


class GameEnvironment:
    def __init__(self):
        self.__enemies = []

    def add_enemy(self, texture, position):
        flyweight = EnemyFlyweightFactory.get_flyweight(texture)
        self.__enemies.append((flyweight, position))

    def render_enemies(self):
        for flyweight, position in self.__enemies:
            flyweight.render(position)


# Example usage
if __name__ == "__main__":
    game = GameEnvironment()

    game.add_enemy("texture_a", (10, 20))
    game.add_enemy("texture_b", (30, 40))
    game.add_enemy("texture_a", (50, 60))
    game.add_enemy("texture_b", (70, 80))

    game.render_enemies()

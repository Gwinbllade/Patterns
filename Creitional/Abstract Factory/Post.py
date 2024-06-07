from abc import ABC, abstractmethod


class CompanyPost(ABC):
    @abstractmethod
    def create_post(self):
        pass


class PostType(ABC):
    @abstractmethod
    def delivery(self):
        pass


class SeaPost(PostType):
    def delivery(self):
        print("Sea post delivery")


class AirPost(PostType):
    def delivery(self):
        print("Air post delivery")


class NovoPost(CompanyPost):
    def create_post(self) -> SeaPost:
        return SeaPost()


class UkrPost(CompanyPost):
    def create_post(self) -> AirPost:
        return AirPost()


def client_code(factory: CompanyPost):
    post = factory.create_post()
    print("Delivery type: ")
    post.delivery()


client_code(NovoPost())
client_code(UkrPost())

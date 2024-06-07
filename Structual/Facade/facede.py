class ProviderCommunication:
    def receive(self):
        print("Receiving goods from the manufacturer ")

    def payment(self):
        print("Payment received")


class Site:
    def placement(self):
        print("Goods placement on site")

    def delete(self):
        print("Goods delete from site")


class Database:
    def insert(self):
        print("Inserting into database")

    def delete(self):
        print("Deleting from database")


class MarketPlace:
    def __init__(self):
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receive(self):
        self._provider_communication.receive()
        self._database.insert()
        self._site.placement()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._database.delete()


mp = MarketPlace()
mp.product_receive()
mp.product_release()

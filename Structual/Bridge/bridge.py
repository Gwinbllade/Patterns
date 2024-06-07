from abc import ABC, abstractmethod


class DataReader(ABC):
    @abstractmethod
    def read(self):
        pass


class DBReader(DataReader):
    def read(self):
        print("Data from DB ", end="")


class FileReader(DBReader):
    def read(self):
        print("Data from file ", end="")


class Sender(ABC):
    def __init__(self, data_reader: DataReader):
        self.reader = data_reader

    def set_data_reader(self, data_reader: DataReader):
        self.reader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, date_reader: DataReader):
        super().__init__(date_reader)

    def send(self):
        self.reader.read()
        print("sent via email ")


class SlackSender(Sender):
    def __init__(self, date_reader: DataReader):
        super().__init__(date_reader)

    def send(self):
        self.reader.read()
        print("sent via Slack ")


sender = EmailSender(DBReader())
sender.send()

sender.set_data_reader(FileReader())
sender.send()

sender = SlackSender(DBReader())
sender.send()

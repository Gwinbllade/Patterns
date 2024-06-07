from abc import abstractmethod


class Reader:
    @abstractmethod
    def load_file(self, file_name: str):
        print(f"{file_name} load")

    @abstractmethod
    def save_file(self, path: str):
        print(f"file save {path}")

    @abstractmethod
    def read(self):
        pass


class PDFReader(Reader):
    def read(self):
        print(".pdf file read")


class DOCSReader(Reader):
    def read(self):
        print(".docs file read")


class XMLReader(Reader):
    def read(self):
        print(".xml file read")


if __name__ == "__main__":
    print("---------------------")
    reader = PDFReader()
    reader.load_file("file.pdf")
    reader.read()
    reader.save_file("/tmp/file.pdf")

    print("---------------------")
    reader = DOCSReader()
    reader.load_file("file.doc")
    reader.read()
    reader.save_file("/tmp/file.doc")

    print("---------------------")
    reader = XMLReader()
    reader.load_file("file.xml")
    reader.read()
    reader.save_file("/tmp/file.xml")

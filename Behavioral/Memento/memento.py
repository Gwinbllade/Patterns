from abc import ABC, abstractmethod
from typing import Deque


class IMemento(ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def set_text(self, text: str) -> None:
        pass


class TextEditorMemento(IMemento):
    def __init__(self, text: str) -> None:
        self.__text = text

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text: str) -> None:
        self.__text = text


class TextEditor:
    def __init__(self, text: str = "") -> None:
        self.__text = text

    def add_symbol(self, symbol: str):
        self.__text += symbol

    def delete_symbol(self):
        self.__text = self.__text[:-1]

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text: str) -> None:
        self.__text = text


class Memory:
    def __init__(self, text_editor: TextEditor) -> None:
        self.__history: Deque[IMemento] = []
        self.__text_editor = text_editor

    def backup(self):
        self.__history.append(TextEditorMemento(self.__text_editor.get_text()))

    def undo(self):
        if len(self.__history) > 0:
            memento = self.__history.pop()
            self.__text_editor.set_text(memento.get_text())


text_editor = TextEditor()
memory = Memory(text_editor)
if __name__ == "__main__":
    while True:
        action = input()
        match action:
            case "":
                text_editor.delete_symbol()
            case "S":
                memory.backup()
                print("save")
            case "U":
                memory.undo()
                print("undo")
            case _:
                text_editor.add_symbol(action)
        print(f"-> {text_editor.get_text()}")

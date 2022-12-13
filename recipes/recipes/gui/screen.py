from tkinter import Text
from tkinter.ttk import Frame, Label, Button, Treeview


class Screen:
    @staticmethod
    def add_frame(root: Frame, column: int, row: int) -> Frame:
        result = Frame(root)
        result.grid(column=column, row=row)
        return result

    @staticmethod
    def add_label(root: Frame, column: int, row: int, text: str) -> Label:
        result = Label(root, text=text)
        result.grid(column=column, row=row)
        return result

    @staticmethod
    def add_text(root: Frame, column: int, row: int) -> Text:
        result = Text(root, height=1, width=25, bg="light cyan")
        result.grid(column=column, row=row)
        return result

    @staticmethod
    def add_button(root: Frame, column: int, row: int, text: str, function) -> Button:
        result = Button(root, command=function, text=text)
        result.grid(column=column, row=row)
        return result

    @staticmethod
    def add_treeview(root: Frame, column: int, row: int):
        result = Treeview(root)
        result.grid(column=column, row=row)
        return result

from tkinter import ttk, Widget
from recepies.cookbook.recepy import Recepy


class RecepyScreen:
    def __init__(self, root) -> None:
        self.root: ttk.Frame = ttk.Frame(root)
        self.recepy
    
    def __clean_screen(self) -> None:
        for child in self.root.winfo_children():
            child.destroy()

    def display_recepy(self, recepy: Recepy) -> None:
        __clean_screen(self)
        self.recepy = recepy
        self.label = ttk.Label(self.root, text=recepy.name)


    

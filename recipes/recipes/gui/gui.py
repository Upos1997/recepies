from tkinter import Tk, ttk

from recipes.recipes.cookbook.cookbook import CookBook
from search_screen import SearchScreen


class Gui:
    def __int__(self):
        self.window = Tk()
        self.window.title("Kookboek")
        frame = ttk.PanedWindow(self.window)
        frame.pack(fill="both", expand=True)
        self.search_screen = SearchScreen(frame)

    def start(self, cookbook: CookBook):
        self.window.mainloop()
        self.search_screen.display()

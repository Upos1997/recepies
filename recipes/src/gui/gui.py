from tkinter import Tk, ttk

from recipes.src.cookbook.cookbook import CookBook
from recipes.src.gui.recipe_screen import RecipeScreen
from recipes.src.gui.search_screen import SearchScreen


class Gui:
    def __init__(self, cookbook: CookBook):
        self.window = Tk()
        self.window.title("Kookboek")
        frame = ttk.PanedWindow(self.window)
        frame.pack(fill="both", expand=True)
        self.search_screen = SearchScreen(frame, cookbook)
        self.recipe_screen = RecipeScreen(frame)

    def start(self):
        self.window.mainloop()

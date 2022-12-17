from recipes.src.cookbook.cookbook import CookBook
from recipes.src.gui.gui import Gui


def main():
    cookbook = CookBook()
    cookbook.load("data/save.json")
    gui = Gui(cookbook)
    gui.start()

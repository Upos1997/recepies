from recipes.recipes.cookbook.cookbook import CookBook
from recipes.recipes.gui.gui import Gui


def main():
    cookbook = CookBook()
    cookbook.load("data/save.json")
    gui = Gui()
    gui.start(cookbook)

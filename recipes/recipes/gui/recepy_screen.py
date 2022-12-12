from tkinter import ttk
from recipes.recipes.cookbook.recipe import Recipe


class RecipeScreen:
    def __init__(self, root) -> None:
        self.nameLabel = None
        self.recipe = None
        self.root: ttk.Frame = ttk.Frame(root)
    
    def __clean_screen(self) -> None:
        for child in self.root.winfo_children():
            child.destroy()

    def display_recipe(self, recipe: Recipe) -> None:
        self.__clean_screen()
        self.recipe = recipe
        self.nameLabel = ttk.Label(self.root, text=recipe.name)


    

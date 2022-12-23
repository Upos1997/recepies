from tkinter import ttk
from recipes.src.cookbook.recipe import Recipe
from recipes.src.gui.screen import Screen


class RecipeScreen(Screen):
    def __init__(self, root, recipe: Recipe) -> None:
        self.root = root
        main_root: ttk.Frame = ttk.Frame(root)
        main_root.grid()
        info_root: ttk.Frame = Screen.add_frame(main_root, 0, 0)
        self.name_label = Screen.add_label(info_root, 0, 0, recipe.name)
        self.name_label.grid(columnspan=4)
        subscript_root = Screen.add_frame(info_root, 0, 1)
        subscript_root.grid(columnspan=4)
        self.category_label = Screen.add_label(subscript_root, 0, 0, ", ".join(recipe.tags))
        self.source_label = Screen.add_label(subscript_root, 0, 1, recipe.source)
        new_button = Screen.add_button(main_root, 1, 0, "Nieuw", self.__clean_screen)
        edit_button = Screen.add_button(main_root, 1, 1, "Aanpassen", self.__clean_screen)
        ingredient_image_frame = ttk.Panedwindow(main_root)
        ingredient_image_frame.grid(row=2, column=0, columnspan=5)
        ingredient_frame = ttk.Frame(ingredient_image_frame)
        ingredient_frame.grid(row=0, column=0)
        self.image_label = ttk.Label(ingredient_image_frame, image=recipe.image)
        self.image_label.grid(row=0, column=1)
        self.recipe_label = ttk.Label(main_root, text="".join(recipe.instructions))


    def __clean_screen(self) -> None:
        for child in self.root.winfo_children():
            child.destroy()

    def display_recipe(self, recipe: Recipe) -> None:
        self.__clean_screen()
        self.nameLabel = ttk.Label(self.root, text=recipe.name)

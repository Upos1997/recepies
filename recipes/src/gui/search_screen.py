from tkinter import CENTER, NO, ttk

from recipes.src.cookbook.cookbook import CookBook
from recipes.src.cookbook.recipe import Recipe
from recipes.src.gui.screen import Screen


class SearchScreen(Screen):
    def __init__(self, root: ttk.Panedwindow, cookbook: CookBook):
        self.cookbook = cookbook
        self.main_root: ttk.Frame = ttk.Frame()
        # Display search section
        self.search_root = Screen.add_frame(self.main_root, 0, 0)
        self.search_root.grid()
        Screen.add_label(self.search_root, 0, 0, "Naam")
        self.name_search = Screen.add_text(self.search_root, 1, 0)
        Screen.add_label(self.search_root, 0, 1, "Ingredient")
        self.ingredient_search = Screen.add_text(self.search_root, 1, 1)
        Screen.add_label(self.search_root, 0, 2, "Categorie")
        self.tag_search = Screen.add_text(self.search_root, 1, 2)
        Screen.add_label(self.search_root, 0, 3, "Bron")
        self.source_search = Screen.add_text(self.search_root, 1, 3)
        Screen.add_button(self.search_root, 2, 3, "Zoek", self.search_cookbook)
        # Display database
        self.database_root = Screen.add_frame(self.main_root, 0, 1)
        self.database_root.grid()
        self.table = Screen.add_treeview(self.database_root, 0, 0)
        self.table['columns'] = ['naam']
        self.table.column("#0", width=0, stretch=NO)
        self.table.column("naam", anchor=CENTER, width=200)
        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("naam", text="Naam", anchor=CENTER)
        self.change_table(cookbook.recipes)
        root.add(self.main_root)

    def search_cookbook(self) -> None:
        names = self.name_search.get("1.0", 'end-1c').split(", ")
        ingredients = self.ingredient_search.get("1.0", 'end-1c').split(", ")
        tags = self.tag_search.get("1.0", 'end-1c').split(", ")
        sources = self.source_search.get("1.0", 'end-1c').split(", ")
        recipes = self.cookbook.find_recipes(names, ingredients, tags, sources)
        self.change_table(recipes)

    def change_table(self, entries: list[Recipe]) -> None:
        for entry in self.table.get_children():
            self.table.delete(entry)
        for entry in entries:
            self.table.insert(parent='', index='end', values=([entry.name]))

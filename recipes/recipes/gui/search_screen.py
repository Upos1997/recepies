from tkinter import CENTER, NO, Text, ttk

from recipes.recipes.cookbook.cookbook import CookBook
from recipes.recipes.cookbook.recipe import Recipe


class SearchScreen:
    def __init__(self, root, cookbook: CookBook):
        self.root = root
        self.cookbook = cookbook
        self.main_root: ttk.Frame = ttk.Frame()
        # Display search section
        self.search_root = ttk.Frame(self.main_root)
        self.search_root.grid(column=0, row=0)
        self.search_root.grid()
        ttk.Label(self.search_root, text="Naam").grid(column=0, row=0)
        self.name_search = Text(self.search_root, height=1, width=25, bg="light cyan")
        self.name_search.grid(column=1, row=0)
        ttk.Label(self.search_root, text="Ingredient").grid(column=0, row=1)
        self.ingredient_search = Text(self.search_root, height=1, width=25, bg="light cyan")
        self.ingredient_search.grid(column=1, row=1)
        ttk.Label(self.search_root, text="Categorie").grid(column=0, row=2)
        self.tag_search = Text(self.search_root, height=1, width=25, bg="light cyan")
        self.tag_search.grid(column=1, row=2)
        ttk.Label(self.search_root, text="Bron").grid(column=0, row=3)
        self.source_search = Text(self.search_root, height=1, width=25, bg="light cyan")
        self.source_search.grid(column=1, row=3)
        ttk.Button(self.search_root, text="Zoek", command=self.search_cookbook, width=10).grid(column=2, row=3)
        # Display database
        self.database_root = ttk.Frame(self.main_root)
        self.database_root.grid(column=0, row=1)
        self.database_root.grid()
        self.table = ttk.Treeview(self.database_root)
        self.table['columns'] = ['naam']
        self.table.column("#0", width=0, stretch=NO)
        self.table.column("naam", anchor=CENTER, width=200)
        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("naam", text="Naam", anchor=CENTER)
        self.table.grid(row=0, column=0)

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

    def display(self) -> None:
        self.root.add(self.main_root)

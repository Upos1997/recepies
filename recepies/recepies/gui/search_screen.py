from tkinter import CENTER, NO, Text, ttk

from recepies.cookbook.cookbook import CookBook

class SearchScreen:
    def __init__(self, root, cookbook: CookBook):
        self.root = root
        self.cookbook = cookbook
        self.main_root: ttk.Frame = ttk.Frame()
        self.search_root = ttk.Frame(self.main_root)
        self.search_root.grid(column=0, row=0)
        self.search_root.grid()
        self.database_root = ttk.Frame(self.main_root)
        self.database_root.grid(column=0, row=1)
        self.database_root.grid()
        self.display_searchframe()
        self.display_databaseframe()

    def search_cookbook(self) -> None:
        names = self.name_search.get("1.0", 'end-1c').split(", ")

    def display_searchframe(self) -> None:
        ttk.Label(self.search_root, text="Naam").grid(column=0, row=0)
        self.name_search = Text(
            self.search_root, height=1, width=25, bg="light cyan")
        self.name_search.grid(column=1, row=0)
        ttk.Label(self.search_root, text="Ingredient").grid(column=0, row=1)
        self.ingredient_search = Text(
            self.search_root, height=1, width=25, bg="light cyan")
        self.ingredient_search.grid(column=1, row=1)
        ttk.Label(self.search_root, text="Categorie").grid(column=0, row=2)
        self.tag_search = Text(self.search_root, height=1,
                               width=25, bg="light cyan")
        self.tag_search.grid(column=1, row=2)
        ttk.Label(self.search_root, text="Bron").grid(column=0, row=3)
        self.source_search = Text(self.search_root, height=1,
                                  width=25, bg="light cyan")
        self.source_search.grid(column=1, row=3)
        ttk.Button(self.search_root, text="Zoek", command=self.search_cookbook,
                   width=10).grid(column=2, row=3)

    def display_databaseframe(self) -> None:
        set = ttk.Treeview(self.database_root)
        set['columns'] = ('naam', 'bron')
        set.column("#0", width=0,  stretch=NO)
        set.column("naam", anchor=CENTER, width=200)
        set.column("bron", anchor=CENTER, width=80)

        set.heading("#0", text="", anchor=CENTER)
        set.heading("naam", text="Naam", anchor=CENTER)
        set.heading("bron", text="Bron", anchor=CENTER)

        set.insert(parent='', index='end', iid=0, text='',
                   values=('Advocaat', 'website.com'))
        set.insert(parent='', index='end', iid=1, text='',
                   values=('Pompoenschotel', 'jos kok'))
        set.insert(parent='', index='end', iid=2, text='',
                   values=('Chocomouse', 'ergens'))
        set.grid(row=0, column=0)

    def display(self) -> None:
        self.root.add(self.main_root)

from tkinter import Tk, ttk

from recipes.recipes.cookbook.cookbook import CookBook
from search_screen import SearchScreen


def main():
    cookbook = CookBook()
    window = Tk()
    window.title("Kookboek")
    frame = ttk.PanedWindow(window)
    frame.pack(fill="both", expand=True)
    search_screen = SearchScreen(frame)

    search_screen.display()
    window.mainloop()


if __name__ == "__main__":
    main()

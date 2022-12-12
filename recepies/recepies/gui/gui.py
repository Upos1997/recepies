from tkinter import Tk, ttk, filedialog
from search_screen import SearchScreen
from recepies.cookbook.cookbook import CookBook


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

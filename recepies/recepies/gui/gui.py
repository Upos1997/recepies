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

    def load_cookbook():
        cookbook.load(filedialog.askopenfile())
        main_screen()

    def clean_screen():
        for widget in frame.winfo_children():
            widget.destroy()

    def load_screen():
        clean_screen()
        ttk.Button(frame, text="Nieuw Kookboek", command=main_screen).grid(
            column=0, row=0
        )
        ttk.Button(frame, text="Laad Kookboek", command=load_cookbook).grid(
            column=0, row=1
        )

    def main_screen():
        clean_screen()
        search_screen.display()

    load_screen()
    window.mainloop()


if __name__ == "__main__":
    main()

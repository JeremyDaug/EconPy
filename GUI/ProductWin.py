import tkinter as tk
import typing


class ProductWin:

    def __init__(self):
        self.Title: str = "Product Editor"
        self.geometry: str = "500x700"
        self.prodWin = None
        return

    def open_window(self):
        self.prodWin = tk.Tk()
        self.prodWin.title(self.Title)
        self.prodWin.geometry(self.geometry)
        self.prodWin.mainloop()
        return


if __name__ == "__main__":
    test = ProductWin()
    test.open_window()

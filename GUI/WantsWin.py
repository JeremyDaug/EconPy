"""
Window file for the Systems want types.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Storage.Wants import Wants


class WantsWin:
    def __init__(self):
        self.Title: str = "Wants Editor"
        self.geometry: str = "300x300"
        self.win = None
        self.main_list = None
        self.delete_button = None
        self.new_want = None
        self.new_want_button = None
        self.save_tags_to_file = None
        # if no wants are in wants, load from file just in case.
        if not Wants.Wants:
            Wants.load_wants()
        return

    def open_window(self):
        self.win = tk.Tk()
        self.win.title(self.Title)
        self.win.geometry(self.geometry)
        self.setup_window()
        self.win.mainloop()
        return

    def setup_window(self):
        main_label = tk.Label(self.win, text="Product Tags")
        main_label.grid(column=0, row=0)
        self.main_list = tk.Listbox(self.win, selectmode="multiple")
        for item in sorted(Wants.Wants, reverse=True):
            self.main_list.insert(0, item)
        self.main_list.grid(column=0, row=1, rowspan=3)
        self.delete_button = tk.Button(self.win,
                                       text="Delete Selected",
                                       command=self.delete)
        self.delete_button.grid(column=1, row=1)
        self.new_want = ttk.Entry(self.win)
        self.new_want.grid(column=1, row=2)
        self.new_want_button = tk.Button(self.win,
                                         text="Add New Tag",
                                         command=self.add_tag)
        self.new_want_button.grid(column=1, row=3)
        self.save_tags_to_file = tk.Button(self.win,
                                           text="Save Tags to File",
                                           command=self.save_wants)
        self.save_tags_to_file.grid(column=0, row=4, columnspan=2)
        return

    def save_wants(self):
        Wants.save_wants()
        return

    def add_tag(self):
        tag: str = self.new_want.get().strip()

        # empty or whitespace check, clear if empty for ease.
        if not tag:
            self.new_want.delete(0, 'end')
            return

        if any([True for x in Wants.Wants if x == tag]):
            messagebox.showwarning("Duplicate Tag", "This tag already exists in your list.")
            return

        # if whitespace, stop and scold
        if any([True for x in tag if x.isspace()]):
            messagebox.showwarning("Improper Tag", "Tags cannot contain any whitespace.")
            return
        # if valid, clear entry and add to list.
        self.new_want.delete(0, 'end')
        Wants.Wants.append(tag)
        self.main_list.insert('end', tag)
        return

    def delete(self):
        selected = self.main_list.curselection()
        for item in reversed(selected):
            Wants.Wants.remove(self.main_list.get(item))
            self.main_list.delete(item)
        return


if __name__ == "__main__":
    test = WantsWin()
    test.open_window()


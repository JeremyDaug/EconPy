import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Storage.ProductTags import ProductTags


class ProductTagsWin:
    def __init__(self, tags: list[str] = None):
        self.Title: str = "Product Tags Editor"
        self.geometry: str = "300x300"
        self.win = None
        self.main_list = None
        self.delete_button = None
        self.new_tag = None
        self.new_tag_button = None
        self.save_tags_to_file = None
        # if no tags are in product tags, load from file just in case.
        if not ProductTags.Tags:
            ProductTags.load_tags()
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
        for item in sorted(ProductTags.Tags, reverse=True):
            self.main_list.insert(0, item)
        self.main_list.grid(column=0, row=1, rowspan=3)
        self.delete_button = tk.Button(self.win,
                                       text="Delete Selected",
                                       command=self.delete)
        self.delete_button.grid(column=1, row=1)
        self.new_tag = ttk.Entry(self.win)
        self.new_tag.grid(column=1, row=2)
        self.new_tag_button = tk.Button(self.win,
                                        text="Add New Tag",
                                        command=self.add_tag)
        self.new_tag_button.grid(column=1, row=3)
        self.save_tags_to_file = tk.Button(self.win,
                                           text="Save Tags to File",
                                           command=self.save_tags)
        self.save_tags_to_file.grid(column=0, row=4, columnspan=2)
        return

    def save_tags(self):
        ProductTags.save_tags()
        return

    def add_tag(self):
        tag: str = self.new_tag.get().strip()

        # empty or whitespace check, clear if empty for ease.
        if not tag:
            self.new_tag.delete(0, 'end')
            return

        if any([True for x in ProductTags.Tags if x == tag]):
            messagebox.showwarning("Duplicate Tag", "This tag already exists in your list.")
            return

        # if whitespace, stop and scold
        if any([True for x in tag if x.isspace()]):
            messagebox.showwarning("Improper Tag", "Tags cannot contain any whitespace.")
            return
        # if valid, clear entry and add to list.
        self.new_tag.delete(0, 'end')
        ProductTags.Tags.append(tag)
        self.main_list.insert('end', tag)
        return

    def delete(self):
        selected = self.main_list.curselection()
        for item in reversed(selected):
            ProductTags.Tags.remove(self.main_list.get(item))
            self.main_list.delete(item)
        return


if __name__ == "__main__":
    test_list = ["luxury", "vanity", "militarygood"]
    test = ProductTagsWin(test_list)
    test.open_window()

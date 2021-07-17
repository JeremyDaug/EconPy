import tkinter as tk
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import typing
from PIL import ImageTk, Image
from Storage.defaults import commonProductImages
from Storage.ProductTags import ProductTags
import os
from Storage.Product import Product


class ProductWin:
    def __init__(self, product=None):
        self.Title: str = "Product Editor"
        self.geometry: str = "500x700"
        if product is None:
            self.current_product = Product()
        else:
            self.current_product = product
        self.win = None
        self.product_name = None
        self.product_name_entry = None
        self.product_variant_name = None
        self.product_variant_entry = None
        self.product_unit = None
        self.product_unit_entry = None
        self.product_quality = None
        self.product_quality_box = None
        self.mass_label = None
        self.mass_entry = None
        self.bulk_label = None
        self.bulk_entry = None
        self.fractional_label = None
        self.fractionalVar = None
        self.fractional_box = None
        self.tag_label = None
        self.tag_selector = None
        self.mttf_label = None
        self.mttf_entry = None
        # fails into
        # maintenance
        self.tech_label = None
        self.tech_entry = None
        # fill tech list
        self.image_label = None
        self.image_path: str = ""
        self.image = None
        self.image_box = None
        self.image_select = None
        self.clear_image_btn = None
        self.save_product_button = None
        return

    def open_window(self):
        self.win = tk.Tk()
        self.win.title(self.Title)
        self.win.geometry(self.geometry)
        self.build_window()
        self.order_window()
        self.win.mainloop()
        return

    def build_window(self):
        self.product_name = tk.Label(self.win, text="Product Name")
        self.product_name_entry = ttk.Entry(self.win)
        self.product_variant_name = tk.Label(self.win, text="Variant Name")
        self.product_variant_entry = ttk.Entry(self.win)
        self.product_unit = tk.Label(self.win, text="Unit")
        self.product_unit_entry = ttk.Entry(self.win)
        self.product_quality = tk.Label(self.win, text="Quality")
        self.product_quality_box = ttk.Entry(self.win)
        self.mass_label = tk.Label(self.win, text="Unit Mass")
        self.mass_entry = ttk.Entry(self.win)
        self.bulk_label = tk.Label(self.win, text="Unit Bulk")
        self.bulk_entry = ttk.Entry(self.win)
        self.fractional_label = tk.Label(self.win, text="Fractional")
        self.fractionalVar = tk.IntVar()
        self.fractional_box = tk.Checkbutton(self.win,
                                             variable=self.fractionalVar)
        self.tag_label = tk.Label(self.win, text="Tags")
        self.tag_selector = tk.Listbox(self.win, selectmode="multiple")
        for item in ProductTags.Tags:
            self.tag_selector.insert(0, item)
        # Wants
        self.mttf_label = tk.Label(self.win, text="Mean Time To Failure")
        self.mttf_entry = ttk.Entry(self.win)
        # fails into
        # maintenance
        self.tech_label = tk.Label(self.win, text="Technology Requirements")
        self.tech_entry = tk.Listbox(self.win, selectmode="multiple")
        # fill tech list
        self.image_label = tk.Label(self.win, text="Product Image")
        self.image_path = os.path.join(commonProductImages, "wheatIcon.png")
        img = Image.open(self.image_path)
        img = img.resize((64, 64), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(img)
        self.image_box = tk.Label(self.win, image=self.image)
        self.image_select = tk.Button(self.win, text="Select Image",
                                      command=self.select_image)
        self.clear_image_btn = tk.Button(self.win, text="Clear Image",
                                         command=self.clear_image)
        self.save_product_button = tk.Button(self.win, text="Save Product",
                                             command=self.save_product)
        return

    def order_window(self):
        self.product_name.grid(column=0, row=0)
        self.product_name_entry.grid(column=1, row=0)
        self.product_variant_name.grid(column=0, row=1)
        self.product_variant_entry.grid(column=1, row=1)
        self.product_unit.grid(column=0, row=2)
        self.product_unit_entry.grid(column=1, row=2)
        self.product_quality.grid(column=0, row=3)
        self.product_quality_box.grid(column=1, row=3)
        self.mass_label.grid(column=0, row=4)
        self.mass_entry.grid(column=1, row=4)
        self.bulk_label.grid(column=0, row=5)
        self.bulk_entry.grid(column=1, row=5)
        self.fractional_label.grid(column=0, row=6)
        self.fractional_box.grid(column=1, row=6)
        self.tag_label.grid(column=0, row=7)
        self.tag_selector.grid(column=1, row=7)
        # Wants
        self.mttf_label.grid(column=0, row=9)
        self.mttf_entry.grid(column=1, row=9)
        # fails into
        # maintenance
        self.tech_label.grid(column=0, row=12)
        self.tech_entry.grid(column=1, row=12)
        self.image_label.grid(column=2, row=0)
        self.image_box.grid(column=2, row=1, rowspan=4)
        self.image_select.grid(column=2, row=6)
        self.clear_image_btn.grid(column=2, row=7)
        self.save_product_button.grid(column=2, row=13)
        return

    def clear_image(self):
        self.image_path = ""
        self.image = None
        self.image_box.configure(image=None)
        self.image_box.image = None
        return

    def select_image(self):
        filename = fd.askopenfilename(title="Select Image File",
                                      initialdir=commonProductImages,
                                      filetypes=[("PNG", ".png")])
        # if none selected,
        if not filename:
            return
        self.image_path = filename
        img = Image.open(self.image_path)
        img = img.resize((64,64), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(img)
        self.image_box.configure(image=self.image)
        self.image_box.image = self.image
        return

    def save_product(self):
        temp = Product()
        name = self.product_name_entry.get()
        if not name:
            messagebox.showerror(title="Product Name Empty",
                                 message="Product must have a name.")
            return
        temp.Name = name
        temp.VariantName = self.product_variant_entry.get()
        unit = self.product_unit_entry.get()
        if not unit:
            messagebox.showerror(title="Unit Name Empty",
                                 message="Product must have a unit.")
            return
        temp.UnitName = unit
        quality = self.product_quality_box.get()
        try:
            quality = int(quality)
        except ValueError:
            messagebox.showerror(title="Quality Error",
                                 message="Quality must be a whole number value.")
            return
        temp.Quality = quality
        mass = self.mass_entry.get()
        try:
            mass = float(mass)
        except ValueError:
            messagebox.showerror(title="Mass Error",
                                 message="Mass must be a decimal value.")
            return
        if mass < 0:
            messagebox.showerror(title="Mass Error",
                                 message="Mass cannot be negative.")
            return
        temp.Mass = mass
        bulk = self.bulk_entry.get()
        try:
            bulk = float(bulk)
        except ValueError:
            messagebox.showerror(title="Bulk Error",
                                 message="Bulk must be a decimal value.")
            return
        if bulk < 0:
            messagebox.showerror(title="Bulk Error",
                                 message="Bulk cannot be negative.")
            return
        temp.Bulk = bulk
        fractional = self.fractionalVar.get()
        temp.Fractional = bool(fractional)
        tagNames = []
        for tag in self.tag_selector.curselection():
            tagNames.append(self.tag_selector.get(tag))
        temp.Tags = ProductTags.combine_tags(tagNames)
        #temp.Wants: str = wants
        mttf = self.mttf_entry.get()
        try:
            mttf = int(mttf)
        except ValueError:
            messagebox.showerror(title="Mean Time To Failure Error",
                                 message="Mean Time To Failure must be an integer.")
            return
        if mttf < -1:
            messagebox.showerror(title="Mean Time To Failure Error",
                                 message="Mean Time to Failure must be an integer greater than or equal to -1.")
        temp.MTTF = mttf
        #temp.FailsInto: dict = failsInto
        #temp.Maintenance: dict = maintenance
        #temp.Technology: str = technology
        #temp.Image: str = imagefile
        return

    def load_product(self):
        ProductTags.load_tags()
        return


if __name__ == "__main__":
    test = ProductWin()
    test.load_product()
    test.open_window()

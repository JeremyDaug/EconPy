"""
File for default information and constants
"""
import os


saveFolder = os.path.abspath(os.path.dirname(__file__))
root: str = os.path.dirname(saveFolder)
"""The root of our project."""

saveFolder: str = os.path.join(root, "SaveData")
"""The Save folder of our project"""

sharedData: str = os.path.join(saveFolder, "SharedData")

sharedProductData: str = os.path.join(sharedData, "Products")
commonProductTags: str = os.path.join(sharedProductData, "ProductTags.json")
commonWants: str = os.path.join(sharedProductData, "Wants.json")
commonProducts: str = os.path.join(sharedProductData, "Products.json")
commonProductImages: str = os.path.join(sharedProductData, "ProductImages")


if __name__ == "__main__":
    pass

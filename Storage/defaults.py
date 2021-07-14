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

sharedProducts: str = os.path.join(sharedData, "Products")
sharedProductTags: str = os.path.join(sharedProducts, "ProductTags.json")

if __name__ == "__main__":
    pass

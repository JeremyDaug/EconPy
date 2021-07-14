"""
Product tag manager.
"""
import typing
import json
from Storage import defaults
import os


class ProductTags:
    """
    Tags are in the form of words, this is effectively a singleton class and should only have one in existence at
    any time.
    """
    Tags: list = list()

    @staticmethod
    def save_tags(file: str = "") -> None:
        """
        Saves the Product tages to a file.
        :param file: The file to save to, if null it saves to SaveData/SharedData/Products/ProductTags.json
        """
        # if no file given, use default.
        if not file:
            file = defaults.sharedProductTags
        with open(file, 'w') as saveFile:
            json.dump(ProductTags.Tags, saveFile)
        return

    @staticmethod
    def load_tags(file: str = "") -> None:
        """
        Loads tags from json file.
        :param file: The file to load from, if empty, defaults to SaveData/SharedData/Products/ProductTags.json
        """
        if not file:
            file = defaults.sharedProductTags
        with open(file, 'r') as loadFile:
            ProductTags.Tags = json.load(loadFile)
        return

    @staticmethod
    def process_tags(tags: str) -> list[str]:
        """
        Takes a delimited list of tags and turns them into a list.
        :param tags: The tags to split
        :return: The tags in a list.
        """
        return tags.split(";")

    @staticmethod
    def combine_tags(tags: list[str]) -> str:
        """
        Takes a list of tags and combines them into delimited list.
        :param tags: The list of tags to combine.
        :return: The tags combined in a ';' delimited list.
        """
        result = ""
        for tag in tags:
            result += tag + ";"
        return result


def reset_tags():
    return


if __name__ == "__main__":
    ProductTags.Tags.append("Luxury")
    ProductTags.Tags.append("Inferior")
    ProductTags.save_tags()

"""
Manager class for Wants available to the system. Basically the same as ProductTags, but with more
processing for delimited lists.
"""


"""
Product tag manager.
"""
import json
from Storage import defaults


class Wants:
    """
    Tags are in the form of words, this is effectively a singleton class and should only have one in existence at
    any time.
    """
    Wants: list = list()  # TODO Consider changing this to a set for easy exclusions.
    """The List of Product Wants which currently exist."""

    @staticmethod
    def save_wants(file: str = "") -> None:
        """
        Saves the Wants to a file.
        :param file: The file to save to, if null it saves to SaveData/SharedData/Products/Wants.json
        """
        # if no file given, use default.
        if not file:  # TODO consider removing this as the common file should never be overridden after creation.
            file = defaults.commonWants
        with open(file, 'w') as saveFile:
            json.dump(Wants.Wants, saveFile)
        return

    @staticmethod
    def load_wants(file: str = "") -> None:
        """
        Loads Wants from json file.
        :param file: The file to load from, if empty, defaults to SaveData/SharedData/Products/Wants.json
        """
        if not file:
            file = defaults.commonWants
        with open(file, 'r') as loadFile:
            Wants.Wants = json.load(loadFile)
        return

    @staticmethod
    def process_wants(wants: str) -> list[str]:
        """
        Takes a delimited list of Wants and turns them into a list.
        :param wants: The Wants to split
        :return: The Wants in a list.
        """
        return wants.split(";")

    @staticmethod
    def combine_wants(wants: list[str]) -> str:
        """
        Takes a list of Wants and combines them into delimited list.
        :param wants: The list of Wants to combine.
        :return: The Wants combined in a ';' delimited list.
        """
        result = ""
        for tag in wants:
            result += tag + ";"
        return result


def reset_wants():
    return


if __name__ == "__main__":
    Wants.Wants.append("Luxury")
    Wants.Wants.append("Inferior")
    Wants.save_wants()

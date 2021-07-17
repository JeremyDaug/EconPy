"""
Product Class for EconPy Project. Used to store the shared data of products.
"""


class Product:
    """
    Product class, stores data of a product.
    """

    def __init__(self, ID: int = 0, name: str = "", variantName: str = "",
                 unitName: str = "", quality: int = 0, mass: float = 0,
                 bulk: float = 0, fractional: bool = False, tags: str = "",
                 wants: str = "", mttf: int = 0, failsInto: dict = None,
                 maintenance: dict = None, technology: str = "", imageFile: str = ""):
        """
        Constructor
        :param ID: The id of the product, should be unique.
        :param name: the name of the product, should not be empty or whitespace.
        :param variantName: The variant name of the product, if it is one.
        :param unitName: The name of unit it is measured in.
        :param quality: The quality of the product.
        :param mass: The mass of the product, must be 0 or greater.
        :param bulk: The volume of the product, must be 0 or greater.
        :param fractional: If the product is fractional or not.
        :param tags: What product tags the product has.
        :param wants: The wants satisfied by the product in Want:##; fashion.
        :param mttf: Mean Time To Failure in days.
        :param failsInto: What it fails into.
        :param maintenance: What can maintain this product, reducing it's failure.
        :param technology: What technology makes this product available, ; separated string.
        :param imageFile: The image file for the product.
        """
        self.Id: int = ID
        """Product Id, must be unique."""
        self.Name: str = name
        """Product Name, must be unique."""
        self.VariantName: str = variantName
        """Name of a variant product, should be unique for the product."""
        self.UnitName: str = unitName
        """The unit the product is measured in."""
        self.Quality: int = quality
        """The Quality of the product."""
        self.Mass: float = mass
        """The Mass of a unit of the product in Kg."""
        self.Bulk: float = bulk
        """The volume bulk of a unit of the product in Kg."""
        self.Fractional: bool = fractional
        """If the product can be moved in fractions of a unit."""
        self.Tags: str = tags
        """The Tags of the product, separated list of 'tag1;tag2'."""
        self.Wants: str = wants
        """
        The wants of the product, separated string 'want1:#;want2:#'.
        Want is the want it applies to, # is satisfaction per unit.
        """
        self.MTTF: int = mttf
        """
        Product's Mean Time To Failure, -1 means it cannot fail,
        0 means it fails at the end of the day.
        """
        self.FailsInto: dict = failsInto
        """What the product fails into and at what rate per unit."""
        self.Maintenance: dict = maintenance
        """Products that maintain this one directly."""
        self.Technology: str = technology
        """The Technologies required to make this product. Semicolon separated list."""
        self.Image: str = imageFile
        """The image file location used to for the product."""
        return

    def failure_chance(self):
        return 1 / self.MTTF


if __name__ == "__main__":
    test = Product()
    test.Id = 1
    test.Mass = 1

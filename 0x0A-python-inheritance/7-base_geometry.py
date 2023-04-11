#!/usr/bin/python3
"""BaseGeometry module
"""


class BaseGeometry:
    """ empty BaseGeometry
    """

    def area(self):
        """Area function that is still empty

        Args:
            self: this object
        Return:
            return area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> Exception:
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

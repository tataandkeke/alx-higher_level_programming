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

    def integer_validator(self, name, value):
        """Validates the Value Parameter

        Args:
            self: this object

            name: name of the value

            value: the number parsed
        """

        if type(value) != int:
            raise TypeError(F"{name} must be an integer")
        if value <= 0:
            raise ValueError(F"{name} must be greater than 0")

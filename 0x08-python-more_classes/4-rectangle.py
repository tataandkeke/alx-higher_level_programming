#!/usr/bin/python3
""" Rectangle module
"""


class Rectangle:

    """ Rectangle Class object
    Attributes:
        height (int): height value
        width (int): width value
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter function
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, width_val):
        """ width setter function
        Args:
            width_val (int): The width value
        Raises:
            TypeError: Width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(width_val, int):
            raise TypeError("width must be an integer")
        if width_val < 0:
            raise ValueError("width must be >= 0")
        self.__width = width_val

    @property
    def height(self):
        """ height getter
        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, height_val):
        """height setter function
        Args:
            height_val (int): Description
        Raises:
            TypeError: height must an integer
            ValueError: height must >= 0
        """
        if not isinstance(height_val, int):
            raise TypeError("height must be an integer")
        if height_val < 0:
            raise ValueError("height must be >= 0")
        self.__height = height_val

    def area(self):
        """Area function to calculate the area of the rectangle
        Returns: an iint value of the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter funtion to calculate perimeter of the rectangle
        Returns: an int value of preimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ __str__ prints rectangles
        Returns:
            str:  # rectangles
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            i = 0
            while i < self.__height:
                string += ("#" * self.__width)
                if i != self.__height - 1:
                    string += "\n"
                i += 1
            return string

    def __repr__(self):
        """__repr__ recreats an instance
        Returns: a string
        """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

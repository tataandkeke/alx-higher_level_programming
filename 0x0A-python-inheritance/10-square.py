#!/usr/bin/python3
""" Square Module
Attributes:
    Rectangle (object): Rectangle class
"""

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):

    """ Square Class
    """

    def __init__(self, size):
        """ Initialization

        Args:
            size (int): the size
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        return self.__height * self.__width

    def __str__(self) -> str:
        return f"[Rectangle] {self.__width:d}/{self.__height:d}"

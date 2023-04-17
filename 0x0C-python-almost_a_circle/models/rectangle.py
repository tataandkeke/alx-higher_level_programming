#!/usr/bin/python3
""" Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class
    Attribtes:
        width: width int variable
        Height: height int variabel
        x: variable
        y: variable
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

        Base.__init__(self, id)

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

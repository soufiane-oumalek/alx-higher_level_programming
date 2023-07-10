#!/usr/bin/python3
"""defines rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initialize rectangle class on bassegeometry"""

    def __init__(self, width, height):
        """initialize rectangle
        Args:
        @width: for rectangle
        @height: for rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

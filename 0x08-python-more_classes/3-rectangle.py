#!/usr/bin/python3
"""defines rectangle"""


class Rectangle:
    """initialize Rectangle"""

    def __init__(self, width=0, height=0):
        """initialize new Rectangle
        Args:
        width (int): for new rectangle
        height (int):for new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """ther perimetet of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """print the rectangle with the character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_angle = []
        for i in range(self.__height):
            [rect_angle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect_angle.append("\n")
        return "".join(rect_angle)

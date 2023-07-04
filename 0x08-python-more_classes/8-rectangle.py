#!/usr/bin/python3
"""defines rectangle"""


class Rectangle:
    """initialize Rectangle"""
    __width = None
    __height = None
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize new Rectangle
        Args:
        width (int): for new rectangle
        height (int):for new rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """rectangle with area
        args:
            rect_1 fisrt rectangle
            rect_2 second rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """print the rectangle with the character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        r_agl = []
        for i in range(self.__height):
            [r_agl.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                r_agl.append("\n")
        return "".join(r_agl)

    def __repr__(self):
        """string of the rectangle"""
        r_agl = "Rectangle(" + str(self.__width)
        r_agl += ", " + str(self.__height) + ")"
        return (r_agl)

    def __del__(self):
        """check if Rectangle delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

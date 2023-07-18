#!/usr/bin/python3
"""class rectangle inheritance of class base"""


from models.base import Base
"""import module"""


class Rectangle(Base):
    """initiaize class
    rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character # - you don't need to
        handle x and y here."""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """method that it returns [Rectangle]"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update rectangle instance"""
        if args is not None and len(args) != 0:
            list_atrri = ['id', 'width', 'height', 'x', 'y']
            for index in range(len(args)):
                setattr(self, list_atrri[index], args[index])
        else:
            for value, ky in kwargs.items():
                setattr(self, value, ky)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_nary = {'id': self.id, 'width': self.__width,
                     'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dict_nary

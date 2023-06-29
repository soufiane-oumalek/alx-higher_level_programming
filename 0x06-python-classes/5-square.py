#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """declare class square"""

    def __init__(self, size=0):
        """intialize square
        Args:

        size (int): size of square"""
        self.size = size

        def area(self):
            return (self.__size ** 2)

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size ust be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def my_print(self):
            if not self.__size:
                print("")
            for i in range(self.__size):
                print("#" * self.__size)

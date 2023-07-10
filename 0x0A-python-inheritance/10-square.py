#!/usr/bin/python3
"""defines rectangle class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialize square"""

    def __init__(self, size):
        """initialize new square
        Args:
        size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

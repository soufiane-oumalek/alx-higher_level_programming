#!/usr/bin/python3
"""defines class"""


class BaseGeometry:
    """initialison class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
        @name: is string name
        @value: validation value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

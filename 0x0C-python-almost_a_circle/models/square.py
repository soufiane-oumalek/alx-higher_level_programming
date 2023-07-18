#!/usr/bin/python3
"""class square inheritance of class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """initialize class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square]({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """return size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size setter for size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square instance"""
        if args is not None and len(args) != 0:
            list_atrri = ['id', 'size', 'x', 'y']
            for index in range(len(args)):
                if list_atrri[index] == 'size':
                    setattr(self, 'width', args[index])
                    setattr(self, 'height', args[index])
                else:
                    setattr(self, list_atrri[index], args[index])
        else:
            for ky, value in kwargs.items():
                if ky == 'size':
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, ky, value)

    def to_dictionary(self):
        """dictionary representation square"""
        dict_nary = {'id': self.id, 'size': self.size,
                     'x': self.x, 'y': self.y}
        return dict_nary

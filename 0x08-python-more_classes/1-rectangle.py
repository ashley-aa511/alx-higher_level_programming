#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width  # Using the property setter
        self.height = height  # Using the property setter

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width  # Using the property setter
        self.height = height  # Using the property setter
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self._height):
                rectangle_str += str(self.print_symbol) * self._width + '\n'
            return rectangle_str.rs

#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """algo"""

        self.height = height
        self.width = width

        @property
        def height(self):
            """ algo """
            return self.__height

        @height.setter
        def height(self, value):
            """ algp """

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value

        @property
        def width(self):
            """ algo """
            return self.__width

        @width.setter
        def width(self, value):
            """ algp """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__width = value

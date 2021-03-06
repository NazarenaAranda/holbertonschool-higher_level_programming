#!/usr/bin/python3
""" importar BaseGeometry de "7-base_geometry.py" """

BaseGeometry = __import__(
        "7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """clase rectangle"""
    def __init__(self, width, height):
        """instanciacion con width y height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

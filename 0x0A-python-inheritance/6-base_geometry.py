#!/usr/bin/python3
""" definiendo la base """


class BaseGeometry():
    """si el area no esta implementada lanza una excepcion"""
    def area(self):
        raise Exception("area() is not implemented")

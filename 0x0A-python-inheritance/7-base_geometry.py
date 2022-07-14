#!/usr/bin/python3
""" definiendo la base """


class BaseGeometry():
    """si el area no esta implementada lanza una excepcion"""
    def area(self):
        """metodo para calcular el area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """si no es entero tira una excepcion"""
        if type(value) is not int:
            raise TypeError(
                    "{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(
                    "{} must be greater than 0".format(name
                        ))

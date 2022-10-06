#!/usr/bin/python3
"""the list of available attributes and methods of an object"""


def lookup(obj):
    """retorna lista de atributos y métodos de un objeto"""
    return list(dir(obj))

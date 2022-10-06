#!/usr/bin/python3
def lookup(obj):
    """retorna lista de atributos y métodos de un objeto"""
    return list(dir(obj))

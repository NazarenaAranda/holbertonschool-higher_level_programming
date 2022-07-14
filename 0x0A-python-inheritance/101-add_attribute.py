#!/usr/bin/python3
"""agregar un nuevo atributo a un obj si es posible"""


def add_attribute(objet, att_name, att_value):
    """Lanza una excepción"""
    if not hasattr(objet, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(objet, att_name, att_value)

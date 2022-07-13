#!/usr/bin/python3
""" funcion qe devuelva true o false """


def inherits_from(obj, a_class):
    """si el objeto es una instancia devuelve True"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

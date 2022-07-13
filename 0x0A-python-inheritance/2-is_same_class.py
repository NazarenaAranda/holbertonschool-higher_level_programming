#!/usr/bin/python3
""" funcion qe devuelva true o false """


def is_same_class(obj, a_class):
    """si el objeto es igual a la instancia devuelve True"""
    if type(obj) is a_class:
        return (True)
    else:
        return(False)

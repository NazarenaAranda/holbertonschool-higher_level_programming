#!/usr/bin/python3
""" starting """


def append_write(filename="", text=""):
    """ escribir archivo """
    with open(filename, 'a', encoding="utf-8") as f:
        """ abrir archivo """
        return f.write(text)

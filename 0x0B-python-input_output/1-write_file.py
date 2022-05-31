#!/usr/bin/python3
""" starting """


def write_file(filename="", text=""):
    """ escribir archivo """
    with open(filename, 'w', encoding="utf-8") as f:
        """ abrir archivo """
        esc = f.write(text)
        return esc

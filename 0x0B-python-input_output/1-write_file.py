#!/usr/bin/python3
""" starting """


def write_file(filename="", text=""):
    """ escribir archivo """
    with open(filename, mode='w', encoding="utf-8") as f:
        """ abrir archivo """
        esc = f.write(text)
        return esc

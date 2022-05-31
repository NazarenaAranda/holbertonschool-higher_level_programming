#!/usr/bin/python3
""" starting """


def read_file(filename=""):
    """ leer archivo """
    with open(filename, encoding="utf-8") as f:
        """ abrir archivo """
        for li in f:
            print(li, end='')

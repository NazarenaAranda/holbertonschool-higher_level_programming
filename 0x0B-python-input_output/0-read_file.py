#!/usr/bin/python3

""" starting """



def read_file(filename=""):

    """ leer archivo """

    with open(filename, encoding="utf-8") as f:
        """ abrir archivo """
        for l in f:
            print (l, end='')

#!/usr/bin/python3
def no_c(my_string):
    c = ''
    for sc in my_string:
        if sc != 'C' or sc != 'c':
            c += sc
        return c

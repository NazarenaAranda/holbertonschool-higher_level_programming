#!/usr/bin/python3
def no_c(my_string):
    c = ""
    for sc in my_string:
        if sc != 'C' and sc != 'c':
            c += sc
    return c

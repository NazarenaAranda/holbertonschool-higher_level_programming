#!/usr/bin/python3
def best_score(a_dictionary):
    max = -255
    nombre = None
    if a_dictionary:
        for n in list(a_dictionary):
            if a_dictionary[n] > max:
                max = a_dictionary[n]
                nombre = n
    return nombre

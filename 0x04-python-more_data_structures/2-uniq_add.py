#!/usr/bin/python3
def uniq_add(my_list=[]):
    resultado = 0
    for n in set(my_list):
        resultado += n
    return resultado

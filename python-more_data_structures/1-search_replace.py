#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nueva_lista = my_list[:]
    for i in range(len(nueva_lista)):
        if nueva_lista[i] == search:
            nueva_lista[i] = replace
    return nueva_lista

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nueva = my_list[:]
    for n in range (len(nueva)):
        if nueva[n] == search:
            nueva[n] = replace
    return nueva

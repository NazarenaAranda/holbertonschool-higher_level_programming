#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tam = 0
    while tam < x:
        try:
            print("{}".format(my_list[tam]), end='')
        except IndexError:
            break
        tam += 1
    print("")
    return (tam)

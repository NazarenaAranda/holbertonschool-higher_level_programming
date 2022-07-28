#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    comp = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            comp.append(True)
        else:
            comp.append(False)

    return (comp)

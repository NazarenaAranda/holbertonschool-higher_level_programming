#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in a:
            print(f"{b}", end='')
            if b != a[-1]:
                print(" ", end='')
        print() 

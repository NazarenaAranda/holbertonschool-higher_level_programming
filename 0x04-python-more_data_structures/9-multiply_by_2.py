#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuev_dic = a_dictionary.copy()
    for n in list(nuev_dic):
        nuev_dic[n] = nuev_dic[n] * 2
    return nuev_dic

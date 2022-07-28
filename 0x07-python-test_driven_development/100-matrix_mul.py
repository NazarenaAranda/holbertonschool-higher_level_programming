#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")

    if all(isinstance(x, (list)) for x in m_a) == True:
        raise TypeError("m_a must be a list of lists")
    elif all(isinstance(x, (list)) for x in m_b) == True:
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or [[]]:
        raise ValueError("m_b can't be empty")

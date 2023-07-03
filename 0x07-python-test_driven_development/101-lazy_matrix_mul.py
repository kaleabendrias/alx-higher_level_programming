#!/usr/bin/python3
""" a function that multiplies two matrixs """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrix """
    return np.dot(m_a, m_b)

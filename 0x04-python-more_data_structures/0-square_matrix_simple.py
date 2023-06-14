#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_i = [x ** 2 for x in i]
        new_mat.append(new_i)
    return (new_mat)

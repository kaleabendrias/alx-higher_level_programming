#!/usr/bin/python3
"""module for dividing matrix"""


def matrix_divided(matrix, div):
    """divide all elemetns of a mtrix by div"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return (new_matrix)

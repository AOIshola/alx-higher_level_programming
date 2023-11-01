#!/usr/bin/python3
"""The matrix division Module"""


def matrix_divided(matrix, div):
    """
    Returns the division of all elements of
    a matrix.

    Parameters:
        matrix (list): the matrix provided
        div (int): the number to divide by
    Returns: a matrix of the same size after division by div
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    err = "matrix must be a matrix (list of lists) of integers/floats"
    results = []
    if (not isinstance(matrix, list) or
            not all(isinstance(item, list) for item in matrix)):
        raise TypeError(err)
    if (not all(isinstance(num, (int, float)) for item in matrix
                for num in item)):
        raise TypeError(err)

    for item in matrix:
        if len(item) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        results.append([round((num / div), 2) for num in item])

    return (results)

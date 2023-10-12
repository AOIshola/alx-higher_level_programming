#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_matrix.append(list(map(lambda x: x ** 2, row)))
    return (square_matrix)

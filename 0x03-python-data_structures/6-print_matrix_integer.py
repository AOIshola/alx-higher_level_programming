#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat_len = len(matrix)
    if mat_len == 0:
        print('$')
    else:
        for row in matrix:
            row_len = len(row)
            for i in range(row_len):
                if i == (row_len - 1):
                    print("{}".format(row[i]), end="")
                else:
                    print("{}".format(row[i]), end=" ")
            print()
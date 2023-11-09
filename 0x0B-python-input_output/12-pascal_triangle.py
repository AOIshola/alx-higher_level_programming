#!/usr/bin/python3
"""The Pascal Triangle Module"""


def pascal_triangle(n):
    """Represents a list of lists of integers
    representing a Pascal's triangle"""
    tri = []
    if n <= 0:
        return (tri)
    for i in range(n):
        res = []
        if i == 0:
            res.append(1)
            tri.append(res)
        elif i > 0:
            if i == 1:
                res = [1]
            last = tri[-1]
            for j in range(i):
                if j == 0 or j == i - 1:
                    res.append(1)
                else:
                    add = last[j - 1] + last[j]
                    res.append(add)
            tri.append(res)
    return (tri)

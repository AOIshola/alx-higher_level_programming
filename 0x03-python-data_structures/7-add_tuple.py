#!/usr/bin/python3
from itertools import zip_longest


def add_tuple(tuple_a=(), tuple_b=()):
    c = tuple(zip_longest(tuple_a, tuple_b, fillvalue=0))
    add_list = []
    for i in range(2):
        add = 0
        for tup in c[i]:
            add += tup
        add_list.append(add)
    return (tuple(add_list))

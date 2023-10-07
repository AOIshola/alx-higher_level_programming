#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    c = tuple(zip(tuple_a, tuple_2))
    add_list = []
    for i in range(2):
        add = 0
        for tup in c[i]:
            add += tup
        add_list.append(add)
    return (tuple(add_list))

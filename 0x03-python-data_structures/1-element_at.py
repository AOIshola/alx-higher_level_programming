#!/usr/bin/python3

def element_at(my_list, idx):
    l_len = len(my_list)
    if idx < 0:
        return (None)
    if idx >= l_len:
        return (None)
    i = 0
    for i in range(l_len):
        if i == idx:
            return (my_list[idx])

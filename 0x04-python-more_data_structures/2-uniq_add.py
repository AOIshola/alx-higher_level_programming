#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_sum = 0
    my_set = set(my_list)
    for num in my_set:
        my_sum += num
    return (my_sum)

#!/usr/bin/python3
"""Finds the peak of an array"""


def find_peak(list_of_integers):
    """Finds the peak of an unsorted list of integers"""
    low, high = 0, len(list_of_integers)
    n = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    while low <= high:
        mid = (low + high) // 2
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        elif mid < n and list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            return (list_of_integers[mid])

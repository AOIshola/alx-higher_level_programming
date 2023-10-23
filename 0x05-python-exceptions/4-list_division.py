#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    zipped = list(zip(my_list_1, my_list_2))
    for j in zipped:
        try:
            result = j[0] / j[1]
            results.append(result)
        except TypeError:
            results.append(0)
            print("wrong type")
        except ZeroDivisionError:
            results.append(0)
            print("division by 0")
        except IndexError:
            results.append(0)
            print("out of range")
    return (results)

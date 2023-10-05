#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argv = sys.argv
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print("{}".format(sum))

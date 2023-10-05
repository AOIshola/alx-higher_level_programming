#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    args = len(argv) - 1
    if args == 1:
        print("{} {}".format(args, 'argument'), end="")
    else:
        print("{} {}".format(args, 'arguments'), end="")
    print("{}".format(":" if args > 0 else "."))
    for i in range(1, args + 1):
        print("{}: {}".format(i, argv[i]))
        i += 1

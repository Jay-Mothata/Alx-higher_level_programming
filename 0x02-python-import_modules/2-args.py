#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arg = argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print("Zero arguments.")
    else:
        if arg_count == 1:
            print("{} argument:\n{}: {}".format(arg_count, arg_count, arg[0]))
        else:
            print("{} arguments:".format(arg_count))
            for i in range(arg_count):
                print("{}: {}".format((i + 1), arg[i]))
